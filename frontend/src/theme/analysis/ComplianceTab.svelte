<script lang="ts">
	import StatsCard from './StatsCard.svelte';
	import ComplianceMetric from './ComplianceMetric.svelte';

	interface ComplianceDoc {
		name: string;
		type: string;
		status: 'APPROVED' | 'REVIEW' | 'PENDING';
		trial: string;
		reviewer: string;
		uploaded: string;
		reviewed?: string;
		approved?: string;
	}

	interface ApprovalWorkflow {
		name: string;
		status: 'APPROVED' | 'PENDING';
		trial: string;
		approver: string;
		submitted: string;
		reviewed?: string;
	}

	const complianceMetrics = [
		{ title: 'Protocol Compliance', description: 'Documentation', value: 95, progress: 95, status: 'compliant' as const },
		{ title: 'Reporting Timeliness', description: 'Timeline', value: 88, progress: 88, status: 'warning' as const },
		{ title: 'Data Entry Accuracy', description: 'Data Quality', value: 92, progress: 92, status: 'compliant' as const },
		{ title: 'AE Reporting Within 24h', description: 'Safety', value: 78, progress: 78, status: 'non-compliant' as const },
		{ title: 'Staff Training Completion', description: 'Training', value: 100, progress: 100, status: 'compliant' as const },
		{ title: 'Site Visit Frequency', description: 'Monitoring', value: 85, progress: 85, status: 'warning' as const }
	];

	const documents: ComplianceDoc[] = [
		{
			name: 'Clinical Trial Protocol',
			type: 'PROTOCOL',
			status: 'APPROVED',
			trial: 'CT-2024-001',
			reviewer: 'Dr. Sarah Johnson',
			uploaded: '15/1/2024',
			reviewed: '20/1/2024',
			approved: '22/1/2024'
		},
		{
			name: 'Informed Consent Form',
			type: 'ICF',
			status: 'REVIEW',
			trial: 'CT-2024-001',
			reviewer: 'IRB Committee',
			uploaded: '10/2/2024',
			reviewed: '15/2/2024'
		}
	];

	const approvalWorkflows: ApprovalWorkflow[] = [
		{
			name: 'PROTOCOL Approval',
			status: 'APPROVED',
			trial: 'CT-2024-001',
			approver: 'Dr. Sarah Johnson',
			submitted: '15/1/2024',
			reviewed: '22/1/2024'
		},
		{
			name: 'BUDGET Approval',
			status: 'PENDING',
			trial: 'CT-2024-002',
			approver: 'Finance Department',
			submitted: '1/2/2024'
		}
	];
</script>

