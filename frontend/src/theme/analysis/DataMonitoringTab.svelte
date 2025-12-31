<script lang="ts">
	import StatsCard from './StatsCard.svelte';
	import ComplianceMetric from './ComplianceMetric.svelte';

	interface DataForm {
		name: string;
		status: 'VERIFIED' | 'ENTERED';
		patient: string;
		visit: string;
		trial: string;
		collected: string;
		verified?: string;
	}

	const dataForms: DataForm[] = [
		{
			name: 'Baseline Assessment',
			status: 'VERIFIED',
			patient: 'SUB-001 (JD)',
			visit: 'Visit 1 - Screening',
			trial: 'CT-2024-001',
			collected: '15/3/2024',
			verified: '16/3/2024'
		},
		{
			name: 'Laboratory Results',
			status: 'ENTERED',
			patient: 'SUB-002 (AB)',
			visit: 'Visit 2 - Visit 2',
			trial: 'CT-2024-001',
			collected: '18/3/2024'
		}
	];
</script>

<div class="space-y-6">
	<!-- Summary Stats -->
	<div class="grid grid-cols-4 gap-4">
		<StatsCard title="Total Forms" value="3" icon="document" variant="primary" />
		<StatsCard title="Verified Data" value="1" icon="check" variant="success" />
		<StatsCard title="Data Queries" value="1" icon="alert" variant="warning" />
		<StatsCard title="Adverse Events" value="2" icon="alert" variant="danger" />
	</div>

	<!-- Data Collection Forms -->
	<div class="bg-white rounded-lg border border-gray-200 p-6">
		<h3 class="font-bold text-gray-900 mb-2 flex items-center gap-2">
			<svg xmlns="http://www.w3.org/2000/svg" class="w-5 h-5 text-gray-600" fill="currentColor" viewBox="0 0 24 24">
				<path d="M14 2H6a2 2 0 00-2 2v16a2 2 0 002 2h12a2 2 0 002-2V8l-8-6z" />
			</svg>
			Clinical Data Forms
		</h3>
		<p class="text-sm text-gray-600 mb-4">Manage and track clinical data collection</p>

		<!-- Search and Filter -->
		<div class="flex gap-3 mb-6">
			<div class="flex-1 relative">
				<input type="text" placeholder="Search by form name, patient, or trial..." class="w-full px-3 py-2 border border-gray-300 rounded-lg text-sm" />
			</div>
			<select class="px-3 py-2 border border-gray-300 rounded-lg text-sm bg-white">
				<option>All Status</option>
				<option>Verified</option>
				<option>Entered</option>
			</select>
		</div>

		<!-- Forms Table -->
		<div class="space-y-3">
			{#each dataForms as form}
				<div class="border border-gray-200 rounded-lg p-4 hover:border-gray-300 transition-colors">
					<div class="flex items-start justify-between mb-2">
						<div>
							<p class="font-semibold text-gray-900">{form.name}</p>
							<div class="flex gap-3 mt-2 text-sm">
								<span class="text-gray-600"><strong>Patient:</strong> {form.patient}</span>
								<span class="text-gray-600"><strong>Visit:</strong> {form.visit}</span>
								<span class="text-gray-600"><strong>Trial:</strong> {form.trial}</span>
							</div>
						</div>
						<span class="px-2 py-1 bg-green-100 text-green-800 text-xs font-semibold rounded">
							{form.status}
						</span>
					</div>
					<div class="flex gap-4 text-xs text-gray-600">
						<span>📅 Collected: {form.collected}</span>
						{#if form.verified}
							<span>✓ Verified: {form.verified}</span>
						{/if}
					</div>
					<div class="flex gap-2 mt-3">
						<button class="px-3 py-1 text-gray-700 border border-gray-300 rounded text-xs hover:bg-gray-50">
							👁️ View
						</button>
						<button class="px-3 py-1 text-gray-700 border border-gray-300 rounded text-xs hover:bg-gray-50">
							✏️ Edit
						</button>
					</div>
				</div>
			{/each}
		</div>

		<!-- Action Buttons -->
		<div class="flex gap-2 mt-6">
			<button class="px-4 py-2 border border-gray-300 rounded-lg text-sm hover:bg-gray-50 flex items-center gap-2">
				📥 Import Data
			</button>
			<button class="px-4 py-2 border border-gray-300 rounded-lg text-sm hover:bg-gray-50 flex items-center gap-2">
				📤 Export
			</button>
		</div>
	</div>
</div>
