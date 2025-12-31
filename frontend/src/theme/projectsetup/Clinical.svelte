<script lang="ts">
	interface Field {
		type: string;
		name: string;
		apiIdentifier: string;
	}

	interface FormGroup {
		id: string;
		name: string;
		apiIdentifier: string;
		description: string;
		isMultipleEventGroup: boolean;
		fieldCount: number;
		fields: Field[];
	}

	let formGroups: FormGroup[] = [
		{
			id: 'mri',
			name: 'MRI',
			apiIdentifier: 'mri_form',
			description: 'MRI scanning form group',
			isMultipleEventGroup: false,
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
			apiIdentifier: 'ct_form',
			description: 'CT scanning form group',
			isMultipleEventGroup: true,
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
		description: '',
		isMultipleEventGroup: false
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

	const fieldTypes = ['text', 'number', 'datetime', 'boolean', 'select', 'textarea'];

	function openAddModal() {
		showModal = true;
		isEditMode = false;
		editingGroupId = null;
		formData = {
			title: '',
			apiIdentifier: '',
			description: '',
			isMultipleEventGroup: false
		};
	}

	function openEditModal(group: FormGroup) {
		showModal = true;
		isEditMode = true;
		editingGroupId = group.id;
		formData = {
			title: group.name,
			apiIdentifier: group.apiIdentifier,
			description: group.description,
			isMultipleEventGroup: group.isMultipleEventGroup
		};
	}

	function closeModal() {
		showModal = false;
		formData = {
			title: '',
			apiIdentifier: '',
			description: '',
			isMultipleEventGroup: false
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
					apiIdentifier: formData.apiIdentifier,
					description: formData.description,
					isMultipleEventGroup: formData.isMultipleEventGroup
				};
				formGroups = formGroups;
				successMessage = 'Group updated successfully!';
			}
		} else {
			// Create new group
			const newGroup: FormGroup = {
				id: Date.now().toString(),
				name: formData.title,
				apiIdentifier: formData.apiIdentifier,
				description: formData.description,
				isMultipleEventGroup: formData.isMultipleEventGroup,
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
			<h2 class="text-xl font-bold text-gray-800">Clinical Groups</h2>
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
		<div class="bg-blue-50 rounded-lg p-5 border border-blue-200 sticky top-4 space-y-6">
			<!-- Clinical Groups Info -->
			<div>
				<h3 class="text-sm font-bold text-gray-800 mb-2 flex items-center gap-2">
					<i class="fas fa-info-circle text-blue-600"></i>
					What are Clinical Groups?
				</h3>
				<p class="text-xs text-gray-700 leading-relaxed">
					Clinical Groups (also called Forms) are structured containers that organize related data collection fields for clinical studies. They group related information together, such as MRI scan data, patient demographics, or lab results.
				</p>
			</div>

			<!-- Why We Need It -->
			<div>
				<h3 class="text-sm font-bold text-gray-800 mb-2 flex items-center gap-2">
					<i class="fas fa-question-circle text-blue-600"></i>
					Why Do We Need Clinical Groups?
				</h3>
				<ul class="text-xs text-gray-700 space-y-1.5 leading-relaxed">
					<li class="flex gap-2">
						<span class="text-blue-600 font-semibold">•</span>
						<span><strong>Organization:</strong> Keep related data fields organized and logically grouped</span>
					</li>
					<li class="flex gap-2">
						<span class="text-blue-600 font-semibold">•</span>
						<span><strong>Scalability:</strong> Manage large forms with multiple sections efficiently</span>
					</li>
					<li class="flex gap-2">
						<span class="text-blue-600 font-semibold">•</span>
						<span><strong>API Structure:</strong> Define how data is structured in API responses</span>
					</li>
					<li class="flex gap-2">
						<span class="text-blue-600 font-semibold">•</span>
						<span><strong>Reusability:</strong> Reuse groups across multiple studies and events</span>
					</li>
				</ul>
			</div>

			<!-- API Identifier -->
			<div>
				<h3 class="text-sm font-bold text-gray-800 mb-2 flex items-center gap-2">
					<i class="fas fa-key text-blue-600"></i>
					API Identifier (Must be Unique)
				</h3>
				<p class="text-xs text-gray-700 leading-relaxed mb-2">
					A unique identifier used in API calls and database storage. Each clinical group must have a distinct API identifier.
				</p>
				<div class="bg-white border border-gray-300 rounded p-2.5 text-xs">
					<p class="text-gray-600 mb-1"><strong>Example:</strong></p>
					<p class="font-mono text-gray-700 text-xs">mri_form_001</p>
					<p class="text-gray-600 text-xs mt-2 leading-relaxed">
						✓ Use lowercase letters, numbers, and underscores<br/>
						✓ No spaces or special characters<br/>
						✓ Must be unique across all groups
					</p>
				</div>
			</div>

			<!-- Fields Info -->
			<div>
				<h3 class="text-sm font-bold text-gray-800 mb-2 flex items-center gap-2">
					<i class="fas fa-list text-blue-600"></i>
					What are Fields?
				</h3>
				<p class="text-xs text-gray-700 leading-relaxed mb-2">
					Fields are individual data collection elements within a clinical group. Each field captures specific information with a defined data type.
				</p>
				<p class="text-xs text-gray-700 leading-relaxed">
					<strong>Supported Field Types:</strong>
				</p>
				<ul class="text-xs text-gray-700 space-y-0.5 mt-1.5">
					<li class="flex gap-2"><span class="text-blue-600">•</span> <span><strong>text</strong> - Short text input</span></li>
					<li class="flex gap-2"><span class="text-blue-600">•</span> <span><strong>number</strong> - Numeric values</span></li>
					<li class="flex gap-2"><span class="text-blue-600">•</span> <span><strong>datetime</strong> - Date and time selection</span></li>
					<li class="flex gap-2"><span class="text-blue-600">•</span> <span><strong>boolean</strong> - Yes/No or true/false</span></li>
					<li class="flex gap-2"><span class="text-blue-600">•</span> <span><strong>select</strong> - Dropdown selection</span></li>
					<li class="flex gap-2"><span class="text-blue-600">•</span> <span><strong>textarea</strong> - Multi-line text</span></li>
				</ul>
			</div>

			<!-- Multiple Event Groups -->
			<div>
				<h3 class="text-sm font-bold text-gray-800 mb-2 flex items-center gap-2">
					<i class="fas fa-repeat text-blue-600"></i>
					Multiple-Event Groups
				</h3>
				<p class="text-xs text-gray-700 leading-relaxed">
					When enabled, this group can be repeated multiple times during a single study event. Useful for collecting the same set of data multiple times (e.g., multiple MRI scans).
				</p>
			</div>

			<!-- Quick Tips -->
			<div class="bg-white rounded p-3 border border-gray-200">
				<h4 class="text-xs font-semibold text-gray-800 mb-2 flex items-center gap-2">
					<i class="fas fa-lightbulb text-yellow-500"></i>
					Quick Tips
				</h4>
				<ul class="text-xs text-gray-700 space-y-1">
					<li class="flex gap-2">
						<span class="text-blue-600">→</span>
						<span>Give clear, descriptive names to groups</span>
					</li>
					<li class="flex gap-2">
						<span class="text-blue-600">→</span>
						<span>Use consistent naming patterns for API identifiers</span>
					</li>
					<li class="flex gap-2">
						<span class="text-blue-600">→</span>
						<span>Add meaningful descriptions for documentation</span>
					</li>
					<li class="flex gap-2">
						<span class="text-blue-600">→</span>
						<span>Test API identifiers before finalizing</span>
					</li>
				</ul>
			</div>
		</div>
	</div>
</div>

<!-- Add/Edit Group Modal -->
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

				<!-- Group Description -->
				<div>
					<label class="block text-sm font-medium text-gray-700 mb-1">Group Description</label>
					<textarea
						bind:value={formData.description}
						placeholder="Enter small description"
						rows="3"
						class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 text-sm"
					></textarea>
					<p class="text-xs text-gray-500 mt-1">It is generated automatically based on the name and will appear in the API responses</p>
				</div>

				<!-- Is this a Multiple-Event Group? -->
				<div>
					<label class="block text-sm font-medium text-gray-700 mb-3">Is this a Multiple-Event Group?</label>
					<div class="flex items-center gap-6">
						<div class="flex items-center">
							<input
								type="radio"
								id="multiYes"
								name="multipleEventGroup"
								value={true}
								bind:group={formData.isMultipleEventGroup}
								class="w-4 h-4 text-blue-600"
							/>
							<label for="multiYes" class="ml-2 text-sm text-gray-700">Yes</label>
						</div>
						<div class="flex items-center">
							<input
								type="radio"
								id="multiNo"
								name="multipleEventGroup"
								value={false}
								bind:group={formData.isMultipleEventGroup}
								class="w-4 h-4 text-gray-600"
							/>
							<label for="multiNo" class="ml-2 text-sm text-gray-700">No</label>
						</div>
					</div>
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
