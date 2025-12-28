<script lang="ts">
	import { page } from '$app/stores';
	import { PROJECT_DETAIL_SETUP_ROUTE } from '$lib/enums/routes';
	import { resolveProjectRoute } from '$lib/utils/routes';
	import InstrumentEditor from '$lib/components/projectsetup/InstrumentEditor.svelte';

	interface FormField {
		id: number;
		fieldName: string;
		fieldLabel: string;
		fieldType: string;
		required: boolean;
	}

	interface Form {
		id: number;
		name: string;
		description: string;
		fields: FormField[];
		status: 'Draft' | 'Active' | 'Locked';
	}

	let forms = $state([
		{
			id: 1,
			name: 'Baseline',
			description: 'Initial participant assessment',
			status: 'Active',
			fields: [
				{ id: 1, fieldName: 'patient_age', fieldLabel: 'Age', fieldType: 'number', required: true },
				{ id: 2, fieldName: 'patient_gender', fieldLabel: 'Gender', fieldType: 'radio', required: true },
				{ id: 3, fieldName: 'medical_history', fieldLabel: 'Medical History', fieldType: 'text', required: false },
				{ id: 4, fieldName: 'consent', fieldLabel: 'Consent', fieldType: 'checkbox', required: true }
			]
		},
		{
			id: 2,
			name: 'Intervention',
			description: 'Intervention form',
			status: 'Active',
			fields: [
				{ id: 5, fieldName: 'intervention_date', fieldLabel: 'Date', fieldType: 'date', required: true },
				{ id: 6, fieldName: 'intervention_type', fieldLabel: 'Type', fieldType: 'dropdown', required: true }
			]
		},
		{
			id: 3,
			name: 'Checkpoint 30 Day',
			description: 'Checkpoint 30 Day form',
			status: 'Active',
			fields: [
				{ id: 7, fieldName: 'checkpoint_date', fieldLabel: 'Date', fieldType: 'date', required: true },
				{ id: 8, fieldName: 'status', fieldLabel: 'Status', fieldType: 'radio', required: true },
				{ id: 9, fieldName: 'notes', fieldLabel: 'Notes', fieldType: 'text', required: false }
			]
		},
		{
			id: 4,
			name: 'Checkpoint 6 Month',
			description: 'Checkpoint 6 Month form',
			status: 'Active',
			fields: [
				{ id: 10, fieldName: 'checkpoint_date', fieldLabel: 'Date', fieldType: 'date', required: true },
				{ id: 11, fieldName: 'status', fieldLabel: 'Status', fieldType: 'radio', required: true },
				{ id: 12, fieldName: 'notes', fieldLabel: 'Notes', fieldType: 'text', required: false }
			]
		},
		{
			id: 5,
			name: 'Checkpoint 1 Year',
			description: 'Checkpoint 1 Year form',
			status: 'Active',
			fields: [
				{ id: 13, fieldName: 'checkpoint_date', fieldLabel: 'Date', fieldType: 'date', required: true },
				{ id: 14, fieldName: 'status', fieldLabel: 'Status', fieldType: 'radio', required: true },
				{ id: 15, fieldName: 'notes', fieldLabel: 'Notes', fieldType: 'text', required: false }
			]
		},
		{
			id: 6,
			name: 'Student Check Up 1',
			description: 'Student Check Up 1 form',
			status: 'Active',
			fields: [
				{ id: 16, fieldName: 'check_date', fieldLabel: 'Date', fieldType: 'date', required: true }
			]
		},
		{
			id: 7,
			name: 'Checkpoint 2 Year',
			description: 'Checkpoint 2 Year form',
			status: 'Active',
			fields: [
				{ id: 17, fieldName: 'checkpoint_date', fieldLabel: 'Date', fieldType: 'date', required: true },
				{ id: 18, fieldName: 'status', fieldLabel: 'Status', fieldType: 'radio', required: true },
				{ id: 19, fieldName: 'notes', fieldLabel: 'Notes', fieldType: 'text', required: false }
			]
		},
		{
			id: 8,
			name: 'Student Check Up 2',
			description: 'Student Check Up 2 form',
			status: 'Active',
			fields: [
				{ id: 20, fieldName: 'check_date', fieldLabel: 'Date', fieldType: 'date', required: true }
			]
		},
		{
			id: 9,
			name: 'Checkpoint 3 Year',
			description: 'Checkpoint 3 Year form',
			status: 'Active',
			fields: [
				{ id: 21, fieldName: 'checkpoint_date', fieldLabel: 'Date', fieldType: 'date', required: true },
				{ id: 22, fieldName: 'status', fieldLabel: 'Status', fieldType: 'radio', required: true },
				{ id: 23, fieldName: 'notes', fieldLabel: 'Notes', fieldType: 'text', required: false }
			]
		},
		{
			id: 10,
			name: 'Checkpoint 4 Year',
			description: 'Checkpoint 4 Year form',
			status: 'Active',
			fields: [
				{ id: 24, fieldName: 'checkpoint_date', fieldLabel: 'Date', fieldType: 'date', required: true },
				{ id: 25, fieldName: 'status', fieldLabel: 'Status', fieldType: 'radio', required: true },
				{ id: 26, fieldName: 'notes', fieldLabel: 'Notes', fieldType: 'text', required: false }
			]
		},
		{
			id: 11,
			name: 'Adverse Events',
			description: 'Adverse Events form',
			status: 'Active',
			fields: [
				{ id: 27, fieldName: 'event_date', fieldLabel: 'Date', fieldType: 'date', required: true },
				{ id: 28, fieldName: 'event_type', fieldLabel: 'Type', fieldType: 'dropdown', required: true }
			]
		}
	]);

	let showNewFormModal = $state(false);
	let newFormName = $state('');
	let newFormDescription = $state('');
	let selectedFormId = $state<number | null>(null);
	let editingFormId = $state<number | null>(null);

	const editingForm = $derived(forms.find(f => f.id === editingFormId));

	const handleSelectChange = (e: Event, formId: number) => {
		const select = e.target as HTMLSelectElement;
		const action = select.value;
		
		if (action === 'Edit') {
			editingFormId = formId;
		} else if (action === 'Delete') {
			deleteForm(formId);
		}
		select.value = 'Choose action';
	};

	const addNewForm = () => {
		const newForm: Form = {
			id: Math.max(...forms.map(f => f.id)) + 1,
			name: newFormName,
			description: newFormDescription,
			status: 'Draft',
			fields: []
		};
		forms = [...forms, newForm];
		showNewFormModal = false;
		newFormName = '';
		newFormDescription = '';
	};

	const deleteForm = (id: number) => {
		forms = forms.filter(f => f.id !== id);
	};

	const getStatusColor = (status: string) => {
		switch (status) {
			case 'Active':
				return 'bg-green-100 text-green-800';
			case 'Draft':
				return 'bg-yellow-100 text-yellow-800';
			case 'Locked':
				return 'bg-gray-100 text-gray-800';
			default:
				return 'bg-gray-100 text-gray-800';
		}
	};

	const projectId = $derived($page.params.projectId ?? '1');
	const setupOverviewRoute = $derived(resolveProjectRoute(PROJECT_DETAIL_SETUP_ROUTE, projectId));
