<script lang="ts">
	import type { Props } from '$lib/modal/theme';
	import { authStore } from '$lib/stores/auth';
	import { goto } from '$app/navigation';

	const { sidebarOpen, onToggleSidebar } = $props<Props>();

	async function handleLogout() {
		await authStore.logout();
		goto('/login');
	}
</script>

<!-- Sidebar -->
<aside
	class={`sidebar fixed top-0 left-0 z-40 h-full bg-white border-r border-gray-100 shadow-sm flex flex-col transition-all duration-300 ease-in-out ${
		sidebarOpen ? 'translate-x-0' : '-translate-x-full'
	} lg:static lg:translate-x-0`}
	class:expanded={sidebarOpen}
	class:collapsed={!sidebarOpen}
>
	<!-- Logo/Brand -->
	<div class="h-[70px] flex items-center border-b border-gray-100 px-4 gap-2">
		<a href="/" class="flex items-center gap-2 flex-1 overflow-hidden">
			<svg
				xmlns="http://www.w3.org/2000/svg"
				class="h-7 w-7 text-indigo-600"
				viewBox="0 0 20 20"
				fill="currentColor"
			>
				<path
					d="M10.394 2.08a1 1 0 00-.788 0l-7 3a1 1 0 000 1.84L5.25 8.051a.999.999 0 01.356-.257l4-1.714a1 1 0 11.788 1.838L7.667 9.088l1.94.831a1 1 0 00.787 0l7-3a1 1 0 000-1.838l-7-3zM3.31 9.397L5 10.12v4.102a8.969 8.969 0 00-1.05-.174 1 1 0 01-.89-.89 11.115 11.115 0 01.25-3.762zM9.3 16.573A9.026 9.026 0 007 14.935v-3.957l1.818.78a3 3 0 002.364 0l5.508-2.361a11.026 11.026 0 01.25 3.762 1 1 0 01-.89.89 8.968 8.968 0 00-5.35 2.524 1 1 0 01-1.4 0zM6 18a1 1 0 001-1v-2.065a8.935 8.935 0 00-2-.712V17a1 1 0 001 1z"
				/>
			</svg>
			<span class="nav-label text-xl font-bold text-gray-800 whitespace-nowrap">MINIBLE</span>
		</a>
		<button
			onclick={onToggleSidebar}
			class="hidden lg:inline-flex items-center justify-center rounded-lg border border-gray-200 p-2 text-gray-600 hover:bg-gray-50"
			aria-label="Toggle sidebar width"
		>
			<svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
				<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16" />
			</svg>
		</button>
	</div>

	<!-- Navigation Menu -->
	<nav class="flex-1 overflow-y-auto py-6">
		<!-- MENU Section -->
		<div class="px-6 mb-2">
			<p class="section-label text-xs font-semibold text-gray-400 uppercase tracking-wider">Menu</p>
		</div>
		<ul class="px-4 space-y-1">
			<li>
				<a
					href="/"
					class="nav-item flex items-center justify-between px-3 py-2 rounded-md bg-indigo-50 text-indigo-600"
				>
					<div class="flex items-center gap-3">
						<svg
							xmlns="http://www.w3.org/2000/svg"
							class="h-5 w-5"
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
						<span class="nav-label text-sm font-medium">Dashboard</span>
					</div>
					<span class="nav-extra px-2 py-0.5 text-xs font-semibold text-white bg-indigo-600 rounded-full">01</span>
				</a>
			</li>
			<li>
				<a
					href="/layouts"
					class="nav-item flex items-center justify-between px-3 py-2 text-gray-600 rounded-md hover:bg-gray-50"
				>
					<div class="flex items-center gap-3">
						<svg
							xmlns="http://www.w3.org/2000/svg"
							class="h-5 w-5"
							fill="none"
							viewBox="0 0 24 24"
							stroke="currentColor"
						>
							<path
								stroke-linecap="round"
								stroke-linejoin="round"
								stroke-width="2"
								d="M4 5a1 1 0 011-1h4a1 1 0 011 1v7a1 1 0 01-1 1H5a1 1 0 01-1-1V5zM14 5a1 1 0 011-1h4a1 1 0 011 1v7a1 1 0 01-1 1h-4a1 1 0 01-1-1V5zM4 16a1 1 0 011-1h4a1 1 0 011 1v3a1 1 0 01-1 1H5a1 1 0 01-1-1v-3zM14 16a1 1 0 011-1h4a1 1 0 011 1v3a1 1 0 01-1 1h-4a1 1 0 01-1-1v-3z"
							/>
						</svg>
						<span class="nav-label text-sm">Layouts</span>
					</div>
					<span class="nav-extra">
						<svg
							xmlns="http://www.w3.org/2000/svg"
							class="h-4 w-4"
							fill="none"
							viewBox="0 0 24 24"
							stroke="currentColor"
						>
							<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
						</svg>
					</span>
				</a>
			</li>
		</ul>

		<!-- APPS Section -->
		<div class="px-6 mt-6 mb-2">
			<p class="section-label text-xs font-semibold text-gray-400 uppercase tracking-wider">Apps</p>
		</div>
		<ul class="px-4 space-y-1">
			<li>
				<a
					href="/calendar"
					class="nav-item flex items-center gap-3 px-3 py-2 text-gray-600 rounded-md hover:bg-gray-50"
				>
					<svg
						xmlns="http://www.w3.org/2000/svg"
						class="h-5 w-5"
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
					<span class="nav-label text-sm">Calendar</span>
				</a>
			</li>
			<li>
				<a
					href="/chat"
					class="nav-item flex items-center gap-3 px-3 py-2 text-gray-600 rounded-md hover:bg-gray-50"
				>
					<svg
						xmlns="http://www.w3.org/2000/svg"
						class="h-5 w-5"
						fill="none"
						viewBox="0 0 24 24"
						stroke="currentColor"
					>
						<path
							stroke-linecap="round"
							stroke-linejoin="round"
							stroke-width="2"
							d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z"
						/>
					</svg>
					<span class="nav-label text-sm">Chat</span>
				</a>
			</li>
			<li>
				<a
					href="/file-manager"
					class="nav-item flex items-center gap-3 px-3 py-2 text-gray-600 rounded-md hover:bg-gray-50"
				>
					<svg
						xmlns="http://www.w3.org/2000/svg"
						class="h-5 w-5"
						fill="none"
						viewBox="0 0 24 24"
						stroke="currentColor"
					>
						<path
							stroke-linecap="round"
							stroke-linejoin="round"
							stroke-width="2"
							d="M3 7v10a2 2 0 002 2h14a2 2 0 002-2V9a2 2 0 00-2-2h-6l-2-2H5a2 2 0 00-2 2z"
						/>
					</svg>
					<span class="nav-label text-sm">File Manager</span>
				</a>
			</li>
			<li>
				<a
					href="/ecommerce"
					class="nav-item flex items-center justify-between px-3 py-2 text-gray-600 rounded-md hover:bg-gray-50"
				>
					<div class="flex items-center gap-3">
						<svg
							xmlns="http://www.w3.org/2000/svg"
							class="h-5 w-5"
							fill="none"
							viewBox="0 0 24 24"
							stroke="currentColor"
						>
							<path
								stroke-linecap="round"
								stroke-linejoin="round"
								stroke-width="2"
								d="M16 11V7a4 4 0 00-8 0v4M5 9h14l1 12H4L5 9z"
							/>
						</svg>
						<span class="nav-label text-sm">Ecommerce</span>
					</div>
					<span class="nav-extra">
						<svg
							xmlns="http://www.w3.org/2000/svg"
							class="h-4 w-4"
							fill="none"
							viewBox="0 0 24 24"
							stroke="currentColor"
						>
							<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
						</svg>
					</span>
				</a>
			</li>
			<li>
				<a
					href="/email"
					class="nav-item flex items-center justify-between px-3 py-2 text-gray-600 rounded-md hover:bg-gray-50"
				>
					<div class="flex items-center gap-3">
						<svg
							xmlns="http://www.w3.org/2000/svg"
							class="h-5 w-5"
							fill="none"
							viewBox="0 0 24 24"
							stroke="currentColor"
						>
							<path
								stroke-linecap="round"
								stroke-linejoin="round"
								stroke-width="2"
								d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"
							/>
						</svg>
						<span class="nav-label text-sm">Email</span>
					</div>
					<span class="nav-extra">
						<svg
							xmlns="http://www.w3.org/2000/svg"
							class="h-4 w-4"
							fill="none"
							viewBox="0 0 24 24"
							stroke="currentColor"
						>
							<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
						</svg>
					</span>
				</a>
			</li>
			<li>
				<a
					href="/invoices"
					class="nav-item flex items-center justify-between px-3 py-2 text-gray-600 rounded-md hover:bg-gray-50"
				>
					<div class="flex items-center gap-3">
						<svg
							xmlns="http://www.w3.org/2000/svg"
							class="h-5 w-5"
							fill="none"
							viewBox="0 0 24 24"
							stroke="currentColor"
						>
							<path
								stroke-linecap="round"
								stroke-linejoin="round"
								d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"
							/>
						</svg>
						<span class="nav-label text-sm">Invoices</span>
					</div>
					<span class="nav-extra">
						<svg
							xmlns="http://www.w3.org/2000/svg"
							class="h-4 w-4"
							fill="none"
							viewBox="0 0 24 24"
							stroke="currentColor"
						>
							<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
						</svg>
					</span>
				</a>
			</li>
			<li>
				<a
					href="/contacts"
					class="nav-item flex items-center justify-between px-3 py-2 text-gray-600 rounded-md hover:bg-gray-50"
				>
					<div class="flex items-center gap-3">
						<svg
							xmlns="http://www.w3.org/2000/svg"
							class="h-5 w-5"
							fill="none"
							viewBox="0 0 24 24"
							stroke="currentColor"
						>
							<path
								stroke-linecap="round"
								stroke-linejoin="round"
								stroke-width="2"
								d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"
							/>
						</svg>
						<span class="nav-label text-sm">Contacts</span>
					</div>
					<span class="nav-extra">
						<svg
							xmlns="http://www.w3.org/2000/svg"
							class="h-4 w-4"
							fill="none"
							viewBox="0 0 24 24"
							stroke="currentColor"
						>
							<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
						</svg>
					</span>
				</a>
			</li>
		</ul>

		<!-- PAGES Section -->
		<div class="px-6 mt-6 mb-2">
			<p class="section-label text-xs font-semibold text-gray-400 uppercase tracking-wider">Pages</p>
		</div>
		<ul class="px-4 space-y-1">
			<li>
				<a
					href="/authentication"
					class="nav-item flex items-center justify-between px-3 py-2 text-gray-600 rounded-md hover:bg-gray-50"
				>
					<div class="flex items-center gap-3">
						<svg
							xmlns="http://www.w3.org/2000/svg"
							class="h-5 w-5"
							fill="none"
							viewBox="0 0 24 24"
							stroke="currentColor"
						>
							<path
								stroke-linecap="round"
								stroke-linejoin="round"
								stroke-width="2"
								d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"
							/>
						</svg>
						<span class="nav-label text-sm">Authentication</span>
					</div>
					<span class="nav-extra">
						<svg
							xmlns="http://www.w3.org/2000/svg"
							class="h-4 w-4"
							fill="none"
							viewBox="0 0 24 24"
							stroke="currentColor"
						>
							<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
						</svg>
					</span>
				</a>
			</li>
			<li>
				<a
					href="/utility"
					class="nav-item flex items-center justify-between px-3 py-2 text-gray-600 rounded-md hover:bg-gray-50"
				>
					<div class="flex items-center gap-3">
						<svg
							xmlns="http://www.w3.org/2000/svg"
							class="h-5 w-5"
							fill="none"
							viewBox="0 0 24 24"
							stroke="currentColor"
						>
							<path
								stroke-linecap="round"
								stroke-linejoin="round"
								stroke-width="2"
								d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"
							/>
						</svg>
						<span class="nav-label text-sm">Utility</span>
					</div>
					<span class="nav-extra">
						<svg
							xmlns="http://www.w3.org/2000/svg"
							class="h-4 w-4"
							fill="none"
							viewBox="0 0 24 24"
							stroke="currentColor"
						>
							<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
						</svg>
					</span>
				</a>
			</li>
		</ul>

		<!-- COMPONENTS Section -->
		<div class="px-6 mt-6 mb-2">
			<p class="section-label text-xs font-semibold text-gray-400 uppercase tracking-wider">Components</p>
		</div>
		<ul class="px-4 space-y-1">
			<li>
				<a
					href="/ui-elements"
					class="nav-item flex items-center justify-between px-3 py-2 text-gray-600 rounded-md hover:bg-gray-50"
				>
					<div class="flex items-center gap-3">
						<svg
							xmlns="http://www.w3.org/2000/svg"
							class="h-5 w-5"
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
						<span class="nav-label text-sm">UI Elements</span>
					</div>
					<span class="nav-extra">
						<svg
							xmlns="http://www.w3.org/2000/svg"
							class="h-4 w-4"
							fill="none"
							viewBox="0 0 24 24"
							stroke="currentColor"
						>
							<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
						</svg>
					</span>
				</a>
			</li>
			<li>
				<a
					href="/forms"
					class="nav-item flex items-center justify-between px-3 py-2 text-gray-600 rounded-md hover:bg-gray-50"
				>
					<div class="flex items-center gap-3">
						<svg
							xmlns="http://www.w3.org/2000/svg"
							class="h-5 w-5"
							fill="none"
							viewBox="0 0 24 24"
							stroke="currentColor"
						>
							<path
								stroke-linecap="round"
								stroke-linejoin="round"
								stroke-width="2"
								d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"
							/>
						</svg>
						<span class="nav-label text-sm">Forms</span>
					</div>
					<span class="nav-extra px-2 py-0.5 text-xs font-semibold text-indigo-600 bg-indigo-100 rounded-full">6</span>
				</a>
			</li>
			<li>
				<a
					href="/tables"
					class="nav-item flex items-center justify-between px-3 py-2 text-gray-600 rounded-md hover:bg-gray-50"
				>
					<div class="flex items-center gap-3">
						<svg
							xmlns="http://www.w3.org/2000/svg"
							class="h-5 w-5"
							fill="none"
							viewBox="0 0 24 24"
							stroke="currentColor"
						>
							<path
								stroke-linecap="round"
								stroke-linejoin="round"
								stroke-width="2"
								d="M3 10h18M3 14h18m-9-4v8m-7 0h14a2 2 0 002-2V8a2 2 0 00-2-2H5a2 2 0 00-2 2v8a2 2 0 002 2z"
							/>
						</svg>
						<span class="nav-label text-sm">Tables</span>
					</div>
					<span class="nav-extra">
						<svg
							xmlns="http://www.w3.org/2000/svg"
							class="h-4 w-4"
							fill="none"
							viewBox="0 0 24 24"
							stroke="currentColor"
						>
							<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
						</svg>
					</span>
				</a>
			</li>
			<li>
				<a
					href="/charts"
					class="nav-item flex items-center justify-between px-3 py-2 text-gray-600 rounded-md hover:bg-gray-50"
				>
					<div class="flex items-center gap-3">
						<svg
							xmlns="http://www.w3.org/2000/svg"
							class="h-5 w-5"
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
						<span class="nav-label text-sm">Charts</span>
					</div>
					<span class="nav-extra">
						<svg
							xmlns="http://www.w3.org/2000/svg"
							class="h-4 w-4"
							fill="none"
							viewBox="0 0 24 24"
							stroke="currentColor"
						>
							<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
						</svg>
					</span>
				</a>
			</li>
			<li>
				<a
					href="/icons"
					class="nav-item flex items-center justify-between px-3 py-2 text-gray-600 rounded-md hover:bg-gray-50"
				>
					<div class="flex items-center gap-3">
						<svg
							xmlns="http://www.w3.org/2000/svg"
							class="h-5 w-5"
							fill="none"
							viewBox="0 0 24 24"
							stroke="currentColor"
						>
							<path
								stroke-linecap="round"
								stroke-linejoin="round"
								stroke-width="2"
								d="M14.828 14.828a4 4 0 01-5.656 0M9 10h.01M15 10h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
							/>
						</svg>
						<span class="nav-label text-sm">Icons</span>
					</div>
					<span class="nav-extra">
						<svg
							xmlns="http://www.w3.org/2000/svg"
							class="h-4 w-4"
							fill="none"
							viewBox="0 0 24 24"
							stroke="currentColor"
						>
							<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
						</svg>
					</span>
				</a>
			</li>
		</ul>
	</nav>

	<!-- Logout -->
	<div class="border-t border-gray-100 p-4">
		<button
			onclick={handleLogout}
			class="w-full flex items-center justify-center gap-2 px-3 py-2 text-sm font-medium text-red-600 rounded-md hover:bg-red-50"
		>
			<svg
				xmlns="http://www.w3.org/2000/svg"
				class="h-4 w-4"
				fill="none"
				viewBox="0 0 24 24"
				stroke="currentColor"
			>
				<path
					stroke-linecap="round"
					stroke-linejoin="round"
					stroke-width="2"
					d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a2 2 0 11-4 0v-1m0-8V7a2 2 0 114 0v1"
				/>
			</svg>
			<span class="nav-label">Log out</span>
		</button>
	</div>
</aside>

<!-- Mobile Overlay -->
{#if sidebarOpen}
	<div class="fixed inset-0 bg-black/40 z-30 lg:hidden" onclick={onToggleSidebar}></div>
{/if}


<style>
	aside.sidebar {
		width: 16rem;
	}

	@media (min-width: 1024px) {
		aside.sidebar {
			width: var(--sidebar-width-lg, 16rem);
		}

		aside.sidebar.collapsed {
			--sidebar-width-lg: 5rem;
		}

		aside.sidebar.expanded {
			--sidebar-width-lg: 16rem;
		}

		aside.sidebar.collapsed .section-label,
		aside.sidebar.collapsed .nav-label {
			display: none;
		}

		aside.sidebar.collapsed .nav-item {
			justify-content: center;
			padding-left: 0.5rem;
			padding-right: 0.5rem;
		}

		aside.sidebar.collapsed .nav-item > :first-child {
			justify-content: center;
		}

		aside.sidebar.collapsed .nav-extra {
			display: none;
		}
	}
</style>
