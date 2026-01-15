<script lang="ts">
	import { goto } from '$app/navigation';
	import { getContextClient } from '@urql/svelte';
	import { onMount } from 'svelte';
	import { SUBSCRIPTIONS_QUERY } from '$lib/gql/subscription';
	import { handleGqlErr } from '$lib/utils/gqlfx';
	import alerts from '$lib/stores/alerts';

	const client = getContextClient();

	const STATUS_OPTIONS = [
		{ label: 'All statuses', value: 'ALL' },
		{ label: 'Active', value: 'ACTIVE' },
		{ label: 'Canceled', value: 'CANCELED' },
		{ label: 'Expired', value: 'EXPIRED' }
	];

	let loading = false;
	let error = '';
	let subscriptions: Array<any> = [];
	let statusFilter = 'ALL';
	let searchTerm = '';

	const formatDate = (dateString: string) => {
		if (!dateString) return '—';
		const parsed = new Date(dateString);
		if (Number.isNaN(parsed.getTime())) {
			return dateString;
		}
		return parsed.toLocaleDateString('en-US', {
			year: 'numeric',
			month: 'short',
			day: 'numeric'
		});
	};

	const formatCurrency = (value: number | string | null | undefined) => {
		if (value === null || value === undefined || value === '') {
			return '—';
		}
		const amount = typeof value === 'number' ? value : parseFloat(value);
		if (Number.isNaN(amount)) {
			return String(value);
		}
		return `$${amount.toFixed(2)}`;
	};

	const statusClasses = (status: string) => {
		switch (status) {
			case 'ACTIVE':
				return 'bg-green-100 text-green-800 border-green-200';
			case 'CANCELED':
				return 'bg-red-100 text-red-800 border-red-200';
			case 'EXPIRED':
				return 'bg-yellow-100 text-yellow-800 border-yellow-200';
			default:
				return 'bg-gray-100 text-gray-800 border-gray-200';
		}
	};

	const subscriberName = (sub: any) => {
		const user = sub?.user;
		if (!user) return 'Unknown user';
		const name = `${user.firstName ?? ''} ${user.lastName ?? ''}`.trim();
		return name || user.email || 'Unknown user';
	};

	const planLabel = (sub: any) => {
		const plan = sub?.plan;
		if (!plan) return '—';
		const parts: string[] = [];
		if (plan.slug) parts.push(plan.slug);
		if (plan.durationDays) parts.push(`${plan.durationDays} day${plan.durationDays === 1 ? '' : 's'}`);
		if (plan.price) parts.push(formatCurrency(plan.price));
		return parts.join(' · ') || '—';
	};

	async function loadSubscriptions() {
		loading = true;
		error = '';
		try {
			const variables: Record<string, string> = {};
			if (statusFilter !== 'ALL') {
				variables.status = statusFilter;
			}
			const response = await client.query(SUBSCRIPTIONS_QUERY, variables).toPromise();
			if (response.error) {
				const errMsg = handleGqlErr(response.error);
				error = errMsg;
				alerts.error('Load subscribers', errMsg);
				return;
			}
			subscriptions = response.data?.subscriptions ?? [];
		} catch (err: any) {
			error = err?.message ?? 'Failed to load subscribers';
			console.error('Failed to load subscriptions', err);
		} finally {
			loading = false;
		}
	}

	function refresh() {
		loadSubscriptions();
	}

	function handleStatusChange() {
		loadSubscriptions();
	}

	const normalizedSearch = () => searchTerm.trim().toLowerCase();

	$: filteredSubscriptions = subscriptions.filter(sub => {
		const term = normalizedSearch();
		if (!term) return true;
		const user = sub?.user ?? {};
		const plan = sub?.plan ?? {};
		const haystack = `${user.firstName ?? ''} ${user.lastName ?? ''} ${user.email ?? ''} ${plan.name ?? ''} ${plan.slug ?? ''}`.toLowerCase();
		return haystack.includes(term);
	});

	onMount(() => {
		loadSubscriptions();
	});
</script>

