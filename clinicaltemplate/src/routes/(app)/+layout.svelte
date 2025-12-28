<script lang="ts">
	import { onMount } from 'svelte';
	import '../layout.css';
	import {
		APPS_ALERTS_ROUTE,
		APPS_API_ROUTE,
		APPS_CALENDAR_ROUTE,
		APPS_COMMENT_LOG_ROUTE,
		APPS_COMPARISON_ROUTE,
		APPS_DASHBOARDS_ROUTE,
		APPS_EMAIL_LOGGING_ROUTE,
		APPS_FILES_ROUTE,
		APPS_IMPORT_ROUTE,
		APPS_LOCKING_ROUTE,
		APPS_LOGGING_ROUTE,
		APPS_MULTI_LANGUAGE_ROUTE,
		APPS_QUALITY_ROUTE,
		APPS_REPORTS_ROUTE,
		APPS_USER_RIGHTS_ROUTE,
		DASHBOARD_ROUTE,
		DATA_RECORDS_ROUTE,
		DATA_STATUS_ROUTE,
		HELP_ADVANCED_ROUTE,
		HELP_FAQ_ROUTE,
		HELP_FEATURE_REQUEST_ROUTE,
		HELP_VIDEOS_ROUTE,
		LOGOUT_ROUTE,
		MESSENGER_ROUTE,
		MODULE_LOGS_ROUTE,
		MODULE_MEDICAL_HISTORY_ROUTE,
		MODULE_MMSE_ROUTE,
		MODULE_RANDOMISATION_ROUTE,
		MODULE_SITE2_LOGS_ROUTE,
		MY_PROJECTS_ROUTE,
		PROJECT_CODEBOOK_ROUTE,
		PROJECT_DATA_STATUS_ROUTE,
		PROJECT_DESIGNER_ROUTE,
		PROJECT_DETAIL_DASHBOARD_ROUTE,
		PROJECT_DETAIL_SETUP_ROUTE,
		PROJECT_DETAIL_SETUP_ROUTE2,
		PROJECT_DICTIONARY_ROUTE,
		PROJECT_EVENTS_ROUTE,
		PROJECT_HOME_ROUTE,
		PROJECT_SETUP_SHORTCUT_ROUTE,
		PROJECTS_ROUTE,
		REPORT_MEDICAL_HISTORY_ROUTE,
		REPORT_MMSE_ROUTE,
		REPORT_RANDOMISATION_ROUTE,
		SETUP_DESIGN_INSTRUMENTS_ROUTE,
		SUPPORT_CONTACT_ROUTE
	} from '$lib/enums/routes';

	interface QuickLink {
		label: string;
		href: string;
		icon: string;
		accent?: boolean;
	}

	interface MenuItem {
		label: string;
		href: string;
		icon?: string;
		description?: string;
		badge?: string;
		prefix?: string;
	}

	interface SectionAction {
		label: string;
		href: string;
	}

	interface MenuSection {
		title: string;
		subtitle?: string;
		badge?: string;
		action?: SectionAction;
		items: MenuItem[];
	}

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

	const quickLinks: QuickLink[] = [
		{ label: 'My Projects', href: MY_PROJECTS_ROUTE, icon: 'fas fa-folder-open' },
		//{ label: 'REDCap Messenger', href: MESSENGER_ROUTE, icon: 'fas fa-comment-dots' },
		{ label: 'Contact Proxmed administrator', href: SUPPORT_CONTACT_ROUTE, icon: 'fas fa-envelope-open-text', accent: true }
	];

	const menuSections: MenuSection[] = [
		{
			title: 'Project Home and Design',
			badge: 'Development',
			items: [
				{ label: 'Home', href: DASHBOARD_ROUTE, icon: 'fas fa-home' },
				{ label: 'Setup', href: PROJECT_DETAIL_SETUP_ROUTE, icon: 'fas fa-cog' },
				//{ label: 'Codebook', href: PROJECT_CODEBOOK_ROUTE, icon: 'fas fa-book' },
				{ label: 'Designer', href: SETUP_DESIGN_INSTRUMENTS_ROUTE, icon: 'fas fa-pencil-ruler' },
				{ label: 'Events', href: PROJECT_DETAIL_SETUP_ROUTE2, icon: 'fas fa-calendar-alt' },
				//{ label: 'Dictionary', href: PROJECT_DICTIONARY_ROUTE, icon: 'fas fa-database' }
			]
		},
		{
			title: 'Data Collection',
			subtitle: '',
			items: [
				{
					label: 'Record Status Dashboard',
					href: PROJECT_DATA_STATUS_ROUTE,
					icon: 'fas fa-clipboard-check',
					description: 'View data collection status of all records'
				},
				{
					label: 'Add / Edit Records',
					href: DATA_RECORDS_ROUTE,
					icon: 'fas fa-edit',
					description: 'Create new records or edit/view existing ones'
				}
			]
		},
		{
			title: 'Applications',
			items: [
				{ label: 'Project Dashboards', href: PROJECT_DETAIL_DASHBOARD_ROUTE, icon: 'fas fa-th-large' },
				{ label: 'Alerts & Notifications', href: APPS_ALERTS_ROUTE, icon: 'fas fa-bell' },
				//{ label: 'Multi-Language Management', href: APPS_MULTI_LANGUAGE_ROUTE, icon: 'fas fa-language' },
				//{ label: 'Calendar', href: APPS_CALENDAR_ROUTE, icon: 'fas fa-calendar' },
				{ label: 'Data Exports, Reports, and Stats', href: APPS_REPORTS_ROUTE, icon: 'fas fa-chart-bar' },
				{ label: 'Data Import Tool', href: APPS_IMPORT_ROUTE, icon: 'fas fa-download' },
				{ label: 'Data Comparison Tool', href: APPS_COMPARISON_ROUTE, icon: 'fas fa-not-equal' },
				{ label: 'Logging', href: APPS_LOGGING_ROUTE, icon: 'fas fa-clipboard-list' },
				{ label: 'Email Logging', href: APPS_EMAIL_LOGGING_ROUTE, icon: 'fas fa-envelope' },
				{ label: 'Field Comment Log', href: APPS_COMMENT_LOG_ROUTE, icon: 'fas fa-comments' },
				{ label: 'File Repository', href: APPS_FILES_ROUTE, icon: 'fas fa-folder' },
				{ label: 'User Rights and DAGs', href: APPS_USER_RIGHTS_ROUTE, icon: 'fas fa-user-shield' },
				{ label: 'Customize & Manage Locking/E-signatures', href: APPS_LOCKING_ROUTE, icon: 'fas fa-lock' },
				{ label: 'Data Quality', href: APPS_QUALITY_ROUTE, icon: 'fas fa-check-circle' },
				{ label: 'API and API Playground', href: APPS_API_ROUTE, icon: 'fas fa-code' }
			]
		},
		/*
		{
			title: 'Reports',
			subtitle: 'Search · Organize · Edit',
			items: [
				{ label: 'randomisation', href: REPORT_RANDOMISATION_ROUTE, prefix: '1)' },
				{ label: 'medical history', href: REPORT_MEDICAL_HISTORY_ROUTE, prefix: '2)' },
				{ label: 'mmse test', href: REPORT_MMSE_ROUTE, prefix: '3)' }
			]
		},
		{
			title: 'External Modules',
			action: { label: 'View Logs', href: MODULE_LOGS_ROUTE },
			items: [
				{ label: 'randomisation', href: MODULE_RANDOMISATION_ROUTE, prefix: '1)' },
				{ label: 'medical history', href: MODULE_MEDICAL_HISTORY_ROUTE, prefix: '2)' },
				{ label: 'mmse test', href: MODULE_MMSE_ROUTE, prefix: '3)' }
			]
		},
		{
			title: 'External Modules',
			action: { label: 'View Logs', href: MODULE_SITE2_LOGS_ROUTE },
			items: [
				{ label: 'randomisation', href: MODULE_RANDOMISATION_ROUTE, prefix: '1)' },
				{ label: 'medical history', href: MODULE_MEDICAL_HISTORY_ROUTE, prefix: '2)' },
				{ label: 'mmse test', href: MODULE_MMSE_ROUTE, prefix: '3)' }
			]
		},
		*/
		{
			title: 'Help & Information',
			items: [
				{ label: 'Help & FAQ', href: HELP_FAQ_ROUTE, icon: 'fas fa-question-circle' },
				{ label: 'Video Tutorials', href: HELP_VIDEOS_ROUTE, icon: 'fas fa-video' },
				//{ label: 'Learn Advanced Design Features', href: HELP_ADVANCED_ROUTE, icon: 'fas fa-graduation-cap' },
				{ label: 'Suggest a New Feature', href: HELP_FEATURE_REQUEST_ROUTE, icon: 'fas fa-lightbulb' }
			]
		}
	];

	const contactActions = [
		{ label: 'Contact Proxmed administrator', href: SUPPORT_CONTACT_ROUTE, icon: 'fas fa-comments' }
	];

	let { children } = $props();
