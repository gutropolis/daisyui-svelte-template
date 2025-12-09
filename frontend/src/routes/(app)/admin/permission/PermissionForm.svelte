<script lang="ts">
	import type { PermissionType } from '$lib/modal/user';

	export let isEditing: boolean = false;
	export let editingId: number | null = null;
	export let features: Array<{ id: number; name: string }> = [];
	export let loading: boolean = false;
	export let error: string = '';
	export let formData = {
		keyName: '',
		name: '',
		description: '',
		icon: '',
		featureId: ''
	};
	export let onSubmit: (isEdit: boolean) => Promise<void>;
	export let onReset: () => void;

	async function handleSubmit() {
		await onSubmit(isEditing);
	}
</script>

<div class="bg-white rounded-lg shadow-md p-6">
	<h2 class="text-xl font-bold text-gray-900 mb-6">
		{isEditing ? 'Edit Permission' : 'Create New Permission'}
	</h2>

	<!-- Error Message -->
	{#if error}
		<div class="mb-4 p-3 bg-red-50 border border-red-200 rounded-md text-red-800 text-sm">
			{error}
		</div>
	{/if}

	<form on:submit|preventDefault={handleSubmit} class="space-y-4">
		<!-- Key Name -->
		<div>
			<label for="keyName" class="block text-sm font-medium text-gray-700 mb-2">
				Key Name
			</label>
			<input
				type="text"
				id="keyName"
				bind:value={formData.keyName}
				placeholder="e.g., permission.create"
				disabled={isEditing}
				class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 disabled:bg-gray-100"
				required
			/>
			<p class="text-xs text-gray-500 mt-1">
				{isEditing ? 'Cannot change key name' : 'Use dot notation (e.g., permission.create)'}
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
				placeholder="e.g., Create Permission"
				class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
				required
			/>
		</div>

		<!-- Feature -->
		<div>
			<label for="featureId" class="block text-sm font-medium text-gray-700 mb-2">
				Feature
			</label>
			<select
				id="featureId"
				bind:value={formData.featureId}
				disabled={isEditing}
				class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 disabled:bg-gray-100"
				required
			>
				<option value="">-- Select Feature --</option>
				{#each features as feature}
					<option value={feature.id}>{feature.name}</option>
				{/each}
			</select>
			<p class="text-xs text-gray-500 mt-1">
				{isEditing ? 'Cannot change feature' : 'Select which feature this permission belongs to'}
			</p>
		</div>

		<!-- Icon -->
		<div>
			<label for="icon" class="block text-sm font-medium text-gray-700 mb-2">
				Icon (Emoji)
			</label>
			<input
				type="text"
				id="icon"
				bind:value={formData.icon}
				placeholder="e.g., ➕, 👁️, ✏️, 🗑️"
				maxlength="10"
				class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
			/>
			<p class="text-xs text-gray-500 mt-1">Optional emoji icon for the permission</p>
		</div>

		<!-- Description -->
		<div>
			<label for="description" class="block text-sm font-medium text-gray-700 mb-2">
				Description
			</label>
			<textarea
				id="description"
				bind:value={formData.description}
				placeholder="Enter permission description..."
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
					<span>⏳ {isEditing ? 'Updating...' : 'Creating...'}</span>
				{:else}
					{isEditing ? 'Update Permission' : 'Create Permission'}
				{/if}
			</button>

			{#if isEditing}
				<button
					type="button"
					on:click={onReset}
					disabled={loading}
					class="flex-1 bg-gray-300 hover:bg-gray-400 text-gray-800 font-medium py-2 px-4 rounded-md disabled:bg-gray-400 transition"
				>
					Cancel
				</button>
			{/if}
		</div>
	</form>
</div>

<style>
</style>
