<script lang="ts">
	import { page } from '$app/stores';
	import { PROJECT_DETAIL_SETUP_ROUTE } from '$lib/enums/routes';
	import { resolveProjectRoute } from '$lib/utils/routes';
	

	interface TestRecord {
		id: number;
		name: string;
		createdAt: string;
		lastModified: string;
		status: 'Draft' | 'Submitted' | 'Complete';
	}

	interface TestCase {
		id: number;
		name: string;
		description: string;
		completed: boolean;
		icon: string;
	}

	let testRecords: TestRecord[] = [
		{
			id: 1,
			name: 'Test Record - Diabetes',
			createdAt: '2024-01-15',
			lastModified: '2024-01-16',
			status: 'Draft'
		},
		{
			id: 2,
			name: 'Test Record - HTN',
			createdAt: '2024-01-14',
			lastModified: '2024-01-14',
			status: 'Complete'
		}
	];

	let testCases: TestCase[] = [
		{
			id: 1,
			name: 'Form Validation',
			description: 'Test required fields and data type validation',
			completed: true,
			icon: 'fa-check-circle'
		},
		{
			id: 2,
			name: 'Branching Logic',
			description: 'Verify conditional field visibility and required field rules',
			completed: true,
			icon: 'fa-code-branch'
		},
		{
			id: 3,
			name: 'Calculations',
			description: 'Test calculated fields and auto-populated values',
			completed: false,
			icon: 'fa-calculator'
		},
		{
			id: 4,
			name: 'Data Exports',
			description: 'Verify data can be exported in all supported formats',
			completed: false,
			icon: 'fa-download'
		},
		{
			id: 5,
			name: 'Repeating Instruments',
			description: 'Test repeating event instances and data entry',
			completed: true,
			icon: 'fa-repeat'
		},
		{
			id: 6,
			name: 'User Permissions',
			description: 'Verify user access controls and DAG restrictions',
			completed: false,
			icon: 'fa-lock'
		}
	];

	let showCreateRecordModal = false;
	let newRecordName = '';
	let selectedEvent = 'baseline';

	const createTestRecord = () => {
		const record: TestRecord = {
			id: Math.max(...testRecords.map(r => r.id), 0) + 1,
			name: newRecordName,
			createdAt: new Date().toISOString().split('T')[0],
			lastModified: new Date().toISOString().split('T')[0],
			status: 'Draft'
		};
		testRecords = [...testRecords, record];
		showCreateRecordModal = false;
		newRecordName = '';
	};

	const deleteTestRecord = (id: number) => {
		testRecords = testRecords.filter(r => r.id !== id);
	};

	const toggleTestCase = (id: number) => {
		const testCase = testCases.find(tc => tc.id === id);
		if (testCase) {
			testCase.completed = !testCase.completed;
			testCases = [...testCases];
		}
	};

	const completedTests = testCases.filter(tc => tc.completed).length;
	const totalTests = testCases.length;

	const projectId = $derived($page.params.projectId ?? '1');
	const setupOverviewRoute = $derived(resolveProjectRoute(PROJECT_DETAIL_SETUP_ROUTE, projectId));
</script>

