<script lang="ts">
	import { page } from '$app/stores';
	import { PROJECT_DETAIL_ROUTE } from '$lib/enums/routes';
	import { resolveProjectRoute } from '$lib/utils/routes';
	interface ExportFormat {
		id: string;
		name: string;
		description: string;
		icon: string;
		mimeType: string;
	}

	interface ReportTemplate {
		id: number;
		name: string;
		description: string;
		type: 'summary' | 'detailed' | 'statistical' | 'compliance';
		fields: string[];
		lastGenerated?: string;
	}

	let exportFormats: ExportFormat[] = [
		{
			id: 'csv',
			name: 'CSV',
			description: 'Comma-separated values for spreadsheet applications',
			icon: 'fa-file-csv',
			mimeType: 'text/csv'
		},
		{
			id: 'xlsx',
			name: 'Excel',
			description: 'Microsoft Excel format with formatting',
			icon: 'fa-file-excel',
			mimeType: 'application/vnd.ms-excel'
		},
		{
			id: 'pdf',
			name: 'PDF',
			description: 'Portable Document Format with charts and tables',
			icon: 'fa-file-pdf',
			mimeType: 'application/pdf'
		},
		{
			id: 'json',
			name: 'JSON',
			description: 'JSON format for data integration and APIs',
			icon: 'fa-file-code',
			mimeType: 'application/json'
		}
	];

	let reportTemplates: ReportTemplate[] = [
		{
			id: 1,
			name: 'Patient Demographics',
			description: 'Summary of enrolled patients and demographics',
			type: 'summary',
			fields: ['patientId', 'name', 'dob', 'gender', 'race'],
			lastGenerated: '2024-01-15'
		},
		{
			id: 2,
			name: 'Data Completion Report',
			description: 'Form completion rates and status by event',
			type: 'detailed',
			fields: ['event', 'form', 'completed', 'incomplete', 'percentage'],
			lastGenerated: '2024-01-14'
		},
		{
			id: 3,
			name: 'Data Quality Report',
			description: 'Validation errors and data quality metrics',
			type: 'compliance',
			fields: ['errors', 'warnings', 'missingValues', 'outliers'],
			lastGenerated: '2024-01-10'
		},
		{
			id: 4,
			name: 'Statistical Summary',
			description: 'Descriptive statistics for key variables',
			type: 'statistical',
			fields: ['variable', 'n', 'mean', 'sd', 'min', 'max'],
			lastGenerated: '2024-01-12'
		}
	];

	let selectedFormat = 'csv';
	let selectedEvent = 'all';
	let selectedReport: ReportTemplate | null = null;
	let includeMetadata = true;
	let includeLocked = false;
	let showExportPreview = false;
	let showReportModal = false;
	let newReportName = '';
	let newReportType: 'summary' | 'detailed' | 'statistical' | 'compliance' = 'summary';

	const exportData = () => {
		const format = exportFormats.find(f => f.id === selectedFormat);
		if (!format) return;

		// Mock export - in production would call API
		console.log(`Exporting data as ${format.name}`, {
			format: selectedFormat,
			event: selectedEvent,
			includeMetadata,
			includeLocked
		});

		// Simulate download
		const mockData = 'patientId,name,event,form,status\nP001,John Smith,Baseline,Demographics,Complete\n';
		const blob = new Blob([mockData], { type: format.mimeType });
		const url = window.URL.createObjectURL(blob);
		const link = document.createElement('a');
		link.href = url;
		link.download = `export-${new Date().toISOString().split('T')[0]}.${selectedFormat}`;
		link.click();
	};

	const generateReport = (report: ReportTemplate) => {
		selectedReport = report;
		showReportModal = true;
	};

	const createCustomReport = () => {
		if (!newReportName.trim()) return;

		const report: ReportTemplate = {
			id: Math.max(...reportTemplates.map(r => r.id), 0) + 1,
			name: newReportName,
			description: 'Custom report template',
			type: newReportType,
			fields: [],
			lastGenerated: undefined
		};
		reportTemplates = [...reportTemplates, report];
		newReportName = '';
		newReportType = 'summary';
	};

	const deleteReport = (id: number) => {
		reportTemplates = reportTemplates.filter(r => r.id !== id);
	};

	const getReportTypeColor = (type: string) => {
		switch (type) {
			case 'summary':
				return 'bg-blue-100 text-blue-800';
			case 'detailed':
				return 'bg-green-100 text-green-800';
			case 'statistical':
				return 'bg-purple-100 text-purple-800';
			case 'compliance':
				return 'bg-red-100 text-red-800';
			default:
				return 'bg-gray-100 text-gray-800';
		}
	};

	const getReportTypeIcon = (type: string) => {
		switch (type) {
			case 'summary':
				return 'fa-file-alt';
			case 'detailed':
				return 'fa-file-lines';
			case 'statistical':
				return 'fa-chart-bar';
			case 'compliance':
				return 'fa-check-double';
			default:
				return 'fa-file';
		};
	};

	const projectId = $derived($page.params.projectId ?? '1');
	const projectDetailRoute = $derived(resolveProjectRoute(PROJECT_DETAIL_ROUTE, projectId));
