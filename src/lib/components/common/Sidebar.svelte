<script lang="ts">
	interface Props {
		sidebarOpen: boolean;
		onToggleSidebar: () => void;
	}

	const { sidebarOpen, onToggleSidebar } = $props<Props>();
</script>

<!-- Sidebar -->
<aside
	class="bg-white border-r border-gray-200 flex flex-col h-full transition-all duration-300 overflow-hidden {sidebarOpen
		? 'w-52 fixed left-0 top-0 z-40 lg:static lg:w-52'
		: 'w-0 lg:w-16 fixed left-0 lg:static top-0 z-40'}"
>
	<!-- Logo/Brand -->
	<div
		class="p-6 lg:p-4 flex items-center gap-2 justify-center lg:justify-start border-b border-gray-200"
	>
		<div class="w-8 h-8 bg-indigo-600 rounded-lg flex items-center justify-center flex-shrink-0">
			<svg
				xmlns="http://www.w3.org/2000/svg"
				class="h-5 w-5 text-white"
				viewBox="0 0 20 20"
				fill="currentColor"
			>
				<path
					d="M10.394 2.08a1 1 0 00-.788 0l-7 3a1 1 0 000 1.84L5.25 8.051a.999.999 0 01.356-.257l4-1.714a1 1 0 11.788 1.838L7.667 9.088l1.94.831a1 1 0 00.787 0l7-3a1 1 0 000-1.838l-7-3zM3.31 9.397L5 10.12v4.102a8.969 8.969 0 00-1.05-.174 1 1 0 01-.89-.89 11.115 11.115 0 01.25-3.762zM9.3 16.573A9.026 9.026 0 007 14.935v-3.957l1.818.78a3 3 0 002.364 0l5.508-2.361a11.026 11.026 0 01.25 3.762 1 1 0 01-.89.89 8.968 8.968 0 00-5.35 2.524 1 1 0 01-1.4 0zM6 18a1 1 0 001-1v-2.065a8.935 8.935 0 00-2-.712V17a1 1 0 001 1z"
				/>
			</svg>
		</div>
		<span
			class="font-bold text-gray-800 hidden"
			class:hidden={!sidebarOpen}
			class:block={sidebarOpen}>REDCap</span
		>
	</div>

	<!-- User Info Section -->
	<div class="p-4 border-b border-gray-200 space-y-3" class:hidden={!sidebarOpen}>
		<div class="flex items-center gap-2">
			<svg
				xmlns="http://www.w3.org/2000/svg"
				class="h-5 w-5 text-gray-600"
				fill="none"
				viewBox="0 0 24 24"
				stroke="currentColor"
			>
				<path
					stroke-linecap="round"
					stroke-linejoin="round"
					stroke-width="2"
					d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z"
				/>
			</svg>
			<span class="text-sm font-medium text-gray-700">Logged in as Ismanandhar</span>
		</div>
		<a href="#" class="text-sm text-red-600 hover:text-red-700 font-medium">Log out</a>
	</div>

	<!-- My Projects Card -->
	<div
		class="mx-4 mt-4 mb-4 p-3 bg-gray-50 rounded-lg border border-gray-200"
		class:hidden={!sidebarOpen}
	>
		<div class="flex items-center gap-2 mb-2">
			<svg
				xmlns="http://www.w3.org/2000/svg"
				class="h-5 w-5 text-gray-600"
				fill="none"
				viewBox="0 0 24 24"
				stroke="currentColor"
			>
				<path
					stroke-linecap="round"
					stroke-linejoin="round"
					stroke-width="2"
					d="M3 7v10a2 2 0 002 2h14a2 2 0 002-2V7M3 7l9-4 9 4m0 0l-9 4m9-4v10"
				/>
			</svg>
			<span class="text-sm font-medium text-gray-900">My Projects</span>
		</div>
	</div>

	<!-- Contact Promed Alert -->
	<div
		class="mx-4 mb-4 p-3 bg-pink-50 rounded-lg border border-pink-200"
		class:hidden={!sidebarOpen}
	>
		<div class="flex items-center gap-2 mb-2">
			<svg
				xmlns="http://www.w3.org/2000/svg"
				class="h-5 w-5 text-pink-600"
				fill="none"
				viewBox="0 0 24 24"
				stroke="currentColor"
			>
				<path
					stroke-linecap="round"
					stroke-linejoin="round"
					stroke-width="2"
					d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
				/>
			</svg>
		</div>
		<p class="text-sm font-semibold text-pink-700">Contact Promed administrator</p>
	</div>

	<!-- Navigation Menu -->
	<nav class="flex-1 px-1 lg:px-3 py-2 overflow-y-auto">
		<!-- Project Home and Design Section -->
		<div class="mt-4 mb-3 px-2 lg:px-3 hidden" class:hidden={!sidebarOpen}>
			<h3 class="text-xs font-semibold text-gray-400 uppercase tracking-wider">
				Project Home and Design
			</h3>
		</div>
		<ul class="space-y-1">
			<li>
				<a
					href="/project/home"
					class="flex items-center justify-center lg:justify-start gap-0 lg:gap-3 px-2 lg:px-3 py-2.5 text-gray-600 hover:bg-gray-100 rounded-lg transition-colors"
					title="Home"
				>
					<svg
						xmlns="http://www.w3.org/2000/svg"
						class="h-5 w-5 flex-shrink-0"
						fill="none"
						viewBox="0 0 24 24"
						stroke="currentColor"
					>
						<path
							stroke-linecap="round"
							stroke-linejoin="round"
							stroke-width="2"
							d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"
						/>
					</svg>
					<span class="text-sm hidden" class:hidden={!sidebarOpen}>Home</span>
				</a>
			</li>
			<li>
				<a
					href="/project/setup"
					class="flex items-center justify-center lg:justify-start gap-0 lg:gap-3 px-2 lg:px-3 py-2.5 text-gray-600 hover:bg-gray-100 rounded-lg transition-colors"
					title="Setup"
				>
					<svg
						xmlns="http://www.w3.org/2000/svg"
						class="h-5 w-5 flex-shrink-0"
						fill="none"
						viewBox="0 0 24 24"
						stroke="currentColor"
					>
						<path
							stroke-linecap="round"
							stroke-linejoin="round"
							stroke-width="2"
							d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z"
						/>
						<path
							stroke-linecap="round"
							stroke-linejoin="round"
							stroke-width="2"
							d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"
						/>
					</svg>
					<span class="text-sm hidden" class:hidden={!sidebarOpen}>Setup</span>
				</a>
			</li>
			<li>
				<a
					href="/project/designer"
					class="flex items-center justify-center lg:justify-start gap-0 lg:gap-3 px-2 lg:px-3 py-2.5 text-gray-600 hover:bg-gray-100 rounded-lg transition-colors"
					title="Designer"
				>
					<svg
						xmlns="http://www.w3.org/2000/svg"
						class="h-5 w-5 flex-shrink-0"
						fill="none"
						viewBox="0 0 24 24"
						stroke="currentColor"
					>
						<path
							stroke-linecap="round"
							stroke-linejoin="round"
							stroke-width="2"
							d="M7 21a4 4 0 01-4-4V5a2 2 0 012-2h4a2 2 0 012 2v12a4 4 0 01-4 4zm0 0h12a2 2 0 002-2v-4a2 2 0 00-2-2h-2.343M11 7.343l1.657-1.657a2 2 0 012.828 0l2.829 2.829a2 2 0 010 2.828l-8.486 8.485M7 17h.01"
						/>
					</svg>
					<span class="text-sm hidden" class:hidden={!sidebarOpen}>Designer</span>
				</a>
			</li>
			<li>
				<a
					href="/project/events"
					class="flex items-center justify-center lg:justify-start gap-0 lg:gap-3 px-2 lg:px-3 py-2.5 text-gray-600 hover:bg-gray-100 rounded-lg transition-colors"
					title="Events"
				>
					<svg
						xmlns="http://www.w3.org/2000/svg"
						class="h-5 w-5 flex-shrink-0"
						fill="none"
						viewBox="0 0 24 24"
						stroke="currentColor"
					>
						<path
							stroke-linecap="round"
							stroke-linejoin="round"
							stroke-width="2"
							d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"
						/>
					</svg>
					<span class="text-sm hidden" class:hidden={!sidebarOpen}>Events</span>
				</a>
			</li>
		</ul>

		<!-- Data Collection Section -->
		<div class="mt-6 mb-3 px-2 lg:px-3 hidden" class:hidden={!sidebarOpen}>
			<h3 class="text-xs font-semibold text-gray-400 uppercase tracking-wider">Data Collection</h3>
		</div>
		<ul class="space-y-1">
			<li>
				<a
					href="/project/record-status"
					class="flex items-center justify-center lg:justify-start gap-0 lg:gap-3 px-2 lg:px-3 py-2.5 text-gray-600 hover:bg-gray-100 rounded-lg transition-colors"
					title="Record Status Dashboard"
				>
					<svg
						xmlns="http://www.w3.org/2000/svg"
						class="h-5 w-5 flex-shrink-0"
						fill="none"
						viewBox="0 0 24 24"
						stroke="currentColor"
					>
						<path
							stroke-linecap="round"
							stroke-linejoin="round"
							stroke-width="2"
							d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"
						/>
					</svg>
					<span class="text-sm hidden" class:hidden={!sidebarOpen}>Record Status Dashboard</span>
				</a>
			</li>
			<li>
				<a
					href="/project/add-edit"
					class="flex items-center justify-center lg:justify-start gap-0 lg:gap-3 px-2 lg:px-3 py-2.5 text-gray-600 hover:bg-gray-100 rounded-lg transition-colors"
					title="Add / Edit Records"
				>
					<svg
						xmlns="http://www.w3.org/2000/svg"
						class="h-5 w-5 flex-shrink-0"
						fill="none"
						viewBox="0 0 24 24"
						stroke="currentColor"
					>
						<path
							stroke-linecap="round"
							stroke-linejoin="round"
							stroke-width="2"
							d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z"
						/>
					</svg>
					<span class="text-sm hidden" class:hidden={!sidebarOpen}>Add / Edit Records</span>
				</a>
			</li>
		</ul>

		<!-- Applications Section -->
		<div class="mt-6 mb-3 px-2 lg:px-3 hidden" class:hidden={!sidebarOpen}>
			<h3 class="text-xs font-semibold text-gray-400 uppercase tracking-wider">Applications</h3>
		</div>
		<ul class="space-y-1">
			<li>
				<a
					href="/project/dashboards"
					class="flex items-center justify-center lg:justify-start gap-0 lg:gap-3 px-2 lg:px-3 py-2.5 text-gray-600 hover:bg-gray-100 rounded-lg transition-colors"
					title="Project Dashboards"
				>
					<svg
						xmlns="http://www.w3.org/2000/svg"
						class="h-5 w-5 flex-shrink-0"
						fill="none"
						viewBox="0 0 24 24"
						stroke="currentColor"
					>
						<path
							stroke-linecap="round"
							stroke-linejoin="round"
							stroke-width="2"
							d="M9 3v2m6-2v2m-9 4h12m-12 0a2 2 0 00-2 2v6a2 2 0 002 2h12a2 2 0 002-2v-6a2 2 0 00-2-2z"
						/>
					</svg>
					<span class="text-sm hidden" class:hidden={!sidebarOpen}>Project Dashboards</span>
				</a>
			</li>
			<li>
				<a
					href="/project/alerts"
					class="flex items-center justify-center lg:justify-start gap-0 lg:gap-3 px-2 lg:px-3 py-2.5 text-gray-600 hover:bg-gray-100 rounded-lg transition-colors"
					title="Alerts & Notifications"
				>
					<svg
						xmlns="http://www.w3.org/2000/svg"
						class="h-5 w-5 flex-shrink-0"
						fill="none"
						viewBox="0 0 24 24"
						stroke="currentColor"
					>
						<path
							stroke-linecap="round"
							stroke-linejoin="round"
							stroke-width="2"
							d="M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6.002 6.002 0 00-4-5.659V5a2 2 0 10-4 0v.341C7.67 6.165 6 8.388 6 11v3.159c0 .538-.214 1.055-.595 1.436L4 17h5m6 0v1a3 3 0 11-6 0v-1m6 0H9"
						/>
					</svg>
					<span class="text-sm hidden" class:hidden={!sidebarOpen}>Alerts & Notifications</span>
				</a>
			</li>
			<li>
				<a
					href="/project/data-exports"
					class="flex items-center justify-center lg:justify-start gap-0 lg:gap-3 px-2 lg:px-3 py-2.5 text-gray-600 hover:bg-gray-100 rounded-lg transition-colors"
					title="Data Exports"
				>
					<svg
						xmlns="http://www.w3.org/2000/svg"
						class="h-5 w-5 flex-shrink-0"
						fill="none"
						viewBox="0 0 24 24"
						stroke="currentColor"
					>
						<path
							stroke-linecap="round"
							stroke-linejoin="round"
							stroke-width="2"
							d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"
						/>
					</svg>
					<span class="text-sm hidden" class:hidden={!sidebarOpen}
						>Data Exports, Reports, and Stats</span
					>
				</a>
			</li>
			<li>
				<a
					href="/project/import"
					class="flex items-center justify-center lg:justify-start gap-0 lg:gap-3 px-2 lg:px-3 py-2.5 text-gray-600 hover:bg-gray-100 rounded-lg transition-colors"
					title="Data Import Tool"
				>
					<svg
						xmlns="http://www.w3.org/2000/svg"
						class="h-5 w-5 flex-shrink-0"
						fill="none"
						viewBox="0 0 24 24"
						stroke="currentColor"
					>
						<path
							stroke-linecap="round"
							stroke-linejoin="round"
							stroke-width="2"
							d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M9 19l3 3m0 0l3-3m-3 3V10"
						/>
					</svg>
					<span class="text-sm hidden" class:hidden={!sidebarOpen}>Data Import Tool</span>
				</a>
			</li>
			<li>
				<a
					href="/project/comparison"
					class="flex items-center justify-center lg:justify-start gap-0 lg:gap-3 px-2 lg:px-3 py-2.5 text-gray-600 hover:bg-gray-100 rounded-lg transition-colors"
					title="Data Comparison Tool"
				>
					<svg
						xmlns="http://www.w3.org/2000/svg"
						class="h-5 w-5 flex-shrink-0"
						fill="none"
						viewBox="0 0 24 24"
						stroke="currentColor"
					>
						<path
							stroke-linecap="round"
							stroke-linejoin="round"
							stroke-width="2"
							d="M9 21H7a2 2 0 01-2-2V9a4 4 0 014-4h5a4 4 0 014 4v10a2 2 0 01-2 2h-2m-4-3h.01M12 17h4"
						/>
					</svg>
					<span class="text-sm hidden" class:hidden={!sidebarOpen}>Data Comparison Tool</span>
				</a>
			</li>
		</ul>
	</nav>
</aside>

<!-- Mobile Overlay -->
{#if sidebarOpen}
	<!-- svelte-ignore a11y_click_events_have_key_events -->
	<!-- svelte-ignore a11y_no_static_element_interactions -->
	<div class="fixed inset-0 bg-black bg-opacity-50 z-30 lg:hidden" onclick={onToggleSidebar}></div>
{/if}
