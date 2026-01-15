<script lang="ts">
	import { goto } from '$app/navigation';
	import { getContextClient } from '@urql/svelte';
	import { onMount } from 'svelte';
	import { CREATE_SUBSCRIPTION_MUTATION } from '$lib/gql/subscription';
	import { ALL_USERS_QUERY } from '$lib/gql/user';
	import { PLANS_QUERY } from '$lib/gql/plan';
	import { handleGqlErr } from '$lib/utils/gqlfx';
	import alerts from '$lib/stores/alerts';

	const client = getContextClient();

	const STATUS_OPTIONS = [
		{ label: 'Active', value: 'ACTIVE' },
		{ label: 'Canceled', value: 'CANCELED' },
		{ label: 'Expired', value: 'EXPIRED' }
	];

	const today = new Date().toISOString().slice(0, 10);

	let loading = true;
	let submitting = false;
	let error = '';
	let success = '';
	let users: Array<any> = [];
	let plans: Array<any> = [];
	let autoFillEndDate = true;

	let formData = {
		userId: '',
		planId: '',
		startDate: today,
		endDate: '',
		status: 'ACTIVE',
		paidStatus: true,
		autoRenew: true
	};

	const userLabel = (user: any) => {
		const name = `${user.firstName ?? ''} ${user.lastName ?? ''}`.trim();
		return name || user.email || `User #${user.id}`;
	};

	const formatCurrency = (value: number | string) => {
		const amount = typeof value === 'number' ? value : parseFloat(String(value));
		if (Number.isNaN(amount)) {
			return '$0.00';
		}
		return `$${amount.toFixed(2)}`;
	};

	const computeEndDate = (startDate: string, durationDays?: number) => {
		if (!startDate || !durationDays) return '';
		const start = new Date(startDate);
		if (Number.isNaN(start.getTime())) return '';
		const end = new Date(start);
		end.setDate(end.getDate() + Number(durationDays));
		return end.toISOString().slice(0, 10);
	};

	async function loadReferenceData() {
		loading = true;
		error = '';
		try {
			const [usersResponse, plansResponse] = await Promise.all([
				client.query(ALL_USERS_QUERY, { isActive: true }).toPromise(),
				client.query(PLANS_QUERY, { page: 1, limit: 100, filterInput: null }).toPromise()
			]);

			if (usersResponse.error) {
				const errMsg = handleGqlErr(usersResponse.error);
				error = errMsg;
				alerts.error('Load users', errMsg);
				return;
			}

			if (plansResponse.error) {
				const errMsg = handleGqlErr(plansResponse.error);
				error = errMsg;
				alerts.error('Load plans', errMsg);
				return;
			}

			users = usersResponse.data?.allUsers ?? [];
			plans = plansResponse.data?.plans?.data ?? [];
		} catch (err: any) {
			error = err?.message ?? 'Failed to load data';
			console.error('Failed to load reference data', err);
		} finally {
			loading = false;
		}
	}

	const findSelectedPlan = () => plans.find(plan => `${plan.id}` === formData.planId);

	$: selectedPlan = findSelectedPlan();

	$: if (autoFillEndDate && formData.startDate && selectedPlan?.durationDays) {
		const computed = computeEndDate(formData.startDate, selectedPlan.durationDays);
		if (computed && formData.endDate !== computed) {
			formData = { ...formData, endDate: computed };
		}
	}

	onMount(() => {
		loadReferenceData();
	});

	async function handleSubmit() {
		if (!formData.userId || !formData.planId || !formData.startDate || !formData.endDate) {
			error = 'Please select a user, plan, start date, and end date.';
			return;
		}

		submitting = true;
		error = '';
		success = '';

		try {
			const payload = {
				userId: parseInt(formData.userId, 10),
				planId: parseInt(formData.planId, 10),
				startDate: formData.startDate,
				endDate: formData.endDate,
				status: formData.status,
				paidStatus: formData.paidStatus,
				autoRenew: formData.autoRenew
			};

			if (Number.isNaN(payload.userId) || Number.isNaN(payload.planId)) {
				error = 'Invalid user or plan selection.';
				submitting = false;
				return;
			}

			const response = await client
				.mutation(CREATE_SUBSCRIPTION_MUTATION, { input: payload })
				.toPromise();

			if (response.error) {
				const errMsg = handleGqlErr(response.error);
				error = errMsg;
				alerts.error('Create subscriber', errMsg);
				return;
			}

			if (!response.data?.createSubscription?.subscription) {
				error = 'Subscription was not created. Please try again.';
				return;
			}

			success = 'Subscriber added successfully!';
			alerts.success('Create subscriber', 'Subscription created');
			setTimeout(() => goto('/admin/subscribers'), 1200);
		} catch (err: any) {
			error = err?.message ?? 'Failed to create subscription';
			console.error('Failed to create subscription', err);
		} finally {
			submitting = false;
		}
	}
</script>

