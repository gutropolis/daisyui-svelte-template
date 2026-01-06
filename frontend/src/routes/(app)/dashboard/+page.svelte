<script lang="ts">
	import { PROJECT_DETAIL_DASHBOARD_ROUTE, PROJECT_DETAIL_SETUP_ROUTE, PROJECT_NEW_ROUTE } from '$lib/enums/routes';
	import { getStatusColor } from '$lib/utils/projecthelper';
	import { onMount } from 'svelte';

	interface Project {
		id: number;
		name: string;
		code: string;
		status: 'Draft' | 'Staging' | 'Production';
	}

	let projects: Project[] = [];

	onMount(() => {
		// Mock data
		projects = [
			{ id: 1, name: 'Diabetes Study 2025', code: 'DS25', status: 'Draft' },
			{ id: 2, name: 'COVID-19 Research', code: 'COVID-19', status: 'Production' },
			{ id: 3, name: 'Hypertension Trial', code: 'HYP-2025', status: 'Staging' },
			{ id: 4, name: 'Cancer Genomics', code: 'CG-2025', status: 'Draft' }
		];
	});

	 
</script>

<div class="p-6 space-y-6">
	<div>
		<h2 class="text-3xl font-bold text-gray-800 mb-2">Dashboard</h2>
		<p class="text-gray-600">Welcome back! Here's an overview of your projects.</p>
	</div>

	<!-- Stats Grid -->
	<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
		<div class="bg-white rounded-lg shadow p-6 border-l-4 border-blue-500">
			<div class="flex items-center justify-between">
				<div>
					<p class="text-gray-600 text-sm">Total Projects</p>
					<p class="text-3xl font-bold text-gray-800">{projects.length}</p>
				</div>
				<i class="fas fa-folder-open text-blue-500 text-4xl opacity-20"></i>
			</div>
		</div>

		<div class="bg-white rounded-lg shadow p-6 border-l-4 border-green-500">
			<div class="flex items-center justify-between">
				<div>
					<p class="text-gray-600 text-sm">Active</p>
					<p class="text-3xl font-bold text-gray-800">{projects.filter(p => p.status === 'Production').length}</p>
				</div>
				<i class="fas fa-check-circle text-green-500 text-4xl opacity-20"></i>
			</div>
		</div>

		<div class="bg-white rounded-lg shadow p-6 border-l-4 border-amber-500">
			<div class="flex items-center justify-between">
				<div>
					<p class="text-gray-600 text-sm">In Staging</p>
					<p class="text-3xl font-bold text-gray-800">{projects.filter(p => p.status === 'Staging').length}</p>
				</div>
				<i class="fas fa-hourglass-half text-amber-500 text-4xl opacity-20"></i>
			</div>
		</div>

		<div class="bg-white rounded-lg shadow p-6 border-l-4 border-purple-500">
			<div class="flex items-center justify-between">
				<div>
					<p class="text-gray-600 text-sm">Drafts</p>
					<p class="text-3xl font-bold text-gray-800">{projects.filter(p => p.status === 'Draft').length}</p>
				</div>
				<i class="fas fa-file text-purple-500 text-4xl opacity-20"></i>
			</div>
		</div>
	</div>

	<!-- Projects Table -->
	<div class="bg-white rounded-lg shadow overflow-hidden">
		<div class="p-6 border-b border-gray-200">
			<h3 class="text-xl font-bold text-gray-800">Your Projects</h3>
		</div>
		<div class="overflow-x-auto">
			<table class="w-full">
				<thead class="bg-gray-50 border-b border-gray-200">
					<tr>
						<th class="px-6 py-3 text-left text-sm font-semibold text-gray-700">Project Name</th>
						<th class="px-6 py-3 text-left text-sm font-semibold text-gray-700">Code</th>
						<th class="px-6 py-3 text-left text-sm font-semibold text-gray-700">Status</th>
						<th class="px-6 py-3 text-left text-sm font-semibold text-gray-700">Actions</th>
					</tr>
				</thead>
				<tbody class="divide-y divide-gray-200">
					{#each projects as project (project.id)}
						<tr class="hover:bg-gray-50 transition-colors">
							<td class="px-6 py-4 text-sm text-gray-800 font-medium">{project.name}</td>
							<td class="px-6 py-4 text-sm text-gray-600">{project.code}</td>
							<td class="px-6 py-4 text-sm">
								<span class={`badge ${getStatusColor(project.status)}`}>{project.status}</span>
							</td>
							<td class="px-6 py-4 text-sm space-x-2">
								<a href={PROJECT_DETAIL_SETUP_ROUTE} class="px-3 py-1 bg-blue-500 text-white rounded hover:bg-blue-600 transition-colors text-xs">Edit</a>
								<a  href={PROJECT_DETAIL_DASHBOARD_ROUTE} class="px-3 py-1 bg-gray-200 text-gray-700 rounded hover:bg-gray-300 transition-colors text-xs">View</a>
							</td>
						</tr>
					{/each}
				</tbody>
			</table>
		</div>
	</div>

	<!-- Create New Project Button -->
	<div class="flex justify-end">
		<a href="{PROJECT_NEW_ROUTE}" class="px-6 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition-colors font-medium">
			<i class="fas fa-plus mr-2"></i>Create New Project
		</a>
	</div>
</div>

<style>
	:global(.badge) {
		display: inline-block;
		padding: 4px 12px;
		border-radius: 9999px;
		font-size: 12px;
		font-weight: 500;
	}

	:global(.badge-warning) {
		background-color: #fef3c7;
		color: #92400e;
	}

	:global(.badge-info) {
		background-color: #bfdbfe;
		color: #1e40af;
	}

	:global(.badge-success) {
		background-color: #bbf7d0;
		color: #065f46;
	}
</style>
