<script lang="ts">
	import { page } from '$app/stores';
	import { GET_PLAN_QUERY, PLAN_FEATURES_QUERY } from '$lib/gql/plan'; 
	import { getContextClient } from '@urql/svelte';
	import { handleGqlErr } from '$lib/utils/gqlfx'; 
	import alerts from '$lib/stores/alerts';
	import { onMount } from 'svelte';

	const client = getContextClient();

	let loading = false;
	let error = '';
	let plan: any = null;
	let allFeatures: Array<{ id: number; name: string }> = [];

	$: planId = parseInt($page.params.id);

	
 
	// Load plan and features
	async function loadData() {
		let title="Load features and plan";
		loading = true;
		try {
			// Load features
			const featuresResponse = await client.query(PLAN_FEATURES_QUERY,{}).toPromise(); 
			if (featuresResponse.error) {
				alerts.error(title, featuresResponse.error.message);
				return;
			} 
			if (featuresResponse.data.planFeatures.success) {
				allFeatures = featuresResponse.data.planFeatures.data;
			}
			 

			// Load plan
		 
			const planResponse = await client.query(GET_PLAN_QUERY,{id: planId }).toPromise(); 
			if (planResponse.data.plan.success) {
				plan = planResponse.data.plan.data;
			} else {
				error = planResponse.data.plan.message;
			}
		} catch (err: any) {
			error = `Failed to load plan: ${err.message}`;
			console.error(err);
		} finally {
			loading = false;
		}
	}

	function formatDate(dateString: string): string {
		return new Date(dateString).toLocaleDateString('en-US', {
			year: 'numeric',
			month: 'long',
			day: 'numeric',
			hour: '2-digit',
			minute: '2-digit'
		});
	}

	function getFeatureName(featureId: number): string {
		const feature = allFeatures.find(f => f.id === featureId);
		return feature ? feature.name : `Feature #${featureId}`;
	}

	onMount(() => loadData());
</script>

<div class="min-h-screen bg-gray-50 p-8">
	<div class="max-w-3xl mx-auto">
		<!-- Header -->
		<div class="mb-8">
			<a href="/admin/plan" class="text-indigo-600 hover:text-indigo-700 font-medium mb-4 inline-block">
				← Back to Plans
			</a>
			<h1 class="text-4xl font-bold text-gray-900">Plan Details</h1>
			<p class="text-gray-600 mt-2">View complete plan information</p>
		</div>

		<!-- Error Alert -->
		{#if error}
			<div class="mb-6 p-4 bg-red-50 border border-red-200 rounded-lg text-red-800">
				<strong>Error:</strong> {error}
			</div>
		{/if}

		{#if loading}
			<div class="text-center py-12">
				<p class="text-gray-500 text-lg">Loading plan...</p>
			</div>
		{:else if plan}
			<div class="space-y-6">
				<!-- Main Info Card -->
				<div class="bg-white rounded-lg shadow-md p-8">
					<div class="grid grid-cols-1 md:grid-cols-2 gap-8">
						<!-- Left Column -->
						<div>
							<h2 class="text-3xl font-bold text-gray-900 mb-2">{plan.name}</h2>
							<p class="text-gray-600 mb-6">
								<code class="bg-gray-100 px-3 py-1 rounded text-sm">{plan.slug}</code>
							</p>

							<div class="space-y-4">
								<div>
									<p class="text-sm text-gray-600">Price</p>
									<p class="text-3xl font-bold text-green-600">${plan.price}</p>
								</div>
								<div>
									<p class="text-sm text-gray-600">Duration</p>
									<p class="text-2xl font-semibold text-gray-900">{plan.durationDays} days</p>
								</div>
							</div>
						</div>

						<!-- Right Column -->
						<div class="bg-gray-50 p-6 rounded-lg">
							<h3 class="text-lg font-semibold text-gray-900 mb-4">Limits</h3>
							<div class="space-y-3">
								<div>
									<p class="text-sm text-gray-600">Max Users</p>
									<p class="text-xl font-bold text-gray-900">
										{plan.maxUsers ? `${plan.maxUsers}` : '∞ Unlimited'}
									</p>
								</div>
								<div>
									<p class="text-sm text-gray-600">Max Studies</p>
									<p class="text-xl font-bold text-gray-900">
										{plan.maxStudies ? `${plan.maxStudies}` : '∞ Unlimited'}
									</p>
								</div>
								<div>
									<p class="text-sm text-gray-600">Max Storage</p>
									<p class="text-xl font-bold text-gray-900">
										{plan.maxStorageGb ? `${plan.maxStorageGb} GB` : '∞ Unlimited'}
									</p>
								</div>
							</div>
						</div>
					</div>
				</div>

				<!-- Features Card -->
				<div class="bg-white rounded-lg shadow-md p-8">
					<h3 class="text-2xl font-bold text-gray-900 mb-6">Included Features</h3>

					{#if plan.features.length === 0}
						<div class="p-6 bg-gray-50 rounded-lg text-center">
							<p class="text-gray-600">No features included in this plan</p>
						</div>
					{:else}
						<div class="grid grid-cols-1 md:grid-cols-2 gap-4">
							{#each plan.features as featureId}
								<div class="flex items-start gap-3 p-4 border border-green-200 bg-green-50 rounded-lg">
									<div class="text-2xl">✓</div>
									<div>
										<p class="font-semibold text-gray-900">{getFeatureName(featureId)}</p>
										<p class="text-xs text-gray-500">Feature ID: {featureId}</p>
									</div>
								</div>
							{/each}
						</div>
					{/if}
				</div>

				<!-- Metadata Card -->
				<div class="bg-white rounded-lg shadow-md p-8">
					<h3 class="text-lg font-semibold text-gray-900 mb-6">Metadata</h3>
					<div class="grid grid-cols-1 md:grid-cols-2 gap-6">
						<div>
							<p class="text-sm text-gray-600 mb-1">Created</p>
							<p class="text-gray-900 font-medium">{formatDate(plan.createdAt)}</p>
						</div>
						<div>
							<p class="text-sm text-gray-600 mb-1">Last Updated</p>
							<p class="text-gray-900 font-medium">{formatDate(plan.updatedAt)}</p>
						</div>
						<div>
							<p class="text-sm text-gray-600 mb-1">Plan ID</p>
							<p class="text-gray-900 font-medium">{plan.id}</p>
						</div>
						<div>
							<p class="text-sm text-gray-600 mb-1">Status</p>
							<p class="text-green-600 font-medium">✓ Active</p>
						</div>
					</div>
				</div>

				<!-- Actions -->
				<div class="flex gap-3">
					<a
						href="/admin/plan/{plan.id}/edit"
						class="flex-1 bg-blue-600 hover:bg-blue-700 text-white font-medium py-3 px-6 rounded-lg transition text-center"
					>
						✏️ Edit Plan
					</a>
					<a
						href="/admin/plan"
						class="flex-1 bg-gray-600 hover:bg-gray-700 text-white font-medium py-3 px-6 rounded-lg transition text-center"
					>
						← Back to List
					</a>
				</div>
			</div>
		{/if}
	</div>
</div>

<style>
	:global(body) {
		background-color: #f9fafb;
	}
</style>
