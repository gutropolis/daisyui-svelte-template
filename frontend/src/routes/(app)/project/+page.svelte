<script lang="ts">
	import { onMount } from 'svelte';

	interface Project {
		id: number;
		name: string;
		status: 'Draft' | 'Staging' | 'Production';
		completedSteps: number;
		totalSteps: number;
	}

	let projects: Project[] = [];

	onMount(() => {
		projects = [
			{ id: 1, name: 'Diabetes Study 2025', status: 'Draft', completedSteps: 0, totalSteps: 8 },
			{ id: 2, name: 'COVID-19 Research', status: 'Production', completedSteps: 8, totalSteps: 8 },
			{ id: 3, name: 'Hypertension Trial', status: 'Staging', completedSteps: 5, totalSteps: 8 }
		];
	});
</script>

<div class="p-6 space-y-6">
	<div>
		<h2 class="text-3xl font-bold text-gray-800">Projects</h2>
		<p class="text-gray-600">Manage and setup your clinical research projects</p>
	</div>

	<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
		{#each projects as project (project.id)}
			<a href={`/project/${project.id}/setup`} class="group">
				<div class="bg-white rounded-lg shadow hover:shadow-lg transition-all p-6 border-l-4 border-blue-500">
					<div class="flex items-start justify-between mb-4">
						<div class="flex-1">
							<h3 class="text-lg font-semibold text-gray-800 group-hover:text-blue-600">{project.name}</h3>
							<p class="text-sm text-gray-500">ID: {project.id}</p>
						</div>
						<span class="px-3 py-1 rounded-full text-xs font-medium" class:bg-yellow-100={project.status === 'Draft'} class:text-yellow-800={project.status === 'Draft'} class:bg-blue-100={project.status === 'Staging'} class:text-blue-800={project.status === 'Staging'} class:bg-green-100={project.status === 'Production'} class:text-green-800={project.status === 'Production'}>
							{project.status}
						</span>
					</div>

					<div class="space-y-3">
						<div>
							<div class="flex justify-between text-xs text-gray-600 mb-1">
								<span>Completion</span>
								<span>{project.completedSteps}/{project.totalSteps}</span>
							</div>
							<div class="w-full bg-gray-200 rounded-full h-2">
								<div
									class="bg-blue-500 h-2 rounded-full transition-all"
									style={`width: ${(project.completedSteps / project.totalSteps) * 100}%`}
								></div>
							</div>
						</div>

						<div class="flex gap-2 pt-2">
							<button class="flex-1 px-3 py-2 bg-blue-50 text-blue-600 rounded hover:bg-blue-100 text-xs font-medium transition-colors">
								Setup
							</button>
							<button class="flex-1 px-3 py-2 bg-gray-100 text-gray-700 rounded hover:bg-gray-200 text-xs font-medium transition-colors">
								View
							</button>
						</div>
					</div>
				</div>
			</a>
		{/each}
	</div>

	<div class="flex justify-end">
		<button class="px-6 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition-colors font-medium">
			<i class="fas fa-plus mr-2"></i>New Project
		</button>
	</div>
</div>
