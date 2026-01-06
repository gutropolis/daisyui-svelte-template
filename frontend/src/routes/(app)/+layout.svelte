<script lang="ts">
	import { onMount } from 'svelte';
	import '../layout.css';
	import Sidebar from '$theme/common/Sidebar.svelte';
	import { PATH } from '$lib/enums/path';
	import { goto } from '$app/navigation';
	import { page } from '$app/stores';
	import { authUser } from '$lib/stores/app';
	import { browser } from '$app/environment';
	import Header from '$theme/common/Header.svelte';

	let sidebarOpen = $state(true);
	let isMobile = $state(false);

	onMount(() => {
		if (!$authUser) {
			localStorage.setItem('returnURL', $page.url.pathname);
			goto(PATH.LOGIN);
		}

		const checkMobile = () => {
			isMobile = window.innerWidth < 768;
			if (isMobile) sidebarOpen = false;
		};

		checkMobile();
		window.addEventListener('resize', checkMobile);
		return () => window.removeEventListener('resize', checkMobile);
	});

	const toggleSidebar = () => {
		sidebarOpen = !sidebarOpen;
	};

	let { children } = $props();
</script>

<div class="flex h-screen w-screen overflow-hidden bg-gray-50">
	<!-- Sidebar -->
	<Sidebar {sidebarOpen} />

	<!-- Main Content Area -->
	<main class="flex-1 flex flex-col overflow-hidden">
		<!-- Top Header -->
		 <Header {sidebarOpen} onToggleSidebar={toggleSidebar} />

		<!-- Page Content -->
		<div class="flex-1 overflow-auto">
			{@render children()}
		</div>
	</main>

	<!-- Mobile Overlay -->
	{#if sidebarOpen && isMobile}
		<button
			type="button"
			class="fixed inset-0 bg-black bg-opacity-50 z-30 md:hidden"
			onclick={() => (sidebarOpen = false)}
			aria-label="Close sidebar"
		></button>
	{/if}
</div>

<style>
	/* Thin scrollbar styling */
	:global(.custom-scrollbar) {
		scrollbar-width: thin;
		scrollbar-color: #cbd5e1 transparent;
	}

	:global(.custom-scrollbar::-webkit-scrollbar) {
		width: 6px;
	}

	:global(.custom-scrollbar::-webkit-scrollbar-track) {
		background: transparent;
	}

	:global(.custom-scrollbar::-webkit-scrollbar-thumb) {
		background-color: #cbd5e1;
		border-radius: 3px;
		border: 2px solid transparent;
		background-clip: content-box;
	}

	:global(.custom-scrollbar::-webkit-scrollbar-thumb:hover) {
		background-color: #94a3b8;
	}
</style>
