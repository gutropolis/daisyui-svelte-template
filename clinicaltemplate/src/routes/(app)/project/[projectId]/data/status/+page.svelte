<script lang="ts">
	interface Subject {
		id: string;
		subjectNumber: string;
		eventStatus: Record<string, string>;
		events: string[];
		completedCount: number;
		incompleteCount: number;
	}

	const statusConfig = {
		complete: { label: 'Complete', color: 'bg-green-500' },
		incomplete: { label: 'Incomplete (no data saved)', color: 'bg-gray-300' },
		unverified: { label: 'Unverified', color: 'bg-yellow-400' },
		issue: { label: 'Has Issue', color: 'bg-red-500' },
		'on-review': { label: 'On review', color: 'bg-purple-400' }
	};

	let subjects: Subject[] = [
		{
			id: '1',
			subjectNumber: '1',
			eventStatus: { Baseline: 'complete', Intervention: 'complete', 'Checkpoint 30 Day': 'incomplete', 'Checkpoint 6 Month': 'complete', 'Checkpoint 1 Year': 'complete', 'Student Check Up 1': 'incomplete', 'Student Checkpoint 2 Year': 'complete', 'Checkpoint Up 2': 'incomplete', 'Checkpoint 3 Year': 'complete', 'Checkpoint 4 Year': 'complete', 'Adverse Events': 'issue' },
			events: ['Baseline', 'Intervention', 'Checkpoint 30 Day', 'Checkpoint 6 Month', 'Checkpoint 1 Year', 'Student Check Up 1', 'Student Checkpoint 2 Year', 'Checkpoint Up 2', 'Checkpoint 3 Year', 'Checkpoint 4 Year', 'Adverse Events'],
			completedCount: 8,
			incompleteCount: 2
		},
		{
			id: '2',
			subjectNumber: '2',
			eventStatus: { Baseline: 'complete', Intervention: 'complete', 'Checkpoint 30 Day': 'complete', 'Checkpoint 6 Month': 'complete', 'Checkpoint 1 Year': 'complete', 'Student Check Up 1': 'incomplete', 'Student Checkpoint 2 Year': 'complete', 'Checkpoint Up 2': 'incomplete', 'Checkpoint 3 Year': 'complete', 'Checkpoint 4 Year': 'incomplete', 'Adverse Events': 'incomplete' },
			events: ['Baseline', 'Intervention', 'Checkpoint 30 Day', 'Checkpoint 6 Month', 'Checkpoint 1 Year', 'Student Check Up 1', 'Student Checkpoint 2 Year', 'Checkpoint Up 2', 'Checkpoint 3 Year', 'Checkpoint 4 Year', 'Adverse Events'],
			completedCount: 8,
			incompleteCount: 3
		}
	];

	let displayedRecords = 2;
	let recordsPerPage = 'ALL (2)';
	let displayMode = 'all';

	const getStatusColor = (status: string) => {
		return statusConfig[status as keyof typeof statusConfig]?.color || 'bg-gray-400';
	};

	const getStatusLabel = (status: string) => {
		return statusConfig[status as keyof typeof statusConfig]?.label || status;
	};
</script>

