<script lang="ts">
	export let isOpen: boolean = false;
	export let searchTerm: string = '';
	export let loading: boolean = false;
	export let onSearch: (term: string) => void;
	export let onClear: () => void;
	export let onClose: () => void;

	let localSearchTerm = searchTerm;

	function handleSearch() {
		onSearch(localSearchTerm);
	}

	function handleClear() {
		localSearchTerm = '';
		onClear();
	}

	$: localSearchTerm = searchTerm;
</script>

{#if isOpen}
	<div class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
		<div class="bg-white rounded-lg shadow-lg p-6 max-w-md w-full mx-4">
			<h2 class="text-xl font-bold text-gray-900 mb-4">Filter & Search</h2>

			<!-- Search Input -->
			<div class="mb-6">
				<label for="search" class="block text-sm font-medium text-gray-700 mb-2">
					Search by Name or Slug
				</label>
				<input
					type="text"
					id="search"
					bind:value={localSearchTerm}
					placeholder="e.g., Starter, pro"
					class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
				/>
				<p class="text-xs text-gray-500 mt-1">
					Searches in plan name and slug (case-insensitive)
				</p>
			</div>

			<!-- Info -->
			<div class="mb-6 p-4 bg-gray-50 rounded-lg">
				<p class="text-sm text-gray-700">
					{#if searchTerm}
						<strong>Active Filter:</strong> Showing results for "{searchTerm}"
					{:else}
						<em>No filters applied. Showing all plans.</em>
					{/if}
				</p>
			</div>

			<!-- Buttons -->
			<div class="flex gap-3">
				<button
					on:click={handleSearch}
					disabled={loading}
					class="flex-1 bg-blue-600 hover:bg-blue-700 disabled:bg-blue-400 text-white font-medium py-2 px-4 rounded-md transition"
				>
					🔍 Search
				</button>
				<button
					on:click={handleClear}
					disabled={loading}
					class="flex-1 bg-gray-600 hover:bg-gray-700 disabled:bg-gray-400 text-white font-medium py-2 px-4 rounded-md transition"
				>
					Clear All
				</button>
			</div>

			<!-- Close Button -->
			<div class="mt-4">
				<button
					on:click={onClose}
					class="w-full bg-red-600 hover:bg-red-700 text-white font-medium py-2 px-4 rounded-md transition"
				>
					Close
				</button>
			</div>
		</div>
	</div>
{/if}

<style>
</style>