<div class="space-y-6">
	<!-- Summary Stats -->
	<div class="grid grid-cols-4 gap-4">
		<StatsCard title="Compliance Score" value="90%" icon="checkmark" variant="success" />
		<StatsCard title="Active Documents" value="3" icon="document" variant="primary" />
		<StatsCard title="Pending Approvals" value="1" icon="alert" variant="warning" />
		<StatsCard title="Inspections" value="2" icon="eye" variant="primary" />
	</div>

	<!-- Compliance Metrics -->
	<div class="grid grid-cols-2 gap-6">
		<!-- Compliance Metrics -->
		<div class="bg-white rounded-lg border border-gray-200 p-6">
			<div class="flex items-center gap-2 mb-4">
				<svg xmlns="http://www.w3.org/2000/svg" class="w-5 h-5 text-gray-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
					<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
				</svg>
				<h3 class="font-bold text-gray-900">Compliance Metrics</h3>
			</div>
			<p class="text-sm text-gray-600 mb-6">Overall compliance status across categories</p>

			<div class="space-y-6">
				{#each complianceMetrics as metric}
					<ComplianceMetric title={metric.title} description={metric.description} value={metric.value} progress={metric.progress} status={metric.status} />
				{/each}
			</div>
		</div>

		<!-- Compliance Summary -->
		<div class="bg-white rounded-lg border border-gray-200 p-6">
			<h3 class="font-bold text-gray-900 mb-4">Compliance Summary</h3>
			<p class="text-sm text-gray-600 mb-6">Key compliance indicators and trends</p>

			<!-- Large Score -->
			<div class="bg-green-50 rounded-lg p-6 mb-6 text-center">
				<p class="text-6xl font-bold text-green-600">90%</p>
				<p class="text-sm text-gray-600 mt-2">Overall Compliance Score</p>
			</div>

			<!-- Status Breakdown -->
			<div class="grid grid-cols-2 gap-4 mb-6">
				<div class="bg-green-50 rounded-lg p-4 text-center">
					<p class="text-3xl font-bold text-green-600">3</p>
					<p class="text-xs text-gray-600 mt-1">Compliant</p>
				</div>
				<div class="bg-amber-50 rounded-lg p-4 text-center">
					<p class="text-3xl font-bold text-amber-600">2</p>
					<p class="text-xs text-gray-600 mt-1">Warning</p>
				</div>
			</div>

			<!-- Action Items -->
			<div class="pt-6 border-t border-gray-200">
				<p class="font-semibold text-gray-900 mb-3">Action Items</p>
				<ul class="space-y-2">
					<li class="flex items-start gap-2 text-sm">
						<svg xmlns="http://www.w3.org/2000/svg" class="w-4 h-4 text-red-600 mt-0.5 shrink-0" fill="currentColor" viewBox="0 0 24 24">
							<path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 15h-2v-2h2v2zm0-4h-2V7h2v6z" />
						</svg>
						<span class="text-gray-700">Improve AE reporting timeliness</span>
					</li>
					<li class="flex items-start gap-2 text-sm">
						<svg xmlns="http://www.w3.org/2000/svg" class="w-4 h-4 text-amber-600 mt-0.5 shrink-0" fill="currentColor" viewBox="0 0 24 24">
							<path d="M1 21h22L12 2 1 21zm12-3h-2v-2h2v2zm0-4h-2v-4h2v4z" />
						</svg>
						<span class="text-gray-700">Increase site monitoring frequency</span>
					</li>
					<li class="flex items-start gap-2 text-sm">
						<svg xmlns="http://www.w3.org/2000/svg" class="w-4 h-4 text-blue-600 mt-0.5 shrink-0" fill="currentColor" viewBox="0 0 24 24">
							<path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm0 16H5V5h14v14zm-5.04-6.71l-2.75 3.54-1.3-1.54c-.3-.36-.77-.36-1.07 0-.3.36-.3.92 0 1.28l1.98 2.36c.3.36.77.36 1.07 0L17.1 9.7c.3-.36.3-.92 0-1.28-.3-.36-.77-.36-1.07 0z" />
						</svg>
						<span class="text-gray-700">Schedule compliance training session</span>
					</li>
				</ul>
			</div>
		</div>
	</div>

	<!-- Regulatory Documents -->
	<div class="bg-white rounded-lg border border-gray-200 p-6">
		<h3 class="font-bold text-gray-900 mb-4 flex items-center gap-2">
			<svg xmlns="http://www.w3.org/2000/svg" class="w-5 h-5 text-gray-600" fill="currentColor" viewBox="0 0 24 24">
				<path d="M14 2H6a2 2 0 00-2 2v16a2 2 0 002 2h12a2 2 0 002-2V8l-8-6z" />
			</svg>
			Regulatory Documents
		</h3>
		<p class="text-sm text-gray-600 mb-4">Manage clinical trial regulatory documentation</p>

		<div class="space-y-3">
			{#each documents as doc}
				<div class="border border-gray-200 rounded-lg p-4">
					<div class="flex items-start justify-between mb-2">
						<div>
							<p class="font-semibold text-gray-900">{doc.name}</p>
							<p class="text-xs text-gray-600 mt-1">
								<strong>Trial:</strong> {doc.trial} | <strong>Reviewer:</strong> {doc.reviewer}
							</p>
						</div>
						<span
							class="px-2 py-1 text-xs font-semibold rounded"
							class:bg-green-100={doc.status === 'APPROVED'}
							class:text-green-800={doc.status === 'APPROVED'}
							class:bg-yellow-100={doc.status === 'REVIEW'}
							class:text-yellow-800={doc.status === 'REVIEW'}
							class:bg-gray-100={doc.status === 'PENDING'}
							class:text-gray-800={doc.status === 'PENDING'}
						>
							{doc.status}
						</span>
					</div>
					<div class="flex gap-4 text-xs text-gray-600">
						<span>📤 Uploaded: {doc.uploaded}</span>
						{#if doc.reviewed}
							<span>👁️ Reviewed: {doc.reviewed}</span>
						{/if}
						{#if doc.approved}
							<span>✓ Approved: {doc.approved}</span>
						{/if}
					</div>
					<div class="flex gap-2 mt-3">
						<button class="px-3 py-1 text-gray-700 border border-gray-300 rounded text-xs hover:bg-gray-50">
							👁️ View
						</button>
						<button class="px-3 py-1 text-gray-700 border border-gray-300 rounded text-xs hover:bg-gray-50">
							📥 Download
						</button>
					</div>
				</div>
			{/each}
		</div>

		<button class="mt-4 px-4 py-2 bg-black text-white rounded-lg text-sm hover:bg-gray-800">
			📄 Upload Document
		</button>
	</div>

	<!-- Approval Workflows -->
	<div class="bg-white rounded-lg border border-gray-200 p-6">
		<div class="flex items-center justify-between mb-4">
			<div class="flex items-center gap-2">
				<svg xmlns="http://www.w3.org/2000/svg" class="w-5 h-5 text-gray-600" fill="currentColor" viewBox="0 0 24 24">
					<path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z" />
				</svg>
				<h3 class="font-bold text-gray-900">Approval Workflows</h3>
			</div>
			<button class="px-4 py-2 bg-black text-white rounded-lg text-sm hover:bg-gray-800 flex items-center gap-2">
				⚙️ New Approval Request
			</button>
		</div>
		<p class="text-sm text-gray-600 mb-4">Track approval status for trials and documents</p>

		<div class="space-y-3">
			{#each approvalWorkflows as workflow}
				<div class="border border-gray-200 rounded-lg p-4">
					<div class="flex items-start justify-between mb-2">
						<div>
							<p class="font-semibold text-gray-900">{workflow.name}</p>
							<p class="text-xs text-gray-600 mt-1">
								<strong>Trial:</strong> {workflow.trial} | <strong>Approver:</strong> {workflow.approver}
							</p>
						</div>
						<span
							class="px-2 py-1 text-xs font-semibold rounded"
							class:bg-green-100={workflow.status === 'APPROVED'}
							class:text-green-800={workflow.status === 'APPROVED'}
							class:bg-yellow-100={workflow.status === 'PENDING'}
							class:text-yellow-800={workflow.status === 'PENDING'}
						>
							{workflow.status}
						</span>
					</div>
					<div class="flex gap-4 text-xs text-gray-600">
						<span>📤 Submitted: {workflow.submitted}</span>
						{#if workflow.reviewed}
							<span>✓ Reviewed: {workflow.reviewed}</span>
						{/if}
					</div>
				</div>
			{/each}
		</div>
	</div>
</div>