<div class="min-h-screen bg-white p-6">
	<!-- Header Section -->
	<div class="mb-6">
		<h1 class="text-xl font-bold text-gray-900 mb-3">Record Status Dashboard (all records)</h1>
		
		<p class="text-sm text-gray-700 leading-relaxed mb-4 max-w-4xl">
			Displayed below is a table listing all existing records/responses and their status for every data collection instrument (and if longitudinal, for every event). You may click any of the colored buttons in the table to open a new tab/window in your browser to view that record on that particular data collection instrument. Please note that if your form-level user privileges are restricted for certain data collection instruments, you will only be able to view those instruments, and if you belong to a Data Access Group, you will only be able to view records that belong to your group.
		</p>

		<!-- Legend and Controls Row -->
		<div class="grid grid-cols-3 gap-6">
			<!-- Legend -->
			<div class="col-span-2">
				<div class="bg-gray-100 p-4 rounded border border-gray-300">
					<h3 class="font-semibold text-gray-900 mb-3 text-sm">Legend for status icons:</h3>
					<div class="grid grid-cols-3 gap-3">
						<div class="flex items-center gap-2">
							<span class="bg-red-500 w-4 h-4 rounded-full inline-block"></span>
							<span class="text-sm text-gray-700">Incomplete</span>
						</div>
						<div class="flex items-center gap-2">
							<span class="bg-gray-300 w-4 h-4 rounded-full inline-block"></span>
							<span class="text-sm text-gray-700">Incomplete (no data saved)</span>
							<span class="text-gray-500 text-xs cursor-help">?</span>
						</div>
						<div class="flex items-center gap-2">
							<span class="bg-yellow-400 w-4 h-4 rounded-full inline-block"></span>
							<span class="text-sm text-gray-700">Unverified</span>
						</div>
						<div class="flex items-center gap-2">
							<span class="bg-green-500 w-4 h-4 rounded-full inline-block"></span>
							<span class="text-sm text-gray-700">Complete</span>
						</div>
					</div>
				</div>
			</div>

			<!-- Dashboard Controls -->
			<div class="bg-gray-100 p-4 rounded border border-gray-300">
				<div class="space-y-3">
					<div>
						<label for="dashboard" class="text-sm font-medium text-gray-700 block mb-1">Dashboard displayed:</label>
						<select id="dashboard" class="w-full px-2 py-1 border border-gray-300 rounded text-sm">
							<option>[Default dashboard]</option>
						</select>
					</div>
					<button class="w-full px-3 py-2 bg-blue-600 text-white rounded text-sm font-medium hover:bg-blue-700 flex items-center justify-center gap-2">
						<i class="fas fa-plus"></i>Create custom dashboard
					</button>
				</div>
			</div>
		</div>
	</div>

	<!-- Controls Row -->
	<div class="bg-gray-50 p-4 rounded border border-gray-300 mb-4 flex flex-wrap items-center justify-between gap-4">
		<div class="flex items-center gap-2 text-sm text-gray-700">
			<span>Displaying record</span>
			<select class="px-2 py-1 border border-gray-300 rounded text-sm bg-white">
				<option>Page 1 of 1: "1" through "2"</option>
			</select>
			<span>of 2 records</span>
		</div>
		<div class="flex items-center gap-2">
			<select class="px-2 py-1 border border-gray-300 rounded text-sm bg-white">
				<option>ALL (2)</option>
				<option>5</option>
				<option>10</option>
				<option>20</option>
			</select>
			<span class="text-sm text-gray-700">records per page</span>
		</div>
	</div>

	<!-- Add New Record Button -->
	<button class="px-3 py-2 bg-green-600 text-white rounded font-semibold hover:bg-green-700 text-sm flex items-center gap-2 mb-4">
		<i class="fas fa-plus"></i>Add new record
	</button>

	<!-- Display Mode Options -->
	<div class="bg-white mb-4 text-sm">
		<span class="font-medium text-gray-700">Displaying:</span>
		<button class="text-gray-600 hover:underline ml-3">Instrument status only</button>
		<span class="text-gray-400">|</span>
		<button class="text-gray-600 hover:underline">Lock status only</button>
		<span class="text-gray-400">|</span>
		<button class="text-blue-600 font-medium hover:underline">All status types</button>
	</div>

	<!-- Table -->
	<div class="overflow-x-auto bg-white border border-gray-300">
		<table class="w-full text-sm border-collapse">
			<thead>
				<tr class="bg-yellow-100 border-b border-gray-400">
					<th class="text-left px-4 py-3 font-bold text-gray-900 border-r border-gray-400">Record ID</th>
					{#each subjects[0].events as event}
						<th class="text-center px-3 py-3 font-bold text-gray-900 border-r border-gray-400 whitespace-nowrap text-xs bg-yellow-100">
							{event}
						</th>
					{/each}
				</tr>
			</thead>
			<tbody>
				{#each subjects as subject (subject.id)}
					<tr class="border-b border-gray-300 hover:bg-gray-50">
						<td class="px-4 py-3 font-semibold text-gray-900 border-r border-gray-300">{subject.subjectNumber}</td>
						{#each subject.events as event}
							{@const status = subject.eventStatus[event]}
							<td class="text-center px-3 py-3 border-r border-gray-300">
								<button
									class="{getStatusColor(status)} w-5 h-5 rounded-full hover:opacity-80 transition-opacity cursor-pointer inline-block"
									title={getStatusLabel(status)}
								></button>
							</td>
						{/each}
					</tr>
				{/each}
			</tbody>
		</table>
	</div>
</div>

<style>
	:global(body) {
		background-color: #ffffff;
	}
</style>