<div class="min-h-screen bg-gray-50 p-8">
	<div class="mx-auto max-w-3xl space-y-6">
		<div>
			<a href="/admin/subscribers" class="text-indigo-600 hover:text-indigo-800">← Back to subscribers</a>
			<h1 class="mt-2 text-3xl font-bold text-gray-900">Add Subscriber</h1>
			<p class="text-gray-600">Assign a plan to an existing user and set their subscription window.</p>
		</div>

		{#if error}
			<div class="rounded-lg border border-red-200 bg-red-50 p-4 text-red-800">
				<strong>Error:</strong> {error}
			</div>
		{/if}

		{#if success}
			<div class="rounded-lg border border-green-200 bg-green-50 p-4 text-green-800">
				✓ {success}
			</div>
		{/if}

		{#if loading}
			<div class="rounded-lg border border-gray-200 bg-white p-8 text-center text-gray-500 shadow">
				Loading users and plans...
			</div>
		{:else}
			<div class="rounded-xl border border-gray-200 bg-white p-6 shadow">
				<form on:submit|preventDefault={handleSubmit} class="space-y-6">
					<div class="space-y-1">
						<label class="text-sm font-medium text-gray-700">Select user <span class="text-red-500">*</span></label>
						<select
							bind:value={formData.userId}
							class="w-full rounded-lg border border-gray-300 px-4 py-2 focus:border-blue-500 focus:outline-none"
							required
						>
							<option value="" disabled>Select a user</option>
							{#each users as user (user.id)}
								<option value={user.id}>{userLabel(user)} ({user.email})</option>
							{/each}
						</select>
					</div>

					<div class="space-y-1">
						<label class="text-sm font-medium text-gray-700">Select plan <span class="text-red-500">*</span></label>
						<select
							bind:value={formData.planId}
							class="w-full rounded-lg border border-gray-300 px-4 py-2 focus:border-blue-500 focus:outline-none"
							required
						>
							<option value="" disabled>Select a plan</option>
							{#each plans as plan (plan.id)}
								<option value={plan.id}>
									{plan.name} · {formatCurrency(plan.price)}
								</option>
							{/each}
						</select>
						{#if selectedPlan}
							<p class="text-xs text-gray-500">
								Duration: {selectedPlan.durationDays} day{selectedPlan.durationDays === 1 ? '' : 's'} · Slug: {selectedPlan.slug}
							</p>
						{/if}
					</div>

					<div class="grid gap-4 md:grid-cols-2">
						<div>
							<label class="text-sm font-medium text-gray-700">Start date <span class="text-red-500">*</span></label>
							<input
								type="date"
								bind:value={formData.startDate}
								class="mt-1 w-full rounded-lg border border-gray-300 px-4 py-2 focus:border-blue-500 focus:outline-none"
								required
							/>
						</div>
						<div>
							<div class="flex items-center justify-between">
								<label class="text-sm font-medium text-gray-700">End date <span class="text-red-500">*</span></label>
								<label class="flex items-center gap-2 text-xs text-gray-500">
									<input type="checkbox" bind:checked={autoFillEndDate} />
									<span>Auto-calc from plan</span>
								</label>
							</div>
							<input
								type="date"
								bind:value={formData.endDate}
								class="mt-1 w-full rounded-lg border border-gray-300 px-4 py-2 focus:border-blue-500 focus:outline-none"
								required
							/>
						</div>
					</div>

					<div class="grid gap-4 md:grid-cols-3">
						<div>
							<label class="text-sm font-medium text-gray-700">Status</label>
							<select
								bind:value={formData.status}
								class="mt-1 w-full rounded-lg border border-gray-300 px-4 py-2 focus:border-blue-500 focus:outline-none"
							>
								{#each STATUS_OPTIONS as option}
									<option value={option.value}>{option.label}</option>
								{/each}
							</select>
						</div>
						<div>
							<label class="text-sm font-medium text-gray-700">Paid status</label>
							<label class="mt-2 flex items-center gap-2 text-sm text-gray-600">
								<input type="checkbox" bind:checked={formData.paidStatus} class="h-5 w-5" />
								<span>{formData.paidStatus ? 'Marked as paid' : 'Mark as unpaid'}</span>
							</label>
						</div>
						<div>
							<label class="text-sm font-medium text-gray-700">Auto renew</label>
							<label class="mt-2 flex items-center gap-2 text-sm text-gray-600">
								<input type="checkbox" bind:checked={formData.autoRenew} class="h-5 w-5" />
								<span>{formData.autoRenew ? 'Auto renew enabled' : 'Auto renew disabled'}</span>
							</label>
						</div>
					</div>

					<div class="flex gap-3 border-t pt-6">
						<button
							type="submit"
							disabled={submitting}
							class="flex-1 rounded-lg bg-green-600 px-6 py-3 font-semibold text-white transition hover:bg-green-700 disabled:cursor-not-allowed disabled:bg-green-400"
						>
							{submitting ? 'Saving...' : 'Add Subscriber'}
						</button>
						<a
							href="/admin/subscribers"
							class="flex-1 rounded-lg bg-gray-200 px-6 py-3 text-center font-semibold text-gray-700 transition hover:bg-gray-300"
						>
							Cancel
						</a>
					</div>
				</form>
			</div>
		{/if}
	</div>
</div>
