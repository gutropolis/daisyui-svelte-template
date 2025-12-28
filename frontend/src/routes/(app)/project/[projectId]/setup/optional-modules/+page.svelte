<script lang="ts">
	import { onMount } from 'svelte';
	import { page } from '$app/stores';
	import { PROJECT_DETAIL_SETUP_ROUTE } from '$lib/enums/routes';
	import { resolveProjectRoute } from '$lib/utils/routes';

	interface Module {
		id: number;
		name: string;
		description: string;
		category: 'communication' | 'automation' | 'advanced';
		enabled: boolean;
		icon: string;
	}

	let modules: Module[] = [
		{
			id: 1,
			name: 'Repeating instruments and events',
			description: 'Allow instruments to be repeated multiple times',
			category: 'advanced',
			enabled: true,
			icon: 'fas fa-repeat'
		},
		{
			id: 2,
			name: 'Auto-numbering for records',
			description: 'Automatically generate record IDs',
			category: 'automation',
			enabled: false,
			icon: 'fas fa-hashtag'
		},
		{
			id: 3,
			name: 'Scheduling module (longitudinal only)',
			description: 'Schedule events and notifications',
			category: 'automation',
			enabled: false,
			icon: 'fas fa-calendar-check'
		},
		{
			id: 4,
			name: 'Randomization module',
			description: 'Randomly assign participants to groups',
			category: 'advanced',
			enabled: false,
			icon: 'fas fa-random'
		},
		{
			id: 5,
			name: 'Designate an email field for communications',
			description: 'Use a field for survey invitations and alerts',
			category: 'communication',
			enabled: false,
			icon: 'fas fa-envelope'
		},
		{
			id: 6,
			name: 'Twilio SMS and Voice Call services',
			description: 'Send SMS and voice calls to participants',
			category: 'communication',
			enabled: false,
			icon: 'fas fa-phone'
		},
		{
			id: 7,
			name: 'MosIO SMS services for surveys and alerts',
			description: 'SMS notifications via MosIO',
			category: 'communication',
			enabled: false,
			icon: 'fas fa-mobile-alt'
		},
		{
			id: 8,
			name: 'SendGrid Template email services',
			description: 'Professional email templates',
			category: 'communication',
			enabled: false,
			icon: 'fas fa-envelope-open'
		}
	];

	const toggleModule = (id: number) => {
		const module = modules.find(m => m.id === id);
		if (module) {
			module.enabled = !module.enabled;
		}
	};

	const getCategoryLabel = (category: string) => {
		switch (category) {
			case 'communication':
				return 'Communication';
			case 'automation':
				return 'Automation';
			case 'advanced':
				return 'Advanced Features';
			default:
				return 'Other';
		}
	};

	const getCategoryColor = (category: string) => {
		switch (category) {
			case 'communication':
				return 'bg-[#0b3a7a]/10 text-[#0b3a7a]';
			case 'automation':
				return 'bg-green-100 text-green-800';
			case 'advanced':
				return 'bg-purple-100 text-purple-800';
			default:
				return 'bg-gray-100 text-gray-800';
		}
	};

	const projectId = $derived($page.params.projectId ?? '1');
	const setupOverviewRoute = $derived(resolveProjectRoute(PROJECT_DETAIL_SETUP_ROUTE, projectId));

	// Group modules by category
	const communicationModules = $derived(modules.filter(m => m.category === 'communication'));
	const automationModules = $derived(modules.filter(m => m.category === 'automation'));
	const advancedModules = $derived(modules.filter(m => m.category === 'advanced'));
</script>