<div class="p-6 space-y-6">
	<!-- Header -->
	<div>
		<a href={setupOverviewRoute} class="flex items-center gap-2 text-[#0b3a7a] hover:text-[#082654] text-sm font-medium mb-4">
			<i class="fas fa-arrow-left"></i>Back to Setup
		</a>
		<h1 class="text-3xl font-bold text-gray-800 mb-2">Test Your Project</h1>
		<p class="text-gray-600">Create test records and validate your project configuration before moving to production</p>
	</div>

	<!-- Test Summary Cards -->
	<div class="grid grid-cols-1 md:grid-cols-3 gap-4">
		<div class="bg-linear-to-br from-[#0b3a7a]/5 to-[#0b3a7a]/10 rounded-lg shadow p-6 border border-[#0b3a7a]/10">
			<div class="flex items-center justify-between">
				<div>
					<p class="text-sm text-gray-600 font-medium">Test Records Created</p>
					<p class="text-3xl font-bold text-[#0b3a7a] mt-1">{testRecords.length}</p>
				</div>
				<i class="fas fa-file-alt text-4xl text-[#0b3a7a]/20"></i>
			</div>
		</div>

		<div class="bg-linear-to-br from-green-50 to-green-100 rounded-lg shadow p-6 border border-green-200">
			<div class="flex items-center justify-between">
				<div>
					<p class="text-sm text-gray-600 font-medium">Test Cases Passed</p>
					<p class="text-3xl font-bold text-green-600 mt-1">{completedTests}/{totalTests}</p>
				</div>
				<i class="fas fa-check-circle text-4xl text-green-200"></i>
			</div>
		</div>

		<div class="bg-linear-to-br from-purple-50 to-purple-100 rounded-lg shadow p-6 border border-purple-200">
			<div class="flex items-center justify-between">
				<div>
					<p class="text-sm text-gray-600 font-medium">Overall Progress</p>
					<p class="text-3xl font-bold text-purple-600 mt-1">{Math.round((completedTests / totalTests) * 100)}%</p>
				</div>
				<i class="fas fa-tasks text-4xl text-purple-200"></i>
			</div>
		</div>
	</div>

	<!-- Progress Bar -->
	<div class="bg-white rounded-lg shadow p-6">
		<div class="flex items-center justify-between mb-2">
			<p class="font-medium text-gray-800">Overall Test Coverage</p>
			<p class="text-sm text-gray-600">{completedTests} of {totalTests} cases passed</p>
		</div>
		<div class="w-full bg-gray-200 rounded-full h-3 overflow-hidden">
			<div
				class="bg-linear-to-r from-green-500 to-green-600 h-full transition-all duration-300"
				style="width: {(completedTests / totalTests) * 100}%"
			></div>
		</div>
	</div>

	<!-- Test Cases Checklist -->
	<div class="bg-white rounded-lg shadow overflow-hidden">
		<div class="p-6 border-b border-gray-200">
			<h2 class="text-xl font-bold text-gray-800 flex items-center gap-2">
				<i class="fas fa-list-check text-[#0b3a7a]"></i>
				Project Test Cases
			</h2>
		</div>

		<div class="p-6 space-y-3">
			{#each testCases as testCase (testCase.id)}
				<div class="flex items-start gap-4 p-4 border border-gray-200 rounded-lg hover:bg-gray-50 transition-colors">
					<button
						on:click={() => toggleTestCase(testCase.id)}
						class="mt-1 w-6 h-6 rounded border-2 {testCase.completed
							? 'bg-green-500 border-green-500'
							: 'border-gray-300 hover:border-green-500'} flex items-center justify-center transition-all"
					>
						{#if testCase.completed}
							<i class="fas fa-check text-white text-xs"></i>
						{/if}
					</button>

					<div class="flex-1 min-w-0">
						<div class="flex items-center gap-2 mb-1">
							<i class="fas {testCase.icon} text-[#0b3a7a]"></i>
							<h3 class="font-semibold text-gray-800">{testCase.name}</h3>
							{#if testCase.completed}
								<span class="px-2 py-1 bg-green-100 text-green-800 text-xs rounded-full font-medium">Passed</span>
							{/if}
						</div>
						<p class="text-sm text-gray-600">{testCase.description}</p>
					</div>
				</div>
			{/each}
		</div>
	</div>

	<!-- Test Records -->
	<div class="bg-white rounded-lg shadow overflow-hidden">
		<div class="p-6 border-b border-gray-200 flex items-center justify-between">
			<h2 class="text-xl font-bold text-gray-800 flex items-center gap-2">
				<i class="fas fa-database text-purple-600"></i>
				Test Records
			</h2>
			<button
				on:click={() => (showCreateRecordModal = true)}
				class="px-4 py-2 bg-[#0b3a7a] text-white rounded-lg hover:bg-[#082654] font-medium transition-colors flex items-center gap-2"
			>
				<i class="fas fa-plus"></i>
				Create Test Record
			</button>
		</div>

		{#if testRecords.length === 0}
			<div class="p-12 text-center">
				<i class="fas fa-inbox text-4xl text-gray-300 mb-4 block"></i>
				<p class="text-gray-500">No test records yet. Create one to start testing your project.</p>
			</div>
		{:else}
			<div class="overflow-x-auto">
				<table class="w-full text-sm">
					<thead class="bg-gray-50 border-b border-gray-200">
						<tr>
							<th class="px-6 py-3 text-left font-semibold text-gray-700">Record Name</th>
							<th class="px-6 py-3 text-left font-semibold text-gray-700">Created</th>
							<th class="px-6 py-3 text-left font-semibold text-gray-700">Last Modified</th>
							<th class="px-6 py-3 text-left font-semibold text-gray-700">Status</th>
							<th class="px-6 py-3 text-left font-semibold text-gray-700">Actions</th>
						</tr>
					</thead>
					<tbody class="divide-y divide-gray-200">
						{#each testRecords as record (record.id)}
							<tr class="hover:bg-gray-50 transition-colors">
								<td class="px-6 py-3 font-medium text-gray-800">{record.name}</td>
								<td class="px-6 py-3 text-gray-600">{record.createdAt}</td>
								<td class="px-6 py-3 text-gray-600">{record.lastModified}</td>
								<td class="px-6 py-3">
									<span
										class="px-3 py-1 rounded-full text-xs font-medium {record.status === 'Draft'
											? 'bg-yellow-100 text-yellow-800'
											: record.status === 'Submitted'
												? 'bg-[#0b3a7a]/10 text-[#0b3a7a]'
												: 'bg-green-100 text-green-800'}"
									>
										{record.status}
									</span>
								</td>
								<td class="px-6 py-3">
									<button class="px-3 py-1 bg-[#0b3a7a]/5 text-[#0b3a7a] rounded hover:bg-[#0b3a7a]/10 text-xs font-medium transition-colors mr-2">
										<i class="fas fa-edit"></i> Edit
									</button>
									<button
										on:click={() => deleteTestRecord(record.id)}
										class="px-3 py-1 bg-red-50 text-red-600 rounded hover:bg-red-100 text-xs font-medium transition-colors"
									>
										<i class="fas fa-trash"></i> Delete
									</button>
								</td>
							</tr>
						{/each}
					</tbody>
				</table>
			</div>
		{/if}
	</div>

	<!-- Recommendations -->
	<div class="bg-orange-50 rounded-lg shadow p-6 border border-orange-200">
		<h3 class="text-lg font-bold text-gray-800 mb-3 flex items-center gap-2">
			<i class="fas fa-lightbulb text-orange-600"></i>
			Testing Recommendations
		</h3>
		<ul class="space-y-2 text-sm text-gray-700">
			<li class="flex items-start gap-2">
				<span class="text-orange-600 font-bold mt-1">1.</span>
				<span>Create at least 2-3 test records to validate all forms and events</span>
			</li>
			<li class="flex items-start gap-2">
				<span class="text-orange-600 font-bold mt-1">2.</span>
				<span>Test all conditional branching logic with different field values</span>
			</li>
			<li class="flex items-start gap-2">
				<span class="text-orange-600 font-bold mt-1">3.</span>
				<span>Verify calculated fields and automated values are correct</span>
			</li>
			<li class="flex items-start gap-2">
				<span class="text-orange-600 font-bold mt-1">4.</span>
				<span>Check all user roles and permissions work as expected</span>
			</li>
			<li class="flex items-start gap-2">
				<span class="text-orange-600 font-bold mt-1">5.</span>
				<span>Test exports and reporting features before production</span>
			</li>
		</ul>
	</div>

	<!-- Create Test Record Modal -->
	{#if showCreateRecordModal}
		<div class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
			<div class="bg-white rounded-lg shadow-xl p-6 max-w-md w-full mx-4">
				<h2 class="text-xl font-bold text-gray-800 mb-4">Create Test Record</h2>

				<div class="space-y-4">
					<div>
						<label class="block text-sm font-medium text-gray-700 mb-1">Record Name</label>
						<input
							type="text"
							bind:value={newRecordName}
							class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-[#0b3a7a] outline-none"
							placeholder="e.g., Test Record - Patient 001"
						/>
					</div>

					<div>
						<label class="block text-sm font-medium text-gray-700 mb-1">Starting Event</label>
						<select
							bind:value={selectedEvent}
							class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-[#0b3a7a] outline-none"
						>
							<option value="baseline">Baseline Visit</option>
							<option value="week4">Week 4 Follow-up</option>
							<option value="week12">Week 12 Follow-up</option>
							<option value="final">Final Visit</option>
						</select>
					</div>
				</div>

				<div class="flex gap-2 justify-end mt-6 border-t pt-4">
					<button
						on:click={() => (showCreateRecordModal = false)}
						class="px-4 py-2 border border-gray-300 text-gray-700 rounded-lg hover:bg-gray-50 font-medium transition-colors"
					>
						Cancel
					</button>
					<button
						on:click={createTestRecord}
						disabled={!newRecordName.trim()}
						class="px-4 py-2 bg-[#0b3a7a] text-white rounded-lg hover:bg-[#082654] font-medium transition-colors disabled:opacity-50"
					>
						Create Record
					</button>
				</div>
			</div>
		</div>
	{/if}
</div>