<div class="min-h-screen bg-gray-50 p-8">
	<div class="max-w-6xl mx-auto space-y-6">
		<div class="flex flex-col gap-4 md:flex-row md:items-center md:justify-between">
			<div>
				<p class="text-sm text-gray-500">Subscribers</p>
				<h1 class="text-3xl font-bold text-gray-900">Plan Subscriptions</h1>
			</div>
			<div class="flex gap-3">
				<button
					type="button"
					on:click={refresh}
					class="flex items-center gap-2 rounded-lg border border-gray-300 px-4 py-2 text-gray-700 hover:bg-gray-100"
				>
					<span>↻</span>
					<span>Refresh</span>
				</button>
				<button
					on:click={() => goto('/admin/subscribers/new')}
					class="rounded-lg bg-blue-600 px-5 py-2 font-semibold text-white shadow hover:bg-blue-700"
				>
					+ Add Subscriber
				</button>
			</div>
		</div>

		<div class="grid gap-4 rounded-xl border border-gray-200 bg-white p-5 shadow-sm md:grid-cols-3">
			<div class="md:col-span-2">
				<label class="block text-sm font-medium text-gray-700">Search</label>
				<input
					type="text"
					placeholder="Search by user or plan"
					bind:value={searchTerm}
					class="mt-1 w-full rounded-lg border border-gray-300 px-4 py-2 focus:border-blue-500 focus:outline-none"
				/>
			</div>
			<div>
				<label class="block text-sm font-medium text-gray-700">Status</label>
				<select
					bind:value={statusFilter}
					class="mt-1 w-full rounded-lg border border-gray-300 px-4 py-2 focus:border-blue-500 focus:outline-none"
					on:change={handleStatusChange}
				>
					{#each STATUS_OPTIONS as option}
						<option value={option.value}>{option.label}</option>
					{/each}
				</select>
			</div>
		</div>

		{#if error}
			<div class="rounded-lg border border-red-200 bg-red-50 p-4 text-red-800">
				<strong class="font-semibold">Error:</strong> {error}
			</div>
		{/if}

		{#if loading}
			<div class="rounded-lg border border-gray-200 bg-white p-8 text-center text-gray-500 shadow">
				Loading subscribers...
			</div>
		{:else if filteredSubscriptions.length === 0}
			<div class="rounded-lg border border-gray-200 bg-white p-8 text-center text-gray-500 shadow">
				No subscribers found.
			</div>
		{:else}
			<div class="overflow-x-auto rounded-xl border border-gray-200 bg-white shadow">
				<table class="min-w-full divide-y divide-gray-200">
					<thead class="bg-gray-50">
						<tr>
							<th class="px-6 py-3 text-left text-xs font-semibold uppercase tracking-wider text-gray-500">Subscriber</th>
							<th class="px-6 py-3 text-left text-xs font-semibold uppercase tracking-wider text-gray-500">Plan</th>
							<th class="px-6 py-3 text-left text-xs font-semibold uppercase tracking-wider text-gray-500">Start</th>
							<th class="px-6 py-3 text-left text-xs font-semibold uppercase tracking-wider text-gray-500">Expires</th>
							<th class="px-6 py-3 text-left text-xs font-semibold uppercase tracking-wider text-gray-500">Status</th>
							<th class="px-6 py-3 text-left text-xs font-semibold uppercase tracking-wider text-gray-500">Billing</th>
						</tr>
					</thead>
					<tbody class="divide-y divide-gray-200">
						{#each filteredSubscriptions as sub (sub.id)}
							<tr class="hover:bg-gray-50">
								<td class="px-6 py-4">
									<div class="font-semibold text-gray-900">{subscriberName(sub)}</div>
									<div class="text-sm text-gray-500">{sub.user?.email ?? '—'}</div>
								</td>
								<td class="px-6 py-4">
									<div class="font-medium text-gray-900">{sub.plan?.name ?? sub.plan?.slug ?? '—'}</div>
									<div class="text-sm text-gray-500">{planLabel(sub)}</div>
								</td>
								<td class="px-6 py-4 text-sm text-gray-900">{formatDate(sub.startDate)}</td>
								<td class="px-6 py-4 text-sm text-gray-900">{formatDate(sub.endDate)}</td>
								<td class="px-6 py-4">
									<span class={`inline-flex rounded-full border px-3 py-1 text-xs font-semibold ${statusClasses(sub.status)}`}>
										{sub.status ?? 'UNKNOWN'}
									</span>
								</td>
								<td class="px-6 py-4 text-sm text-gray-900">
									<div class="flex flex-col gap-1">
										<span class="text-gray-700">{sub.paidStatus ? 'Paid' : 'Unpaid'}</span>
										<span class="text-xs text-gray-500">Auto renew: {sub.autoRenew ? 'On' : 'Off'}</span>
									</div>
								</td>
							</tr>
						{/each}
					</tbody>
				</table>
			</div>
		{/if}
	</div>
</div>