<div class="p-6 space-y-6">
	<!-- Header -->
	<div>
		<a href={setupOverviewRoute} class="flex items-center gap-2 text-[#0b3a7a] hover:text-[#082654] text-sm font-medium mb-4">
			<i class="fas fa-arrow-left"></i>Back to Setup
		</a>
		<h1 class="text-3xl font-bold text-gray-800 mb-2">Enable Optional Modules and Customizations</h1>
		<p class="text-gray-600">Configure advanced features and integrations for your project</p>
	</div>

	<!-- Communication Modules -->
	<div class="space-y-4">
		<h2 class="text-xl font-bold text-gray-800 flex items-center gap-2">
			<i class="fas fa-envelope text-[#0b3a7a]"></i>
			Communication Modules
		</h2>

		<div class="space-y-3">
			{#each communicationModules as module (module.id)}
				<div class="bg-white rounded-lg shadow p-6 flex items-start justify-between hover:shadow-md transition-shadow">
					<div class="flex items-start gap-4 flex-1">
						<div class="w-12 h-12 rounded-lg bg-[#0b3a7a]/10 flex items-center justify-center flex-shrink-0">
							<i class={`${module.icon} text-[#0b3a7a] text-lg`}></i>
						</div>
						<div class="flex-1">
							<h3 class="font-bold text-gray-800">{module.name}</h3>
							<p class="text-sm text-gray-600 mt-1">{module.description}</p>
						</div>
					</div>

					<label class="relative inline-flex items-center cursor-pointer ml-4 flex-shrink-0">
						<input
							type="checkbox"
							checked={module.enabled}
							on:change={() => toggleModule(module.id)}
							class="sr-only peer"
						/>
						<div class="w-11 h-6 bg-gray-300 peer-focus:outline-none peer-focus:ring-4 peer-focus:ring-[#0b3a7a]/30 rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:bg-[#0b3a7a]"></div>
					</label>
				</div>
			{/each}
		</div>
	</div>

	<!-- Automation Modules -->
	<div class="space-y-4">
		<h2 class="text-xl font-bold text-gray-800 flex items-center gap-2">
			<i class="fas fa-cogs text-green-500"></i>
			Automation Modules
		</h2>

		<div class="space-y-3">
			{#each automationModules as module (module.id)}
				<div class="bg-white rounded-lg shadow p-6 flex items-start justify-between hover:shadow-md transition-shadow">
					<div class="flex items-start gap-4 flex-1">
						<div class="w-12 h-12 rounded-lg bg-green-100 flex items-center justify-center flex-shrink-0">
							<i class={`${module.icon} text-green-600 text-lg`}></i>
						</div>
						<div class="flex-1">
							<h3 class="font-bold text-gray-800">{module.name}</h3>
							<p class="text-sm text-gray-600 mt-1">{module.description}</p>
						</div>
					</div>

					<label class="relative inline-flex items-center cursor-pointer ml-4 flex-shrink-0">
						<input
							type="checkbox"
							checked={module.enabled}
							on:change={() => toggleModule(module.id)}
							class="sr-only peer"
						/>
						<div class="w-11 h-6 bg-gray-300 peer-focus:outline-none peer-focus:ring-4 peer-focus:ring-[#0b3a7a]/30 rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:bg-[#0b3a7a]"></div>
					</label>
				</div>
			{/each}
		</div>
	</div>

	<!-- Advanced Features -->
	<div class="space-y-4">
		<h2 class="text-xl font-bold text-gray-800 flex items-center gap-2">
			<i class="fas fa-star text-purple-500"></i>
			Advanced Features
		</h2>

		<div class="space-y-3">
			{#each advancedModules as module (module.id)}
				<div class="bg-white rounded-lg shadow p-6 flex items-start justify-between hover:shadow-md transition-shadow">
					<div class="flex items-start gap-4 flex-1">
						<div class="w-12 h-12 rounded-lg bg-purple-100 flex items-center justify-center flex-shrink-0">
							<i class={`${module.icon} text-purple-600 text-lg`}></i>
						</div>
						<div class="flex-1">
							<h3 class="font-bold text-gray-800">{module.name}</h3>
							<p class="text-sm text-gray-600 mt-1">{module.description}</p>
						</div>
					</div>

					<label class="relative inline-flex items-center cursor-pointer ml-4 flex-shrink-0">
						<input
							type="checkbox"
							checked={module.enabled}
							on:change={() => toggleModule(module.id)}
							class="sr-only peer"
						/>
						<div class="w-11 h-6 bg-gray-300 peer-focus:outline-none peer-focus:ring-4 peer-focus:ring-[#0b3a7a]/30 rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:bg-[#0b3a7a]"></div>
					</label>
				</div>
			{/each}
		</div>
	</div>

	<!-- Summary -->
	<div class="bg-[#0b3a7a]/5 rounded-lg shadow p-6 border border-[#0b3a7a]/10">
		<h3 class="text-lg font-bold text-gray-800 mb-3 flex items-center gap-2">
			<i class="fas fa-info-circle text-[#0b3a7a]"></i>
			Module Summary
		</h3>
		<div class="space-y-2">
			<p class="text-sm text-gray-700">
				<strong>Enabled Modules:</strong>
				{modules.filter(m => m.enabled).length} of {modules.length}
			</p>
			{#if modules.filter(m => m.enabled).length > 0}
				<ul class="text-sm text-gray-700 ml-4 space-y-1">
					{#each modules.filter(m => m.enabled) as module (module.id)}
						<li class="flex items-center gap-2">
							<span class="text-[#0b3a7a]">✓</span>
							{module.name}
						</li>
					{/each}
				</ul>
			{:else}
				<p class="text-sm text-gray-600 italic">No optional modules enabled yet</p>
			{/if}
		</div>
	</div>

	<!-- Save Button -->
	<div class="flex justify-end gap-3 border-t pt-6">
		<button class="px-6 py-2 border border-gray-300 text-gray-700 rounded-lg hover:bg-gray-50 font-medium transition-colors">
			Discard Changes
		</button>
		<button class="px-6 py-2 bg-[#0b3a7a] text-white rounded-lg hover:bg-[#082654] font-medium transition-colors">
			<i class="fas fa-save mr-2"></i>Save Configuration
		</button>
	</div>
</div>
