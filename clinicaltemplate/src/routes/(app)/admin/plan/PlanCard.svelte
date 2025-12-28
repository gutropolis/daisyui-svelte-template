<script lang="ts">
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
	export let onDelete: (id: number) => void;
	export let onRefresh: () => void;
	export let isLoading: boolean = false;

	function formatDate(dateString: string): string {
		return new Date(dateString).toLocaleDateString('en-US', {
			year: 'numeric',
			month: 'short',
			day: 'numeric'
		});
	}
</script>

<div class="border border-gray-200 rounded-lg p-6 hover:shadow-lg transition bg-white">
	<!-- Header -->
	<div class="mb-4">
		<h3 class="text-lg font-bold text-gray-900">{plan.name}</h3>
		<p class="text-sm text-gray-600 mt-1">
			<code class="bg-gray-100 px-2 py-0.5 rounded text-xs">{plan.slug}</code>
		</p>
	</div>

	<!-- Price and Duration -->
	<div class="mb-4 p-3 bg-gradient-to-r from-green-50 to-blue-50 rounded-lg">
		<p class="text-3xl font-bold text-green-600">${plan.price}</p>
		<p class="text-xs text-gray-600 mt-1">{plan.durationDays} days</p>
	</div>

	<!-- Limits Grid -->
	<div class="grid grid-cols-3 gap-2 mb-4 p-3 bg-gray-50 rounded">
		<div class="text-center">
			<p class="text-xs text-gray-600">Users</p>
			<p class="text-sm font-bold text-gray-900">
				{plan.maxUsers ? `${plan.maxUsers}` : '∞'}
			</p>
		</div>
		<div class="text-center">
			<p class="text-xs text-gray-600">Studies</p>
			<p class="text-sm font-bold text-gray-900">
				{plan.maxStudies ? `${plan.maxStudies}` : '∞'}
			</p>
		</div>
		<div class="text-center">
			<p class="text-xs text-gray-600">Storage</p>
			<p class="text-sm font-bold text-gray-900">
				{plan.maxStorageGb ? `${plan.maxStorageGb}GB` : '∞'}
			</p>
		</div>
	</div>

	<!-- Features -->
	{#if plan.features.length > 0}
		<div class="mb-4">
			<p class="text-xs font-semibold text-gray-700 mb-2">Features ({plan.features.length}):</p>
			<div class="flex flex-wrap gap-1">
				{#each plan.features as featureId}
					<span class="inline-block bg-blue-100 text-blue-800 text-xs px-2 py-1 rounded">
						#{featureId}
					</span>
				{/each}
			</div>
		</div>
	{/if}

	<!-- Metadata -->
	<div class="text-xs text-gray-500 mb-4 pb-4 border-b border-gray-200">
		<p>Created: {formatDate(plan.createdAt)}</p>
		<p>Updated: {formatDate(plan.updatedAt)}</p>
	</div>

	<!-- Actions -->
	<div class="flex gap-2">
		<a
			href="/admin/plan/{plan.id}/edit"
			class="flex-1 bg-blue-600 hover:bg-blue-700 text-white text-sm font-medium py-2 px-3 rounded transition text-center"
		>
			✏️ Edit
		</a>
		<a
			href="/admin/plan/{plan.id}"
			class="flex-1 bg-purple-600 hover:bg-purple-700 text-white text-sm font-medium py-2 px-3 rounded transition text-center"
		>
			👁️ View
		</a>
		<button
			on:click={() => {
				if (confirm(`Are you sure you want to delete "${plan.name}"?`)) {
					onDelete(plan.id);
				}
			}}
			disabled={isLoading}
			class="flex-1 bg-red-600 hover:bg-red-700 disabled:bg-red-400 text-white text-sm font-medium py-2 px-3 rounded transition"
		>
			🗑️ Delete
		</button>
	</div>
</div>

<style>
</style>
