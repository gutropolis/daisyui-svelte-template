<script lang="ts">
	import { authStore } from '$lib/stores/auth';

	interface Props {
		sidebarOpen: boolean;
		onToggleSidebar: () => void;
	}

	const { sidebarOpen, onToggleSidebar } = $props<Props>();
	const iconButtonClasses =
		'inline-flex h-10 w-10 items-center justify-center rounded-full border border-slate-200 bg-white text-slate-500 transition hover:border-slate-300 hover:text-slate-700';

	// Get user initials
	const getUserInitials = (fullName: string | undefined) => {
		if (!fullName) return 'U';
		const names = fullName.split(' ');
		if (names.length >= 2) {
			return `${names[0][0]}${names[1][0]}`.toUpperCase();
		}
		return fullName[0].toUpperCase();
	};
</script>

<!-- Header -->
<header class="bg-white border-b border-slate-100 px-4 lg:px-8">
	<div class="flex h-[72px] items-center justify-between gap-4">
		<!-- Left cluster -->
		<div class="flex items-center gap-3 flex-1 min-w-0">
			<button
				class={`inline-flex h-10 w-10 items-center justify-center rounded-lg border border-slate-200 text-slate-500 transition hover:border-slate-300 hover:text-slate-700 ${
					sidebarOpen ? 'bg-slate-50' : 'bg-white'
				}`}
				onclick={onToggleSidebar}
				aria-label="Toggle sidebar"
				aria-pressed={sidebarOpen}
			>
				<svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
					<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16" />
				</svg>
			</button>

			<div class="relative flex-1 min-w-[220px]">
				<span class="absolute left-3 top-1/2 -translate-y-1/2 text-slate-400">
					<svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
						<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
					</svg>
				</span>
				<input
					type="text"
					placeholder="Search..."
					class="w-full rounded-full border border-slate-200 bg-slate-50/70 py-2 pl-10 pr-4 text-sm text-slate-700 placeholder:text-slate-400 focus:border-slate-300 focus:bg-white focus:outline-none"
				/>
			</div>
		</div>

		<!-- Right cluster -->
		<div class="flex items-center gap-2 text-slate-500">
			<button class={iconButtonClasses} aria-label="Language">
				<img src="https://flagcdn.com/w40/us.png" alt="US Flag" class="h-4 w-6 rounded object-cover" />
			</button>
			<button class={iconButtonClasses} aria-label="Grid view">
				<svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
					<path
						stroke-linecap="round"
						stroke-linejoin="round"
						stroke-width="2"
						d="M4 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2V6zM14 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2V6zM4 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2v-2zM14 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2v-2z"
					/>
				</svg>
			</button>
			<button class={iconButtonClasses} aria-label="Fullscreen">
				<svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
					<path
						stroke-linecap="round"
						stroke-linejoin="round"
						stroke-width="2"
						d="M4 8V4m0 0h4M4 4l5 5m11-1V4m0 0h-4m4 0l-5 5M4 16v4m0 0h4m-4 0l5-5m11 5l-5-5m5 5v-4m0 4h-4"
					/>
				</svg>
			</button>
			<button class={`${iconButtonClasses} relative`} aria-label="Notifications">
				<svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
					<path
						stroke-linecap="round"
						stroke-linejoin="round"
						stroke-width="2"
						d="M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6.002 6.002 0 00-4-5.659V5a2 2 0 10-4 0v.341C7.67 6.165 6 8.388 6 11v3.159c0 .538-.214 1.055-.595 1.436L4 17h5m6 0v1a3 3 0 11-6 0v-1m6 0H9"
					/>
				</svg>
				<span class="absolute -top-0.5 -right-0.5 h-4 w-4 rounded-full bg-rose-500 text-[10px] font-semibold text-white flex items-center justify-center">3</span>
			</button>
			<div class="dropdown dropdown-end">
				<button
					tabindex="0"
					class="flex items-center gap-2 rounded-full border border-slate-200 bg-white px-2.5 py-1 text-sm font-medium text-slate-600"
					aria-label="User menu"
				>
					{#if $authStore.user?.avatarUrl}
						<img src={$authStore.user.avatarUrl} alt="User avatar" class="h-9 w-9 rounded-full object-cover" />
					{:else}
						<div class="h-9 w-9 rounded-full bg-slate-200 text-slate-600 flex items-center justify-center text-sm font-semibold">
							{getUserInitials($authStore.user?.fullName)}
						</div>
					{/if}
					<span class="hidden sm:inline text-slate-700">{$authStore.user?.fullName || 'Marcus'}</span>
					<svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 text-slate-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
						<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
					</svg>
				</button>
			</div>
			<button class={iconButtonClasses} aria-label="Settings">
				<svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
					<path
						stroke-linecap="round"
						stroke-linejoin="round"
						stroke-width="2"
						d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1 1 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z"
					/>
					<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
				</svg>
			</button>
		</div>
	</div>
</header>

