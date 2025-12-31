<script lang="ts">
	export let instrument: any = null;
	export let onClose: () => void = () => {};

	interface FormField {
		id: number;
		fieldName: string;
		fieldLabel: string;
		fieldType: string;
		required: boolean;
	}

	let fields: FormField[] = instrument?.fields || [];
	let showAddFieldModal = false;
	let newFieldLabel = '';
	let newFieldName = '';
	let newFieldType = 'text';

	const addField = () => {
		const field: FormField = {
			id: Math.max(...fields.map(f => f.id), 0) + 1,
			fieldName: newFieldName || `field_${Date.now()}`,
			fieldLabel: newFieldLabel,
			fieldType: newFieldType,
			required: false
		};
		fields = [...fields, field];
		newFieldLabel = '';
		newFieldName = '';
		newFieldType = 'text';
		showAddFieldModal = false;
	};

	const deleteField = (id: number) => {
		fields = fields.filter(f => f.id !== id);
	};

	const moveFieldUp = (index: number) => {
		if (index > 0) {
			[fields[index], fields[index - 1]] = [fields[index - 1], fields[index]];
			fields = fields;
		}
	};

	const moveFieldDown = (index: number) => {
		if (index < fields.length - 1) {
			[fields[index], fields[index + 1]] = [fields[index + 1], fields[index]];
			fields = fields;
		}
	};

	const getFieldIcon = (type: string) => {
		switch (type) {
			case 'text':
				return 'fa-align-left';
			case 'number':
				return 'fa-hashtag';
			case 'date':
				return 'fa-calendar';
			case 'radio':
				return 'fa-circle';
			case 'checkbox':
				return 'fa-check-square';
			case 'dropdown':
				return 'fa-list';
			default:
				return 'fa-file';
		}
	};
</script>

