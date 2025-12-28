<script lang="ts">
	export let isOpen: boolean = false;
	export let loading: boolean = false;
	export let searchTerm: string = '';
	export let selectedFeature: string = '';
	export let features: Array<{ id: number; name: string }> = [];
	export let onSearch: (term: string) => void;
	export let onFilterByFeature: (featureId: string) => void;
	export let onClear: () => void;
	export let onClose: () => void;
</script>

{#if isOpen}
	<div class="fixed inset-0 bg-black/50 flex items-center justify-center z-50">
		<div class="bg-white rounded-lg shadow-lg p-6 w-full max-w-md">
			<div class="flex justify-between items-center mb-6">
				<h3 class="text-xl font-bold text-gray-900">Filter & Search</h3>
				<button
					on:click={onClose}
					class="text-gray-500 hover:text-gray-700 text-2xl leading-none"
				>
					✕
				</button>
			</div>

			<!-- Search -->
			<div class="mb-6">
				<label for="search" class="block text-sm font-medium text-gray-700 mb-2">
					Search Permissions
				</label>
				<input
					type="text"
					id="search"
					placeholder="Search by name or key..."
					value={searchTerm}
					on:input={(e) => onSearch(e.currentTarget.value)}
					class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
				/>
				<p class="text-xs text-gray-500 mt-1">Search in name and key name</p>
			</div>

			<!-- Filter by Feature -->
			<div class="mb-6">
				<label for="feature" class="block text-sm font-medium text-gray-700 mb-2">
					Filter by Feature
				</label>
				<select
					id="feature"
					value={selectedFeature}
					on:change={(e) => onFilterByFeature(e.currentTarget.value)}
					class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
				>
					<option value="">-- All Features --</option>
					{#each features as feature}
						<option value={feature.id}>{feature.name}</option>
					{/each}
				</select>
				<p class="text-xs text-gray-500 mt-1">Show only permissions for selected feature</p>
			</div>

			<!-- Buttons -->
			<div class="flex gap-3">
				<button
					on:click={onClear}
					disabled={loading}
					class="flex-1 bg-gray-300 hover:bg-gray-400 disabled:bg-gray-200 text-gray-800 font-medium py-2 px-4 rounded transition"
				>
					Clear Filters
				</button>
				<button
					on:click={onClose}
					class="flex-1 bg-blue-600 hover:bg-blue-700 text-white font-medium py-2 px-4 rounded transition"
				>
					Done
				</button>
			</div>
		</div>
	</div>
{/if}

<style>
</style>
