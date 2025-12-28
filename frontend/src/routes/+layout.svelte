<script lang="ts">
	import favicon from '$lib/assets/favicon.svg';
	import { navigating } from '$app/state';

	import './layout.css';
	import Progress from '$lib/components/common/Progress.svelte';

	let { children } = $props();
	let sidebarOpen = $state(false);

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
</div>
