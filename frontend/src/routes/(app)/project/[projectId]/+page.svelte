<script lang="ts">
	import { page } from '$app/stores';
	import { PROJECT_DETAIL_ROUTE } from '$lib/enums/routes';
	import { getStatusColor, getStatusIcon } from '$lib/utils/projecthelper';
	import { resolveProjectRoute } from '$lib/utils/routes';

	interface FormField {
		id: string;
		name: string;
		label: string;
		type: 'text' | 'number' | 'email' | 'date' | 'select' | 'checkbox' | 'radio' | 'textarea';
		required: boolean;
		value: string | number | boolean;
		options?: { label: string; value: string }[];
		placeholder?: string;
		validation?: string;
	}

	interface DataRecord {
		id: number;
		patientId: string;
		name: string;
		status: 'Draft' | 'Incomplete' | 'Unverified' | 'Complete';
		event: string;
		form: string;
		completedDate?: string;
	}

	let records: DataRecord[] = [
		{
			id: 1,
			patientId: 'P001',
			name: 'John Smith',
			status: 'Complete',
			event: 'Baseline Visit',
			form: 'Demographics',
			completedDate: '2024-01-15'
		},
		{
			id: 2,
			patientId: 'P002',
			name: 'Jane Doe',
			status: 'Incomplete',
			event: 'Week 4 Follow-up',
			form: 'Vital Signs',
			completedDate: undefined
		},
		{
			id: 3,
			patientId: 'P003',
			name: 'Bob Johnson',
			status: 'Draft',
			event: 'Baseline Visit',
			form: 'Medical History',
			completedDate: undefined
		}
	];

	let formFields: FormField[] = [
		{
			id: 'demographics_dob',
			name: 'dob',
			label: 'Date of Birth',
			type: 'date',
			required: true,
			value: '',
			placeholder: 'MM/DD/YYYY'
		},
		{
			id: 'demographics_gender',
			name: 'gender',
			label: 'Gender',
			type: 'select',
			required: true,
			value: '',
			options: [
				{ label: 'Select...', value: '' },
				{ label: 'Male', value: 'M' },
				{ label: 'Female', value: 'F' },
				{ label: 'Other', value: 'O' }
			]
		},
		{
			id: 'demographics_race',
			name: 'race',
			label: 'Race/Ethnicity',
			type: 'select',
			required: false,
			value: '',
			options: [
				{ label: 'Select...', value: '' },
				{ label: 'White', value: 'W' },
				{ label: 'Black/African American', value: 'B' },
				{ label: 'Asian', value: 'A' },
				{ label: 'Hispanic/Latino', value: 'H' }
			]
		},
		{
			id: 'demographics_phone',
			name: 'phone',
			label: 'Phone Number',
			type: 'text',
			required: false,
			value: '',
			placeholder: '(555) 123-4567',
			validation: 'phone'
		},
		{
			id: 'demographics_email',
			name: 'email',
			label: 'Email Address',
			type: 'email',
			required: false,
			value: '',
			placeholder: 'patient@example.com'
		}
	];

	let selectedRecord: DataRecord | null = null;
	let showRecordModal = false;
	let showFormModal = false;
	let newPatientId = '';
	let selectedEvent = 'baseline';
	let selectedForm = 'demographics';
	let formStatus = 'Draft';

 
 

	const createNewRecord = () => {
		if (!newPatientId.trim()) return;

		const record: DataRecord = {
			id: Math.max(...records.map(r => r.id), 0) + 1,
			patientId: newPatientId,
			name: `Patient ${newPatientId}`,
			status: 'Draft',
			event: selectedEvent,
			form: selectedForm
		};
		records = [...records, record];
		showRecordModal = false;
		newPatientId = '';
	};

	const deleteRecord = (id: number) => {
		records = records.filter(r => r.id !== id);
	};

	const openFormEntry = (record: DataRecord) => {
		selectedRecord = record;
		showFormModal = true;
	};

	const saveFormData = () => {
		if (selectedRecord) {
			const recordIndex = records.findIndex(r => r.id === selectedRecord!.id);
			if (recordIndex >= 0) {
				records[recordIndex].status = 'Complete';
				records[recordIndex].completedDate = new Date().toISOString().split('T')[0];
				records = [...records];
			}
		}
		showFormModal = false;
		selectedRecord = null;
		formFields.forEach(f => (f.value = ''));
	};

	const validateForm = () => {
		return formFields.every(f => !f.required || f.value !== '');
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
		<h1 class="text-3xl font-bold text-gray-800 mb-2">Data Entry & Records</h1>
		<p class="text-gray-600">View and manage patient records and data entry forms</p>
	</div>

	<!-- Summary Cards -->
	<div class="grid grid-cols-1 md:grid-cols-4 gap-4">
		<div class="bg-linear-to-br from-blue-50 to-blue-100 rounded-lg shadow p-6 border border-blue-200">
			<div class="flex items-center justify-between">
				<div>
					<p class="text-sm text-gray-600 font-medium">Total Records</p>
					<p class="text-3xl font-bold text-blue-600 mt-1">{records.length}</p>
				</div>
				<i class="fas fa-database text-4xl text-blue-200"></i>
			</div>
		</div>

		<div class="bg-linear-to-br from-green-50 to-green-100 rounded-lg shadow p-6 border border-green-200">
			<div class="flex items-center justify-between">
				<div>
					<p class="text-sm text-gray-600 font-medium">Completed</p>
					<p class="text-3xl font-bold text-green-600 mt-1">{records.filter(r => r.status === 'Complete').length}</p>
				</div>
				<i class="fas fa-check-circle text-4xl text-green-200"></i>
			</div>
		</div>

		<div class="bg-linear-to-br from-yellow-50 to-yellow-100 rounded-lg shadow p-6 border border-yellow-200">
			<div class="flex items-center justify-between">
				<div>
					<p class="text-sm text-gray-600 font-medium">Incomplete</p>
					<p class="text-3xl font-bold text-yellow-600 mt-1">{records.filter(r => r.status === 'Incomplete' || r.status === 'Draft').length}</p>
				</div>
				<i class="fas fa-hourglass-half text-4xl text-yellow-200"></i>
			</div>
		</div>

		<div class="bg-linear-to-br from-purple-50 to-purple-100 rounded-lg shadow p-6 border border-purple-200">
			<div class="flex items-center justify-between">
				<div>
					<p class="text-sm text-gray-600 font-medium">Completion Rate</p>
					<p class="text-3xl font-bold text-purple-600 mt-1">{Math.round((records.filter(r => r.status === 'Complete').length / records.length) * 100)}%</p>
				</div>
				<i class="fas fa-chart-pie text-4xl text-purple-200"></i>
			</div>
		</div>
	</div>

	<!-- Add Record Button -->
	<button
		on:click={() => (showRecordModal = true)}
		class="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 font-medium transition-colors flex items-center gap-2"
	>
		<i class="fas fa-plus"></i>
		Create New Record
	</button>

	<!-- Records Table -->
	<div class="bg-white rounded-lg shadow overflow-hidden">
		<div class="p-6 border-b border-gray-200">
			<h2 class="text-xl font-bold text-gray-800 flex items-center gap-2">
				<i class="fas fa-list text-blue-600"></i>
				Patient Records
			</h2>
		</div>

		{#if records.length === 0}
			<div class="p-12 text-center">
				<i class="fas fa-inbox text-4xl text-gray-300 mb-4 block"></i>
				<p class="text-gray-500">No records yet. Create one to start data entry.</p>
			</div>
		{:else}
			<div class="overflow-x-auto">
				<table class="w-full text-sm">
					<thead class="bg-gray-50 border-b border-gray-200">
						<tr>
							<th class="px-6 py-3 text-left font-semibold text-gray-700">Patient ID</th>
							<th class="px-6 py-3 text-left font-semibold text-gray-700">Name</th>
							<th class="px-6 py-3 text-left font-semibold text-gray-700">Event</th>
							<th class="px-6 py-3 text-left font-semibold text-gray-700">Form</th>
							<th class="px-6 py-3 text-left font-semibold text-gray-700">Status</th>
							<th class="px-6 py-3 text-left font-semibold text-gray-700">Last Updated</th>
							<th class="px-6 py-3 text-left font-semibold text-gray-700">Actions</th>
						</tr>
					</thead>
					<tbody class="divide-y divide-gray-200">
						{#each records as record (record.id)}
							<tr class="hover:bg-gray-50 transition-colors">
								<td class="px-6 py-3 font-semibold text-gray-800">{record.patientId}</td>
								<td class="px-6 py-3 text-gray-700">{record.name}</td>
								<td class="px-6 py-3 text-gray-600">{record.event}</td>
								<td class="px-6 py-3 text-gray-600">{record.form}</td>
								<td class="px-6 py-3">
									<div class="flex items-center gap-2">
										<i class="fas {getStatusIcon(record.status)}"></i>
										<span class="px-3 py-1 rounded-full text-xs font-medium {getStatusColor(record.status)}">
											{record.status}
										</span>
									</div>
								</td>
								<td class="px-6 py-3 text-gray-600">{record.completedDate || '—'}</td>
								<td class="px-6 py-3 space-x-2 flex">
									<button
										on:click={() => openFormEntry(record)}
										class="px-3 py-1 bg-blue-50 text-blue-600 rounded hover:bg-blue-100 text-xs font-medium transition-colors"
									>
										<i class="fas fa-edit"></i> Edit
									</button>
									<button
										on:click={() => deleteRecord(record.id)}
										class="px-3 py-1 bg-red-50 text-red-600 rounded hover:bg-red-100 text-xs font-medium transition-colors"
										aria-label="Delete record {record.patientId}"
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

	<!-- Data Entry Best Practices -->
	<div class="bg-blue-50 rounded-lg shadow p-6 border border-blue-200">
		<h3 class="text-lg font-bold text-gray-800 mb-3 flex items-center gap-2">
			<i class="fas fa-info-circle text-blue-600"></i>
			Data Entry Best Practices
		</h3>
		<ul class="space-y-2 text-sm text-gray-700">
			<li class="flex items-start gap-2">
				<span class="text-blue-600 font-bold">•</span>
				<span><strong>Save drafts:</strong> Save incomplete forms as drafts before closing</span>
			</li>
			<li class="flex items-start gap-2">
				<span class="text-blue-600 font-bold">•</span>
				<span><strong>Verify data:</strong> Double-check entries for accuracy before marking complete</span>
			</li>
			<li class="flex items-start gap-2">
				<span class="text-blue-600 font-bold">•</span>
				<span><strong>Follow protocols:</strong> Adhere to study SOPs when collecting data</span>
			</li>
			<li class="flex items-start gap-2">
				<span class="text-blue-600 font-bold">•</span>
				<span><strong>Track changes:</strong> All modifications are logged with timestamp and user</span>
			</li>
		</ul>
	</div>

	<!-- Create Record Modal -->
	{#if showRecordModal}
		<div class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
			<div class="bg-white rounded-lg shadow-xl p-6 max-w-md w-full mx-4">
				<h2 class="text-xl font-bold text-gray-800 mb-4">Create New Record</h2>

				<div class="space-y-4">
					<div>
						<label for="patient-id" class="block text-sm font-medium text-gray-700 mb-1">Patient ID</label>
						<input
							id="patient-id"
							type="text"
							bind:value={newPatientId}
							class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 outline-none"
							placeholder="e.g., P001"
						/>
					</div>

					<div>
						<label for="event-select" class="block text-sm font-medium text-gray-700 mb-1">Event</label>
						<select
							id="event-select"
							bind:value={selectedEvent}
							class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 outline-none"
						>
							<option value="baseline">Baseline Visit</option>
							<option value="week4">Week 4 Follow-up</option>
							<option value="week12">Week 12 Follow-up</option>
							<option value="final">Final Visit</option>
						</select>
					</div>

					<div>
						<label for="form-select" class="block text-sm font-medium text-gray-700 mb-1">Starting Form</label>
						<select
							id="form-select"
							bind:value={selectedForm}
							class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 outline-none"
						>
							<option value="demographics">Demographics</option>
							<option value="vital-signs">Vital Signs</option>
							<option value="medical-history">Medical History</option>
							<option value="medications">Current Medications</option>
						</select>
					</div>
				</div>

				<div class="flex gap-2 justify-end mt-6 border-t pt-4">
					<button
						on:click={() => (showRecordModal = false)}
						class="px-4 py-2 border border-gray-300 text-gray-700 rounded-lg hover:bg-gray-50 font-medium transition-colors"
					>
						Cancel
					</button>
					<button
						on:click={createNewRecord}
						disabled={!newPatientId.trim()}
						class="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 font-medium transition-colors disabled:opacity-50"
					>
						Create Record
					</button>
				</div>
			</div>
		</div>
	{/if}

	<!-- Data Entry Form Modal -->
	{#if showFormModal && selectedRecord}
		<div class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50 overflow-y-auto">
			<div class="bg-white rounded-lg shadow-xl p-6 max-w-2xl w-full mx-4 my-8">
				<div class="flex items-center justify-between mb-6 border-b pb-4">
					<div>
						<h2 class="text-2xl font-bold text-gray-800">Data Entry Form</h2>
						<p class="text-sm text-gray-600 mt-1">
							Patient <span class="font-semibold">{selectedRecord.patientId}</span> - {selectedRecord.form}
						</p>
					</div>
					<button
						on:click={() => {
							showFormModal = false;
							selectedRecord = null;
						}}
						class="text-gray-500 hover:text-gray-700 text-2xl"
						aria-label="Close form"
					>
						×
					</button>
				</div>

				<div class="space-y-6 max-h-[60vh] overflow-y-auto mb-6">
					{#each formFields as field (field.id)}
						<div>
							<label for={field.id} class="block text-sm font-medium text-gray-700 mb-2">
								{field.label}
								{#if field.required}
									<span class="text-red-500">*</span>
								{/if}
							</label>

							{#if field.type === 'text' || field.type === 'email' || field.type === 'number'}
								<input
									id={field.id}
									type={field.type}
									bind:value={field.value}
									placeholder={field.placeholder}
									class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 outline-none"
								/>
							{:else if field.type === 'date'}
								<input
									id={field.id}
									type="date"
									bind:value={field.value}
									class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 outline-none"
								/>
							{:else if field.type === 'select'}
								<select
									id={field.id}
									bind:value={field.value}
									class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 outline-none"
								>
									{#each field.options || [] as option}
										<option value={option.value}>{option.label}</option>
									{/each}
								</select>
							{:else if field.type === 'textarea'}
								<textarea
									id={field.id}
									bind:value={field.value}
									placeholder={field.placeholder}
									class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 outline-none"
									rows="4"
								></textarea>
							{:else if field.type === 'checkbox'}
								<label class="flex items-center gap-2 cursor-pointer">
									<input
										id={field.id}
										type="checkbox"
										checked={field.value === true || field.value === 'true'}
										class="w-4 h-4 text-blue-600 rounded"
									/>
									<span class="text-gray-700">{field.label}</span>
								</label>
							{:else if field.type === 'radio'}
								<div class="space-y-2">
									{#each field.options || [] as option}
										<label class="flex items-center gap-2 cursor-pointer">
											<input
												type="radio"
												name={field.id}
												value={option.value}
												bind:group={field.value}
												class="w-4 h-4 text-blue-600"
											/>
											<span class="text-gray-700">{option.label}</span>
										</label>
									{/each}
								</div>
							{/if}
						</div>
					{/each}
				</div>

				<div class="flex gap-2 justify-end border-t pt-4">
					<button
						on:click={() => {
							showFormModal = false;
							selectedRecord = null;
							formFields.forEach(f => (f.value = ''));
						}}
						class="px-4 py-2 border border-gray-300 text-gray-700 rounded-lg hover:bg-gray-50 font-medium transition-colors"
					>
						Discard
					</button>
					<button
						on:click={saveFormData}
						disabled={!validateForm()}
						class="px-4 py-2 bg-green-600 text-white rounded-lg hover:bg-green-700 font-medium transition-colors disabled:opacity-50"
					>
						<i class="fas fa-save mr-2"></i>
						Save & Complete
					</button>
				</div>
			</div>
		</div>
	{/if}
</div>
