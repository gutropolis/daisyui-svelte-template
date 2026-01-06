<script lang="ts">
	import { onMount } from 'svelte';
	import { graphqlClient } from '$lib/graphql/client';
	import PlanCard from './PlanCard.svelte';
	import FilterModal from './FilterModal.svelte';
	import PaginationModal from './PaginationModal.svelte';
	import { DELETE_PLAN_MUTATION, PLANS_QUERY } from '$lib/gql/plan';

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

	// State
	let plans: Plan[] = [];
	let loading = false;
	let error = '';
	let success = '';
	let paginationModalOpen = false;
	let filterModalOpen = false;

	// Pagination state
	let currentPage = 1;
	let totalPages = 1;
	let total = 0;
	let hasNext = false;
	let hasPrev = false;

	// Filter state
	let searchTerm = '';

	

	// Load plans on mount
	onMount(async () => {
		await loadPlans();
	});

	// Load plans
	async function loadPlans() {
		loading = true;
		error = '';
		try {
			const filterInput: any = {};
			if (searchTerm) {
				filterInput.search = searchTerm;
			}

			const response = await graphqlClient.request(PLANS_QUERY, {
				page: currentPage,
				limit: 10,
				filterInput: Object.keys(filterInput).length > 0 ? filterInput : null
			});

			if (response.plans.success) {
				plans = response.plans.data;
				const pagination = response.plans.pagination;
				totalPages = pagination.totalPages;
				total = pagination.total;
				hasNext = pagination.hasNext;
				hasPrev = pagination.hasPrev;
			} else {
				error = response.plans.message;
			}
		} catch (err: any) {
			error = `Failed to load plans: ${err.message}`;
			console.error(err);
		} finally {
			loading = false;
		}
	}

	// Delete plan
	async function handleDelete(id: number) {
		if (!confirm('Are you sure you want to delete this plan?')) {
			return;
		}

		loading = true;
		error = '';
		success = '';

		try {
			const response = await graphqlClient.request(DELETE_PLAN_MUTATION, {
				id
			});

			if (response.deletePlan.success) {
				success = 'Plan deleted successfully!';
				await loadPlans();
				setTimeout(() => (success = ''), 3000);
			} else {
				error = response.deletePlan.message;
			}
		} catch (err: any) {
			error = `Failed to delete plan: ${err.message}`;
			console.error(err);
		} finally {
			loading = false;
		}
	}

	// Handle page change
	function handlePageChange(newPage: number) {
		currentPage = newPage;
		loadPlans();
		paginationModalOpen = false;
	}

	// Handle search
	function handleSearch(term: string) {
		searchTerm = term;
		currentPage = 1;
		loadPlans();
	}

	// Clear filters
	function clearFilters() {
		searchTerm = '';
		currentPage = 1;
		loadPlans();
		filterModalOpen = false;
	}
</script>

<div class="min-h-screen bg-gray-50 p-8">
	<div class="max-w-7xl mx-auto">
		<!-- Header -->
		<div class="mb-8 flex items-center justify-between">
			<div>
				<h1 class="text-4xl font-bold text-gray-900">Plans Management</h1>
				<p class="text-gray-600 mt-2">View, edit, and manage subscription plans</p>
			</div>
			<a
				href="/admin/plan/new"
				class="bg-green-600 hover:bg-green-700 text-white font-medium py-3 px-6 rounded-lg transition flex items-center gap-2"
			>
				➕ New Plan
			</a>
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

		<!-- Controls -->
		<div class="mb-6 bg-white rounded-lg shadow-md p-4">
			<div class="flex gap-3">
				<button
					on:click={() => (filterModalOpen = true)}
					class="flex-1 bg-indigo-600 hover:bg-indigo-700 text-white font-medium py-2 px-4 rounded-md transition"
				>
					🔍 Filter & Search
				</button>
				<button
					on:click={() => (paginationModalOpen = true)}
					class="flex-1 bg-purple-600 hover:bg-purple-700 text-white font-medium py-2 px-4 rounded-md transition"
				>
					📄 Pagination ({currentPage}/{totalPages})
				</button>
				<button
					on:click={loadPlans}
					disabled={loading}
					class="flex-1 bg-gray-600 hover:bg-gray-700 disabled:bg-gray-400 text-white font-medium py-2 px-4 rounded-md transition"
				>
					🔄 Refresh
				</button>
			</div>
		</div>

		<!-- Plans List -->
		{#if loading}
			<div class="text-center py-12">
				<p class="text-gray-500 text-lg">Loading plans...</p>
			</div>
		{:else if plans.length === 0}
			<div class="text-center py-12 bg-white rounded-lg shadow-md">
				<p class="text-gray-500 text-lg">No plans found. Create one to get started!</p>
				<a
					href="/admin/plan/new"
					class="mt-4 inline-block bg-green-600 hover:bg-green-700 text-white font-medium py-2 px-6 rounded-lg transition"
				>
					Create First Plan
				</a>
			</div>
		{:else}
			<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
				{#each plans as plan (plan.id)}
					<PlanCard
						{plan}
						{loading}
						onDelete={handleDelete}
						onRefresh={loadPlans}
					/>
				{/each}
			</div>
		{/if}
	</div>
</div>

<!-- Modals -->
<PaginationModal
	isOpen={paginationModalOpen}
	page={currentPage}
	{totalPages}
	{total}
	{hasNext}
	{hasPrev}
	{loading}
	onPageChange={handlePageChange}
	onClose={() => (paginationModalOpen = false)}
/>

<FilterModal
	isOpen={filterModalOpen}
	searchTerm={searchTerm}
	{loading}
	onSearch={handleSearch}
	onClear={clearFilters}
	onClose={() => (filterModalOpen = false)}
/>

<style>
	:global(body) {
		background-color: #f9fafb;
	}
</style>
