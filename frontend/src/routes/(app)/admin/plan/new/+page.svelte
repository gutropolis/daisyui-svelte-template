<script lang="ts">
	import { goto } from '$app/navigation';
	import { CREATE_PLAN_MUTATION, PLAN_FEATURES_QUERY } from '$lib/gql/plan'; 
	import { getContextClient } from '@urql/svelte';
	import { handleGqlErr } from '$lib/utils/gqlfx'; 

	const client = getContextClient();
	let loading = false;
	let error = '';
	let features: Array<{ id: number; name: string }> = [];
	let selectedFeatures: Set<number> = new Set();

	
	let formData = {
		slug: '',
		name: '',
		price: '',
		durationDays: 30,
		maxUsers: '',
		maxStudies: '',
		maxStorageGb: ''
	};

	// Load features on mount
	async function loadFeatures() {
		let title="New Plan";
		try {
			const response = await client.query(PLAN_FEATURES_QUERY,{}).toPromise(); 
			if (response.error) {
				alerts.error(title, response.error.message);
				return;
			} 
			if (response.data.planFeatures.success) {
				features = response.data.planFeatures.data;
			}
		} catch (err: any) {
			console.error('Failed to load features:', err);
		}
	}

	// Toggle feature
	function toggleFeature(featureId: number) {
		if (selectedFeatures.has(featureId)) {
			selectedFeatures.delete(featureId);
		} else {
			selectedFeatures.add(featureId);
		}
		selectedFeatures = selectedFeatures; // Trigger reactivity
	}

	async function handleSubmit() {
		let title="Create Plan";
		if (!formData.slug || !formData.name || !formData.price || !formData.durationDays) {
			error = 'Slug, name, price, and duration are required';
			return;
		}

		if (formData.durationDays < 1) {
			error = 'Duration must be at least 1 day';
			return;
		}

		loading = true;
		error = '';

		try {

			 const response = await client.mutation(CREATE_PLAN_MUTATION, {
				input: {
					slug: formData.slug,
					name: formData.name,
					price: formData.price.toString(),
					durationDays: parseInt(formData.durationDays.toString()),
					maxUsers: formData.maxUsers ? parseInt(formData.maxUsers) : null,
					maxStudies: formData.maxStudies ? parseInt(formData.maxStudies) : null,
					maxStorageGb: formData.maxStorageGb ? parseInt(formData.maxStorageGb) : null,
					features: Array.from(selectedFeatures)
				}}).toPromise(); 

        
        if (response.error) {
            const errMsg = handleGqlErr(response.error);
            alerts.error(title, errMsg);
            return "";
        }

			 

			if (response.data.createPlan.success) {
				goto('/admin/plan');
			} else {
				error = response.data.createPlan.message;
			}
		} catch (err: any) {
			error = `Failed to create plan: ${err.message}`;
			console.error(err);
		} finally {
			loading = false;
		}
	}

	// Load features on component mount
	import { onMount } from 'svelte';
	import alerts from '$lib/stores/alerts';
	onMount(() => loadFeatures());
</script>

<div class="min-h-screen bg-gray-50 p-8">
	<div class="max-w-2xl mx-auto">
		<!-- Header -->
		<div class="mb-8">
			<a href="/admin/plan" class="text-indigo-600 hover:text-indigo-700 font-medium mb-4 inline-block">
				← Back to Plans
			</a>
			<h1 class="text-4xl font-bold text-gray-900">Create New Plan</h1>
			<p class="text-gray-600 mt-2">Add a new subscription plan to your system</p>
		</div>

		<!-- Error Alert -->
		{#if error}
			<div class="mb-6 p-4 bg-red-50 border border-red-200 rounded-lg text-red-800">
				<strong>Error:</strong> {error}
			</div>
		{/if}

		<!-- Form -->
		<div class="bg-white rounded-lg shadow-md p-8">
			<form on:submit|preventDefault={handleSubmit} class="space-y-6">
				<!-- Slug -->
				<div>
					<label for="slug" class="block text-sm font-medium text-gray-700 mb-2">
						Slug <span class="text-red-500">*</span>
					</label>
					<input
						type="text"
						id="slug"
						bind:value={formData.slug}
						placeholder="e.g., starter"
						class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
						required
					/>
					<p class="text-xs text-gray-500 mt-1">Unique identifier (immutable after creation)</p>
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
						{loading ? 'Creating...' : '✓ Create Plan'}
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
	</div>
</div>

<style>
	:global(body) {
		background-color: #f9fafb;
	}
</style>
