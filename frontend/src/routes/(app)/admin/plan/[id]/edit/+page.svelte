<script lang="ts">
	import { goto, page } from '$app/navigation';
	import { graphqlClient } from '$lib/graphql/client';
	import { onMount } from 'svelte';

	let loading = false;
	let error = '';
	let success = '';
	let features: Array<{ id: number; name: string }> = [];
	let selectedFeatures: Set<number> = new Set();
	let plan: any = null;

	const planId = parseInt($page.params.id);

	const GET_PLAN_QUERY = `
		query GetPlan($id: Int!) {
			plan(id: $id) {
				success
				message
				data {
					id
					slug
					name
					price
					durationDays
					maxUsers
					maxStudies
					maxStorageGb
					features
					createdAt
					updatedAt
				}
			}
		}
	`;

	const PLAN_FEATURES_QUERY = `
		query {
			planFeatures {
				success
				message
				data {
					id
					name
				}
			}
		}
	`;

	const UPDATE_PLAN_MUTATION = `
		mutation UpdatePlan($id: Int!, $input: UpdatePlanInput!) {
			updatePlan(id: $id, input: $input) {
				success
				message
				data {
					id
					slug
					name
					price
					durationDays
					maxUsers
					maxStudies
					maxStorageGb
					features
					createdAt
					updatedAt
				}
			}
		}
	`;

	let formData = {
		name: '',
		price: '',
		durationDays: 30,
		maxUsers: '',
		maxStudies: '',
		maxStorageGb: ''
	};

	// Load plan and features
	async function loadData() {
		loading = true;
		try {
			// Load features
			const featuresResponse = await graphqlClient.request(PLAN_FEATURES_QUERY);
			if (featuresResponse.planFeatures.success) {
				features = featuresResponse.planFeatures.data;
			}

			// Load plan
			const planResponse = await graphqlClient.request(GET_PLAN_QUERY, {
				id: planId
			});

			if (planResponse.plan.success) {
				plan = planResponse.plan.data;
				formData = {
					name: plan.name,
					price: plan.price,
					durationDays: plan.durationDays,
					maxUsers: plan.maxUsers?.toString() || '',
					maxStudies: plan.maxStudies?.toString() || '',
					maxStorageGb: plan.maxStorageGb?.toString() || ''
				};
				selectedFeatures = new Set(plan.features);
			} else {
				error = planResponse.plan.message;
			}
		} catch (err: any) {
			error = `Failed to load plan: ${err.message}`;
			console.error(err);
		} finally {
			loading = false;
		}
	}

	// Toggle feature
	function toggleFeature(featureId: number) {
		if (selectedFeatures.has(featureId)) {
			selectedFeatures.delete(featureId);
		} else {
			selectedFeatures.add(featureId);
		}
		selectedFeatures = selectedFeatures;
	}

	async function handleSubmit() {
		if (!formData.name || !formData.price || !formData.durationDays) {
			error = 'Name, price, and duration are required';
			return;
		}

		if (formData.durationDays < 1) {
			error = 'Duration must be at least 1 day';
			return;
		}

		loading = true;
		error = '';
		success = '';

		try {
			const response = await graphqlClient.request(UPDATE_PLAN_MUTATION, {
				id: planId,
				input: {
					name: formData.name,
					price: formData.price.toString(),
					durationDays: parseInt(formData.durationDays.toString()),
					maxUsers: formData.maxUsers ? parseInt(formData.maxUsers) : null,
					maxStudies: formData.maxStudies ? parseInt(formData.maxStudies) : null,
					maxStorageGb: formData.maxStorageGb ? parseInt(formData.maxStorageGb) : null,
					features: Array.from(selectedFeatures)
				}
			});

			if (response.updatePlan.success) {
				success = 'Plan updated successfully!';
				setTimeout(() => goto('/admin/plan'), 2000);
			} else {
				error = response.updatePlan.message;
			}
		} catch (err: any) {
			error = `Failed to update plan: ${err.message}`;
			console.error(err);
		} finally {
			loading = false;
		}
	}

	onMount(() => loadData());
</script>

