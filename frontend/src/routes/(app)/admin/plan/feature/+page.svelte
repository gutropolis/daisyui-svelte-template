<script lang="ts">
	import { onMount } from 'svelte';
	import { authStore } from '$lib/stores/auth';
	import { graphqlClient } from '$lib/graphql/client';
	import type { PlanFeatureType } from '$lib/modal/user';

	// State
	let features: PlanFeatureType[] = [];
	let loading = false;
	let error = '';
	let success = '';
	let isEditing = false;
	let editingId: number | null = null;

	// Form state
	let formData = {
		keyName: '',
		name: '',
		description: ''
	};

	// GraphQL Queries
	const PLAN_FEATURES_QUERY = `
		query {
			planFeatures {
				success
				message
				data {
					id
					keyName
					name
					description
					createdAt
					updatedAt
				}
			}
		}
	`;

	const CREATE_PLAN_FEATURE = `
		mutation CreatePlanFeature($input: CreatePlanFeatureInput!) {
			createPlanFeature(input: $input) {
				success
				message
				data {
					id
					keyName
					name
					description
					createdAt
					updatedAt
				}
			}
		}
	`;

	const UPDATE_PLAN_FEATURE = `
		mutation UpdatePlanFeature($id: Int!, $input: UpdatePlanFeatureInput!) {
			updatePlanFeature(id: $id, input: $input) {
				success
				message
				data {
					id
					keyName
					name
					description
					createdAt
					updatedAt
				}
			}
		}
	`;

	const DELETE_PLAN_FEATURE = `
		mutation DeletePlanFeature($id: Int!) {
			deletePlanFeature(id: $id) {
				success
				message
			}
		}
	`;

	// Load features on mount
	onMount(async () => {
		await loadFeatures();
	});

	// Load all features
	async function loadFeatures() {
		loading = true;
		error = '';
		try {
			const response = await graphqlClient.request(PLAN_FEATURES_QUERY);
			if (response.planFeatures.success) {
				features = response.planFeatures.data;
			} else {
				error = response.planFeatures.message;
			}
		} catch (err: any) {
			error = `Failed to load features: ${err.message}`;
			console.error(err);
		} finally {
			loading = false;
		}
	}

	// Create new feature
	async function handleCreate() {
		if (!formData.keyName || !formData.name) {
			error = 'Key name and name are required';
			return;
		}

		loading = true;
		error = '';
		success = '';

		try {
			const response = await graphqlClient.request(CREATE_PLAN_FEATURE, {
				input: {
					keyName: formData.keyName,
					name: formData.name,
					description: formData.description || null
				}
			});

			if (response.createPlanFeature.success) {
				success = 'Feature created successfully!';
				await loadFeatures();
				resetForm();
				setTimeout(() => (success = ''), 3000);
			} else {
				error = response.createPlanFeature.message;
			}
		} catch (err: any) {
			error = `Failed to create feature: ${err.message}`;
			console.error(err);
		} finally {
			loading = false;
		}
	}

	// Update feature
	async function handleUpdate() {
		if (!editingId || !formData.name) {
			error = 'Name is required';
			return;
		}

		loading = true;
		error = '';
		success = '';

		try {
			const response = await graphqlClient.request(UPDATE_PLAN_FEATURE, {
				id: editingId,
				input: {
					name: formData.name,
					description: formData.description || null
				}
			});

			if (response.updatePlanFeature.success) {
				success = 'Feature updated successfully!';
				await loadFeatures();
				resetForm();
				setTimeout(() => (success = ''), 3000);
			} else {
				error = response.updatePlanFeature.message;
			}
		} catch (err: any) {
			error = `Failed to update feature: ${err.message}`;
			console.error(err);
		} finally {
			loading = false;
		}
	}

	// Delete feature
	async function handleDelete(id: number) {
		if (!confirm('Are you sure you want to delete this feature?')) {
			return;
		}

		loading = true;
		error = '';
		success = '';

		try {
			const response = await graphqlClient.request(DELETE_PLAN_FEATURE, {
				id
			});

			if (response.deletePlanFeature.success) {
				success = 'Feature deleted successfully!';
				await loadFeatures();
				setTimeout(() => (success = ''), 3000);
			} else {
				error = response.deletePlanFeature.message;
			}
		} catch (err: any) {
			error = `Failed to delete feature: ${err.message}`;
			console.error(err);
		} finally {
			loading = false;
		}
	}

	// Edit feature
	function startEdit(feature: PlanFeatureType) {
		isEditing = true;
		editingId = feature.id;
		formData = {
			keyName: feature.keyName,
			name: feature.name,
			description: feature.description || ''
		};
	}

	// Reset form
	function resetForm() {
		isEditing = false;
		editingId = null;
		formData = {
			keyName: '',
			name: '',
			description: ''
		};
		error = '';
	}

	// Format date
	function formatDate(date: string) {
		return new Date(date).toLocaleDateString('en-US', {
			year: 'numeric',
			month: 'short',
			day: 'numeric',
			hour: '2-digit',
			minute: '2-digit'
		});
	}
</script>

