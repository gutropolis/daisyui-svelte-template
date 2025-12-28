<script lang="ts">
	interface ReportField {
		id: number;
		fieldName: string;
		fieldLabel: string;
		instrument: string;
	}

	interface Report {
		id: number;
		name: string;
		description: string;
		createdDate: string;
		createdBy: string;
		status: 'active' | 'draft';
		fieldsCount: number;
	}

	let activeTab = $state('my-reports');
	let currentStep = $state(1);
	let showReportForm = $state(false);

	// Report Form State
	let reportName = $state('');
	let reportDescription = $state('');
	let isPublic = $state(false);

	// Step 1 - Access Control
	let viewAccessType = $state('all-users');
	let editAccessType = $state('all-users');

	// Step 2 - Fields
	let selectedFields = $state<ReportField[]>([]);
	let availableFields = $state<ReportField[]>([
		{ id: 1, fieldName: 'record_id', fieldLabel: 'Record ID', instrument: 'Enrollment and Status' },
		{ id: 2, fieldName: 'difficulty_falling_asleep', fieldLabel: 'Difficulty falling asleep', instrument: 'ISI' },
		{ id: 3, fieldName: 'difficulty_staying_asleep', fieldLabel: 'Difficulty staying asleep', instrument: 'ISI' },
		{ id: 4, fieldName: 'waking_early', fieldLabel: 'Problem waking up too early', instrument: 'ISI' },
		{ id: 5, fieldName: 'isi_matrix_1_score', fieldLabel: 'Matrix 1 total score', instrument: 'ISI' },
		{ id: 6, fieldName: 'isi_satisfied_sleep', fieldLabel: 'How SATISFIED/DISSATISFIED are you with your sleep pattern?', instrument: 'ISI' },
		{ id: 7, fieldName: 'isi_noticeable_prob', fieldLabel: 'How NOTICEABLE to others is any impairment in your daytime functioning?', instrument: 'ISI' },
		{ id: 8, fieldName: 'isi_worried_prob', fieldLabel: 'How WORRIED/DISTRESSED are you about your current sleep problem?', instrument: 'ISI' },
		{ id: 9, fieldName: 'isi_sleep_interfere', fieldLabel: 'To what extent do you consider your sleep problem to INTERFERE with your daily functioning?', instrument: 'ISI' },
		{ id: 10, fieldName: 'isi_total_score', fieldLabel: 'Total Score', instrument: 'ISI' },
		{ id: 11, fieldName: 'isi_complete', fieldLabel: 'Complete?', instrument: 'ISI' },
		{ id: 12, fieldName: 'enrollment_date', fieldLabel: 'Enrollment Date', instrument: 'Enrollment and Status' }
	]);

	let showAllFieldsDropdown = $state(false);
	let selectedInstrument = $state('');

	// Step 3 - Filters
	let showDataAllEvents = $state(true);
	let filters = $state<Array<{ id: number; field: string; event: string; operator: string; value: string }>>([
		{ id: 1, field: '', event: 'All events', operator: '=', value: '' }
	]);

	let additionalFilters = $state<Array<{ id: number; event: string }>>([]);
	let liveFilters = $state<Array<{ id: number; field: string }>>([
		{ id: 1, field: '' },
		{ id: 2, field: '' },
		{ id: 3, field: '' }
	]);

	// Step 4 - Ordering
	let orderBy = $state([
		{ id: 1, field: 'record_id', order: 'ascending' },
		{ id: 2, field: '', order: 'ascending' },
		{ id: 3, field: '', order: 'ascending' }
	]);

	let myReports = $state<Report[]>([
		{
			id: 1,
			name: 'Insomnia Severity Index_JD',
			description: 'Report showing ISI scores for all enrolled participants',
			createdDate: '2024-01-15',
			createdBy: 'John Doe',
			status: 'active',
			fieldsCount: 8
		},
		{
			id: 2,
			name: 'Demographics Report_SM',
			description: 'Baseline demographics and enrollment information',
			createdDate: '2024-01-10',
			createdBy: 'Sarah Miller',
			status: 'active',
			fieldsCount: 6
		},
		{
			id: 3,
			name: 'Study Progress_Admin',
			description: 'Track enrollment and completion rates',
			createdDate: '2024-01-05',
			createdBy: 'Admin',
			status: 'draft',
			fieldsCount: 4
		}
	]);

	const addField = (field: ReportField) => {
		if (!selectedFields.find(f => f.id === field.id)) {
			selectedFields = [...selectedFields, field];
		}
	};

	const removeField = (id: number) => {
		selectedFields = selectedFields.filter(f => f.id !== id);
	};

	const addAllFieldsFromInstrument = () => {
		if (selectedInstrument) {
			const instrumentFields = availableFields.filter(f => f.instrument === selectedInstrument);
			const newFields = instrumentFields.filter(
				f => !selectedFields.find(sf => sf.id === f.id)
			);
			selectedFields = [...selectedFields, ...newFields];
		}
	};

	const saveReport = () => {
		if (!reportName.trim()) {
			alert('Please enter a report name');
			return;
		}

		const newReport: Report = {
			id: myReports.length + 1,
			name: reportName,
			description: reportDescription,
			createdDate: new Date().toISOString().split('T')[0],
			createdBy: 'Current User',
			status: 'active',
			fieldsCount: selectedFields.length
		};

		myReports = [...myReports, newReport];
		showReportForm = false;
		resetForm();

		alert(`Your report has been saved!\n\nThe report named "${reportName}" has been successfully saved.`);
	};

	const resetForm = () => {
		reportName = '';
		reportDescription = '';
		isPublic = false;
		selectedFields = [];
		currentStep = 1;
		showAllFieldsDropdown = false;
	};

	const instruments = $derived(Array.from(new Set(availableFields.map(f => f.instrument))));
