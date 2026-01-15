<script lang="ts">
	import { goto } from '$app/navigation';
	import { PATH } from '$lib/enums/path'; 
	import { authUser } from '$lib/stores/app'; 
	import {  storeProjID } from '$lib/stores/app';
	import { onMount } from 'svelte';
	import favicon from '$lib/assets/favicon.svg';
	import { navigating } from '$app/state';
	import Progress from '$theme/common/Progress.svelte';

	let { children } = $props();

	onMount(() => {
		console.log("AUTH USER LOGIN",$authUser);
		if ($authUser) { 
			goto(PATH.MY_PROFILE);
			return;
		}
		goto(PATH.LOGIN);
		return;
	});

 
    $effect(() => {
        if (!$authUser) {
			console.log("App Auth User:", $authUser);
			goto(PATH.LOGIN);
		}
    });
</script>

<svelte:head>
	import { navigating } from '$app/stores';
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
