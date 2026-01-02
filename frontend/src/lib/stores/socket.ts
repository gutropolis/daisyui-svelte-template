/*
 * Copyright (c) Simsaw Software Pvt. Ltd. 2022.
 * Author: Ankit Patial <ankit@simsaw.com>
 */

import { derived, get, type Writable, writable } from 'svelte/store';
import { authUser } from '$lib/stores/app';
import { SOCKET_ACTION } from '$lib/enums/socket';
import type { SocketMsg } from '$lib/models/SocketMsg';
import sleep from '$lib/utils/sleep';
import { page } from '$app/stores';

let client: WebSocket | undefined;

function createSocket() {
	let attempt = 0,
		connecting = false,
		host: string,
		pingTimeOut: any;

	function ping(userId: string | undefined = undefined, pathname: string | undefined = undefined) {
		// debounce ping for a second
		if (pingTimeOut) clearTimeout(pingTimeOut);
		pingTimeOut = setTimeout(() => {
			send(SOCKET_ACTION.SAY_HELLO, { userId, pathname }).catch(console.error);
		}, 800);
	}

	function attemptConnection() {
		if (connecting) return;

		connecting = true;
		client = undefined;
		sleep(2000)
			.then(() => {
				attempt++;
				connect(host, true);
			})
			.catch((ex) => {
				console.log('ws: failed to connect', ex);
			})
			.finally(() => {
				connecting = false;
			});
	}

	function setMsg(msg: string) {
		try {
			const obj = typeof msg === 'object' ? msg : JSON.parse(msg);
			wsMessage.set(obj);
		} catch (err) {
			console.error('ws: failed to parse msg', err, msg);
		}
	}

	function connect(wsHost: string, force = false) {
		if (!force && client) {
			return;
		}

		host = wsHost;
		client = newWebSocket(host);
		if (!client) return;

		client.onopen = () => {
			attempt = 0;
			const d = {
				appID: getAppID(),
				action: SOCKET_ACTION.SAY_HELLO,
				data: { userId: get(authUser)?.id, pathname: get(page)?.url?.pathname }
			};
			client?.send(JSON.stringify(d));
		};

		// on socket message
		client.onmessage = (evt: any) => {
			const msg = evt?.data;
			if (!msg) {
				return;
			}

			setMsg(msg);
		};

		// on error
		client.onerror = (event: any) => {
			console.log('ws: error', event);
		};

		// on close
		client.onclose = (event: any) => {
			console.log(
				`ws: connection closed, code=${event.code} reason=${event.reason}`
			);
			attemptConnection();
		};
	}

	async function send(action: SOCKET_ACTION, data: object) {
		let sent = false;
		attempt = 0;
		while (!sent && attempt < 30) {
			attempt++;
			if (!client || connecting) {
				// will attempt in a second
				// console.log("ws: failed to send as socket connection is not ready");
				await sleep(1000);
				continue;
			}

			try {
				// web version
				await client.send(JSON.stringify({ appID: getAppID(), action, data }));
				sent = true;
			} catch (ex: any) {
				// console.log("ws: failed to send message, error", ex);
				if (ex.toString().includes('connection not found')) {
					client = undefined;
					attemptConnection();
					continue;
				}
				await sleep(2);
			}
		}
	}

	return {
		connect,
		send,
		close: (reason: string) => {
			if (!client) return;

			client.close(3000, reason);
		},
		ping
	};
}

function getAppID(): string | null {
	if (!window) {
		return null;
	}

	let id = window.localStorage.getItem('AppID');
	if (!id) {
		id = crypto.randomUUID();
		window.localStorage.setItem('AppID', id);
	}

	return id;
}

function newWebSocket(host: string) {
	if (typeof WebSocket !== 'undefined') {
		return new WebSocket(host);
	}

	// eslint-disable-next-line @typescript-eslint/ban-ts-comment
	// @ts-ignore
	if (typeof MozWebSocket !== 'undefined') {
		// eslint-disable-next-line @typescript-eslint/ban-ts-comment
		// @ts-ignore
		return new MozWebSocket(host);
	}

	if (typeof window !== 'undefined') {
		// eslint-disable-next-line @typescript-eslint/ban-ts-comment
		// @ts-ignore
		const WS = window.WebSocket || window.MozWebSocket;
		if (WS) {
			return new WS(host);
		}
	}

	return undefined;
}

export const socket = createSocket();

export const wsMessage = writable<SocketMsg<any>>();

export interface PathDataChange {
	pathname: string,
	data: any
}

export const wsPathDataChange = derived<Writable<SocketMsg<any>>, PathDataChange>(wsMessage, ($msg, set) => {
	if (!$msg || $msg?.action !== SOCKET_ACTION.PATH_DATA_CHANGE) return;

	set({ pathname: $msg.data.pathname, data: { ...$msg.data, pathname: undefined } });
});