<div class="fixed inset-0 bg-black bg-opacity-40 flex items-start justify-center z-50 pt-6 pb-6 overflow-y-auto">
	<div class="bg-white shadow-lg w-full max-w-4xl">
		<!-- Header -->
		<div class="bg-gray-50 border-b border-gray-300 p-4 flex items-center justify-between">
			<div>
				<button on:click={onClose} class="px-3 py-2 bg-blue-600 text-white rounded text-sm font-medium hover:bg-blue-700 flex items-center gap-2">
					<i class="fas fa-arrow-left"></i>
					Return to list of instruments
				</button>
			</div>
			<button on:click={onClose} class="text-gray-500 hover:text-gray-700 text-xl" title="Close editor" aria-label="Close editor">
				<i class="fas fa-times"></i>
			</button>
		</div>

		<!-- Content -->
		<div class="p-6 space-y-6">
			<!-- Info Section -->
			<div class="bg-blue-50 border border-blue-200 rounded p-4">
			<p class="text-sm text-gray-700 leading-relaxed">
				This page allows you to build and customize your data collection instruments one field at a time. You may add new fields or edit existing ones. New fields may be added by clicking the <span class="font-semibold">Add Field</span> buttons. You can begin editing an existing field by clicking on the <span class="font-semibold"><i class="fas fa-pen"></i> Edit</span> icon. If you decide that you do not want to keep a field, you can simply delete it by clicking on the <span class="font-semibold"><i class="fas fa-times text-red-500"></i> Delete</span> icon. To reorder the fields, simply drag and drop a field to a different position within the form below. NOTE: While in development status, all field changes will take effect immediately in real time.
			</p>
				<div class="mt-4 flex flex-wrap gap-2">
					<span class="px-2 py-1 bg-green-100 text-green-700 rounded text-xs font-medium flex items-center gap-1">
						<i class="fas fa-check-circle"></i>Smart Variables
					</span>
					<span class="px-2 py-1 bg-blue-100 text-blue-700 rounded text-xs font-medium flex items-center gap-1">
						<i class="fas fa-code-branch"></i>Piping
					</span>
					<span class="px-2 py-1 bg-red-100 text-red-700 rounded text-xs font-medium flex items-center gap-1">
						<i class="fas fa-tag"></i>Action Tags
					</span>
					<span class="px-2 py-1 bg-yellow-100 text-yellow-700 rounded text-xs font-medium flex items-center gap-1">
						<i class="fas fa-layer-group"></i>Field Embedding
					</span>
					<span class="px-2 py-1 bg-blue-100 text-blue-700 rounded text-xs font-medium flex items-center gap-1">
						<i class="fas fa-bolt"></i>Special Functions
					</span>
				</div>
			</div>

			<!-- Current Instrument -->
			<div>
				<div class="flex items-center justify-between mb-4">
					<h2 class="text-lg font-bold text-gray-800">Current instrument: <span class="text-red-600">{instrument?.name}</span></h2>
					<button class="px-3 py-2 bg-gray-400 text-white rounded text-sm hover:bg-gray-500">
						Preview instrument
					</button>
				</div>

				<!-- Action Buttons -->
				<div class="flex gap-2 mb-6 border-b border-gray-300 pb-4">
					<button class="px-3 py-2 bg-blue-600 text-white rounded text-xs font-medium hover:bg-blue-700">
						Add Field
					</button>
					<button class="px-3 py-2 bg-blue-600 text-white rounded text-xs font-medium hover:bg-blue-700">
						Add Matrix of Fields
					</button>
					<button class="px-3 py-2 bg-blue-600 text-white rounded text-xs font-medium hover:bg-blue-700">
						Import from Field Bank
					</button>
				</div>

				<!-- Fields List -->
				<div class="space-y-4">
					{#each fields as field, index (field.id)}
						<div class="bg-gray-50 border border-gray-300 rounded p-4">
							<div class="flex items-start gap-3">
								<!-- Drag Handle -->
								<div class="flex flex-col gap-1">
									<button on:click={() => moveFieldUp(index)} class="text-gray-400 hover:text-gray-600" title="Move up">
										<i class="fas fa-chevron-up text-xs"></i>
									</button>
									<i class="fas fa-ellipsis-v text-gray-400 text-xs"></i>
									<button on:click={() => moveFieldDown(index)} class="text-gray-400 hover:text-gray-600" title="Move down">
										<i class="fas fa-chevron-down text-xs"></i>
									</button>
								</div>

								<!-- Field Info -->
								<div class="flex-1">
									<div class="flex items-start gap-3">
										<!-- Icons -->
										<div class="flex gap-1 pt-1">
											<button class="text-orange-500 hover:text-orange-700 text-sm" title="Edit">
												<i class="fas fa-pen"></i>
											</button>
											<button class="text-green-500 hover:text-green-700 text-sm" title="Copy">
												<i class="fas fa-copy"></i>
											</button>
											<button class="text-blue-500 hover:text-blue-700 text-sm" title="Branching">
												<i class="fas fa-code-branch"></i>
											</button>
											<button class="text-gray-500 hover:text-gray-700 text-sm" title="Lock">
												<i class="fas fa-lock"></i>
											</button>
											<button class="text-red-500 hover:text-red-700 text-sm" on:click={() => deleteField(field.id)} title="Delete">
												<i class="fas fa-times"></i>
											</button>
										</div>

										<!-- Field Details -->
										<div class="flex-1">
											<p class="text-xs text-gray-600 italic">Variable: {field.fieldName}</p>
											<h3 class="text-base font-bold text-gray-900 mb-3">{field.fieldLabel}</h3>
											
											<!-- Field Type Input -->
											<div class="bg-white border border-gray-300 rounded p-3 min-h-20">
												{#if field.fieldType === 'date'}
													<input type="text" class="w-full border border-gray-300 rounded px-2 py-1 text-sm" />
													<div class="flex gap-2 mt-2 text-xs">
														<button class="px-2 py-1 bg-gray-200 hover:bg-gray-300 rounded">Today</button>
														<button class="px-2 py-1 bg-gray-200 hover:bg-gray-300 rounded">M-D-Y</button>
													</div>
												{:else if field.fieldType === 'text'}
													<textarea class="w-full border border-gray-300 rounded px-2 py-1 text-sm" rows="2"></textarea>
												{:else if field.fieldType === 'radio' || field.fieldType === 'checkbox'}
													<div class="space-y-2">
														<div class="flex items-center gap-2">
															<input type="radio" id="opt1" name={`field_${field.id}`} class="w-4 h-4" />
															<label for="opt1" class="text-sm">Option 1</label>
														</div>
														<div class="flex items-center gap-2">
															<input type="radio" id="opt2" name={`field_${field.id}`} class="w-4 h-4" />
															<label for="opt2" class="text-sm">Option 2</label>
														</div>
													</div>
												{:else}
													<input type="text" class="w-full border border-gray-300 rounded px-2 py-1 text-sm" />
												{/if}
											</div>

											<!-- Field Actions -->
											<div class="flex gap-2 mt-3 border-t border-gray-300 pt-3">
												<button class="px-2 py-1 bg-blue-600 text-white rounded text-xs font-medium hover:bg-blue-700">
													Add Field
												</button>
												<button class="px-2 py-1 bg-blue-600 text-white rounded text-xs font-medium hover:bg-blue-700">
													Add Matrix of Fields
												</button>
												<button class="px-2 py-1 bg-blue-600 text-white rounded text-xs font-medium hover:bg-blue-700">
													Import from Field Bank
												</button>
											</div>
										</div>
									</div>
								</div>
							</div>
						</div>
					{/each}
				</div>

				<!-- Add Field Section -->
				<div class="mt-6 flex gap-2 border-t border-gray-300 pt-4">
					<button class="px-3 py-2 bg-blue-600 text-white rounded text-xs font-medium hover:bg-blue-700">
						Add Field
					</button>
					<button class="px-3 py-2 bg-blue-600 text-white rounded text-xs font-medium hover:bg-blue-700">
						Add Matrix of Fields
					</button>
					<button class="px-3 py-2 bg-blue-600 text-white rounded text-xs font-medium hover:bg-blue-700">
						Import from Field Bank
					</button>
				</div>
			</div>

			<!-- Right Sidebar Info -->
			<div class="absolute right-6 top-32 w-60 bg-white border border-gray-300 rounded p-4 shadow-md">
				<h3 class="text-sm font-bold text-gray-900 mb-3">
					<i class="fas fa-lightbulb text-blue-500 mr-2"></i>How to embed a field elsewhere
				</h3>
				<p class="text-xs text-gray-700 leading-relaxed mb-3">
					Learn how to customize your instrument or survey by using <button class="text-blue-600 hover:underline bg-transparent border-0 cursor-pointer p-0">Field Embedding</button>.
				</p>
				
				<h3 class="text-sm font-bold text-gray-900 mb-3 pt-3 border-t border-gray-300">
					<i class="fas fa-lightbulb text-blue-500 mr-2"></i>How to modify multiple fields together
				</h3>
				<p class="text-xs text-gray-700 leading-relaxed">
					Learn how to quickly modify your fields by editing a <button class="text-blue-600 hover:underline bg-transparent border-0 cursor-pointer p-0">matrix of fields</button>.
				</p>
			</div>
		</div>
	</div>
</div>

<style>
	:global(body) {
		overflow: hidden;
	}
</style>
