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
	<div class="p-6 lg:p-2 flex items-center gap-2 justify-center lg:justify-center">
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
			class:block={sidebarOpen}>WhatsMark</span
		>
	</div>

	<!-- Navigation Menu -->
	<nav class="flex-1 px-1 lg:px-3 py-2 overflow-y-auto">
		<ul class="space-y-1">
			<li>
				<a
					href="/"
					class="flex items-center justify-center lg:justify-start gap-0 lg:gap-3 px-2 lg:px-3 py-2.5 text-gray-600 hover:bg-gray-100 rounded-lg transition-colors"
					title="Dashboard"
				>
					<svg
						xmlns="http://www.w3.org/2000/svg"
						class="h-8 w-8 lg:h-6 lg:w-6 flex-shrink-0"
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
					<span class="text-sm hidden" class:hidden={!sidebarOpen}>Dashboard</span>
				</a>
			</li>
			<li>
				<a
					href="/connect"
					class="flex items-center justify-center lg:justify-start gap-0 lg:gap-3 px-2 lg:px-3 py-2.5 text-gray-600 hover:bg-gray-100 rounded-lg transition-colors"
					title="Connect WABA"
				>
					<svg
						xmlns="http://www.w3.org/2000/svg"
						class="h-8 w-8 lg:h-6 lg:w-6 flex-shrink-0"
						fill="none"
						viewBox="0 0 24 24"
						stroke="currentColor"
					>
						<path
							stroke-linecap="round"
							stroke-linejoin="round"
							stroke-width="2"
							d="M13.828 10.172a4 4 0 00-5.656 0l-4 4a4 4 0 105.656 5.656l1.102-1.101m-.758-4.899a4 4 0 005.656 0l4-4a4 4 0 00-5.656-5.656l-1.1 1.1"
						/>
					</svg>
					<span class="text-sm hidde" class:hidden={!sidebarOpen}>Connect WABA</span>
				</a>
			</li>
			<li>
				<a
					href="/chat"
					class="flex items-center justify-center lg:justify-start gap-0 lg:gap-3 px-2 lg:px-3 py-2.5 text-gray-600 hover:bg-gray-100 rounded-lg transition-colors"
					title="Chat"
				>
					<svg
						xmlns="http://www.w3.org/2000/svg"
						class="h-8 w-8 lg:h-6 lg:w-6 flex-shrink-0"
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
					<span class="text-sm hidden" class:hidden={!sidebarOpen}>Chat</span>
				</a>
			</li>
			<li>
				<a
					href="/bot-flow"
					class="flex items-center justify-center lg:justify-start gap-0 lg:gap-3 px-2 lg:px-3 py-2.5 bg-indigo-50 text-indigo-600 rounded-lg transition-colors"
					title="Bot Flow"
				>
					<svg
						xmlns="http://www.w3.org/2000/svg"
						class="h-8 w-8 lg:h-6 lg:w-6 flex-shrink-0"
						fill="none"
						viewBox="0 0 24 24"
						stroke="currentColor"
					>
						<path
							stroke-linecap="round"
							stroke-linejoin="round"
							stroke-width="2"
							d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10"
						/>
					</svg>
					<span class="text-sm font-medium hidden" class:hidden={!sidebarOpen}>Bot Flow</span>
				</a>
			</li>
		</ul>

		<!-- Section Divider -->
		<div class="mt-6 mb-3 px-2 lg:px-3 hidden" class:hidden={!sidebarOpen}>
			<h3 class="text-xs font-semibold text-gray-400 uppercase tracking-wider">My Subscription</h3>
		</div>
		<ul class="space-y-1">
			<li>
				<a
					href="/subscription"
					class="flex items-center justify-center lg:justify-start gap-0 lg:gap-3 px-2 lg:px-3 py-2.5 text-gray-600 hover:bg-gray-100 rounded-lg transition-colors"
					title="Subscription"
				>
					<svg
						xmlns="http://www.w3.org/2000/svg"
						class="h-8 w-8 lg:h-6 lg:w-6 flex-shrink-0"
						fill="none"
						viewBox="0 0 24 24"
						stroke="currentColor"
					>
						<path
							stroke-linecap="round"
							stroke-linejoin="round"
							stroke-width="2"
							d="M3 10h18M7 15h1m4 0h1m-7 4h12a3 3 0 003-3V8a3 3 0 00-3-3H6a3 3 0 00-3 3v8a3 3 0 003 3z"
						/>
					</svg>
					<span class="text-sm hidden" class:hidden={!sidebarOpen}>Subscription</span>
				</a>
			</li>
			<li>
				<a
					href="/invoices"
					class="flex items-center justify-center lg:justify-start gap-0 lg:gap-3 px-2 lg:px-3 py-2.5 text-gray-600 hover:bg-gray-100 rounded-lg transition-colors"
					title="Invoices"
				>
					<svg
						xmlns="http://www.w3.org/2000/svg"
						class="h-8 w-8 lg:h-6 lg:w-6 flex-shrink-0"
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
					<span class="text-sm hidden" class:hidden={!sidebarOpen}>Invoices</span>
				</a>
			</li>
		</ul>

		<!-- Contact Section -->
		<div class="mt-6 mb-3 px-2 lg:px-3 hidden" class:hidden={!sidebarOpen}>
			<h3 class="text-xs font-semibold text-gray-400 uppercase tracking-wider">Contact</h3>
		</div>
		<ul class="space-y-1">
			<li>
				<a
					href="/contact"
					class="flex items-center justify-center lg:justify-start gap-0 lg:gap-3 px-2 lg:px-3 py-2.5 text-gray-600 hover:bg-gray-100 rounded-lg transition-colors"
					title="Contact"
				>
					<svg
						xmlns="http://www.w3.org/2000/svg"
						class="h-8 w-8 lg:h-6 lg:w-6 flex-shrink-0"
						fill="none"
						viewBox="0 0 24 24"
						stroke="currentColor"
					>
						<path
							stroke-linecap="round"
							stroke-linejoin="round"
							stroke-width="2"
							d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z"
						/>
					</svg>
					<span class="text-sm hidden" class:hidden={!sidebarOpen}>Contact</span>
				</a>
			</li>
		</ul>

		<!-- Templates Section -->
		<div class="mt-6 mb-3 px-2 lg:px-3 hidden" class:hidden={!sidebarOpen}>
			<h3 class="text-xs font-semibold text-gray-400 uppercase tracking-wider">Templates</h3>
		</div>
		<ul class="space-y-1">
			<li>
				<a
					href="/templates"
					class="flex items-center justify-center lg:justify-start gap-0 lg:gap-3 px-2 lg:px-3 py-2.5 text-gray-600 hover:bg-gray-100 rounded-lg transition-colors"
					title="Templates"
				>
					<svg
						xmlns="http://www.w3.org/2000/svg"
						class="h-8 w-8 lg:h-6 lg:w-6 flex-shrink-0"
						fill="none"
						viewBox="0 0 24 24"
						stroke="currentColor"
					>
						<path
							stroke-linecap="round"
							stroke-linejoin="round"
							stroke-width="2"
							d="M7 21h10a2 2 0 002-2V9.414a1 1 0 00-.293-.707l-5.414-5.414A1 1 0 0012.586 3H7a2 2 0 00-2 2v14a2 2 0 002 2z"
						/>
					</svg>
					<span class="text-sm hidden" class:hidden={!sidebarOpen}>Templates</span>
				</a>
			</li>
		</ul>

		<!-- Marketing Section -->
		<div class="mt-6 mb-3 px-2 lg:px-3 hidden" class:hidden={!sidebarOpen}>
			<h3 class="text-xs font-semibold text-gray-400 uppercase tracking-wider">Marketing</h3>
		</div>
		<ul class="space-y-1">
			<li>
				<a
					href="/campaign"
					class="flex items-center justify-center lg:justify-start gap-0 lg:gap-3 px-2 lg:px-3 py-2.5 text-gray-600 hover:bg-gray-100 rounded-lg transition-colors"
					title="Campaign"
				>
					<svg
						xmlns="http://www.w3.org/2000/svg"
						class="h-8 w-8 lg:h-6 lg:w-6 flex-shrink-0"
						fill="none"
						viewBox="0 0 24 24"
						stroke="currentColor"
					>
						<path
							stroke-linecap="round"
							stroke-linejoin="round"
							stroke-width="2"
							d="M11 5.882V19.24a1.76 1.76 0 01-3.417.592l-2.147-6.15M18 13a3 3 0 100-6M5.436 13.683A4.001 4.001 0 017 6h1.832c4.1 0 7.625-1.234 9.168-3v14c-1.543-1.766-5.067-3-9.168-3H7a3.988 3.988 0 01-1.564-.317z"
						/>
					</svg>
					<span class="text-sm hidden" class:hidden={!sidebarOpen}>Campaign</span>
				</a>
			</li>
			<li>
				<a
					href="/message-bot"
					class="flex items-center justify-center lg:justify-start gap-0 lg:gap-3 px-2 lg:px-3 py-2.5 text-gray-600 hover:bg-gray-100 rounded-lg transition-colors"
					title="Message Bot"
				>
					<svg
						xmlns="http://www.w3.org/2000/svg"
						class="h-8 w-8 lg:h-6 lg:w-6 flex-shrink-0"
						fill="none"
						viewBox="0 0 24 24"
						stroke="currentColor"
					>
						<path
							stroke-linecap="round"
							stroke-linejoin="round"
							stroke-width="2"
							d="M8 10h.01M12 10h.01M16 10h.01M9 16H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-5l-5 5v-5z"
						/>
					</svg>
					<span class="text-sm hidden" class:hidden={!sidebarOpen}>Message Bot</span>
				</a>
			</li>
			<li>
				<a
					href="/template-bot"
					class="flex items-center justify-center lg:justify-start gap-0 lg:gap-3 px-2 lg:px-3 py-2.5 text-gray-600 hover:bg-gray-100 rounded-lg transition-colors"
					title="Template Bot"
				>
					<svg
						xmlns="http://www.w3.org/2000/svg"
						class="h-8 w-8 lg:h-6 lg:w-6 flex-shrink-0"
						fill="none"
						viewBox="0 0 24 24"
						stroke="currentColor"
					>
						<path
							stroke-linecap="round"
							stroke-linejoin="round"
							stroke-width="2"
							d="M7 8h10M7 12h4m1 8l-4-4H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-3l-4 4z"
						/>
					</svg>
					<span class="text-sm hidden" class:hidden={!sidebarOpen}>Template Bot</span>
				</a>
			</li>
		</ul>

		<!-- Setup -->
		<ul class="space-y-1 mt-6">
			<li>
				<a
					href="/setup"
					class="flex items-center justify-center lg:justify-start gap-0 lg:gap-3 px-2 lg:px-3 py-2.5 text-gray-600 hover:bg-gray-100 rounded-lg transition-colors"
					title="Setup"
				>
					<svg
						xmlns="http://www.w3.org/2000/svg"
						class="h-8 w-8 lg:h-6 lg:w-6 flex-shrink-0"
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
		</ul>
	</nav>
</aside>

<!-- Mobile Overlay -->
{#if sidebarOpen}
	<!-- svelte-ignore a11y_click_events_have_key_events -->
	<!-- svelte-ignore a11y_no_static_element_interactions -->
	<div class="fixed inset-0 bg-black bg-opacity-50 z-30 lg:hidden" onclick={onToggleSidebar}></div>
{/if}
