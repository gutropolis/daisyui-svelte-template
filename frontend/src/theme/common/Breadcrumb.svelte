<script lang="ts">
	import { page } from '$app/stores';

	interface BreadcrumbItem {
		label: string;
		href?: string;
	}

	// Default breadcrumb items based on route
	function generateBreadcrumbs(): BreadcrumbItem[] {
		const path = $page.url.pathname;
		const segments = path.split('/').filter(Boolean);

		const breadcrumbs: BreadcrumbItem[] = [{ label: 'Dashboard', href: '/' }];

		if (segments.length > 0) {
			segments.forEach((segment, index) => {
				const href = '/' + segments.slice(0, index + 1).join('/');
				const label = segment.charAt(0).toUpperCase() + segment.slice(1).replace(/-/g, ' ');
				breadcrumbs.push({ label, href: index === segments.length - 1 ? undefined : href });
			});
		}

		return breadcrumbs;
	}

	$: breadcrumbs = generateBreadcrumbs();
	$: currentTitle = breadcrumbs[breadcrumbs.length - 1]?.label ?? 'Dashboard';
</script>

<section class="mb-6">
	<div class="flex flex-col gap-1">
		<p class="text-xs font-semibold uppercase tracking-widest text-gray-400">Overview</p>
		<h1 class="text-2xl font-semibold text-gray-900">{currentTitle}</h1>
	</div>
	<nav aria-label="Breadcrumb" class="mt-3 flex items-center gap-2 text-sm text-gray-500">
		{#each breadcrumbs as item, index}
			{#if item.href}
				<a
					href={item.href}
					class="flex items-center gap-2 rounded-full px-2 py-1 hover:bg-gray-100 hover:text-gray-900"
				>
					{#if index === 0}
						<svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
							<path
								stroke-linecap="round"
								stroke-linejoin="round"
								stroke-width="2"
								d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"
							/>
						</svg>
					{/if}
					{item.label}
				</a>
				<svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 text-gray-300" fill="none" viewBox="0 0 24 24" stroke="currentColor">
					<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
				</svg>
			{:else}
				<span class="text-gray-900 font-semibold">{item.label}</span>
			{/if}
		{/each}
	</nav>
</section>
