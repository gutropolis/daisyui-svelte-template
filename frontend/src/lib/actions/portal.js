// ref: https://svelte.dev/repl/8364bc976f0c4ff9b83adf6e7a3c19fd?version=3.29.4

import { tick } from 'svelte';

const portal_map = new Map();

export function createPortal(node, id = 'default') {
	const key = `$$portal.${id}`;
	if (portal_map.has(key)) throw `duplicate portal key "${id}"`;
	else portal_map.set(key, node);

	return { destroy: portal_map.delete.bind(portal_map, key) };
}

function mount(node, key) {
	if (!portal_map.has(key)) throw `unknown portal ${key}`;
	const host = portal_map.get(key);
	host.insertBefore(node, null);

	return () => host.contains(node) && host.removeChild(node);
}

export function portal(node, id = 'default') {
	let destroy;
	const key = `$$portal.${id}`;
	if (!portal_map.has(key))
		tick().then(() => {
			destroy = mount(node, key);
		});
	else destroy = mount(node, key);
	return { destroy: () => destroy?.() };
}

