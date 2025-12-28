<script lang="ts">
	import { page } from '$app/stores';
	import {
		PROJECT_DETAIL_EXPORT_ROUTE,
		PROJECT_DETAIL_ROUTE,
		PROJECT_DETAIL_SETUP_ROUTE
	} from '$lib/enums/routes';
	import { resolveProjectRoute } from '$lib/utils/routes';

	interface DashboardStat {
		label: string;
		value: number | string;
		icon: string;
		color: 'blue' | 'green' | 'yellow' | 'red' | 'purple';
		change?: string;
	}

	interface ActivityLog {
		id: number;
		user: string;
		action: string;
		timestamp: string;
		details: string;
	}

	interface FormMetric {
		name: string;
		total: number;
		completed: number;
		incomplete: number;
		percentage: number;
	}

	let stats: DashboardStat[] = [
		{
			label: 'Total Patients',
			value: 47,
			icon: 'fa-users',
			color: 'blue',
			change: '+3 this week'
		},
		{
			label: 'Data Entry Progress',
			value: '78%',
			icon: 'fa-chart-pie',
			color: 'green',
			change: '+5% from last week'
		},
		{
			label: 'Validation Issues',
			value: 12,
			icon: 'fa-exclamation-triangle',
			color: 'yellow',
			change: '-2 resolved'
		},
		{
			label: 'Project Status',
			value: 'Production',
			icon: 'fa-rocket',
			color: 'purple',
			change: 'Live since 2024-01-10'
		}
	];

	let formMetrics: FormMetric[] = [
		{
			name: 'Demographics',
			total: 47,
			completed: 47,
			incomplete: 0,
			percentage: 100
		},
		{
			name: 'Vital Signs',
			total: 47,
			completed: 43,
			incomplete: 4,
			percentage: 91
		},
		{
			name: 'Medical History',
			total: 47,
			completed: 38,
			incomplete: 9,
			percentage: 81
		},
		{
			name: 'Lab Results',
			total: 47,
			completed: 28,
			incomplete: 19,
			percentage: 60
		},
		{
			name: 'Medications',
			total: 47,
			completed: 35,
			incomplete: 12,
			percentage: 74
		},
		{
			name: 'Follow-up Notes',
			total: 47,
			completed: 21,
			incomplete: 26,
			percentage: 45
		}
	];

	let activityLogs: ActivityLog[] = [
		{
			id: 1,
			user: 'Dr. Sarah Johnson',
			action: 'Completed form entry',
			timestamp: '2024-01-16 14:30',
			details: 'Patient P045 - Medical History'
		},
		{
			id: 2,
			user: 'John Davis',
			action: 'Created new record',
			timestamp: '2024-01-16 13:15',
			details: 'Patient P047 - Baseline Visit'
		},
		{
			id: 3,
			user: 'Dr. Sarah Johnson',
			action: 'Resolved validation error',
			timestamp: '2024-01-16 12:45',
			details: 'Patient P023 - Vital Signs: BP value corrected'
		},
		{
			id: 4,
			user: 'Admin',
			action: 'Updated project settings',
			timestamp: '2024-01-16 10:20',
			details: 'Added new user: Jane Smith'
		},
		{
			id: 5,
			user: 'John Davis',
			action: 'Exported data',
			timestamp: '2024-01-16 09:00',
			details: 'CSV export for week ending 2024-01-12'
		}
	];

	let selectedTimeframe = '7days';
	let showDetailsModal = false;
	let selectedMetric: FormMetric | null = null;

	const getColorClasses = (color: string) => {
		const colors: { [key: string]: { bg: string; text: string; icon: string } } = {
			blue: { bg: 'bg-blue-50', text: 'text-blue-600', icon: 'text-blue-200' },
			green: { bg: 'bg-green-50', text: 'text-green-600', icon: 'text-green-200' },
			yellow: { bg: 'bg-yellow-50', text: 'text-yellow-600', icon: 'text-yellow-200' },
			red: { bg: 'bg-red-50', text: 'text-red-600', icon: 'text-red-200' },
			purple: { bg: 'bg-purple-50', text: 'text-purple-600', icon: 'text-purple-200' }
		};
		return colors[color] || colors.blue;
	};

	const getProgressColor = (percentage: number) => {
		if (percentage >= 90) return 'from-green-500 to-green-600';
		if (percentage >= 70) return 'from-yellow-500 to-yellow-600';
		return 'from-red-500 to-red-600';
	};

	const viewMetricDetails = (metric: FormMetric) => {
		selectedMetric = metric;
		showDetailsModal = true;
	};

	const projectId = $derived($page.params.projectId ?? '1');
	const projectRecordsRoute = $derived(resolveProjectRoute(PROJECT_DETAIL_ROUTE, projectId));
	const projectSetupRoute = $derived(resolveProjectRoute(PROJECT_DETAIL_SETUP_ROUTE, projectId));
	const projectExportRoute = $derived(resolveProjectRoute(PROJECT_DETAIL_EXPORT_ROUTE, projectId));