</script>

<div class="p-6 space-y-6 min-h-screen bg-gray-50">
	<!-- Header -->
	<div class="flex items-start justify-between">
		<div>
			<h1 class="text-3xl font-bold text-gray-800 mb-2">Data Exports, Reports & Stats</h1>
			<p class="text-gray-600 text-sm max-w-4xl leading-relaxed">
				A REDCap report is a useful tool for selecting the specific fields/variables for your analysis. You can add as many fields/variables to your report as you would like and you can choose who has access to view the report. Reports help with organization, data analysis, and team accountability by allowing you to focus on relevant data and monitor research progression.
			</p>
		</div>
	</div>

	<!-- Tabs -->
	<div class="flex gap-1 border-b border-gray-200">
		<button
			onclick={() => (activeTab = 'my-reports')}
			class="px-4 py-3 font-medium text-sm border-b-2 transition-all {activeTab === 'my-reports'
				? 'border-[#0b3a7a] text-[#0b3a7a]'
				: 'border-transparent text-gray-600 hover:text-[#0b3a7a]'}"
		>
			<i class="fas fa-file-alt mr-2"></i>My Reports & Exports
		</button>
		<button
			onclick={() => (activeTab = 'other-exports')}
			class="px-4 py-3 font-medium text-sm border-b-2 transition-all {activeTab === 'other-exports'
				? 'border-[#0b3a7a] text-[#0b3a7a]'
				: 'border-transparent text-gray-600 hover:text-[#0b3a7a]'}"
		>
			<i class="fas fa-download mr-2"></i>Other Export Options
		</button>
	</div>

	<!-- My Reports & Exports Tab -->
	{#if activeTab === 'my-reports'}
		<div class="space-y-6">
			{#if !showReportForm}
				<!-- Create Report Button -->
				<button
					onclick={() => (showReportForm = true)}
					class="px-6 py-3 bg-[#0b3a7a] hover:bg-[#082654] text-white rounded-lg flex items-center gap-2 transition-colors font-medium border-2 border-[#0b3a7a]"
				>
					<i class="fas fa-plus"></i>Create New Report
				</button>

				<!-- Reports List -->
				<div class="bg-white rounded-lg shadow-sm border border-gray-200 overflow-hidden">
					<div class="bg-gray-50 px-6 py-4 border-b border-gray-200">
						<h2 class="text-lg font-semibold text-gray-800">
							My Reports ({myReports.length})
						</h2>
					</div>

					{#if myReports.length > 0}
						<div class="divide-y divide-gray-200">
							{#each myReports as report (report.id)}
								<div class="p-6 hover:bg-gray-50 transition-colors">
									<div class="flex items-start justify-between">
										<div class="flex-1">
											<h3 class="font-semibold text-gray-900 text-lg mb-1">{report.name}</h3>
											<p class="text-sm text-gray-600 mb-2">{report.description}</p>
											<div class="flex gap-4 text-xs text-gray-500">
												<span><i class="fas fa-user mr-1"></i>By {report.createdBy}</span>
												<span><i class="fas fa-calendar mr-1"></i>{report.createdDate}</span>
												<span><i class="fas fa-database mr-1"></i>{report.fieldsCount} fields</span>
												<span class="inline-block px-2 py-1 rounded {report.status === 'active'
													? 'bg-green-100 text-green-800'
													: 'bg-yellow-100 text-yellow-800'}">
													{report.status === 'active' ? 'Active' : 'Draft'}
												</span>
											</div>
										</div>
										<div class="flex gap-2 ml-4">
											<button class="px-3 py-2 rounded text-sm font-medium bg-blue-50 text-blue-700 hover:bg-blue-100 transition-colors">
												<i class="fas fa-edit mr-1"></i>Edit
											</button>
											<button class="px-3 py-2 rounded text-sm font-medium bg-gray-100 text-gray-700 hover:bg-gray-200 transition-colors">
												<i class="fas fa-eye mr-1"></i>View
											</button>
											<button class="px-3 py-2 rounded text-sm font-medium bg-red-50 text-red-700 hover:bg-red-100 transition-colors">
												<i class="fas fa-trash"></i>
											</button>
										</div>
									</div>
								</div>
							{/each}
						</div>
					{:else}
						<div class="p-12 text-center text-gray-500">
							<i class="fas fa-inbox text-4xl mb-4 block text-gray-300"></i>
							<p>No reports created yet. Create your first report to get started.</p>
						</div>
					{/if}
				</div>
			{:else}
				<!-- Create Report Form -->
				<div class="space-y-6">
					<!-- Header Section -->
					<div class="bg-white rounded-lg shadow-sm border border-gray-200 p-6">
						<div class="mb-6">
							<h2 class="text-xl font-bold text-gray-900 mb-2">Create New Report</h2>
							<p class="text-sm text-gray-600">
								You may create a new report by selecting the fields/variables below that you want to include in the report. You may add as many fields to your report as you wish. You will also need to provide a name for your report, which will then be displayed on the project's left-hand menu for anyone to whom you have given access. You can filter the results returned in the report in a variety of ways, including using complex AND/OR logic. When you are finished, click the Save Report button at the bottom.
							</p>
						</div>

						<!-- Report Name and Settings -->
						<div class="space-y-4 bg-yellow-50 border border-yellow-200 p-4 rounded">
							<div>
								<label class="block text-sm font-medium text-gray-900 mb-2">Name of Report:</label>
								<input
									type="text"
									bind:value={reportName}
									placeholder="e.g., Insomnia Severity Index"
									class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-[#0b3a7a]"
								/>
							</div>

							<div>
								<label class="block text-sm font-medium text-gray-900 mb-2">Set as "public":</label>
								<div class="flex items-center gap-3">
									<label class="flex items-center gap-2 cursor-pointer">
										<input type="checkbox" bind:checked={isPublic} class="w-4 h-4 rounded" />
										<span class="text-sm text-gray-700">Report is publicly viewable by anyone with the public link</span>
									</label>
								</div>
								<p class="text-xs text-gray-500 mt-2">
									Enabling this feature below will auto-generate a public link for viewing the report without needing to log in to REDCap.
								</p>
							</div>

							<div>
								<label class="block text-sm font-medium text-gray-900 mb-2">Description (optional):</label>
								<textarea
									bind:value={reportDescription}
									placeholder="Displayed on page below report name"
									rows="4"
									class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-[#0b3a7a]"
								></textarea>
							</div>
						</div>
					</div>

					<!-- Step 1: User Access -->
					<div class="bg-white rounded-lg shadow-sm border border-gray-200 p-6">
						<h3 class="text-lg font-bold text-gray-900 mb-4">
							<span class="inline-block bg-gray-300 text-gray-800 px-3 py-1 rounded-full text-sm font-semibold mr-2">STEP 1</span>
							User & Edit Access
						</h3>

						<div class="space-y-6">
							<!-- View Access -->
							<div class="bg-gray-50 p-4 rounded border border-gray-200">
								<p class="text-sm font-semibold text-gray-900 mb-3 flex items-center gap-2">
									<i class="fas fa-eye text-green-600"></i>View Access: Choose who sees this report on their left-hand project menu
								</p>
								<div class="space-y-2">
									<label class="flex items-center gap-2">
										<input type="radio" bind:group={viewAccessType} value="all-users" class="w-4 h-4" />
										<span class="text-sm text-gray-700">All users</span>
									</label>
									<label class="flex items-center gap-2">
										<input type="radio" bind:group={viewAccessType} value="custom" class="w-4 h-4" />
										<span class="text-sm text-gray-700">Custom user access (Choose specific users, roles, or data access groups who will have access)</span>
									</label>
								</div>
							</div>

							<!-- Edit Access -->
							<div class="bg-gray-50 p-4 rounded border border-gray-200">
								<p class="text-sm font-semibold text-gray-900 mb-3 flex items-center gap-2">
									<i class="fas fa-edit text-blue-600"></i>Edit Access: Choose who can edit, copy, or delete this report
								</p>
								<div class="space-y-2">
									<label class="flex items-center gap-2">
										<input type="radio" bind:group={editAccessType} value="all-users" class="w-4 h-4" />
										<span class="text-sm text-gray-700">All users</span>
									</label>
									<label class="flex items-center gap-2">
										<input type="radio" bind:group={editAccessType} value="custom" class="w-4 h-4" />
										<span class="text-sm text-gray-700">Custom user access (Choose specific users, roles, or data access groups who will have access)</span>
									</label>
								</div>
							</div>
						</div>
					</div>

					<!-- Step 2: Fields -->
					<div class="bg-white rounded-lg shadow-sm border border-gray-200 p-6">
						<h3 class="text-lg font-bold text-gray-900 mb-4">
							<span class="inline-block bg-gray-300 text-gray-800 px-3 py-1 rounded-full text-sm font-semibold mr-2">STEP 2</span>
							Fields to include in report
						</h3>

						<div class="mb-4 flex gap-2">
							<button class="px-3 py-2 bg-green-100 text-green-800 rounded text-sm font-medium hover:bg-green-200">
								<i class="fas fa-plus mr-1"></i>Quick Add
							</button>
							<div class="flex-1 flex gap-2 items-center justify-end">
								<span class="text-sm text-gray-600">Add all fields from selected instrument:</span>
								<select
									bind:value={selectedInstrument}
									class="px-3 py-2 border border-gray-300 rounded text-sm"
								>
									<option value="">-- choose instrument --</option>
									{#each instruments as instrument}
										<option value={instrument}>{instrument}</option>
									{/each}
								</select>
								<button
									onclick={addAllFieldsFromInstrument}
									class="px-3 py-2 bg-gray-200 text-gray-800 rounded text-sm hover:bg-gray-300"
								>
									Add all
								</button>
							</div>
						</div>

						<!-- Selected Fields -->
						<div class="bg-gray-50 rounded border border-gray-200 overflow-hidden">
							{#each selectedFields as field, index (field.id)}
								<div class="p-4 border-b border-gray-200 flex items-center justify-between {index % 2 === 0 ? 'bg-white' : 'bg-gray-50'}">
									<div class="flex-1">
										<p class="text-sm font-medium text-gray-900">
											{field.fieldName}
											<span class="text-gray-500 font-normal">"{field.fieldLabel}"</span>
										</p>
										<p class="text-xs text-gray-500 mt-1">Instrument: {field.instrument}</p>
									</div>
									<button
										onclick={() => removeField(field.id)}
										class="px-3 py-1 rounded text-red-600 hover:bg-red-50 text-lg"
									>
										<i class="fas fa-times"></i>
									</button>
								</div>
							{/each}
						</div>

						{#if selectedFields.length === 0}
							<div class="p-6 text-center text-gray-500">
								<p>No fields selected yet. Add fields from the available options above.</p>
							</div>
						{/if}

						<!-- Additional Options -->
						<div class="mt-6 bg-gray-50 border border-gray-200 p-4 rounded">
							<p class="text-sm font-semibold text-gray-900 mb-3">
								<i class="fas fa-cog mr-2"></i>Additional report options (optional)
							</p>
							<div class="space-y-2">
								<label class="flex items-center gap-2">
									<input type="checkbox" class="w-4 h-4 rounded" />
									<span class="text-sm text-gray-700">Include the survey identifier field and survey timestamp field(s)?</span>
								</label>
								<label class="flex items-center gap-2">
									<input type="checkbox" class="w-4 h-4 rounded" />
									<span class="text-sm text-gray-700">Combine checkbox options into single column of only the checked-off options</span>
								</label>
								<label class="flex items-center gap-2">
									<input type="checkbox" checked class="w-4 h-4 rounded" />
									<span class="text-sm text-gray-700">Include the repeating instance fields in the report and data export?</span>
								</label>
								<label class="flex items-center gap-2">
									<input type="checkbox" checked class="w-4 h-4 rounded" />
									<span class="text-sm text-gray-700">Remove line breaks/carriage returns from all text data values</span>
								</label>
							</div>
						</div>
					</div>

					<!-- Step 3: Filters -->
					<div class="bg-white rounded-lg shadow-sm border border-gray-200 p-6">
						<h3 class="text-lg font-bold text-gray-900 mb-4">
							<span class="inline-block bg-gray-300 text-gray-800 px-3 py-1 rounded-full text-sm font-semibold mr-2">STEP 3</span>
							Filters (optional)
						</h3>

						<div class="mb-4">
							<label class="flex items-center gap-2">
								<input type="checkbox" bind:checked={showDataAllEvents} class="w-4 h-4 rounded" />
								<span class="text-sm font-semibold text-gray-900">
									Show data for all events or repeating instruments for each record returned
								</span>
							</label>
						</div>

						<div class="bg-gray-50 p-4 rounded border border-gray-200 mb-4">
							<p class="text-sm font-semibold text-gray-900 mb-3 flex items-center gap-2">
								<i class="fas fa-filter text-red-600"></i>Filters
							</p>
							{#each filters as filter}
								<div class="flex gap-2 mb-3">
									<input
										type="text"
										placeholder="Type variable name or field label"
										class="flex-1 px-3 py-2 border border-gray-300 rounded text-sm"
									/>
									<select class="px-3 py-2 border border-gray-300 rounded text-sm min-w-32">
										<option>All events</option>
									</select>
									<select class="px-3 py-2 border border-gray-300 rounded text-sm">
										<option>=</option>
										<option>&lt;</option>
										<option>&gt;</option>
									</select>
									<input
										type="text"
										placeholder="Value"
										class="w-32 px-3 py-2 border border-gray-300 rounded text-sm"
									/>
								</div>
							{/each}
						</div>

						<div class="bg-blue-50 p-4 rounded border border-blue-200 text-sm text-blue-800">
							<p><strong>Tip:</strong> Use advanced logic format for more sophisticated filtering options.</p>
						</div>
					</div>

					<!-- Step 4: Ordering -->
					<div class="bg-white rounded-lg shadow-sm border border-gray-200 p-6">
						<h3 class="text-lg font-bold text-gray-900 mb-4">
							<span class="inline-block bg-gray-300 text-gray-800 px-3 py-1 rounded-full text-sm font-semibold mr-2">STEP 4</span>
							Order the Results (optional)
						</h3>

						<div class="space-y-3">
							{#each orderBy as order, index}
								<div class="flex gap-2 items-center">
									<span class="text-sm font-medium text-gray-700 w-20">{index === 0 ? 'First by' : index === 1 ? 'Then by' : 'Then by'}</span>
									<select class="flex-1 px-3 py-2 border border-gray-300 rounded text-sm">
										<option value="">-- choose field --</option>
										{#each selectedFields as field}
											<option value={field.fieldName}>{field.fieldName}</option>
										{/each}
									</select>
									<select class="px-3 py-2 border border-gray-300 rounded text-sm">
										<option>Ascending order</option>
										<option>Descending order</option>
									</select>
								</div>
							{/each}
						</div>
					</div>

					<!-- Action Buttons -->
					<div class="flex gap-4 justify-end">
						<button
							onclick={() => {
								showReportForm = false;
								resetForm();
							}}
							class="px-6 py-2 border border-gray-300 text-gray-700 rounded-lg hover:bg-gray-50 font-medium"
						>
							Cancel
						</button>
						<button
							onclick={saveReport}
							class="px-6 py-2 bg-[#0b3a7a] hover:bg-[#082654] text-white rounded-lg font-medium"
						>
							<i class="fas fa-save mr-2"></i>Save Report
						</button>
					</div>
				</div>
			{/if}
		</div>
	{/if}

	<!-- Other Export Options Tab -->
	{#if activeTab === 'other-exports'}
		<div class="bg-white rounded-lg shadow-sm border border-gray-200 p-6">
			<h2 class="text-lg font-semibold text-gray-800 mb-4">Other Export Options</h2>
			<p class="text-gray-600">Additional export formats and options are available here for exporting your project data in various formats including CSV, Excel, SPSS, SAS, R, and Stata.</p>
		</div>
	{/if}
</div>

<style>
	:global(body) {
		font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen', 'Ubuntu',
			'Cantarell', 'Fira Sans', 'Droid Sans', 'Helvetica Neue', sans-serif;
	}
</style>
