<script lang="ts">
	import StatsCard from './StatsCard.svelte';

	interface QuickAction {
		icon: 'users' | 'document' | 'alert' | 'eye';
		title: string;
		description: string;
	}

	const quickActions: QuickAction[] = [
		{ icon: 'users', title: 'Enroll Patient', description: 'Add new patient to trial' },
		{ icon: 'document', title: 'Add Form', description: 'Create clinical data form' },
		{ icon: 'alert', title: 'Report AE', description: 'Report adverse event' },
		{ icon: 'eye', title: 'Compliance', description: 'View compliance status' }
	];
</script>

<div class="space-y-6">
	<!-- Summary Stats -->
	<div class="grid grid-cols-4 gap-4">
		<StatsCard title="Active Trials" value="2" icon="folder" variant="primary" />
		<StatsCard title="Total Enrollment" value="132/450" icon="users" variant="success" />
		<StatsCard title="Milestones" value="5/8" icon="checkmark" variant="warning" />
		<StatsCard title="Study Sites" value="24" icon="document" variant="primary" />
	</div>

	<!-- Quick Actions -->
	<div class="bg-white rounded-lg border border-gray-200 p-6">
		<h3 class="font-bold text-gray-900 mb-4">Quick Actions</h3>
		<p class="text-sm text-gray-600 mb-4">Common tasks and shortcuts</p>
		<div class="grid grid-cols-4 gap-4">
			{#each quickActions as action}
				<button class="p-4 border border-gray-200 rounded-lg hover:bg-gray-50 transition-colors flex flex-col items-center gap-3">
					<div class="w-10 h-10 bg-blue-50 rounded-lg flex items-center justify-center">
						{#if action.icon === 'users'}
							<svg xmlns="http://www.w3.org/2000/svg" class="w-5 h-5 text-blue-600" fill="currentColor" viewBox="0 0 24 24">
								<path d="M16 11c1.66 0 2.99-1.34 2.99-3S17.66 5 16 5c-1.66 0-3 1.34-3 3s1.34 3 3 3zm-8 0c1.66 0 2.99-1.34 2.99-3S9.66 5 8 5C6.34 5 5 6.34 5 8s1.34 3 3 3zm0 2c-2.33 0-7 1.17-7 3.5V19h14v-2.5c0-2.33-4.67-3.5-7-3.5zm8 0c-.29 0-.62.02-.97.05 1.16.84 1.97 1.97 1.97 3.45V19h6v-2.5c0-2.33-4.67-3.5-7-3.5z" />
							</svg>
						{:else if action.icon === 'document'}
							<svg xmlns="http://www.w3.org/2000/svg" class="w-5 h-5 text-blue-600" fill="currentColor" viewBox="0 0 24 24">
								<path d="M14 2H6a2 2 0 00-2 2v16a2 2 0 002 2h12a2 2 0 002-2V8l-8-6z" />
							</svg>
						{:else if action.icon === 'alert'}
							<svg xmlns="http://www.w3.org/2000/svg" class="w-5 h-5 text-blue-600" fill="currentColor" viewBox="0 0 24 24">
								<path d="M1 21h22L12 2 1 21zm12-3h-2v-2h2v2zm0-4h-2v-4h2v4z" />
							</svg>
						{:else if action.icon === 'eye'}
							<svg xmlns="http://www.w3.org/2000/svg" class="w-5 h-5 text-blue-600" fill="currentColor" viewBox="0 0 24 24">
								<path d="M12 4.5C7 4.5 2.73 7.61 1 12c1.73 4.39 6 7.5 11 7.5s9.27-3.11 11-7.5c-1.73-4.39-6-7.5-11-7.5zM12 17c-2.76 0-5-2.24-5-5s2.24-5 5-5 5 2.24 5 5-2.24 5-5 5zm0-8c-1.66 0-3 1.34-3 3s1.34 3 3 3 3-1.34 3-3-1.34-3-3-3z" />
							</svg>
						{/if}
					</div>
					<div class="text-center">
						<p class="font-semibold text-sm text-gray-900">{action.title}</p>
						<p class="text-xs text-gray-500">{action.description}</p>
					</div>
				</button>
			{/each}
		</div>
	</div>
</div>
