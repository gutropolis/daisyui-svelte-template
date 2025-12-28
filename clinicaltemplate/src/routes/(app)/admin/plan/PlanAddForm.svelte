<script lang="ts">
	import { graphqlClient } from '$lib/graphql/client';

	export let loading: boolean = false;
	export let success: string = '';
	export let error: string = '';
	export let onSuccess: () => Promise<void>;

	const CREATE_PLAN_MUTATION = `
		mutation CreatePlan($input: CreatePlanInput!) {
			createPlan(input: $input) {
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
		slug: '',
		name: '',
		price: '',
		durationDays: 30,
		maxUsers: '',
		maxStudies: '',
		maxStorageGb: '',
		features: ''
	};

	async function handleSubmit() {
		if (!formData.slug || !formData.name || !formData.price || !formData.durationDays) {
			error = 'Slug, name, price, and duration are required';
			return;
		}

		// Validate duration
		if (formData.durationDays < 1) {
			error = 'Duration must be at least 1 day';
			return;
		}

		loading = true;
		error = '';
		success = '';

		try {
			// Parse features string to array
			const featuresArray = formData.features
				? formData.features.split(',').map((f) => parseInt(f.trim())).filter(f => !isNaN(f))
				: [];

			const response = await graphqlClient.request(CREATE_PLAN_MUTATION, {
				input: {
					slug: formData.slug,
					name: formData.name,
					price: formData.price.toString(),
					durationDays: parseInt(formData.durationDays.toString()),
					maxUsers: formData.maxUsers ? parseInt(formData.maxUsers) : null,
					maxStudies: formData.maxStudies ? parseInt(formData.maxStudies) : null,
					maxStorageGb: formData.maxStorageGb ? parseInt(formData.maxStorageGb) : null,
					features: featuresArray
				}
			});

			if (response.createPlan.success) {
				success = 'Plan created successfully!';
				resetForm();
				await onSuccess();
			} else {
				error = response.createPlan.message;
			}
		} catch (err: any) {
			error = `Failed to create plan: ${err.message}`;
			console.error(err);
		} finally {
			loading = false;
		}
	}

	function resetForm() {
		formData = {
			slug: '',
			name: '',
			price: '',
			durationDays: 30,
			maxUsers: '',
			maxStudies: '',
			maxStorageGb: '',
			features: ''
		};
	}
</script>

<div class="bg-white rounded-lg shadow-md p-6">
	<h2 class="text-xl font-bold text-gray-900 mb-6">Create New Plan</h2>

	<!-- Error Message -->
	{#if error}
		<div class="mb-4 p-3 bg-red-50 border border-red-200 rounded-md text-red-800 text-sm">
			{error}
		</div>
	{/if}

	<!-- Success Message -->
	{#if success}
		<div class="mb-4 p-3 bg-green-50 border border-green-200 rounded-md text-green-800 text-sm">
			✓ {success}
		</div>
	{/if}

	<form on:submit|preventDefault={handleSubmit} class="space-y-4">
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
				class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
				required
			/>
			<p class="text-xs text-gray-500 mt-1">Unique identifier (immutable)</p>
		</div>

		<!-- Name -->
		<div>
			<label for="name" class="block text-sm font-medium text-gray-700 mb-2">
				Name <span class="text-red-500">*</span>
			</label>
			<input
				type="text"
				id="name"
				bind:value={formData.name}
				placeholder="e.g., Starter Plan"
				class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
				required
			/>
		</div>

		<!-- Price -->
		<div>
			<label for="price" class="block text-sm font-medium text-gray-700 mb-2">
				Price ($) <span class="text-red-500">*</span>
			</label>
			<input
				type="number"
				id="price"
				bind:value={formData.price}
				placeholder="9.99"
				step="0.01"
				class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
				required
			/>
		</div>

		<!-- Duration Days -->
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
				class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
				required
			/>
		</div>

		<!-- Max Users -->
		<div>
			<label for="maxUsers" class="block text-sm font-medium text-gray-700 mb-2">
				Max Users
			</label>
			<input
				type="number"
				id="maxUsers"
				bind:value={formData.maxUsers}
				placeholder="Leave empty for unlimited"
				min="1"
				class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
			/>
			<p class="text-xs text-gray-500 mt-1">Leave blank for unlimited</p>
		</div>

		<!-- Max Studies -->
		<div>
			<label for="maxStudies" class="block text-sm font-medium text-gray-700 mb-2">
				Max Studies
			</label>
			<input
				type="number"
				id="maxStudies"
				bind:value={formData.maxStudies}
				placeholder="Leave empty for unlimited"
				min="1"
				class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
			/>
			<p class="text-xs text-gray-500 mt-1">Leave blank for unlimited</p>
		</div>

		<!-- Max Storage GB -->
		<div>
			<label for="maxStorageGb" class="block text-sm font-medium text-gray-700 mb-2">
				Max Storage (GB)
			</label>
			<input
				type="number"
				id="maxStorageGb"
				bind:value={formData.maxStorageGb}
				placeholder="Leave empty for unlimited"
				min="1"
				class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
			/>
			<p class="text-xs text-gray-500 mt-1">Leave blank for unlimited</p>
		</div>

		<!-- Features -->
		<div>
			<label for="features" class="block text-sm font-medium text-gray-700 mb-2">
				Features
			</label>
			<input
				type="text"
				id="features"
				bind:value={formData.features}
				placeholder="e.g., 1,2,3"
				class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
			/>
			<p class="text-xs text-gray-500 mt-1">Comma-separated feature IDs</p>
		</div>

		<!-- Buttons -->
		<div class="flex gap-3 pt-4">
			<button
				type="submit"
				disabled={loading}
				class="flex-1 bg-blue-600 hover:bg-blue-700 disabled:bg-blue-400 text-white font-medium py-2 px-4 rounded-md transition"
			>
				{loading ? 'Creating...' : '✓ Create Plan'}
			</button>
			<button
				type="reset"
				on:click={resetForm}
				disabled={loading}
				class="flex-1 bg-gray-300 hover:bg-gray-400 disabled:bg-gray-200 text-gray-800 font-medium py-2 px-4 rounded-md transition"
			>
				Clear
			</button>
		</div>
	</form>
</div>

<style>
</style>
