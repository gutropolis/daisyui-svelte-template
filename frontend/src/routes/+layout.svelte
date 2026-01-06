<script lang="ts">
	import { browser } from '$app/environment';
	import { navigating } from '$app/state';
	import { GRAPHQL_PATH } from '$lib/enums/path';
	import { createPortal } from '$lib/actions/portal';
	import favicon from '$lib/assets/favicon.svg';
	import SnackBar from '$theme/common/SnackBar.svelte';
	import './layout.css';
	import Progress from '$theme/common/Progress.svelte';
	import { cacheExchange, createClient, fetchExchange, setContextClient } from '@urql/svelte';
	import { authUser } from '$lib/stores/app';
	import client from '$lib/gql/client';

	let { data, children } = $props();

	let sidebarOpen = $state(false);

	 
   authUser.set(data?.authUser);
    setContextClient(client);  

	function toggleSidebar() {
		sidebarOpen = !sidebarOpen;
	}
</script>

<svelte:head>
	<link rel="icon" href={favicon} />
</svelte:head>
{#if navigating}
	<Progress />
{/if}
<div class="bg-base-200">
	{@render children()}
	<div use:createPortal={'modals'}></div>
	<SnackBar />
</div>
