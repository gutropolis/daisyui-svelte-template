<script lang="ts"> 
    import { authUser }   from '$lib/stores/app';
	interface Props {
		sidebarOpen: boolean;
		onToggleSidebar: () => void;
	}

	 

	let { sidebarOpen, onToggleSidebar } = $props<Props>();
	const iconButtonClasses =
		'inline-flex h-11 w-11 items-center justify-center rounded-2xl border border-slate-200/70 bg-white/70 text-slate-600 shadow-sm transition hover:-translate-y-0.5 hover:border-slate-300 hover:shadow-lg dark:border-white/10 dark:bg-white/10 dark:text-slate-200';

	const getUserInitials = (fullName: string | undefined) => {
		if (!fullName) return 'U';
		const names = fullName.split(' ');
		if (names.length >= 2) {
			return `${names[0][0]}${names[1][0]}`.toUpperCase();
		}
		return fullName[0].toUpperCase();
	};
</script>
 
<header class="sticky top-0 z-40   py-1 text-slate-900 dark:text-slate-100">
	<div
		class="mx-auto flex w-full items-center gap-6 border border-slate-200/80 bg-white/80 px-6 py-3 shadow-[0_18px_50px_rgba(15,23,42,0.12)] backdrop-blur-2xl transition dark:border-white/10 dark:bg-slate-900/70 dark:shadow-[0_18px_50px_rgba(2,6,23,0.7)]"
	>
		<div class="flex flex-1 items-center gap-4">
			<button
				class={`${
					sidebarOpen ? 'bg-white text-slate-900 dark:bg-white/20 dark:text-white' : 'bg-white/70 dark:bg-white/10'
				} inline-flex h-11 w-11 items-center justify-center rounded-2xl border border-slate-200/70 text-slate-700 shadow-sm transition hover:-translate-y-0.5 hover:border-slate-300 hover:shadow-lg dark:border-white/15 dark:text-slate-100`}
				onclick={onToggleSidebar}
				aria-label="Toggle sidebar"
				aria-pressed={sidebarOpen}
			>
				<svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
					<path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M4 6h16M4 12h16M4 18h16" />
				</svg>
			</button>
			<a href="/" class="flex items-center gap-3">
			 
				<div>
					<p class="text-lg font-semibold tracking-wide">Clinical Trial</p>
					<p class="text-xs text-slate-500 dark:text-slate-400">Operational Console</p>
				</div>
			</a>
		</div>

		<div class="hidden flex-1 justify-center md:flex">
			<div class="flex w-full max-w-md items-center gap-3 rounded-2xl border border-slate-200/70 bg-white/60 px-4 py-2 text-sm text-slate-500 shadow-inner dark:border-white/10 dark:bg-white/5 dark:text-slate-300">
				<svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
					<path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
				</svg>
				<input type="text" placeholder="Search anything…" class="flex-1 bg-transparent text-base-content/80 outline-none dark:text-white" />
			</div>
		</div>

		<div class="flex flex-1 items-center justify-end gap-3">
			<button class={iconButtonClasses} aria-label="Notifications">
				<span class="absolute -right-0.5 -top-0.5 inline-flex h-4 min-w-[1rem] items-center justify-center rounded-full bg-rose-500 px-1 text-[10px] font-semibold text-white">3</span>
				<svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
					<path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M15 17h5l-1.4-1.4A2 2 0 0118 14v-3a6 6 0 10-12 0v3c0 .53-.21 1.04-.6 1.42L4 17h5m6 0v1a3 3 0 11-6 0v-1" />
				</svg>
			</button>
			<div class="dropdown dropdown-end">
				<button tabindex="0" class="flex items-center gap-3 rounded-[999px] border border-slate-200/70 bg-white/70 px-2.5 py-1.5 text-left text-sm font-medium shadow-sm transition hover:-translate-y-0.5 hover:border-slate-300 hover:shadow-lg dark:border-white/10 dark:bg-white/10">
					{#if $authUser?.fullName}
						<div class="avatar">
							<div class="w-10 rounded-full">
								<img src={$authUser?.avatar || 'https://picsum.photos/seed/user/80/80'} alt="User avatar" />
							</div>
						</div>
					{:else}
						<div class="avatar placeholder">
							<div class="w-10 rounded-full bg-gradient-to-br from-indigo-500 to-sky-400 text-white">
								<span class="text-sm font-semibold">{getUserInitials($authUser?.firstName)}</span>
							</div>
						</div>
					{/if}
					<div class="hidden text-left leading-tight sm:block">
						<p class="text-sm font-semibold">{$authUser?.fullName || 'Amelia Carter'}</p>
						<p class="text-xs text-slate-500 dark:text-slate-400">{$authUser?.role || 'Product Ops'}</p>
					</div>
					<svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 text-slate-500 dark:text-slate-300" fill="none" viewBox="0 0 24 24" stroke="currentColor">
						<path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M19 9l-7 7-7-7" />
					</svg>
				</button>
				<div
					tabindex="0"
					class="dropdown-content mt-3 w-60 rounded-3xl border border-slate-200/70 bg-white/95 p-2 text-sm shadow-2xl backdrop-blur-xl transition dark:border-white/10 dark:bg-slate-900/90"
				>
					<ul class="menu menu-sm gap-1 text-slate-600 dark:text-slate-200">
						<li><a class="rounded-2xl px-3 py-2 hover:bg-slate-100/80 dark:hover:bg-white/10"><span>My Profile</span></a></li>
						<li><a class="rounded-2xl px-3 py-2 hover:bg-slate-100/80 dark:hover:bg-white/10">Account Settings</a></li>
						<li><a class="rounded-2xl px-3 py-2 hover:bg-slate-100/80 dark:hover:bg-white/10">Billing</a></li>
						<li><a class="rounded-2xl px-3 py-2 hover:bg-slate-100/80 dark:hover:bg-white/10">Team</a></li>
						<li><a class="rounded-2xl px-3 py-2 hover:bg-slate-100/80 dark:hover:bg-white/10">Support</a></li>
					</ul>
					<div class="my-1 h-px bg-gradient-to-r from-transparent via-slate-200 to-transparent dark:via-white/10"></div>
					<button class="w-full rounded-2xl bg-rose-500/10 px-3 py-2 text-center text-rose-600 transition hover:bg-rose-500/20 dark:bg-rose-500/20 dark:text-rose-100">
						Log out
					</button>
				</div>
			</div>
		</div>
	</div>
</header>
