<script lang="ts">
	import type { PermissionType } from '$lib/modal/user';

	export let permission: PermissionType;
	export let onEdit: (permission: PermissionType) => void;
	export let onDelete: (id: number) => void;
	export let isLoading: boolean = false;

	function handleEdit() {
		onEdit(permission);
	}

	function handleDelete() {
		if (confirm(`Are you sure you want to delete "${permission.name}"?`)) {
			onDelete(permission.id);
		}
	}

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

<div class="border border-gray-200 rounded-lg p-4 hover:shadow-md transition">
	<!-- Header -->
	<div class="flex items-start justify-between mb-3">
		<div class="flex-1">
			<div class="flex items-center gap-2">
				{#if permission.icon}
					<span class="text-2xl">{permission.icon}</span>
				{/if}
				<h3 class="text-lg font-semibold text-gray-900">{permission.name}</h3>
			</div>
			<p class="text-sm text-gray-500 font-mono mt-1">{permission.keyName}</p>
		</div>
		<div class="flex gap-2">
			<button
				on:click={handleEdit}
				disabled={isLoading}
				class="bg-blue-500 hover:bg-blue-600 text-white px-3 py-1 rounded text-sm disabled:bg-gray-400 transition"
			>
				✏️ Edit
			</button>
			<button
				on:click={handleDelete}
				disabled={isLoading}
				class="bg-red-500 hover:bg-red-600 text-white px-3 py-1 rounded text-sm disabled:bg-gray-400 transition"
			>
				🗑️ Delete
			</button>
		</div>
	</div>

	<!-- Description -->
	{#if permission.description}
		<p class="text-gray-700 text-sm mb-3">{permission.description}</p>
	{/if}

	<!-- Timestamps -->
	<div class="text-xs text-gray-400 space-y-1">
		<p>Created: {formatDate(permission.createdAt)}</p>
		<p>Updated: {formatDate(permission.updatedAt)}</p>
	</div>
</div>

<style>
</style>
