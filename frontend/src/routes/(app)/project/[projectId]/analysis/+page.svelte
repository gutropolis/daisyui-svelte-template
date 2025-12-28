<script lang="ts">
	import { page } from '$app/stores';
	import OverviewTab from '$lib/components/analysis/OverviewTab.svelte';
	import RoadmapTab from '$lib/components/analysis/RoadmapTab.svelte';
	import EnrollmentTab from '$lib/components/analysis/EnrollmentTab.svelte';
	import DataMonitoringTab from '$lib/components/analysis/DataMonitoringTab.svelte';
	import ComplianceTab from '$lib/components/analysis/ComplianceTab.svelte';

	let activeTab = 'overview';

	const projectId = $page.params.projectId;
</script>

<div class="p-8 space-y-6">
	<!-- Header -->
	<div class="flex items-start justify-between">
		<div>
			<h1 class="text-3xl font-bold text-gray-900">CT-2024-001 - Analysis</h1>
			<p class="text-sm text-gray-600 mt-1">Novel Immunotherapy for Advanced Melanoma</p>
		</div>
		<button class="px-4 py-2 bg-white border border-gray-300 rounded-lg hover:bg-gray-50 font-medium text-sm flex items-center gap-2">
			<svg xmlns="http://www.w3.org/2000/svg" class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
				<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4" />
			</svg>
			Export Timeline
		</button>
	</div>

	<!-- Tab Navigation -->
	<div class="flex gap-8 border-b border-gray-200">
		<button
			on:click={() => (activeTab = 'overview')}
			class="px-4 py-3 font-medium text-sm border-b-2 transition-colors {activeTab === 'overview'
				? 'border-[#0b3a7a] text-[#0b3a7a]'
				: 'border-transparent text-gray-600 hover:text-gray-900'}"
		>
			Overview
		</button>
		<button
			on:click={() => (activeTab = 'roadmap')}
			class="px-4 py-3 font-medium text-sm border-b-2 transition-colors {activeTab === 'roadmap'
				? 'border-[#0b3a7a] text-[#0b3a7a]'
				: 'border-transparent text-gray-600 hover:text-gray-900'}"
		>
			Roadmap
		</button>
		<button
			on:click={() => (activeTab = 'enrollment')}
			class="px-4 py-3 font-medium text-sm border-b-2 transition-colors {activeTab === 'enrollment'
				? 'border-[#0b3a7a] text-[#0b3a7a]'
				: 'border-transparent text-gray-600 hover:text-gray-900'}"
		>
			Enrollment
		</button>
		<button
			on:click={() => (activeTab = 'data-monitoring')}
			class="px-4 py-3 font-medium text-sm border-b-2 transition-colors {activeTab === 'data-monitoring'
				? 'border-[#0b3a7a] text-[#0b3a7a]'
				: 'border-transparent text-gray-600 hover:text-gray-900'}"
		>
			Data & Monitoring
		</button>
		<button
			on:click={() => (activeTab = 'compliance')}
			class="px-4 py-3 font-medium text-sm border-b-2 transition-colors {activeTab === 'compliance'
				? 'border-[#0b3a7a] text-[#0b3a7a]'
				: 'border-transparent text-gray-600 hover:text-gray-900'}"
		>
			Compliance
		</button>
	</div>

	<!-- Overview Tab -->
	{#if activeTab === 'overview'}
		<OverviewTab />
	{:else if activeTab === 'roadmap'}
		<RoadmapTab />
	{:else if activeTab === 'enrollment'}
		<EnrollmentTab />
	{:else if activeTab === 'data-monitoring'}
		<DataMonitoringTab />
	{:else if activeTab === 'compliance'}
		<ComplianceTab />
	{/if}
</div>

