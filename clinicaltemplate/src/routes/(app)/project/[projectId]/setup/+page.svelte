<script lang="ts">
	import { onMount } from 'svelte';

		type StepStatus = 'Completed' | 'In progress' | 'Pending';

		interface StepAction {
			label: string;
			icon: string;
		}

		interface SetupStep {
			id: number;
			name: string;
			description: string;
			status: StepStatus;
			icon: string;
			route: string;
			buttonLabel: string;
			isCompleted: boolean;
			actions?: StepAction[];
		}

		interface ProjectSetup {
			projectId: number;
			projectName: string;
			status: string;
			steps: SetupStep[];
		}

		const baseSteps: SetupStep[] = [
			{
				id: 1,
				name: 'Main Project Settings',
				description: 'Configure basic project settings and preferences.',
				status: 'Completed',
				icon: 'fas fa-gear',
				route: 'settings',
				buttonLabel: 'Configure Settings',
				isCompleted: true,
				actions: [{ label: 'Enable Surveys/Events', icon: 'fas fa-calendar-check' }]
			},
			{
				id: 2,
				name: 'Design Data Collection Instruments',
				description: 'Create and configure data collection tools.',
				status: 'Completed',
				icon: 'fas fa-database',
				route: 'design-instruments',
				buttonLabel: 'Design Instruments',
				isCompleted: true,
				actions: [{ label: 'Online Designer/Data Dictionary/Shared Library', icon: 'fas fa-pencil-alt' }]
			},
			{
				id: 3,
				name: 'Configure User Management',
				description: 'Set up user roles and permissions.',
				status: 'Pending',
				icon: 'fas fa-user-cog',
				route: 'user-management',
				buttonLabel: 'Add Users',
				isCompleted: false,
				actions: [
					{ label: 'Set Roles', icon: 'fas fa-users-cog' },
					{ label: 'Configure Permissions', icon: 'fas fa-key' }
				]
			},
			{
				id: 4,
				name: 'Define Data Entry Forms',
				description: 'Create data entry forms and validation rules.',
				status: 'Pending',
				icon: 'fas fa-file-alt',
				route: 'data-entry-forms',
				buttonLabel: 'Create Forms',
				isCompleted: false,
				actions: [
					{ label: 'Set Validation', icon: 'fas fa-check-double' },
					{ label: 'Test Forms', icon: 'fas fa-vial' }
				]
			},
			{
				id: 5,
				name: 'Security & Compliance',
				description: 'Configure security settings and compliance measures.',
				status: 'Pending',
				icon: 'fas fa-shield-alt',
				route: 'security-compliance',
				buttonLabel: 'Set Security',
				isCompleted: false,
				actions: [
					{ label: 'Configure HIPAA', icon: 'fas fa-id-badge' },
					{ label: 'Enable Audit Logs', icon: 'fas fa-clipboard-check' }
				]
			},
			{
				id: 6,
				name: 'Final Testing & Validation',
				description: 'Perform final testing and validation before production.',
				status: 'Pending',
				icon: 'fas fa-clipboard-list',
				route: 'final-testing',
				buttonLabel: 'Run Tests',
				isCompleted: false,
				actions: [
					{ label: 'Validate Data', icon: 'fas fa-tasks' },
					{ label: 'Review Setup', icon: 'fas fa-search' }
				]
			}
		];

		let project: ProjectSetup = {
			projectId: 1,
			projectName: 'Clinical Trial Manager',
			status: 'Development',
			steps: structuredClone(baseSteps)
		};

		let completedSteps = 0;

		onMount(() => updateProgress());

		function updateProgress() {
			completedSteps = project.steps.filter((step) => step.isCompleted || step.status === 'Completed').length;
		}

		function toggleStepCompletion(id: number) {
			const step = project.steps.find((item) => item.id === id);
			if (!step) return;
			step.isCompleted = !step.isCompleted;
			step.status = step.isCompleted ? 'Completed' : 'Pending';
			updateProgress();
		}

		function getProgressPercentage() {
			if (!project.steps.length) {
				return 0;
			}
			return Math.round((completedSteps / project.steps.length) * 100);
		}

		function getStepCardClass(status: StepStatus) {
			return status === 'Completed'
				? 'bg-green-50/70 border-green-100'
				: 'bg-white border-gray-200';
		}

		function getStepIconClass(status: StepStatus) {
			return status === 'Completed'
				? 'border-green-200 bg-white text-green-600'
				: 'border-gray-300 bg-white text-gray-400';
		}

		function getStatusPillClass(status: StepStatus) {
			return status === 'Completed'
				? 'bg-green-100 text-green-700'
				: 'bg-gray-100 text-gray-600';
		}
	</script>

	<div class="p-8 space-y-6">
		<!-- Header -->
		<div class="flex items-start justify-between">
			<div>
				<h1 class="text-3xl font-bold text-gray-900">Project Setup</h1>
				<p class="text-sm text-gray-600 mt-1">Complete all setup steps to move your project from development to production.</p>
			</div>
			<div class="text-right">
				<p class="text-3xl font-bold text-gray-900">{getProgressPercentage()}%</p>
				<p class="text-xs text-gray-500">{completedSteps} of {project.steps.length} steps</p>
			</div>
		</div>

		<!-- Progress Bar -->
		<div class="bg-white rounded-lg border border-gray-200 p-6">
			<div class="flex items-center justify-between mb-3">
				<p class="text-sm font-semibold text-gray-700">Overall Progress</p>
				<p class="text-sm font-bold text-gray-900">{getProgressPercentage()}%</p>
			</div>
			<div class="w-full bg-gray-200 rounded-full h-2 overflow-hidden">
				<div class="bg-[#0b3a7a] h-full rounded-full transition-all" style={`width: ${getProgressPercentage()}%`}></div>
			</div>
		</div>

		<!-- Steps Grid -->
		<div class="grid grid-cols-1 gap-6">
			{#each project.steps as step (step.id)}
				<div class="bg-white rounded-lg border border-gray-200 p-6 hover:shadow-md transition-shadow">
					<!-- Header with Status -->
					<div class="flex items-start justify-between mb-4">
						<div class="flex items-start gap-4 flex-1">
							<div class={`flex h-10 w-10 items-center justify-center rounded-full border-2 flex-shrink-0 ${getStepIconClass(step.status)}`}>
								<i class={`${step.status === 'Completed' ? 'fas fa-check' : 'far fa-circle'}`}></i>
							</div>
							<div>
								<p class="text-xs font-semibold tracking-wide text-gray-500 uppercase">Step {step.id}</p>
								<h3 class="text-lg font-bold text-[#0b3a7a] mt-1">{step.name}</h3>
								<p class="text-sm text-gray-600 mt-2">{step.description}</p>
							</div>
						</div>
						<span class={`px-3 py-1 rounded-full text-xs font-semibold whitespace-nowrap ml-4 ${getStatusPillClass(step.status)}`}>
							{step.status}
						</span>
					</div>

					<!-- Action Buttons -->
					<div class="flex flex-wrap gap-2 pt-4 border-t border-gray-200">
						<a
							href={`/project/${project.projectId}/setup/${step.route}`}
							class="px-4 py-2 bg-[#0b3a7a] text-white rounded-lg hover:bg-[#082654] font-medium text-sm transition-colors"
						>
							{step.buttonLabel}
						</a>
						<button
							type="button"
							on:click={() => toggleStepCompletion(step.id)}
							class="px-4 py-2 border border-gray-300 text-gray-700 rounded-lg hover:bg-gray-50 font-medium text-sm transition-colors"
						>
							{step.isCompleted ? 'Mark Pending' : 'Mark Complete'}
						</button>
						{#if step.actions}
							{#each step.actions as action}
								<button type="button" class="px-4 py-2 border border-gray-300 text-gray-700 rounded-lg hover:bg-gray-50 font-medium text-sm transition-colors">
									<i class={`${action.icon} mr-1`}></i>
									{action.label}
								</button>
							{/each}
						{/if}
					</div>
				</div>
			{/each}
		</div>

		<!-- CTA Section -->
		<div class="bg-white rounded-lg border border-gray-200 p-6 flex items-center justify-between">
			<div>
				<h3 class="text-lg font-bold text-gray-900">Ready for Production?</h3>
				<p class="text-sm text-gray-600 mt-1">Complete all {project.steps.length} setup steps before moving to production.</p>
			</div>
			<a
				href={`/project/${project.projectId}/setup/production`}
				class="px-6 py-2 bg-[#0b3a7a] text-white rounded-lg hover:bg-[#082654] font-medium transition-colors whitespace-nowrap ml-4"
			>
				Move to Production
			</a>
		</div>
	</div>