</script>

<div class="p-6 space-y-6">
	<!-- Header -->
	<div class="flex items-center justify-between">
		<div>
			<h1 class="text-3xl font-bold text-gray-800 mb-2">Project Dashboard</h1>
			<p class="text-gray-600">Real-time analytics and project monitoring</p>
		</div>

		<div class="flex gap-2">
			<select
				bind:value={selectedTimeframe}
				class="px-4 py-2 border border-gray-300 rounded-lg hover:border-blue-300 focus:ring-2 focus:ring-blue-500 outline-none text-sm"
			>
				<option value="today">Today</option>
				<option value="7days">Last 7 Days</option>
				<option value="30days">Last 30 Days</option>
				<option value="alltime">All Time</option>
			</select>
		</div>
	</div>

	<!-- Key Metrics -->
	<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
		{#each stats as stat (stat.label)}
			<div class="bg-white rounded-lg shadow p-6 border-l-4 {stat.color === 'blue'
				? 'border-l-blue-600'
				: stat.color === 'green'
					? 'border-l-green-600'
					: stat.color === 'yellow'
						? 'border-l-yellow-600'
						: stat.color === 'red'
							? 'border-l-red-600'
							: 'border-l-purple-600'}">
				<div class="flex items-start justify-between">
					<div>
						<p class="text-sm text-gray-600 font-medium">{stat.label}</p>
						<p class="text-3xl font-bold text-gray-800 mt-2">{stat.value}</p>
						{#if stat.change}
							<p class="text-xs text-gray-500 mt-2">{stat.change}</p>
						{/if}
					</div>
					<i class="fas {stat.icon} text-3xl {stat.color === 'blue'
						? 'text-blue-200'
						: stat.color === 'green'
							? 'text-green-200'
							: stat.color === 'yellow'
								? 'text-yellow-200'
								: stat.color === 'red'
									? 'text-red-200'
									: 'text-purple-200'}"></i>
				</div>
			</div>
		{/each}
	</div>

	<!-- Form Completion Metrics -->
	<div class="bg-white rounded-lg shadow overflow-hidden">
		<div class="p-6 border-b border-gray-200">
			<h2 class="text-xl font-bold text-gray-800 flex items-center gap-2">
				<i class="fas fa-tasks text-blue-600"></i>
				Form Completion Status
			</h2>
			<p class="text-sm text-gray-600 mt-1">Overall completion rate by form</p>
		</div>

		<div class="p-6 space-y-4">
			{#each formMetrics as metric (metric.name)}
				<button
					on:click={() => viewMetricDetails(metric)}
					class="w-full text-left cursor-pointer hover:bg-gray-50 p-4 rounded-lg transition-colors border-none bg-transparent"
				>
					<div class="flex items-center justify-between mb-2">
						<div>
							<h3 class="font-semibold text-gray-800">{metric.name}</h3>
							<p class="text-sm text-gray-600">{metric.completed}/{metric.total} completed</p>
						</div>
						<span class="text-2xl font-bold {metric.percentage >= 90
							? 'text-green-600'
							: metric.percentage >= 70
								? 'text-yellow-600'
								: 'text-red-600'}">{metric.percentage}%</span>
					</div>

					<div class="w-full bg-gray-200 rounded-full h-2 overflow-hidden">
						<div
							class="bg-linear-to-r {getProgressColor(metric.percentage)} h-full transition-all duration-300"
							style="width: {metric.percentage}%"
						></div>
					</div>
				</button>
			{/each}
		</div>
	</div>

	<div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
		<!-- Activity Log -->
		<div class="lg:col-span-2 bg-white rounded-lg shadow overflow-hidden">
			<div class="p-6 border-b border-gray-200">
				<h2 class="text-xl font-bold text-gray-800 flex items-center gap-2">
					<i class="fas fa-history text-purple-600"></i>
					Recent Activity
				</h2>
			</div>

			<div class="divide-y divide-gray-200 max-h-96 overflow-y-auto">
				{#each activityLogs as log (log.id)}
					<div class="p-4 hover:bg-gray-50 transition-colors">
						<div class="flex items-start gap-4">
							<div class="w-10 h-10 rounded-full bg-blue-100 flex items-center justify-center shrink-0">
								<i class="fas fa-user-circle text-blue-600"></i>
							</div>

							<div class="flex-1 min-w-0">
								<div class="flex items-center justify-between">
									<p class="font-semibold text-gray-800">{log.user}</p>
									<span class="text-xs text-gray-500">{log.timestamp}</span>
								</div>
								<p class="text-sm text-gray-600 mt-1">{log.action}</p>
								<p class="text-xs text-gray-500 mt-1">{log.details}</p>
							</div>
						</div>
					</div>
				{/each}
			</div>
		</div>

		<!-- Quick Stats -->
		<div class="space-y-4">
			<!-- Data Quality -->
			<div class="bg-white rounded-lg shadow p-6 border-t-4 border-t-blue-600">
				<h3 class="font-bold text-gray-800 mb-4 flex items-center gap-2">
					<i class="fas fa-check-double text-blue-600"></i>
					Data Quality
				</h3>

				<div class="space-y-3 text-sm">
					<div class="flex items-center justify-between">
						<span class="text-gray-600">Complete records</span>
						<span class="font-bold text-gray-800">95%</span>
					</div>
					<div class="flex items-center justify-between">
						<span class="text-gray-600">Validation passed</span>
						<span class="font-bold text-gray-800">98%</span>
					</div>
					<div class="flex items-center justify-between">
						<span class="text-gray-600">No errors</span>
						<span class="font-bold text-green-600">12 issues</span>
					</div>
				</div>
			</div>

			<!-- Team Activity -->
			<div class="bg-white rounded-lg shadow p-6 border-t-4 border-t-green-600">
				<h3 class="font-bold text-gray-800 mb-4 flex items-center gap-2">
					<i class="fas fa-users text-green-600"></i>
					Team Activity
				</h3>

				<div class="space-y-3 text-sm">
					<div class="flex items-center justify-between">
						<span class="text-gray-600">Active users</span>
						<span class="font-bold text-gray-800">8</span>
					</div>
					<div class="flex items-center justify-between">
						<span class="text-gray-600">Today's entries</span>
						<span class="font-bold text-gray-800">23</span>
					</div>
					<div class="flex items-center justify-between">
						<span class="text-gray-600">Avg per user</span>
						<span class="font-bold text-gray-800">2.9</span>
					</div>
				</div>
			</div>

			<!-- Quick Links -->
			<div class="bg-white rounded-lg shadow p-6 border-t-4 border-t-purple-600">
				<h3 class="font-bold text-gray-800 mb-4 flex items-center gap-2">
					<i class="fas fa-link text-purple-600"></i>
					Quick Links
				</h3>

				<div class="space-y-2">
					<a href={projectRecordsRoute} class="block px-3 py-2 bg-blue-50 text-blue-600 rounded hover:bg-blue-100 text-sm font-medium transition-colors">
						<i class="fas fa-arrow-right mr-2"></i>View Records
					</a>
					<a href={projectSetupRoute} class="block px-3 py-2 bg-green-50 text-green-600 rounded hover:bg-green-100 text-sm font-medium transition-colors">
						<i class="fas fa-cog mr-2"></i>Project Setup
					</a>
					<a href={projectExportRoute} class="block px-3 py-2 bg-purple-50 text-purple-600 rounded hover:bg-purple-100 text-sm font-medium transition-colors">
						<i class="fas fa-download mr-2"></i>Export Data
					</a>
				</div>
			</div>
		</div>
	</div>

	<!-- Metric Details Modal -->
	{#if showDetailsModal && selectedMetric}
		<div class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
			<div class="bg-white rounded-lg shadow-xl p-6 max-w-md w-full mx-4">
				<h2 class="text-xl font-bold text-gray-800 mb-4">{selectedMetric.name} Details</h2>

				<div class="space-y-4 mb-6">
					<div class="bg-gray-50 rounded p-4">
						<p class="text-sm text-gray-600">Total Expected</p>
						<p class="text-2xl font-bold text-gray-800">{selectedMetric.total}</p>
					</div>

					<div class="grid grid-cols-2 gap-4">
						<div class="bg-green-50 rounded p-4">
							<p class="text-sm text-gray-600">Completed</p>
							<p class="text-2xl font-bold text-green-600">{selectedMetric.completed}</p>
						</div>
						<div class="bg-yellow-50 rounded p-4">
							<p class="text-sm text-gray-600">Remaining</p>
							<p class="text-2xl font-bold text-yellow-600">{selectedMetric.incomplete}</p>
						</div>
					</div>

					<div class="bg-blue-50 rounded p-4">
						<p class="text-sm text-gray-600">Completion Rate</p>
						<p class="text-3xl font-bold text-blue-600">{selectedMetric.percentage}%</p>
					</div>
				</div>

				<button
					on:click={() => (showDetailsModal = false)}
					class="w-full px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 font-medium transition-colors"
				>
					Close
				</button>
			</div>
		</div>
	{/if}
</div>