</script>

<div class="flex h-screen w-screen overflow-hidden bg-gray-50">
	<!-- Sidebar -->
	<aside
		class={`w-64 bg-white border-r border-gray-200 flex flex-col fixed md:relative top-0 left-0 h-full z-40 transition-transform duration-300 transform ${
			sidebarOpen ? 'translate-x-0' : '-translate-x-full md:translate-x-0'
		}`}
	>
		<!-- Logo Section -->
		<div class="p-6 border-b border-gray-200 shrink-0">
			<div class="flex items-center">
				<div
					class="w-10 h-10 bg-linear-to-br from-red-500 to-red-600 rounded-lg flex items-center justify-center mr-3 shadow-lg"
				>
					<i class="fas fa-database text-white text-lg"></i>
				</div>
				<span class="text-xl font-bold text-gray-800">Proxmed</span>
			</div>
		</div>

		<!-- Navigation Menu -->
		<nav class="flex-1 overflow-y-auto custom-scrollbar py-4">
			<div class="mb-6 px-4">
				<div class="rounded-xl border border-gray-200 bg-gray-50 p-4">
					<p class="text-xs font-semibold text-gray-700 flex items-center gap-2">
						<i class="fas fa-lock text-gray-500"></i>
						Logged in as <span class="text-gray-900">Ismanandhar</span>
					</p>
					<p class="mt-2 text-xs text-blue-600">
						<a href={LOGOUT_ROUTE} class="hover:underline">Log out</a>
					</p>
				</div>
			</div>

			<div class="px-4 mb-6 space-y-2">
				{#each quickLinks as link}
					<a
						href={link.href}
						class={`flex items-center gap-3 rounded-lg border px-4 py-2 text-sm font-medium transition-colors ${
							link.accent
								? 'border-red-200 bg-red-50 text-red-700 hover:bg-red-100'
								: 'border-gray-200 bg-white text-gray-700 hover:bg-gray-50'
						}`}
					>
						<i class={`${link.icon} text-gray-500`}></i>
						<span>{link.label}</span>
					</a>
				{/each}
			</div>

			{#each menuSections as section}
				<div class="mb-6">
					<div class="flex items-center justify-between px-6 mb-2">
						<div>
							<p class="text-xs font-semibold uppercase tracking-widest text-gray-400">{section.title}</p>
							{#if section.subtitle}
								<p class="text-xs text-gray-500 mt-1">{section.subtitle}</p>
							{/if}
						</div>
						<div class="flex items-center gap-2">
							{#if section.badge}
								<span class="rounded-full bg-gray-100 px-3 py-1 text-[11px] font-semibold text-gray-600">{section.badge}</span> 
							{/if}
							{#if section.action}
								<a href={section.action.href} class="text-xs font-semibold text-blue-600 hover:underline">{section.action.label}</a>
							{/if}
						</div>
					</div>
					<ul class="px-3 space-y-1">
						{#each section.items as item}
							<li>
								<a
									href={item.href}
									class="flex items-start gap-3 rounded-lg px-4 py-2 text-sm text-gray-700 hover:bg-blue-50 hover:text-blue-700 transition-colors"
								>
									{#if item.icon}
										<i class={`${item.icon} mt-1 text-gray-400`}></i>
									{:else if item.prefix}
										<span class="text-xs font-semibold text-gray-500 mt-0.5">{item.prefix}</span>
									{/if}
									<div class="flex flex-col">
										<span class="font-medium">{item.label}</span>
										{#if item.description}
											<p class="text-xs text-gray-500">{item.description}</p>
										{/if}
									</div>
								</a>
							</li>
						{/each}
					</ul>
				</div>
			{/each}

			<div class="px-4 pb-6">
				{#each contactActions as action}
					<a
						href={action.href}
						class="flex items-center justify-center gap-2 rounded-lg bg-blue-600 px-4 py-3 text-sm font-semibold text-white shadow hover:bg-blue-700"
					>
						<i class={action.icon}></i>
						{action.label}
					</a>
				{/each}
			</div>
		</nav>

		<!-- User Profile Section -->
		<div class="p-4 border-t border-gray-200 bg-gray-50 shrink-0">
			<div class="flex items-center px-2">
				<div class="relative">
					<img
						src="https://picsum.photos/seed/user123/40/40.jpg"
						alt="User"
						class="w-10 h-10 rounded-full ring-2 ring-white shadow-sm"
					/>
					<div class="absolute bottom-0 right-0 w-3 h-3 bg-green-500 rounded-full border-2 border-white"
					></div>
				</div>
				<div class="ml-3 flex-1 min-w-0">
					<p class="text-sm font-semibold text-gray-700">Admin User</p>
					<p class="text-xs text-gray-500">admin@redcap.com</p>
				</div>
				<button class="p-2 hover:bg-gray-200 rounded-lg transition-colors shrink-0" aria-label="Sign out">
					<i class="fas fa-sign-out-alt text-gray-500 text-sm"></i>
				</button>
			</div>
		</div>
	</aside>

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