<div class="min-h-screen bg-gray-50 p-8">
	<div class="max-w-6xl mx-auto">
		<!-- Header -->
		<div class="mb-8">
			<h1 class="text-4xl font-bold text-gray-900">Plan Features</h1>
			<p class="text-gray-600 mt-2">Manage plan features and capabilities</p>
		</div>

		<!-- Alerts -->
		{#if error}
			<div class="mb-6 p-4 bg-red-50 border border-red-200 rounded-lg text-red-800">
				<strong>Error:</strong> {error}
			</div>
		{/if}

		{#if success}
			<div class="mb-6 p-4 bg-green-50 border border-green-200 rounded-lg text-green-800">
				✓ {success}
			</div>
		{/if}

		<div class="grid grid-cols-1 lg:grid-cols-3 gap-8">
			<!-- Form Section -->
			<div class="lg:col-span-1">
				<div class="bg-white rounded-lg shadow-md p-6">
					<h2 class="text-xl font-bold text-gray-900 mb-6">
						{isEditing ? 'Edit Feature' : 'Create New Feature'}
					</h2>

					<form on:submit|preventDefault={isEditing ? handleUpdate : handleCreate} class="space-y-4">
						<!-- Key Name -->
						<div>
							<label for="keyName" class="block text-sm font-medium text-gray-700 mb-2">
								Key Name
							</label>
							<input
								type="text"
								id="keyName"
								bind:value={formData.keyName}
								placeholder="e.g. trial_management"
								disabled={isEditing}
								class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 disabled:bg-gray-100"
								required
							/>
							<p class="text-xs text-gray-500 mt-1">
								{isEditing ? 'Cannot change key name' : 'Use lowercase with underscores'}
							</p>
						</div>

						<!-- Name -->
						<div>
							<label for="name" class="block text-sm font-medium text-gray-700 mb-2">
								Name
							</label>
							<input
								type="text"
								id="name"
								bind:value={formData.name}
								placeholder="e.g. Trial Management"
								class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
								required
							/>
						</div>

						<!-- Description -->
						<div>
							<label for="description" class="block text-sm font-medium text-gray-700 mb-2">
								Description
							</label>
							<textarea
								id="description"
								bind:value={formData.description}
								placeholder="Enter feature description..."
								rows="4"
								class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
							/>
						</div>

						<!-- Buttons -->
						<div class="flex gap-3 pt-4">
							<button
								type="submit"
								disabled={loading}
								class="flex-1 bg-blue-600 hover:bg-blue-700 text-white font-medium py-2 px-4 rounded-md disabled:bg-gray-400 transition"
							>
								{#if loading}
									<span class="inline-block">⏳ {isEditing ? 'Updating...' : 'Creating...'}</span>
								{:else}
									{isEditing ? 'Update Feature' : 'Create Feature'}
								{/if}
							</button>

							{#if isEditing}
								<button
									type="button"
									on:click={resetForm}
									class="flex-1 bg-gray-300 hover:bg-gray-400 text-gray-800 font-medium py-2 px-4 rounded-md transition"
								>
									Cancel
								</button>
							{/if}
						</div>
					</form>
				</div>
			</div>

			<!-- Features List Section -->
			<div class="lg:col-span-2">
				<div class="bg-white rounded-lg shadow-md p-6">
					<div class="flex items-center justify-between mb-6">
						<h2 class="text-xl font-bold text-gray-900">Features List</h2>
						{#if !loading}
							<button
								on:click={loadFeatures}
								class="text-sm bg-gray-200 hover:bg-gray-300 text-gray-800 px-3 py-1 rounded"
							>
								🔄 Refresh
							</button>
						{/if}
					</div>

					{#if loading}
						<div class="text-center py-12">
							<p class="text-gray-500">Loading features...</p>
						</div>
					{:else if features.length === 0}
						<div class="text-center py-12 text-gray-500">
							<p>No features found. Create one to get started!</p>
						</div>
					{:else}
						<div class="space-y-4">
							{#each features as feature (feature.id)}
								<div
									class="border border-gray-200 rounded-lg p-4 hover:shadow-md transition"
									class:ring-2={editingId === feature.id}
									class:ring-blue-500={editingId === feature.id}
								>
									<!-- Feature Header -->
									<div class="flex items-start justify-between mb-3">
										<div class="flex-1">
											<h3 class="text-lg font-semibold text-gray-900">{feature.name}</h3>
											<p class="text-sm text-gray-500 font-mono">{feature.keyName}</p>
										</div>
										<div class="flex gap-2">
											<button
												on:click={() => startEdit(feature)}
												class="bg-blue-500 hover:bg-blue-600 text-white px-3 py-1 rounded text-sm"
											>
												✏️ Edit
											</button>
											<button
												on:click={() => handleDelete(feature.id)}
												disabled={loading}
												class="bg-red-500 hover:bg-red-600 text-white px-3 py-1 rounded text-sm disabled:bg-gray-400"
											>
												🗑️ Delete
											</button>
										</div>
									</div>

									<!-- Description -->
									{#if feature.description}
										<p class="text-gray-700 text-sm mb-3">{feature.description}</p>
									{/if}

									<!-- Timestamps -->
									<div class="text-xs text-gray-400 space-y-1">
										<p>Created: {formatDate(feature.createdAt)}</p>
										<p>Updated: {formatDate(feature.updatedAt)}</p>
									</div>
								</div>
							{/each}
						</div>
					{/if}
				</div>
			</div>
		</div>
	</div>
</div>

<style>
	:global(body) {
		background-color: #f9fafb;
	}
</style>