</script>

<div class="p-6 space-y-6">
	<!-- Header -->
	<div>
		<a href={projectDetailRoute} class="flex items-center gap-2 text-blue-600 hover:text-blue-700 text-sm font-medium mb-4">
			<i class="fas fa-arrow-left"></i>Back to Project
		</a>
		<h1 class="text-3xl font-bold text-gray-800 mb-2">Data Export & Reporting</h1>
		<p class="text-gray-600">Export data and generate comprehensive project reports</p>
	</div>

	<!-- Export Section -->
	<div class="bg-white rounded-lg shadow overflow-hidden">
		<div class="p-6 border-b border-gray-200">
			<h2 class="text-xl font-bold text-gray-800 flex items-center gap-2">
				<i class="fas fa-download text-blue-600"></i>
				Export Project Data
			</h2>
		</div>

		<div class="p-6 space-y-6">
			<!-- Export Format Selection -->
			<div>
				<h3 class="font-semibold text-gray-800 mb-4">Select Export Format</h3>
				<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
					{#each exportFormats as format (format.id)}
						<button
							on:click={() => (selectedFormat = format.id)}
							class="p-4 border-2 rounded-lg transition-all text-left hover:shadow-md {selectedFormat === format.id
								? 'border-blue-500 bg-blue-50'
								: 'border-gray-200 hover:border-gray-300'}"
						>
							<i class="fas {format.icon} text-2xl text-gray-700 mb-2 block"></i>
							<p class="font-semibold text-gray-800">{format.name}</p>
							<p class="text-xs text-gray-600 mt-1">{format.description}</p>
						</button>
					{/each}
				</div>
			</div>

			<!-- Export Options -->
			<div>
				<h3 class="font-semibold text-gray-800 mb-4">Export Options</h3>
				<div class="space-y-4">
					<div>
						<label for="event-select" class="block text-sm font-medium text-gray-700 mb-2">Events to Include</label>
						<select
							id="event-select"
							bind:value={selectedEvent}
							class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 outline-none"
						>
							<option value="all">All Events</option>
							<option value="baseline">Baseline Visit</option>
							<option value="week4">Week 4 Follow-up</option>
							<option value="week12">Week 12 Follow-up</option>
							<option value="final">Final Visit</option>
						</select>
					</div>

					<div class="space-y-3">
						<label class="flex items-center gap-3 cursor-pointer">
							<input type="checkbox" bind:checked={includeMetadata} class="w-4 h-4 text-blue-600 rounded" />
							<span class="text-sm text-gray-700">Include metadata (timestamps, user info)</span>
						</label>
						<label class="flex items-center gap-3 cursor-pointer">
							<input type="checkbox" bind:checked={includeLocked} class="w-4 h-4 text-blue-600 rounded" />
							<span class="text-sm text-gray-700">Include locked/completed records</span>
						</label>
					</div>
				</div>
			</div>

			<!-- Action Buttons -->
			<div class="flex gap-3 pt-4 border-t">
				<button
					on:click={() => (showExportPreview = true)}
					class="px-4 py-2 border border-gray-300 text-gray-700 rounded-lg hover:bg-gray-50 font-medium transition-colors flex items-center gap-2"
				>
					<i class="fas fa-eye"></i>
					Preview
				</button>
				<button
					on:click={exportData}
					class="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 font-medium transition-colors flex items-center gap-2"
				>
					<i class="fas fa-download"></i>
					Export Now
				</button>
			</div>
		</div>
	</div>

	<!-- Reports Section -->
	<div class="bg-white rounded-lg shadow overflow-hidden">
		<div class="p-6 border-b border-gray-200 flex items-center justify-between">
			<h2 class="text-xl font-bold text-gray-800 flex items-center gap-2">
				<i class="fas fa-chart-line text-green-600"></i>
				Report Templates
			</h2>
			<button
				on:click={() => (showReportModal = true)}
				class="px-4 py-2 bg-green-600 text-white rounded-lg hover:bg-green-700 font-medium transition-colors flex items-center gap-2"
			>
				<i class="fas fa-plus"></i>
				Create Report
			</button>
		</div>

		<div class="grid grid-cols-1 md:grid-cols-2 gap-4 p-6">
			{#each reportTemplates as report (report.id)}
				<div class="border border-gray-200 rounded-lg p-4 hover:shadow-md transition-shadow">
					<div class="flex items-start justify-between mb-3">
						<div class="flex items-center gap-2">
							<i class="fas {getReportTypeIcon(report.type)} text-xl text-gray-600"></i>
							<h3 class="font-bold text-gray-800">{report.name}</h3>
						</div>
						<button
							on:click={() => deleteReport(report.id)}
							class="px-2 py-1 bg-red-50 text-red-600 rounded hover:bg-red-100 text-xs"
							aria-label="Delete report {report.name}"
						>
							<i class="fas fa-trash"></i>
						</button>
					</div>

					<p class="text-sm text-gray-600 mb-3">{report.description}</p>

					<div class="flex items-center justify-between mb-4">
						<span class="px-2 py-1 rounded text-xs font-medium {getReportTypeColor(report.type)}">
							{report.type.charAt(0).toUpperCase() + report.type.slice(1)}
						</span>
						{#if report.lastGenerated}
							<span class="text-xs text-gray-500">Generated: {report.lastGenerated}</span>
						{/if}
					</div>

					<button
						on:click={() => generateReport(report)}
						class="w-full px-3 py-2 bg-green-600 text-white rounded hover:bg-green-700 text-sm font-medium transition-colors"
					>
						<i class="fas fa-cog mr-1"></i>
						Generate Report
					</button>
				</div>
			{/each}
		</div>
	</div>

	<!-- Report Options -->
	<div class="bg-green-50 rounded-lg shadow p-6 border border-green-200">
		<h3 class="text-lg font-bold text-gray-800 mb-3 flex items-center gap-2">
			<i class="fas fa-lightbulb text-green-600"></i>
			Reporting Features
		</h3>
		<ul class="space-y-2 text-sm text-gray-700">
			<li class="flex items-start gap-2">
				<span class="text-green-600 font-bold">•</span>
				<span><strong>Custom Reports:</strong> Design custom reports with selected fields and filters</span>
			</li>
			<li class="flex items-start gap-2">
				<span class="text-green-600 font-bold">•</span>
				<span><strong>Scheduled Exports:</strong> Set up automated daily/weekly/monthly exports</span>
			</li>
			<li class="flex items-start gap-2">
				<span class="text-green-600 font-bold">•</span>
				<span><strong>Data Validation:</strong> Built-in quality checks and anomaly detection</span>
			</li>
			<li class="flex items-start gap-2">
				<span class="text-green-600 font-bold">•</span>
				<span><strong>Audit Trail:</strong> Track all exports with timestamps and user information</span>
			</li>
		</ul>
	</div>

	<!-- Export Preview Modal -->
	{#if showExportPreview}
		<div class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
			<div class="bg-white rounded-lg shadow-xl p-6 max-w-2xl w-full mx-4 max-h-[80vh] overflow-y-auto">
				<h2 class="text-xl font-bold text-gray-800 mb-4">Export Preview</h2>

				<div class="bg-gray-50 rounded p-4 mb-4 max-h-[40vh] overflow-y-auto font-mono text-xs text-gray-700">
					<div>patientId,name,event,form,status,completedDate</div>
					<div>P001,John Smith,Baseline,Demographics,Complete,2024-01-15</div>
					<div>P002,Jane Doe,Week 4,Vital Signs,Incomplete,</div>
					<div>P003,Bob Johnson,Baseline,Medical History,Draft,</div>
					<div>P004,Alice Williams,Final,Lab Results,Complete,2024-01-16</div>
				</div>

				<p class="text-sm text-gray-600 mb-6">
					This preview shows the first few rows. The actual export will include all matching records.
				</p>

				<div class="flex gap-2 justify-end border-t pt-4">
					<button
						on:click={() => (showExportPreview = false)}
						class="px-4 py-2 border border-gray-300 text-gray-700 rounded-lg hover:bg-gray-50 font-medium transition-colors"
					>
						Close
					</button>
					<button
						on:click={() => {
							exportData();
							showExportPreview = false;
						}}
						class="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 font-medium transition-colors"
					>
						<i class="fas fa-download mr-2"></i>
						Download
					</button>
				</div>
			</div>
		</div>
	{/if}

	<!-- Create Report Modal -->
	{#if showReportModal}
		<div class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
			<div class="bg-white rounded-lg shadow-xl p-6 max-w-md w-full mx-4">
				<h2 class="text-xl font-bold text-gray-800 mb-4">Create Custom Report</h2>

				<div class="space-y-4">
					<div>
						<label for="report-name" class="block text-sm font-medium text-gray-700 mb-1">Report Name</label>
						<input
							id="report-name"
							type="text"
							bind:value={newReportName}
							class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500 outline-none"
							placeholder="e.g., Weekly Summary"
						/>
					</div>

					<div>
						<label for="report-type" class="block text-sm font-medium text-gray-700 mb-1">Report Type</label>
						<select
							id="report-type"
							bind:value={newReportType}
							class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500 outline-none"
						>
							<option value="summary">Summary</option>
							<option value="detailed">Detailed</option>
							<option value="statistical">Statistical</option>
							<option value="compliance">Compliance</option>
						</select>
					</div>
				</div>

				<div class="flex gap-2 justify-end mt-6 border-t pt-4">
					<button
						on:click={() => (showReportModal = false)}
						class="px-4 py-2 border border-gray-300 text-gray-700 rounded-lg hover:bg-gray-50 font-medium transition-colors"
					>
						Cancel
					</button>
					<button
						on:click={createCustomReport}
						disabled={!newReportName.trim()}
						class="px-4 py-2 bg-green-600 text-white rounded-lg hover:bg-green-700 font-medium transition-colors disabled:opacity-50"
					>
						Create Report
					</button>
				</div>
			</div>
		</div>
	{/if}
</div>
