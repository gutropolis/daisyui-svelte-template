<script lang="ts">
	import { page } from '$app/stores';
	import { PROJECT_DETAIL_SETUP_ROUTE } from '$lib/enums/routes';
	import { resolveProjectRoute } from '$lib/utils/routes';

	interface ValidationItem {
		id: number;
		name: string;
		description: string;
		status: 'complete' | 'warning' | 'incomplete';
		icon: string;
	}

	let projectStatus: 'development' | 'staging' | 'production' = 'development';

	let validationItems: ValidationItem[] = [
		{
			id: 1,
			name: 'Project Settings',
			description: 'Project name and purpose defined',
			status: 'complete',
			icon: 'fa-gear'
		},
		{
			id: 2,
			name: 'Data Collection Instruments',
			description: 'At least one form has been created',
			status: 'complete',
			icon: 'fa-wpforms'
		},
		{
			id: 3,
			name: 'Events Defined',
			description: 'Events created and instruments assigned',
			status: 'complete',
			icon: 'fa-calendar'
		},
		{
			id: 4,
			name: 'User Permissions',
			description: 'At least one project user configured',
			status: 'complete',
			icon: 'fa-users'
		},
		{
			id: 5,
			name: 'Testing Complete',
			description: 'Test records created and validated',
			status: 'warning',
			icon: 'fa-vial'
		},
		{
			id: 6,
			name: 'Production Ready',
			description: 'All configurations finalized and approved',
			status: 'incomplete',
			icon: 'fa-rocket'
		}
	];

	let showProductionDialog = false;
	let productionPassword = '';
	let confirmPassword = '';

	const projectId = $derived($page.params.projectId ?? '1');
	const setupOverviewRoute = $derived(resolveProjectRoute(PROJECT_DETAIL_SETUP_ROUTE, projectId));

	const getStatusColor = (status: string) => {
		switch (status) {
			case 'complete':
				return 'text-green-600';
			case 'warning':
				return 'text-orange-600';
			case 'incomplete':
				return 'text-red-600';
			default:
				return 'text-gray-600';
		}
	};

	const getStatusBgColor = (status: string) => {
		switch (status) {
			case 'complete':
				return 'bg-green-100';
			case 'warning':
				return 'bg-orange-100';
			case 'incomplete':
				return 'bg-red-100';
			default:
				return 'bg-gray-100';
		}
	};

	const getStatusIcon = (status: string) => {
		switch (status) {
			case 'complete':
				return 'fa-check-circle';
			case 'warning':
				return 'fa-exclamation-circle';
			case 'incomplete':
				return 'fa-times-circle';
			default:
				return 'fa-circle';
		}
	};

	const completeItems = validationItems.filter(v => v.status === 'complete').length;
	const totalItems = validationItems.length;

	const moveToProduction = () => {
		if (productionPassword === confirmPassword && productionPassword) {
			projectStatus = 'production';
			showProductionDialog = false;
			productionPassword = '';
			confirmPassword = '';
		}
	};

	const moveToStaging = () => {
		projectStatus = 'staging';
	};
</script>

