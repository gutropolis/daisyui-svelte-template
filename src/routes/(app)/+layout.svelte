<script lang="ts">
	import favicon from '$lib/assets/favicon.svg';
	import Sidebar from '$lib/components/common/Sidebar.svelte';
	import Header from '$lib/components/common/Header.svelte';
	import Footer from '$lib/components/common/Footer.svelte';
	import Breadcrumb from '$lib/components/common/Breadcrumb.svelte';
	let { children } = $props();
	let sidebarOpen = $state(false);

	function toggleSidebar() {
		sidebarOpen = !sidebarOpen;
	}
</script>

<div class="flex h-screen bg-gray-50">
	<!-- Sidebar Component -->
	<Sidebar {sidebarOpen} onToggleSidebar={toggleSidebar} />

	<!-- Main Content Area -->
	<div class="flex-1 flex flex-col">
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
</div>