</script>

<div class="p-6 space-y-6">
	<!-- Header -->
	<div>
		<a href={setupOverviewRoute} class="flex items-center gap-2 text-[#0b3a7a] hover:text-[#082654] text-sm font-medium mb-4">
			<i class="fas fa-arrow-left"></i>Back to Setup
		</a>
		<h1 class="text-3xl font-bold text-gray-800 mb-2">Design Your Data Collection Instruments</h1>
		<p class="text-gray-600">Add or edit fields on your data collection instruments using the Online Designer</p>
	</div>

	<!-- Info Banner -->
	<div class="bg-[#0b3a7a]/5 border border-[#0b3a7a]/10 rounded-lg p-4 flex items-start gap-3">
		<i class="fas fa-lightbulb text-[#0b3a7a] mt-1"></i>
		<div>
			<p class="font-medium text-gray-800">You can design forms by using the Online Designer or by uploading a Data Dictionary.</p>
			<p class="text-sm text-gray-600 mt-1">
				<a href="#" class="text-[#0b3a7a] hover:underline">Download the current data dictionary</a>
			</p>
		</div>
	</div>

	<!-- Action Buttons -->
	<div class="flex flex-wrap gap-3">
		<button
			onclick={() => (showNewFormModal = true)}
			class="px-4 py-2 bg-[#0b3a7a] text-white rounded-lg hover:bg-[#082654] font-medium transition-colors flex items-center gap-2"
		>
			<i class="fas fa-plus"></i>
			Online Designer
		</button>
		<button class="px-4 py-2 bg-gray-600 text-white rounded-lg hover:bg-gray-700 font-medium transition-colors flex items-center gap-2">
			<i class="fas fa-upload"></i>
			Data Dictionary
		</button>
		<button class="px-4 py-2 bg-green-600 text-white rounded-lg hover:bg-green-700 font-medium transition-colors flex items-center gap-2">
			<i class="fas fa-download"></i>
			Download Data Dictionary
		</button>
		<button class="px-4 py-2 bg-purple-600 text-white rounded-lg hover:bg-purple-700 font-medium transition-colors flex items-center gap-2">
			<i class="fas fa-search"></i>
			Check For Identifiers
		</button>
	</div>

	<!-- Feature Badges -->
	<div class="flex flex-wrap gap-2">
		<span class="px-3 py-1 bg-green-100 text-green-800 rounded-full text-xs font-medium flex items-center gap-1">
			<i class="fas fa-check-circle"></i>Smart Variables
		</span>
		<span class="px-3 py-1 bg-[#0b3a7a]/10 text-[#0b3a7a] rounded-full text-xs font-medium flex items-center gap-1">
			<i class="fas fa-code-branch"></i>Piping
		</span>
		<span class="px-3 py-1 bg-purple-100 text-purple-800 rounded-full text-xs font-medium flex items-center gap-1">
			<i class="fas fa-tag"></i>Action Tags
		</span>
		<span class="px-3 py-1 bg-orange-100 text-orange-800 rounded-full text-xs font-medium flex items-center gap-1">
			<i class="fas fa-layer-group"></i>Field Embedding
		</span>
		<span class="px-3 py-1 bg-indigo-100 text-indigo-800 rounded-full text-xs font-medium flex items-center gap-1">
			<i class="fas fa-star"></i>Special Functions
		</span>
	</div>

	<!-- Forms List -->
	<div class="bg-white rounded-lg shadow overflow-hidden">
		<div class="p-6 border-b border-gray-200">
			<h2 class="text-xl font-bold text-gray-800 mb-4">Data Collection Instruments</h2>
			
			<!-- Add new instrument section -->
			<div class="bg-gray-100 p-4 rounded border border-gray-300">
				<p class="text-sm font-medium text-gray-700 mb-3">Add new instrument:</p>
				<div class="flex flex-wrap gap-3">
					<button class="px-4 py-2 bg-green-600 text-white rounded text-sm font-medium hover:bg-green-700 flex items-center gap-2">
						<i class="fas fa-plus"></i>Create
						<span class="text-xs font-normal">a new instrument from scratch</span>
					</button>
					<button class="px-4 py-2 bg-blue-600 text-white rounded text-sm font-medium hover:bg-blue-700 flex items-center gap-2">
						<i class="fas fa-download"></i>Import
						<span class="text-xs font-normal">a new instrument from the official <a href="#" class="underline">REDCap Instrument Library</a></span>
					</button>
					<button class="px-4 py-2 bg-orange-600 text-white rounded text-sm font-medium hover:bg-orange-700 flex items-center gap-2">
						<i class="fas fa-upload"></i>Upload
						<span class="text-xs font-normal">instrument ZIP file from another project/user or <a href="#" class="underline">external libraries</a></span>
					</button>
				</div>
			</div>
		</div>

		<!-- Table -->
		<div class="overflow-x-auto">
			<table class="w-full text-sm border-collapse">
				<thead>
					<tr class="bg-gray-200 border-b border-gray-400">
						<th class="text-left px-4 py-3 font-bold text-gray-900">Instrument name</th>
						<th class="text-center px-4 py-3 font-bold text-gray-900">Fields</th>
						<th class="text-center px-4 py-3 font-bold text-gray-900">View PDF</th>
						<th class="text-left px-4 py-3 font-bold text-gray-900">Instrument actions</th>
					</tr>
				</thead>
				<tbody>
					{#each forms as form (form.id)}
						<tr class="border-b border-gray-300 hover:bg-blue-50 {selectedFormId === form.id ? 'bg-blue-100' : ''}" onclick={() => selectedFormId = form.id}>
							<td class="px-4 py-3 font-medium text-gray-900">{form.name}</td>
							<td class="text-center px-4 py-3 text-gray-700">{form.fields.length}</td>
							<td class="text-center px-4 py-3">
								<button class="text-red-600 hover:text-red-700" title="Download PDF">
									<i class="fas fa-file-pdf"></i>
								</button>
							</td>
							<td class="px-4 py-3">
								<select 
									class="px-3 py-1 border border-gray-300 rounded text-sm bg-white text-gray-700 hover:border-gray-400"
									onchange={(e) => handleSelectChange(e, form.id)}
								>
									<option value="Choose action">Choose action</option>
									<option value="Edit">Edit</option>
									<option value="Preview">Preview</option>
									<option value="Delete">Delete</option>
									<option value="Duplicate">Duplicate</option>
								</select>
							</td>
						</tr>
					{/each}
				</tbody>
			</table>
		</div>
	</div>


</div>

{#if editingFormId && editingForm}
	<InstrumentEditor 
		instrument={editingForm}
		onClose={() => editingFormId = null}
	/>
{/if}
