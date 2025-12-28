<script lang="ts">
	import { onMount } from 'svelte';
	import '../layout.css';
	import Sidebar from '$lib/components/common/Sidebar.svelte';

	let sidebarOpen = $state(true);
	let isMobile = $state(false);

	onMount(() => {
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
		<header
			class="h-16 bg-white border-b border-gray-200 flex items-center justify-between px-4 md:px-6 shadow-sm shrink-0"
		>
			<div class="flex items-center gap-2 md:gap-4 min-w-0">
				<!-- Menu Toggle Button -->
				<button
					onclick={toggleSidebar}
					class="p-2 hover:bg-gray-100 rounded-lg transition-all duration-300 text-gray-700 hover:text-blue-600 shrink-0"
					aria-label={sidebarOpen ? 'Hide sidebar' : 'Show sidebar'}
					title={sidebarOpen ? 'Hide sidebar' : 'Show sidebar'}
				>
					{#if sidebarOpen}
						<i class="fas fa-chevron-left text-lg"></i>
					{:else}
						<i class="fas fa-chevron-right text-lg"></i>
					{/if}
				</button>
				<h1 class="text-lg md:text-2xl font-bold text-gray-800 truncate">Clinical Data Capture System</h1>
			</div>

			<div class="flex items-center gap-2 md:gap-4 shrink-0">
				<!-- Search Bar -->
				<div class="hidden md:flex items-center bg-gray-100 rounded-lg px-4 py-2">
					<i class="fas fa-search text-gray-400 mr-2"></i>
					<input
						type="text"
						placeholder="Search..."
						class="bg-transparent text-sm text-gray-700 outline-none w-32"
					/>
				</div>

				<!-- Notifications -->
				<button
					class="relative p-2 hover:bg-gray-100 rounded-lg transition-colors"
					aria-label="Notifications"
					title="View notifications"
				>
					<i class="fas fa-bell text-gray-700 text-lg"></i>
					<span class="absolute top-1 right-1 w-2 h-2 bg-red-500 rounded-full"></span>
				</button>

				<!-- User Menu -->
				<div class="relative">
					<button class="flex items-center gap-2 p-2 hover:bg-gray-100 rounded-lg transition-colors">
						<img
							src="https://picsum.photos/seed/user123/32/32.jpg"
							alt="User"
							class="w-8 h-8 rounded-full"
						/>
						<i class="fas fa-chevron-down text-gray-400 text-xs hidden md:inline"></i>
					</button>
				</div>
			</div>
		</header>

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
