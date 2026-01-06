<script lang="ts">
	import ProjectSetup from '$theme/projectsetup/ProjectSetup.svelte';
	import EventSetup from '$theme//projectsetup/EventSetup.svelte';
	import SiteSetup from '$theme//projectsetup/SiteSetup.svelte';
	import Imaging from '$theme//projectsetup/Imaging.svelte';
	import Clinical from '$theme//projectsetup/Clinical.svelte';
	import EventMatrix from '$theme//projectsetup/EventMatrix.svelte';

	let activeTab = 'project';

	// Sample project data
	const projectInfo = {
		name: 'COVID-19 Vaccine Trial',
		phase: 'Phase III',
		therapeuticArea: 'Immunology',
		sponsor: 'Clinical Research Inc.',
		status: 'Active',
		startDate: 'Jan 15, 2024',
		sites: 12,
		participants: 2450
	};

	const tabs = [
		{ id: 'project', label: 'Project', icon: 'fa-folder', component: ProjectSetup },
		{ id: 'event', label: 'Event', icon: 'fa-calendar', component: EventSetup },
		{ id: 'site', label: 'Site', icon: 'fa-building', component: SiteSetup },
		{ id: 'imaging', label: 'Imaging', icon: 'fa-image', component: Imaging },
		{ id: 'clinical', label: 'Clinical', icon: 'fa-stethoscope', component: Clinical },
		{ id: 'eventsetup', label: 'Event Setup', icon: 'fa-table', component: EventMatrix }
	];

	$: currentTab = tabs.find(tab => tab.id === activeTab);
	$: CurrentComponent = currentTab?.component || ProjectSetup;
</script>

<div class="p-8">
	<!-- Header -->
	<div class="mb-8">
		<h1 class="text-4xl font-bold text-gray-800 mb-2">Project Setup</h1>
		<p class="text-gray-600">Configure your clinical research project</p>
	</div>

	<!-- Project Information Card -->
	<div class="mb-6 bg-white rounded-lg shadow-md border border-gray-200 p-6">
		<div class="grid grid-cols-2 md:grid-cols-4 gap-6">
			<!-- Project Name -->
			<div class="border-r border-gray-200 pr-6">
				<p class="text-xs font-semibold text-gray-500 uppercase tracking-wide mb-2">Project Name</p>
				<p class="text-lg font-bold text-gray-800">{projectInfo.name}</p>
			</div>

			<!-- Phase & Therapeutic Area -->
			<div class="border-r border-gray-200 pr-6">
				<p class="text-xs font-semibold text-gray-500 uppercase tracking-wide mb-2">Phase & Area</p>
				<div class="flex flex-col gap-1">
					<span class="inline-block px-3 py-1 bg-blue-100 text-blue-700 text-sm font-semibold rounded w-fit">
						{projectInfo.phase}
					</span>
					<span class="text-sm text-gray-600">{projectInfo.therapeuticArea}</span>
				</div>
			</div>

			<!-- Sponsor -->
			<div class="border-r border-gray-200 pr-6">
				<p class="text-xs font-semibold text-gray-500 uppercase tracking-wide mb-2">Sponsor</p>
				<p class="text-sm font-medium text-gray-700">{projectInfo.sponsor}</p>
			</div>

			<!-- Status & Sites -->
			<div>
				<p class="text-xs font-semibold text-gray-500 uppercase tracking-wide mb-2">Status</p>
				<div class="flex flex-col gap-2">
					<span class="inline-flex items-center gap-2 px-3 py-1 bg-green-100 text-green-700 text-sm font-semibold rounded w-fit">
						<i class="fas fa-check-circle"></i>
						{projectInfo.status}
					</span>
					<p class="text-xs text-gray-600">Started: {projectInfo.startDate}</p>
				</div>
			</div>
		</div>

	 
	</div>

	<!-- Tab Navigation -->
	<div class="bg-white rounded-t-lg shadow-md border-b border-gray-200">
		<div class="flex gap-0">
			{#each tabs as tab (tab.id)}
				<button
					on:click={() => (activeTab = tab.id)}
					class="flex items-center gap-2 px-6 py-4 font-medium transition-all border-b-2 {activeTab === tab.id
						? 'border-[#0b3a7a] text-[#0b3a7a] bg-[#0b3a7a]/5'
						: 'border-transparent text-gray-600 hover:text-[#0b3a7a] hover:bg-gray-50'}"
				>
					<i class="fas {tab.icon}"></i>
					<span>{tab.label}</span>
				</button>
			{/each}
		</div>
	</div>

	<!-- Tab Content -->
	<div class="bg-white rounded-b-lg shadow-md p-8">
		<svelte:component this={CurrentComponent} />
	</div>

	<!-- Action Buttons -->
	<div class="mt-6 flex gap-3 justify-end">
		<button class="px-6 py-2 border border-gray-300 text-gray-700 rounded-lg hover:bg-gray-50 font-medium transition-colors">
			Cancel
		</button>
		<button class="px-6 py-2 bg-[#0b3a7a] text-white rounded-lg hover:bg-[#082654] font-medium transition-colors">
			Save & Next
		</button>
	</div>
</div>

<style>
	:global(body) {
		background-color: #f9fafb;
	}
</style>
