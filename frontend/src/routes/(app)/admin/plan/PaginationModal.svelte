<script lang="ts">
	export let isOpen: boolean = false;
	export let page: number = 1;
	export let totalPages: number = 1;
	export let total: number = 0;
	export let hasNext: boolean = false;
	export let hasPrev: boolean = false;
	export let loading: boolean = false;
	export let onPageChange: (newPage: number) => void;
	export let onClose: () => void;

	function goToPage(newPage: number) {
		if (newPage >= 1 && newPage <= totalPages) {
			onPageChange(newPage);
		}
	}
</script>

{#if isOpen}
	<div class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
		<div class="bg-white rounded-lg shadow-lg p-6 max-w-md w-full mx-4">
			<h2 class="text-xl font-bold text-gray-900 mb-4">Pagination</h2>

			<!-- Info -->
			<div class="mb-6 p-4 bg-gray-50 rounded-lg">
				<p class="text-sm text-gray-700 mb-2">
					<strong>Total Records:</strong> {total}
				</p>
				<p class="text-sm text-gray-700 mb-2">
					<strong>Current Page:</strong> {page} of {totalPages}
				</p>
				<p class="text-sm text-gray-700">
					<strong>Status:</strong> {hasPrev ? 'Has Previous' : 'First Page'} | {hasNext ? 'Has Next' : 'Last Page'}
				</p>
			</div>

			<!-- Page Input -->
			<div class="mb-6">
				<label for="pageInput" class="block text-sm font-medium text-gray-700 mb-2">
					Go to page:
				</label>
				<div class="flex gap-2">
					<input
						type="number"
						id="pageInput"
						value={page}
						min="1"
						max={totalPages}
						on:change={(e) => {
							const newPage = parseInt(e.target.value);
							goToPage(newPage);
						}}
						class="flex-1 px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
					/>
					<button
						on:click={() => goToPage(page)}
						disabled={loading}
						class="bg-blue-600 hover:bg-blue-700 disabled:bg-blue-400 text-white font-medium py-2 px-4 rounded-md transition"
					>
						Go
					</button>
				</div>
			</div>

			<!-- Navigation Buttons -->
			<div class="flex gap-3 mb-6">
				<button
					on:click={() => goToPage(page - 1)}
					disabled={!hasPrev || loading}
					class="flex-1 bg-gray-600 hover:bg-gray-700 disabled:bg-gray-400 text-white font-medium py-2 px-4 rounded-md transition"
				>
					← Previous
				</button>
				<button
					on:click={() => goToPage(page + 1)}
					disabled={!hasNext || loading}
					class="flex-1 bg-gray-600 hover:bg-gray-700 disabled:bg-gray-400 text-white font-medium py-2 px-4 rounded-md transition"
				>
					Next →
				</button>
			</div>

			<!-- Quick Navigation -->
			{#if totalPages <= 10}
				<div class="mb-6">
					<p class="text-sm font-medium text-gray-700 mb-3">Quick Jump:</p>
					<div class="grid grid-cols-5 gap-2">
						{#each Array.from({ length: totalPages }, (_, i) => i + 1) as pageNum}
							<button
								on:click={() => goToPage(pageNum)}
								class={`py-2 px-2 rounded text-sm font-medium transition ${
									pageNum === page
										? 'bg-blue-600 text-white'
										: 'bg-gray-200 hover:bg-gray-300 text-gray-800'
								}`}
							>
								{pageNum}
							</button>
						{/each}
					</div>
				</div>
			{/if}

			<!-- Close Button -->
			<div>
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
