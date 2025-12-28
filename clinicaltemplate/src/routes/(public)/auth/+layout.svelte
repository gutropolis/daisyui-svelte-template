<script lang="ts">
	import favicon from '$lib/assets/favicon.svg';
	import { navigating } from '$app/state';
	import Progress from '$lib/components/common/Progress.svelte';

	let { children } = $props();
</script>

<svelte:head>
	<link rel="icon" href={favicon} />
</svelte:head>

{#if navigating}
	<Progress />
{/if}

<div class="auth-wrapper min-h-screen bg-base-200 flex items-center justify-center p-4">
	<div class="auth-container w-full max-w-md">
		{@render children()}
	</div>
</div>

<style>
	.auth-wrapper {
		display: flex;
		align-items: center;
		justify-content: center;
	}

	.auth-container {
		width: 100%;
		max-width: 28rem;
	}

	:global(body) {
		margin: 0;
		padding: 0;
	}
</style>
