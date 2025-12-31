<!--
  - Copyright (c) Simsaw Software Pvt. Ltd. 2022.
  - Author: Ankit Patial <ankit@simsaw.com>
  -->

<script lang='ts'>
	import { onMount } from 'svelte';
	import { socket, wsMessage } from '$lib/stores/socket';
	import alerts from '$lib/stores/alerts';
	import { SOCKET_ACTION } from '$lib/enums/socket';
	import { page } from '$app/stores';
	import { authUser, authUserBusy } from '$lib/stores/app';
	import { afterNavigate } from '$app/navigation';
	import { humanize } from '$lib/utils/string';

	let host = import.meta.env.VITE_WS_HOST;
	let activePath, pingInterval, interval = 1000 * 60 * 2;

	$: if ($wsMessage) {

		switch ($wsMessage.action) {
			case SOCKET_ACTION.ALERT:
				alerts.push({ type: 'info', body: $wsMessage.data });
				break;

			case SOCKET_ACTION.TASK_PROGRESS:
				handleTaskProgressMessage()
				break;
		}
	}

	onMount(() => {
		socket.connect(host);
		pingInterval = setInterval(() => {
			socket.ping($authUser?.id, $page.url.pathname);
		}, interval);
	});

	// on route change set socket connection active path
	afterNavigate(({ to }) => {
		if ($authUserBusy && !to?.url) return;

		setActivePath(to?.url?.pathname);
	});

	function setActivePath(pathname) {
		if (activePath == pathname) return;
		activePath = pathname;
		socket
			.send(SOCKET_ACTION.ACTIVE_PATH, { userId: $authUser?.id, pathname })
			.catch(console.error);
	}
	function handleTaskProgressMessage() {
		if (!$wsMessage) return;

		const taskData = $wsMessage.data;
		const isDone = taskData.done === true;
		const taskName = humanize(taskData.task);
		const message = taskData.message;

		if (taskData.task === 'project-codebook-pdf' || taskData.task === 'export-project-site-subjects') {
			if (isDone) {
				const fileURL = taskData.task === 'project-codebook-pdf' ? taskData.data.url : taskData.data.exportCsvUrl;
				if (fileURL) {
					alerts.push({
						type: 'success',
						title: 'CSV Export',
						body: taskData.task === 'project-codebook-pdf' ? 'Pdf generate successfully!!' : 'Thank you for keeping patience. Csv File export successfully!!'
					});

					const alink = document.createElement('a');
					alink.setAttribute('target', '_blank');
					alink.href = fileURL;
					alink.download = fileURL;
					alink.click();
				}
			} else if (message && message !== '') {
				alerts.error('Error', message);
			}

			wsMessage.set({ action: SOCKET_ACTION.TASK_PROGRESS, data: { task: '', done: false } });
		} else {
			alerts.info(taskName, message);
		}
	}
</script>
