<script lang="ts">
	import type { PermissionType } from '$lib/modal/user';

	export let isOpen: boolean = false;
	export let page: number = 1;
	export let totalPages: number = 1;
	export let total: number = 0;
	export let hasNext: boolean = false;
	export let hasPrev: boolean = false;
	export let loading: boolean = false;
	export let onPageChange: (newPage: number) => void;
	export let onClose: () => void;
</script>

{#if isOpen}
	<div class="fixed inset-0 bg-black/50 flex items-center justify-center z-50">
		<div class="bg-white rounded-lg shadow-lg p-6 w-full max-w-md">
			<div class="flex justify-between items-center mb-6">
				<h3 class="text-xl font-bold text-gray-900">Pagination</h3>
				<button
					on:click={onClose}
					class="text-gray-500 hover:text-gray-700 text-2xl leading-none"
				>
					✕
				</button>
			</div>

			<!-- Pagination Info -->
			<div class="bg-gray-50 p-4 rounded mb-6">
				<p class="text-sm text-gray-700">
					<strong>Page:</strong> {page} of {totalPages}
				</p>
				<p class="text-sm text-gray-700 mt-2">
					<strong>Total Permissions:</strong> {total}
				</p>
				<p class="text-sm text-gray-700 mt-2">
					<strong>Items Per Page:</strong> 10
				</p>
			</div>

			<!-- Page Navigation -->
			<div class="flex gap-3 mb-6">
				<button
					on:click={() => onPageChange(page - 1)}
					disabled={!hasPrev || loading}
					class="flex-1 bg-gray-300 hover:bg-gray-400 disabled:bg-gray-200 text-gray-800 font-medium py-2 px-4 rounded transition"
				>
					← Previous
				</button>
				<button
					on:click={() => onPageChange(page + 1)}
					disabled={!hasNext || loading}
					class="flex-1 bg-gray-300 hover:bg-gray-400 disabled:bg-gray-200 text-gray-800 font-medium py-2 px-4 rounded transition"
				>
					Next →
				</button>
			</div>

			<!-- Quick Page Jump -->
			<div class="mb-6">
				<label class="block text-sm font-medium text-gray-700 mb-2">
					Go to Page:
				</label>
				<input
					type="number"
					min="1"
					max={totalPages}
					value={page}
					on:change={(e) => {
						const newPage = parseInt(e.currentTarget.value);
						if (newPage >= 1 && newPage <= totalPages) {
							onPageChange(newPage);
						}
					}}
					class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
				/>
			</div>

			<!-- Close Button -->
			<button
				on:click={onClose}
				class="w-full bg-gray-300 hover:bg-gray-400 text-gray-800 font-medium py-2 px-4 rounded transition"
			>
				Close
			</button>
		</div>
	</div>
{/if}

<style>
</style>
