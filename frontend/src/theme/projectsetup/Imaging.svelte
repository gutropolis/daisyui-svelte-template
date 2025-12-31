<script lang="ts">
	interface Field {
		type: string;
		name: string;
		apiIdentifier: string;
	}

	interface FormGroup {
		id: string;
		name: string;
		description: string;
		expectedType: string;
		fieldCount: number;
		fields: Field[];
	}

	let formGroups: FormGroup[] = [
		{
			id: 'mri',
			name: 'MRI',
			description: 'Expected type of scan: CT',
			expectedType: 'CT',
			fieldCount: 1,
			fields: [
				{
					type: 'datetime',
					name: 'dateAndTime',
					apiIdentifier: 'datetime'
				}
			]
		},
		{
			id: 'ct',
			name: 'CT',
			description: 'Expected type of scan: CT',
			expectedType: 'CT',
			fieldCount: 2,
			fields: [
				{
					type: 'number',
					name: 'number',
					apiIdentifier: 'number'
				},
				{
					type: 'text',
					name: 'text',
					apiIdentifier: 'text'
				}
			]
		}
	];

	let previewMode = false;
	let showModal = false;
	let isEditMode = false;
	let editingGroupId: string | null = null;
	let successMessage = '';

	// Group form fields
	let formData = {
		title: '',
		apiIdentifier: '',
		scanType: 'Angiography',
		seriesList: ''
	};

	// Field modal state
	let showFieldModal = false;
	let isEditFieldMode = false;
	let editingGroupIdForField: string | null = null;
	let editingFieldIndex: number | null = null;
	let fieldFormData = {
		type: '',
		name: '',
		apiIdentifier: ''
	};

	const scanTypes = ['Angiography', 'CT', 'MRI', 'Ultrasound', 'X-Ray', 'PET'];
	const fieldTypes = ['text', 'number', 'datetime', 'boolean', 'select', 'textarea'];

	function openAddModal() {
		showModal = true;
		isEditMode = false;
		editingGroupId = null;
		formData = {
			title: '',
			apiIdentifier: '',
			scanType: 'Angiography',
			seriesList: ''
		};
	}

	function openEditModal(group: FormGroup) {
		showModal = true;
		isEditMode = true;
		editingGroupId = group.id;
		formData = {
			title: group.name,
			apiIdentifier: group.description,
			scanType: group.expectedType,
			seriesList: ''
		};
	}

	function closeModal() {
		showModal = false;
		formData = {
			title: '',
			apiIdentifier: '',
			scanType: 'Angiography',
			seriesList: ''
		};
	}

	function saveGroup() {
		if (!formData.title.trim() || !formData.apiIdentifier.trim()) {
			alert('Please fill in all required fields');
			return;
		}

		if (isEditMode && editingGroupId) {
			// Update existing group
			const index = formGroups.findIndex(g => g.id === editingGroupId);
			if (index !== -1) {
				formGroups[index] = {
					...formGroups[index],
					name: formData.title,
					description: formData.apiIdentifier,
					expectedType: formData.scanType
				};
				formGroups = formGroups;
				successMessage = 'Group updated successfully!';
			}
		} else {
			// Create new group
			const newGroup: FormGroup = {
				id: Date.now().toString(),
				name: formData.title,
				description: formData.apiIdentifier,
				expectedType: formData.scanType,
				fieldCount: 0,
				fields: []
			};
			formGroups = [...formGroups, newGroup];
			successMessage = 'Group added successfully!';
		}

		closeModal();
		setTimeout(() => {
			successMessage = '';
		}, 3000);
	}

	function deleteGroup(id: string) {
		if (confirm('Are you sure you want to delete this group?')) {
			formGroups = formGroups.filter(g => g.id !== id);
			successMessage = 'Group deleted successfully!';
			setTimeout(() => {
				successMessage = '';
			}, 3000);
		}
	}

	// Field CRUD functions
	function openAddFieldModal(groupId: string) {
		showFieldModal = true;
		isEditFieldMode = false;
		editingGroupIdForField = groupId;
		editingFieldIndex = null;
		fieldFormData = {
			type: 'text',
			name: '',
			apiIdentifier: ''
		};
	}

	function openEditFieldModal(groupId: string, fieldIndex: number) {
		showFieldModal = true;
		isEditFieldMode = true;
		editingGroupIdForField = groupId;
		editingFieldIndex = fieldIndex;
		const group = formGroups.find(g => g.id === groupId);
		if (group && group.fields[fieldIndex]) {
			fieldFormData = { ...group.fields[fieldIndex] };
		}
	}

	function closeFieldModal() {
		showFieldModal = false;
		fieldFormData = {
			type: 'text',
			name: '',
			apiIdentifier: ''
		};
		editingGroupIdForField = null;
		editingFieldIndex = null;
	}

	function saveField() {
		if (!fieldFormData.type.trim() || !fieldFormData.name.trim() || !fieldFormData.apiIdentifier.trim()) {
			alert('Please fill in all required fields');
			return;
		}

		const groupIndex = formGroups.findIndex(g => g.id === editingGroupIdForField);
		if (groupIndex === -1) return;

		if (isEditFieldMode && editingFieldIndex !== null) {
			// Update existing field
			formGroups[groupIndex].fields[editingFieldIndex] = { ...fieldFormData };
			successMessage = 'Field updated successfully!';
		} else {
			// Add new field
			formGroups[groupIndex].fields = [...formGroups[groupIndex].fields, { ...fieldFormData }];
			formGroups[groupIndex].fieldCount = formGroups[groupIndex].fields.length;
			successMessage = 'Field added successfully!';
		}

		formGroups = formGroups;
		closeFieldModal();
		setTimeout(() => {
			successMessage = '';
		}, 3000);
	}

	function deleteField(groupId: string, fieldIndex: number) {
		if (confirm('Are you sure you want to delete this field?')) {
			const groupIndex = formGroups.findIndex(g => g.id === groupId);
			if (groupIndex !== -1) {
				formGroups[groupIndex].fields = formGroups[groupIndex].fields.filter((_, i) => i !== fieldIndex);
				formGroups[groupIndex].fieldCount = formGroups[groupIndex].fields.length;
				formGroups = formGroups;
				successMessage = 'Field deleted successfully!';
				setTimeout(() => {
					successMessage = '';
				}, 3000);
			}
		}
	}