<div class="min-h-screen bg-gray-50 p-8">
	<div class="max-w-2xl mx-auto">
		<!-- Header -->
		<div class="mb-8">
			<a href="/admin/plan" class="text-indigo-600 hover:text-indigo-700 font-medium mb-4 inline-block">
				← Back to Plans
			</a>
			<h1 class="text-4xl font-bold text-gray-900">Edit Plan</h1>
			<p class="text-gray-600 mt-2">Update plan details and features</p>
		</div>

		<!-- Error Alert -->
		{#if error}
			<div class="mb-6 p-4 bg-red-50 border border-red-200 rounded-lg text-red-800">
				<strong>Error:</strong> {error}
			</div>
		{/if}

		<!-- Success Alert -->
		{#if success}
			<div class="mb-6 p-4 bg-green-50 border border-green-200 rounded-lg text-green-800">
				✓ {success}
			</div>
		{/if}

		{#if loading && !plan}
			<div class="text-center py-12">
				<p class="text-gray-500 text-lg">Loading plan...</p>
			</div>
		{:else if plan}
			<!-- Form -->
			<div class="bg-white rounded-lg shadow-md p-8">
				<form on:submit|preventDefault={handleSubmit} class="space-y-6">
					<!-- Slug (Read-only) -->
					<div>
						<label for="slug" class="block text-sm font-medium text-gray-700 mb-2">
							Slug (Immutable)
						</label>
						<input
							type="text"
							id="slug"
							value={plan.slug}
							disabled
							class="w-full px-4 py-2 border border-gray-300 rounded-lg bg-gray-100 text-gray-600 cursor-not-allowed"
						/>
						<p class="text-xs text-gray-500 mt-1">Cannot be changed after creation</p>
					</div>

					<!-- Name -->
					<div>
						<label for="name" class="block text-sm font-medium text-gray-700 mb-2">
							Plan Name <span class="text-red-500">*</span>
						</label>
						<input
							type="text"
							id="name"
							bind:value={formData.name}
							placeholder="e.g., Starter Plan"
							class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
							required
						/>
					</div>

					<!-- Price -->
					<div>
						<label for="price" class="block text-sm font-medium text-gray-700 mb-2">
							Price (USD) <span class="text-red-500">*</span>
						</label>
						<input
							type="number"
							id="price"
							bind:value={formData.price}
							placeholder="9.99"
							step="0.01"
							class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
							required
						/>
					</div>

					<!-- Duration -->
					<div>
						<label for="durationDays" class="block text-sm font-medium text-gray-700 mb-2">
							Duration (Days) <span class="text-red-500">*</span>
						</label>
						<input
							type="number"
							id="durationDays"
							bind:value={formData.durationDays}
							placeholder="30"
							min="1"
							class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
							required
						/>
					</div>

					<!-- Limits Section -->
					<div class="border-t pt-6">
						<h3 class="text-lg font-semibold text-gray-900 mb-4">Limits (leave blank for unlimited)</h3>

						<!-- Max Users -->
						<div class="mb-4">
							<label for="maxUsers" class="block text-sm font-medium text-gray-700 mb-2">
								Max Users
							</label>
							<input
								type="number"
								id="maxUsers"
								bind:value={formData.maxUsers}
								placeholder="e.g., 5"
								min="1"
								class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
							/>
						</div>

						<!-- Max Studies -->
						<div class="mb-4">
							<label for="maxStudies" class="block text-sm font-medium text-gray-700 mb-2">
								Max Studies
							</label>
							<input
								type="number"
								id="maxStudies"
								bind:value={formData.maxStudies}
								placeholder="e.g., 10"
								min="1"
								class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
							/>
						</div>

						<!-- Max Storage -->
						<div>
							<label for="maxStorageGb" class="block text-sm font-medium text-gray-700 mb-2">
								Max Storage (GB)
							</label>
							<input
								type="number"
								id="maxStorageGb"
								bind:value={formData.maxStorageGb}
								placeholder="e.g., 100"
								min="1"
								class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
							/>
						</div>
					</div>

					<!-- Features Section -->
					<div class="border-t pt-6">
						<h3 class="text-lg font-semibold text-gray-900 mb-4">Features</h3>
						<p class="text-sm text-gray-600 mb-4">Select which features are included in this plan</p>

						{#if features.length === 0}
							<div class="p-4 bg-gray-50 rounded-lg text-gray-600">
								No features available. Create features first.
							</div>
						{:else}
							<div class="space-y-3">
								{#each features as feature (feature.id)}
									<label class="flex items-center gap-3 p-3 border border-gray-200 rounded-lg hover:bg-gray-50 cursor-pointer">
										<input
											type="checkbox"
											checked={selectedFeatures.has(feature.id)}
											on:change={() => toggleFeature(feature.id)}
											class="w-5 h-5 text-blue-600 rounded focus:ring-2 focus:ring-blue-500"
										/>
										<div>
											<p class="font-medium text-gray-900">{feature.name}</p>
											<p class="text-xs text-gray-500">Feature ID: {feature.id}</p>
										</div>
									</label>
								{/each}
							</div>

							{#if selectedFeatures.size > 0}
								<div class="mt-4 p-3 bg-blue-50 border border-blue-200 rounded-lg">
									<p class="text-sm text-blue-800">
										<strong>{selectedFeatures.size}</strong> feature(s) selected
									</p>
								</div>
							{/if}
						{/if}
					</div>

					<!-- Submit Buttons -->
					<div class="flex gap-3 pt-6 border-t">
						<button
							type="submit"
							disabled={loading}
							class="flex-1 bg-green-600 hover:bg-green-700 disabled:bg-green-400 text-white font-medium py-3 px-6 rounded-lg transition"
						>
							{loading ? 'Updating...' : '✓ Update Plan'}
						</button>
						<a
							href="/admin/plan"
							class="flex-1 bg-gray-300 hover:bg-gray-400 text-gray-800 font-medium py-3 px-6 rounded-lg transition text-center"
						>
							Cancel
						</a>
					</div>
				</form>
			</div>
		{/if}
	</div>
</div>

<style>
	:global(body) {
		background-color: #f9fafb;
	}
</style>
