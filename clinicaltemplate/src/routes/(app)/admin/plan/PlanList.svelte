<script lang="ts">
	import PlanCard from './PlanCard.svelte';

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

	export let plans: Plan[] = [];
	export let loading: boolean = false;
	export let onEdit: (plan: Plan) => void;
	export let onDelete: (id: number) => void;
	export let onRefresh: () => void;
</script>

<div class="bg-white rounded-lg shadow-md p-6">
	<div class="flex items-center justify-between mb-6">
		<h2 class="text-xl font-bold text-gray-900">Plans List</h2>
		{#if !loading}
			<button
				on:click={onRefresh}
				class="text-sm bg-gray-200 hover:bg-gray-300 text-gray-800 px-3 py-1 rounded transition"
			>
				🔄 Refresh
			</button>
		{/if}
	</div>

	{#if loading}
		<div class="text-center py-12">
			<p class="text-gray-500">Loading plans...</p>
		</div>
	{:else if plans.length === 0}
		<div class="text-center py-12 text-gray-500">
			<p>No plans found. Create one to get started!</p>
		</div>
	{:else}
		<div class="space-y-4">
			{#each plans as plan (plan.id)}
				<PlanCard
					{plan}
					{onEdit}
					{onDelete}
					isLoading={loading}
				/>
			{/each}
		</div>
	{/if}
</div>

<style>
</style>