<div class="p-6 space-y-6">
	<!-- Header -->
	<div>
		<a href={setupOverviewRoute} class="flex items-center gap-2 text-[#0b3a7a] hover:text-[#082654] text-sm font-medium mb-4">
			<i class="fas fa-arrow-left"></i>Back to Setup
		</a>
		<h1 class="text-3xl font-bold text-gray-800 mb-2">Move to Production</h1>
		<p class="text-gray-600">Review your project configuration and move to production when ready</p>
	</div>

	<!-- Project Status Timeline -->
	<div class="bg-white rounded-lg shadow p-6">
		<h2 class="text-lg font-bold text-gray-800 mb-4">Project Status</h2>
		<div class="flex items-center justify-center gap-4">
			<div
				class="flex flex-col items-center {projectStatus === 'development' || projectStatus === 'staging' || projectStatus === 'production'
					? 'text-[#0b3a7a]'
					: 'text-gray-400'}"
			>
				<div
					class="w-12 h-12 rounded-full flex items-center justify-center {projectStatus === 'development' ||
					projectStatus === 'staging' ||
					projectStatus === 'production'
						? 'bg-[#0b3a7a]/10'
						: 'bg-gray-100'}"
				>
					<i class="fas fa-pencil"></i>
				</div>
				<span class="text-xs font-medium mt-2">development</span>
			</div>

			<div class="flex-1 h-1 bg-gray-200"></div>

			<div
				class="flex flex-col items-center {projectStatus === 'staging' || projectStatus === 'production'
					? 'text-[#0b3a7a]'
					: 'text-gray-400'}"
			>
				<div
					class="w-12 h-12 rounded-full flex items-center justify-center {projectStatus === 'staging' || projectStatus === 'production'
						? 'bg-[#0b3a7a]/10'
						: 'bg-gray-100'}"
				>
					<i class="fas fa-flask"></i>
				</div>
				<span class="text-xs font-medium mt-2">Staging</span>
			</div>

			<div class="flex-1 h-1 bg-gray-200"></div>

			<div class="flex flex-col items-center {projectStatus === 'production' ? 'text-green-600' : 'text-gray-400'}">
				<div
					class="w-12 h-12 rounded-full flex items-center justify-center {projectStatus === 'production'
						? 'bg-green-100'
						: 'bg-gray-100'}"
				>
					<i class="fas fa-rocket"></i>
				</div>
				<span class="text-xs font-medium mt-2">Production</span>
			</div>
		</div>
	</div>

	<!-- Current Status Badge -->
	<div
		class="rounded-lg shadow p-6 {projectStatus === 'development'
			? 'bg-[#0b3a7a]/5 border border-[#0b3a7a]/10'
			: projectStatus === 'staging'
				? 'bg-orange-50 border border-orange-200'
				: 'bg-green-50 border border-green-200'}"
	>
		<div class="flex items-center justify-between">
			<div>
				<p class="text-sm font-medium text-gray-600">Current Project Status</p>
				<p class="text-sm font-bold mt-2 {projectStatus === 'development'
					? 'text-[#0b3a7a]'
					: projectStatus === 'staging'
						? 'text-orange-600'
						: 'text-green-600'}">
					{projectStatus.charAt(0).toUpperCase() + projectStatus.slice(1)}
				</p>
			</div>
			<i
				class="fas {projectStatus === 'development'
					? 'fa-pencil text-4xl text-blue-200'
					: projectStatus === 'staging'
						? 'fa-flask text-4xl text-orange-200'
						: 'fa-rocket text-4xl text-green-200'}"
			></i>
		</div>
	</div>

	<!-- Validation Checklist -->
	<div class="bg-white rounded-lg shadow overflow-hidden">
		<div class="p-6 border-b border-gray-200">
			<h2 class="text-xl font-bold text-gray-800 flex items-center gap-2">
				<i class="fas fa-clipboard-check text-blue-600"></i>
				Production Readiness Checklist
			</h2>
			<p class="text-sm text-gray-600 mt-1">
				{completeItems}/{totalItems} requirements met
			</p>
		</div>

		<div class="p-6 space-y-3">
			{#each validationItems as item (item.id)}
				<div class="flex items-start gap-4 p-4 {getStatusBgColor(item.status)} rounded-lg border {item.status === 'complete'
					? 'border-green-200'
					: item.status === 'warning'
						? 'border-orange-200'
						: 'border-red-200'}">
					<i class="fas {getStatusIcon(item.status)} text-xl {getStatusColor(item.status)} mt-1"></i>

					<div class="flex-1">
						<h3 class="font-semibold text-gray-800">{item.name}</h3>
						<p class="text-sm text-gray-600">{item.description}</p>
					</div>

					<span
						class="px-3 py-1 rounded-full text-xs font-medium {item.status === 'complete'
							? 'bg-green-200 text-green-800'
							: item.status === 'warning'
								? 'bg-orange-200 text-orange-800'
								: 'bg-red-200 text-red-800'}"
					>
						{item.status.charAt(0).toUpperCase() + item.status.slice(1)}
					</span>
				</div>
			{/each}
		</div>
	</div>

	<!-- Progress Bar -->
	<div class="bg-white rounded-lg shadow p-6">
		<div class="flex items-center justify-between mb-2">
			<p class="font-medium text-gray-800">Production Readiness</p>
			<p class="text-sm text-gray-600">{completeItems} of {totalItems} complete</p>
		</div>
		<div class="w-full bg-gray-200 rounded-full h-3 overflow-hidden">
			<div
				class="bg-linear-to-r from-green-500 to-green-600 h-full transition-all duration-300"
				style="width: {(completeItems / totalItems) * 100}%"
			></div>
		</div>
	</div>

	<!-- Action Buttons -->
	<div class="bg-white rounded-lg shadow p-6">
		<h3 class="font-bold text-gray-800 mb-4">Project Status Actions</h3>
		<div class="grid grid-cols-1 md:grid-cols-2 gap-4">
			{#if projectStatus === 'development'}
				<button
					on:click={moveToStaging}
					class="px-6 py-3 bg-orange-600 text-white rounded-lg hover:bg-orange-700 font-medium transition-colors flex items-center justify-center gap-2"
				>
					<i class="fas fa-flask"></i>
					Move to Staging
				</button>
				<button class="px-6 py-3 bg-gray-100 text-gray-600 rounded-lg cursor-not-allowed font-medium flex items-center justify-center gap-2">
					<i class="fas fa-lock"></i>
					Move to Production (Disabled)
				</button>
			{:else if projectStatus === 'staging'}
				<button
					on:click={() => (projectStatus = 'development')}
					class="px-6 py-3 bg-gray-600 text-white rounded-lg hover:bg-gray-700 font-medium transition-colors flex items-center justify-center gap-2"
				>
					<i class="fas fa-undo"></i>
					Back to development
				</button>
				<button
					on:click={() => (showProductionDialog = true)}
					class="px-6 py-3 bg-green-600 text-white rounded-lg hover:bg-green-700 font-medium transition-colors flex items-center justify-center gap-2"
				>
					<i class="fas fa-rocket"></i>
					Move to Production
				</button>
			{:else}
				<div class="md:col-span-2">
					<div class="bg-green-50 border border-green-200 rounded-lg p-4 flex items-center gap-3">
						<i class="fas fa-check-circle text-2xl text-green-600"></i>
						<div>
							<p class="font-bold text-green-800">Project is in Production</p>
							<p class="text-sm text-green-700">Your project is now live and ready for data entry</p>
						</div>
					</div>
				</div>
			{/if}
		</div>
	</div>

	<!-- Important Notes -->
	<div class="bg-red-50 rounded-lg shadow p-6 border border-red-200">
		<h3 class="text-lg font-bold text-gray-800 mb-3 flex items-center gap-2">
			<i class="fas fa-exclamation-triangle text-red-600"></i>
			Important Notes Before Production
		</h3>
		<ul class="space-y-2 text-sm text-gray-700">
			<li class="flex items-start gap-2">
				<span class="text-red-600 font-bold mt-0.5">•</span>
				<span><strong>No form modifications:</strong> Once in production, form structure cannot be changed without creating a new version</span>
			</li>
			<li class="flex items-start gap-2">
				<span class="text-red-600 font-bold mt-0.5">•</span>
				<span><strong>Existing data:</strong> Ensure all test records are deleted before moving to production</span>
			</li>
			<li class="flex items-start gap-2">
				<span class="text-red-600 font-bold mt-0.5">•</span>
				<span><strong>User training:</strong> Ensure all users understand the forms and workflows before going live</span>
			</li>
			<li class="flex items-start gap-2">
				<span class="text-red-600 font-bold mt-0.5">•</span>
				<span><strong>Data backups:</strong> Enable automated backups in production settings</span>
			</li>
			<li class="flex items-start gap-2">
				<span class="text-red-600 font-bold mt-0.5">•</span>
				<span><strong>Support contact:</strong> Have technical support contact information readily available</span>
			</li>
		</ul>
	</div>

	<!-- Production Confirmation Modal -->
	{#if showProductionDialog}
		<div class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
			<div class="bg-white rounded-lg shadow-xl p-6 max-w-md w-full mx-4">
				<div class="flex items-center gap-3 mb-4">
					<i class="fas fa-exclamation-circle text-3xl text-orange-600"></i>
					<h2 class="text-xl font-bold text-gray-800">Move to Production?</h2>
				</div>

				<p class="text-gray-600 mb-4">
					You are about to move your project to production. This is a significant step and should be taken carefully. Please review all settings
					before confirming.
				</p>

				<div class="space-y-4 mb-6">
					<div>
						<label class="block text-sm font-medium text-gray-700 mb-1">Confirmation Password</label>
						<input
							type="password"
							bind:value={productionPassword}
							class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-[#0b3a7a] outline-none"
							placeholder="Enter password to confirm"
						/>
					</div>

					<div>
						<label class="block text-sm font-medium text-gray-700 mb-1">Confirm Password</label>
						<input
							type="password"
							bind:value={confirmPassword}
							class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-[#0b3a7a] outline-none"
							placeholder="Re-enter password"
						/>
					</div>
				</div>

				<div class="flex gap-2 justify-end border-t pt-4">
					<button
						on:click={() => (showProductionDialog = false)}
						class="px-4 py-2 border border-gray-300 text-gray-700 rounded-lg hover:bg-gray-50 font-medium transition-colors"
					>
						Cancel
					</button>
					<button
						on:click={moveToProduction}
						disabled={!productionPassword || productionPassword !== confirmPassword}
						class="px-4 py-2 bg-green-600 text-white rounded-lg hover:bg-green-700 font-medium transition-colors disabled:opacity-50"
					>
						Move to Production
					</button>
				</div>
			</div>
		</div>
	{/if}
</div>