</script>

{#if successMessage}
	<div class="mb-4 p-3 bg-green-100 text-green-700 rounded-lg text-sm flex items-center gap-2">
		<i class="fas fa-check-circle"></i>
		{successMessage}
	</div>
{/if}

<div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
	<!-- Main Content Area -->
	<div class="lg:col-span-2 space-y-4">
		<!-- Header with controls -->
		<div class="flex items-center justify-between">
			<h2 class="text-xl font-bold text-gray-800">Imaging Groups</h2>
			<div class="flex items-center gap-3">
				<div class="flex items-center gap-2">
					<span class="text-xs text-gray-600">PREVIEW</span>
					<button
						on:click={() => (previewMode = !previewMode)}
						class="relative inline-flex h-5 w-9 items-center rounded-full transition-colors {previewMode
							? 'bg-blue-500'
							: 'bg-gray-300'}"
					>
						<span
							class="inline-block h-3 w-3 transform rounded-full bg-white transition-transform {previewMode
								? 'translate-x-5'
								: 'translate-x-1'}"
						/>
					</button>
				</div>
				<button on:click={openAddModal} class="text-blue-600 text-sm font-semibold hover:text-blue-700">ADD GROUPS</button>
			</div>
		</div>

		<!-- Form Groups Listing -->
		<div class="space-y-3">
		{#if formGroups.length === 0}
			<div class="text-center py-8 text-gray-500">
				<i class="fas fa-inbox text-3xl mb-2 block"></i>
				<p class="text-sm">No groups added yet. Click "ADD GROUPS" to create one.</p>
			</div>
		{:else}
			{#each formGroups as group (group.id)}
				<div class="bg-gray-50 rounded p-4 border border-gray-200">
					<!-- Group Header -->
					<div class="flex items-center justify-between mb-3">
						<div class="flex-1">
							<h3 class="text-sm font-bold text-gray-800">{group.name}</h3>
							<p class="text-xs text-gray-600">{group.description}</p>
						</div>
						<div class="flex items-center gap-2 ml-3">
							<button
								on:click={() => openEditModal(group)}
								class="p-1 text-gray-400 hover:text-blue-600 transition-colors text-sm"
								title="Edit"
							>
								<i class="fas fa-pen-square"></i>
							</button>
							<button
								on:click={() => deleteGroup(group.id)}
								class="p-1 text-gray-400 hover:text-red-600 transition-colors text-sm"
								title="Delete"
							>
								<i class="fas fa-trash"></i>
							</button>
						</div>
					</div>

					<!-- Field count -->
					<div class="text-xs text-gray-600 mb-2 flex justify-between">
						<span><strong>Series type:</strong> {group.description}</span>
						<span>Total fields: <strong>{group.fieldCount}</strong></span>
					</div>

					<!-- Fields section -->
					<div>
						<div class="flex items-center gap-2 mb-2">
							<h4 class="text-xs font-semibold text-gray-700">Fields</h4>
							<button 
								on:click={() => openAddFieldModal(group.id)}
								class="p-0.5 text-gray-400 hover:text-blue-600 text-xs"
								title="Add Field"
							>
								<i class="fas fa-plus"></i>
							</button>
							<button class="p-0.5 text-gray-400 hover:text-gray-600 text-xs">
								<i class="fas fa-search"></i>
							</button>
						</div>

						<!-- Fields Table -->
						<div class="overflow-x-auto">
							<table class="w-full text-xs">
								<thead>
									<tr class="bg-gray-100">
										<th class="px-3 py-1.5 text-left font-semibold text-gray-700">TYPE</th>
										<th class="px-3 py-1.5 text-left font-semibold text-gray-700">NAME</th>
										<th class="px-3 py-1.5 text-left font-semibold text-gray-700">API IDENTIFIER</th>
										<th class="px-3 py-1.5 text-left font-semibold text-gray-700">ACTION</th>
									</tr>
								</thead>
								<tbody>
									{#if group.fields.length === 0}
										<tr>
											<td colspan="4" class="px-3 py-3 text-center text-gray-500 text-xs">No fields added yet</td>
										</tr>
									{:else}
										{#each group.fields as field, fieldIndex (fieldIndex)}
											<tr class="border-t border-gray-200 hover:bg-white transition-colors">
												<td class="px-3 py-2 text-gray-700">{field.type}</td>
												<td class="px-3 py-2 text-gray-700">{field.name}</td>
												<td class="px-3 py-2 text-blue-600">{field.apiIdentifier}</td>
												<td class="px-3 py-2">
													<div class="flex gap-1">
														<button 
															on:click={() => openEditFieldModal(group.id, fieldIndex)}
															class="p-0.5 text-gray-400 hover:text-blue-600 transition-colors" 
															title="Edit"
														>
															<i class="fas fa-pen-square text-xs"></i>
														</button>
														<button 
															on:click={() => deleteField(group.id, fieldIndex)}
															class="p-0.5 text-gray-400 hover:text-red-600 transition-colors" 
															title="Delete"
														>
															<i class="fas fa-trash text-xs"></i>
														</button>
													</div>
												</td>
											</tr>
										{/each}
									{/if}
								</tbody>
							</table>
						</div>
					</div>
				</div>
			{/each}
		{/if}
		</div>
	</div>

	<!-- Sidebar with Information -->
	<div class="lg:col-span-1">
		<div class="bg-purple-50 rounded-lg p-5 border border-purple-200 sticky top-4 space-y-6">
			<!-- Imaging Groups Info -->
			<div>
				<h3 class="text-sm font-bold text-gray-800 mb-2 flex items-center gap-2">
					<i class="fas fa-image text-purple-600"></i>
					What are Imaging Groups?
				</h3>
				<p class="text-xs text-gray-700 leading-relaxed">
					Imaging Groups are structured containers that organize imaging study protocols and sequences. They define how medical imaging data (DICOM files) should be collected, organized, and processed for clinical research studies.
				</p>
			</div>

			<!-- Why We Need It -->
			<div>
				<h3 class="text-sm font-bold text-gray-800 mb-2 flex items-center gap-2">
					<i class="fas fa-question-circle text-purple-600"></i>
					Why Do We Need Imaging Groups?
				</h3>
				<ul class="text-xs text-gray-700 space-y-1.5 leading-relaxed">
					<li class="flex gap-2">
						<span class="text-purple-600 font-semibold">•</span>
						<span><strong>Protocol Organization:</strong> Organize imaging sequences and series logically</span>
					</li>
					<li class="flex gap-2">
						<span class="text-purple-600 font-semibold">•</span>
						<span><strong>DICOM Management:</strong> Standardize DICOM file handling and identification</span>
					</li>
					<li class="flex gap-2">
						<span class="text-purple-600 font-semibold">•</span>
						<span><strong>Data Consistency:</strong> Ensure consistent imaging data collection across sites</span>
					</li>
					<li class="flex gap-2">
						<span class="text-purple-600 font-semibold">•</span>
						<span><strong>Quality Control:</strong> Track and validate imaging series and metadata</span>
					</li>
				</ul>
			</div>

			<!-- API Identifier -->
			<div>
				<h3 class="text-sm font-bold text-gray-800 mb-2 flex items-center gap-2">
					<i class="fas fa-key text-purple-600"></i>
					API Identifier (Must be Unique)
				</h3>
				<p class="text-xs text-gray-700 leading-relaxed mb-2">
					A unique identifier for the imaging group used in API calls and system references. Must be distinct across all imaging groups in the study.
				</p>
				<div class="bg-white border border-gray-300 rounded p-2.5 text-xs">
					<p class="text-gray-600 mb-1"><strong>Example:</strong></p>
					<p class="font-mono text-gray-700 text-xs">mri_brain_t1w</p>
					<p class="text-gray-600 text-xs mt-2 leading-relaxed">
						✓ Use lowercase letters, numbers, and underscores<br/>
						✓ No spaces or special characters<br/>
						✓ Must be unique across all groups
					</p>
				</div>
			</div>

			<!-- Series Information -->
			<div>
				<h3 class="text-sm font-bold text-gray-800 mb-2 flex items-center gap-2">
					<i class="fas fa-layer-group text-purple-600"></i>
					What are Series?
				</h3>
				<p class="text-xs text-gray-700 leading-relaxed mb-2">
					Series are individual sequences within an imaging group. Each series represents a specific imaging acquisition with its own protocol and parameters (e.g., T1-weighted, T2-weighted, FLAIR for MRI).
				</p>
				<p class="text-xs text-gray-700 leading-relaxed">
					<strong>Common Series Types:</strong>
				</p>
				<ul class="text-xs text-gray-700 space-y-0.5 mt-1.5">
					<li class="flex gap-2"><span class="text-purple-600">•</span> <span>T1, T2, FLAIR (MRI)</span></li>
					<li class="flex gap-2"><span class="text-purple-600">•</span> <span>CT, Localizer, Scout</span></li>
					<li class="flex gap-2"><span class="text-purple-600">•</span> <span>DWI, DTI, fMRI (Functional)</span></li>
				</ul>
			</div>

			<!-- DCM Identifier -->
			<div>
				<h3 class="text-sm font-bold text-gray-800 mb-2 flex items-center gap-2">
					<i class="fas fa-barcode text-purple-600"></i>
					DICOM Identifier (DCM Identifier)
				</h3>
				<p class="text-xs text-gray-700 leading-relaxed mb-2">
					A unique identifier used to match and identify DICOM files within a series. Essential for:
				</p>
				<ul class="text-xs text-gray-700 space-y-1 mb-2">
					<li class="flex gap-2">
						<span class="text-purple-600">→</span>
						<span>Automated DICOM file routing and processing</span>
					</li>
					<li class="flex gap-2">
						<span class="text-purple-600">→</span>
						<span>Quality assurance and validation checks</span>
					</li>
					<li class="flex gap-2">
						<span class="text-purple-600">→</span>
						<span>Linking imaging data to clinical data</span>
					</li>
				</ul>
				<div class="bg-white border border-gray-300 rounded p-2.5 text-xs">
					<p class="text-gray-600 mb-1"><strong>Example:</strong></p>
					<p class="font-mono text-gray-700 text-xs">BRAIN_T1_001</p>
					<p class="text-gray-600 text-xs mt-2">
						Must match DICOM SeriesDescription in image headers
					</p>
				</div>
			</div>

			<!-- Fields Info -->
			<div>
				<h3 class="text-sm font-bold text-gray-800 mb-2 flex items-center gap-2">
					<i class="fas fa-list text-purple-600"></i>
					What are Fields?
				</h3>
				<p class="text-xs text-gray-700 leading-relaxed mb-2">
					Fields capture imaging metadata and acquisition parameters for each series. These can include protocol details, reconstruction methods, or QA measurements.
				</p>
				<p class="text-xs text-gray-700 leading-relaxed">
					<strong>Supported Field Types:</strong>
				</p>
				<ul class="text-xs text-gray-700 space-y-0.5 mt-1.5">
					<li class="flex gap-2"><span class="text-purple-600">•</span> <span><strong>text</strong> - Protocol names, techniques</span></li>
					<li class="flex gap-2"><span class="text-purple-600">•</span> <span><strong>number</strong> - TR, TE, flip angles, slice thickness</span></li>
					<li class="flex gap-2"><span class="text-purple-600">•</span> <span><strong>datetime</strong> - Acquisition time</span></li>
					<li class="flex gap-2"><span class="text-purple-600">•</span> <span><strong>boolean</strong> - Quality flags, compliance</span></li>
					<li class="flex gap-2"><span class="text-purple-600">•</span> <span><strong>select</strong> - Reconstruction methods, anatomy</span></li>
					<li class="flex gap-2"><span class="text-purple-600">•</span> <span><strong>textarea</strong> - Comments, notes</span></li>
				</ul>
			</div>

			<!-- Quick Tips -->
			<div class="bg-white rounded p-3 border border-gray-200">
				<h4 class="text-xs font-semibold text-gray-800 mb-2 flex items-center gap-2">
					<i class="fas fa-lightbulb text-yellow-500"></i>
					Quick Tips
				</h4>
				<ul class="text-xs text-gray-700 space-y-1">
					<li class="flex gap-2">
						<span class="text-purple-600">→</span>
						<span>Use descriptive series names matching DICOM protocols</span>
					</li>
					<li class="flex gap-2">
						<span class="text-purple-600">→</span>
						<span>DCM Identifier must match DICOM SeriesDescription</span>
					</li>
					<li class="flex gap-2">
						<span class="text-purple-600">→</span>
						<span>Document all custom fields for data validation</span>
					</li>
					<li class="flex gap-2">
						<span class="text-purple-600">→</span>
						<span>Test DCM matching with sample DICOM files</span>
					</li>
				</ul>
			</div>
		</div>
	</div>
</div>
{#if showModal}
	<div class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
		<div class="bg-white rounded-lg shadow-lg w-full max-w-lg mx-4 p-6">
			<h2 class="text-lg font-bold text-gray-800 mb-4">{isEditMode ? 'Edit Group' : 'Add New Group'}</h2>

			<div class="space-y-4">
				<!-- Title -->
				<div>
					<label class="block text-sm font-medium text-gray-700 mb-1">Title</label>
					<input
						type="text"
						bind:value={formData.title}
						placeholder="Enter title"
						class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 text-sm"
					/>
					<p class="text-xs text-gray-500 mt-1">It will appear in the entry editor</p>
				</div>

				<!-- API Level Identifier -->
				<div>
					<label class="block text-sm font-medium text-gray-700 mb-1">API Level Identifier</label>
					<input
						type="text"
						bind:value={formData.apiIdentifier}
						placeholder="Enter api level identifier"
						class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 text-sm"
					/>
					<p class="text-xs text-gray-500 mt-1">Database level identifier</p>
				</div>

				<!-- Scan Type -->
				<div>
					<label class="block text-sm font-medium text-gray-700 mb-1">Scan Type</label>
					<select
						bind:value={formData.scanType}
						class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 text-sm"
					>
						{#each scanTypes as type}
							<option value={type}>{type}</option>
						{/each}
					</select>
				</div>

				<!-- Series List -->
				<div>
					<label class="block text-sm font-medium text-gray-700 mb-1">Series List</label>
					<textarea
						bind:value={formData.seriesList}
						placeholder="Enter series list"
						rows="4"
						class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 text-sm"
					></textarea>
				</div>
			</div>

			<!-- Action Buttons -->
			<div class="mt-6 flex gap-3 justify-end">
				<button
					on:click={closeModal}
					class="px-4 py-2 border border-gray-300 text-gray-700 rounded-lg hover:bg-gray-50 font-medium text-sm transition-colors"
				>
					CANCEL
				</button>
				<button
					on:click={saveGroup}
					class="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 font-medium text-sm transition-colors"
				>
					SAVE
				</button>
			</div>
		</div>
	</div>
{/if}

<!-- Add/Edit Field Modal -->
{#if showFieldModal}
	<div class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
		<div class="bg-white rounded-lg shadow-lg w-full max-w-lg mx-4 p-6">
			<h2 class="text-lg font-bold text-gray-800 mb-4">{isEditFieldMode ? 'Edit Field' : 'Add New Field'}</h2>

			<div class="space-y-4">
				<!-- Field Type -->
				<div>
					<label class="block text-sm font-medium text-gray-700 mb-1">Type</label>
					<select
						bind:value={fieldFormData.type}
						class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 text-sm"
					>
						{#each fieldTypes as type}
							<option value={type}>{type}</option>
						{/each}
					</select>
				</div>

				<!-- Field Name -->
				<div>
					<label class="block text-sm font-medium text-gray-700 mb-1">Name</label>
					<input
						type="text"
						bind:value={fieldFormData.name}
						placeholder="Enter field name"
						class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 text-sm"
					/>
				</div>

				<!-- API Level Identifier -->
				<div>
					<label class="block text-sm font-medium text-gray-700 mb-1">API Level Identifier</label>
					<input
						type="text"
						bind:value={fieldFormData.apiIdentifier}
						placeholder="Enter api level identifier"
						class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 text-sm"
					/>
				</div>
			</div>

			<!-- Action Buttons -->
			<div class="mt-6 flex gap-3 justify-end">
				<button
					on:click={closeFieldModal}
					class="px-4 py-2 border border-gray-300 text-gray-700 rounded-lg hover:bg-gray-50 font-medium text-sm transition-colors"
				>
					CANCEL
				</button>
				<button
					on:click={saveField}
					class="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 font-medium text-sm transition-colors"
				>
					SAVE
				</button>
			</div>
		</div>
	</div>
{/if}
