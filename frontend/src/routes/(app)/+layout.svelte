<script lang="ts">
	import favicon from '$lib/assets/favicon.svg';
	import Sidebar from '$lib/components/common/Sidebar.svelte';
	import Header from '$lib/components/common/Header.svelte';
	import Footer from '$lib/components/common/Footer.svelte';
	import Breadcrumb from '$lib/components/common/Breadcrumb.svelte';
	import { authStore } from '$lib/stores/auth';
	import { goto } from '$app/navigation';
	import { browser } from '$app/environment';
	import { onMount } from 'svelte';

	let { children } = $props();
	let sidebarOpen = $state(false);
	let isChecking = $state(true);

	function toggleSidebar() {
		sidebarOpen = !sidebarOpen;
	}

	// Only run authentication check in browser on mount
	onMount(() => {
		if (browser) {
			if (!$authStore.isAuthenticated) {
				console.log('🔐 Not authenticated, redirecting to login...');
				goto('/login');
			} else {
				console.log('✅ User authenticated, allowing access to protected route');
				// Load user data if not already loaded
				if (!$authStore.user) {
					authStore.loadUser();
				}
			}
		}
		isChecking = false;
	});
</script>

<div class="flex h-screen bg-gray-50">
	{#if isChecking}
		<!-- Loading State -->
		<div class="w-full flex items-center justify-center">
			<div class="text-center">
				<span class="loading loading-spinner loading-lg text-primary"></span>
				<p class="mt-4 text-gray-600">Verifying access...</p>
			</div>
		</div>
	{:else}
		<!-- Sidebar Component -->
		<Sidebar {sidebarOpen} onToggleSidebar={toggleSidebar} />

		<!-- Main Content Area -->
		<div class={`flex-1 flex flex-col transition-[margin] duration-300 ${
			sidebarOpen ? 'lg:ml-64' : 'lg:ml-20'
		}`}>
			<!-- Header Component -->
			<Header {sidebarOpen} onToggleSidebar={toggleSidebar} />

			<!-- Page Content -->
			<main class="flex-1 overflow-auto p-6">
				<Breadcrumb />
				{@render children()}
			</main>

			<!-- Footer Component -->
			<Footer />
		</div>
	{/if}
</div>
