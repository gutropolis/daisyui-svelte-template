<script lang="ts">
	import { graphqlClient } from '$lib/graphql/client';

	interface Plan {
		id: number;
		slug: string;
		name: string;
		price: string;
		durationDays: number;
		maxUsers: number | null;
		maxStudies: number | null;
		maxStorageGb: number | null;
		features: number[];
		createdAt: string;
		updatedAt: string;
	}

	export let plan: Plan;
	export let loading: boolean = false;
	export let success: string = '';
	export let error: string = '';
	export let onSuccess: () => Promise<void>;
	export let onCancel: () => void;

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
		name: plan.name,
		price: plan.price,
		durationDays: plan.durationDays,
		maxUsers: plan.maxUsers?.toString() || '',
		maxStudies: plan.maxStudies?.toString() || '',
		maxStorageGb: plan.maxStorageGb?.toString() || '',
		features: plan.features.join(',')
	};

	async function handleSubmit() {
		if (!formData.name || !formData.price || !formData.durationDays) {
			error = 'Name, price, and duration are required';
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

			const response = await graphqlClient.request(UPDATE_PLAN_MUTATION, {
				id: plan.id,
				input: {
					name: formData.name,
					price: formData.price.toString(),
					durationDays: parseInt(formData.durationDays.toString()),
					maxUsers: formData.maxUsers ? parseInt(formData.maxUsers) : null,
					maxStudies: formData.maxStudies ? parseInt(formData.maxStudies) : null,
					maxStorageGb: formData.maxStorageGb ? parseInt(formData.maxStorageGb) : null,
					features: featuresArray
				}
			});

			if (response.updatePlan.success) {
				success = 'Plan updated successfully!';
				await onSuccess();
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

	function resetForm() {
		formData = {
			name: plan.name,
			price: plan.price,
			durationDays: plan.durationDays,
			maxUsers: plan.maxUsers?.toString() || '',
			maxStudies: plan.maxStudies?.toString() || '',
			maxStorageGb: plan.maxStorageGb?.toString() || '',
			features: plan.features.join(',')
		};
	}
</script>

<div class="bg-white rounded-lg shadow-md p-6">
	<h2 class="text-xl font-bold text-gray-900 mb-2">Edit Plan</h2>
	<p class="text-sm text-gray-600 mb-6">
		Slug: <code class="bg-gray-100 px-2 py-1 rounded">{plan.slug}</code>
	</p>

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
				class="w-full px-3 py-2 border border-gray-300 rounded-md bg-gray-100 text-gray-600"
			/>
			<p class="text-xs text-gray-500 mt-1">Cannot be changed after creation</p>
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
				class="flex-1 bg-green-600 hover:bg-green-700 disabled:bg-green-400 text-white font-medium py-2 px-4 rounded-md transition"
			>
				{loading ? 'Updating...' : '✓ Update Plan'}
			</button>
			<button
				type="button"
				on:click={resetForm}
				disabled={loading}
				class="flex-1 bg-gray-300 hover:bg-gray-400 disabled:bg-gray-200 text-gray-800 font-medium py-2 px-4 rounded-md transition"
			>
				Reset
			</button>
			<button
				type="button"
				on:click={onCancel}
				disabled={loading}
				class="flex-1 bg-red-600 hover:bg-red-700 disabled:bg-red-400 text-white font-medium py-2 px-4 rounded-md transition"
			>
				Cancel
			</button>
		</div>
	</form>
</div>

<style>
</style>
