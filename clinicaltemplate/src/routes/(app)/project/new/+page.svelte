<script lang="ts">
	import { goto } from '$app/navigation';
	import { PROJECT_DETAIL_SETUP_ROUTE, PROJECT_SETUP_ROUTE, PROJECTS_ROUTE, ROOT_ROUTE } from '$lib/enums/routes';
	let projectTitle = $state('');
	let projectPurpose = $state('');
	let projectNotes = $state('');
	let assignFolder = $state(false);
	let piFirstName = $state('');
	let piMiddleName = $state('');
	let piLastName = $state('');
	let piEmail = $state('');
	let piPublicationName = $state('');
	let irbNumber = $state('');
	let researchTypes = $state({
		basic: false,
		clinical: false,
		translational1: false,
		translational2: false,
		behavioral: false,
		epidemiology: false,
		repository: false,
		other: false
	});

	let startProjectType: 'empty' | 'upload' | 'template' = $state('empty');
	let selectedTemplate: string | null = $state(null);

	const templates = [
		{
			id: 'basic-demography',
			title: 'Basic Demography',
			description: 'Contains a single data collection instrument to capture basic demographic information.'
		},
		{
			id: 'camh-dictionary',
			title: 'CAMH Data Dictionary',
			description:
				'Collaborative effort of CAMH researchers Contains a lot of measures used in CAMH studies for internal use only'
		},
		{
			id: 'classic-database',
			title: 'Classic Database',
			description:
				'Contains six data entry forms, including forms for demography and baseline data, three monthly data forms, and concludes with a completion data form.'
		},
		{
			id: 'common-elements',
			title: 'Common Data Elements',
			description:
				'Contains: Subject Enrollment and Informed Consent, Demographic Form, QIDS-SR, GAD7, PSQI, WHOQOL, Sheehan Disability, Standard values codes and formats for common response categories.'
		}
	];

	const purposes = [
		'--- Select One ---',
		'Practice / Just for fun',
		'Operational Support',
		'Research',
		'Quality Improvement',
		'Other'
	];

	// Check if PI information should be visible
	let showPISection = $derived(projectPurpose && projectPurpose !== '--- Select One ---');
	
	// Check if Research Type section should be visible
	let showResearchTypes = $derived(projectPurpose === 'Research');

	const researchTypeLabels = {
		basic: 'Basic or bench research',
		clinical: 'Clinical research study or trial',
		translational1: 'Translational research 1 (applying discoveries to the development of trials and studies in humans)',
		translational2: 'Translational research 2 (enhancing adoption of research findings and best practices into the community)',
		behavioral: 'Behavioral or psychosocial research study',
		epidemiology: 'Epidemiology',
		repository: 'Repository (developing a data or specimen repository for future use by investigators)',
		other: 'Other'
	};

	function handleCreateProject(): void {
		// Validate required fields
		if (!projectTitle.trim()) {
			alert('Project title is required');
			return;
		}

		if (!projectPurpose || projectPurpose === '--- Select One ---') {
			alert('Please select a project purpose');
			return;
		}

		// Log form data
		console.log('Creating project with:', {
			projectTitle,
			projectPurpose,
			projectNotes,
			assignFolder,
			pi: {
				firstName: piFirstName,
				middleName: piMiddleName,
				lastName: piLastName,
				email: piEmail,
				publicationName: piPublicationName,
				irbNumber
			},
			researchTypes: Object.keys(researchTypes).filter(key => researchTypes[key]),
			startProjectType,
			selectedTemplate
		});
        goto(PROJECT_DETAIL_SETUP_ROUTE.replace(':projectId', 'newly-created-id'));
		alert('Project created successfully! (Check console for details)');
	}

	function handleCancel(): void {
		if (confirm('Are you sure you want to cancel? Any unsaved changes will be lost.')) {
			window.history.back();
		}
	}
</script>

<div class="min-h-screen page-bg">
	 

	<div class="p-4 md:p-8">
		<div class="max-w-5xl mx-auto">
			<!-- Header -->
			<div class="mb-6">
				<h2 class="text-2xl font-bold mb-1 section-heading">
					<i class="fas fa-plus mr-2"></i>Create a new REDCap Project
				</h2>
				<p class="text-sm form-label">
					You may begin the creation of a new REDCap project on your own by completing the form below and clicking the Create Project button at the bottom.
				</p>
			</div>

		<!-- Main Form Card -->
		<div class="rounded-lg shadow-sm overflow-hidden form-card">
			<!-- Basic Information Section -->
			<div class="p-8 border-b form-section">
				<h2 class="text-lg font-bold mb-8 section-heading">
					<i class="fas fa-info-circle mr-2"></i>Basic Information
				</h2>

				<div class="grid grid-cols-1 md:grid-cols-2 gap-8">
					<!-- Project Title -->
					<div>
						<label for="projectTitle" class="block text-sm font-semibold mb-2 form-label">
							Project title
						</label>
						<input
							id="projectTitle"
							type="text"
							bind:value={projectTitle}
							placeholder="e.g., REDCap Basics 2019"
							class="w-full px-4 py-2 border rounded-md focus:outline-none text-sm form-input"
						/>
						<p class="text-xs mt-1 helper-text">Title to be displayed on project webpage</p>
					</div>

					<!-- Purpose of Project -->
					<div>
						<label for="projectPurpose" class="block text-sm font-semibold mb-2 form-label">
							Purpose of this project
						</label>
						<select
							id="projectPurpose"
							bind:value={projectPurpose}
							class="w-full px-4 py-2 border rounded-md focus:outline-none bg-white text-sm form-select"
						>
							{#each purposes as purpose}
								<option value={purpose}>{purpose}</option>
							{/each}
						</select>
						<p class="text-xs mt-1 italic helper-text">How will it be used?</p>
					</div>
				</div>

				<!-- Project Notes - Full Width -->
				<div class="mt-6">
					<label for="projectNotes" class="block text-sm font-semibold mb-2 form-label">
						Project notes (optional)
					</label>
					<textarea
						id="projectNotes"
						bind:value={projectNotes}
						placeholder="Comments describing the project's use or purpose that are displayed on the My Projects page."
						rows="3"
						class="w-full px-4 py-2 border rounded-md focus:outline-none resize-none text-sm form-textarea"
					></textarea>
				</div>

				<!-- Assign to Folder -->
				<div class="mt-4 flex items-center gap-3">
					<input
						id="assignFolder"
						type="checkbox"
						bind:checked={assignFolder}
						class="w-4 h-4 rounded cursor-pointer border"
					/>
					<label for="assignFolder" class="text-sm font-semibold cursor-pointer form-label">
						Assign project to a Project Folder?
					</label>
				</div>
			</div>

			<!-- Principal Investigator Section (Conditional) -->
			{#if showPISection}
				<div class="p-8 border-b animate-in fade-in duration-300 form-section">
					<h2 class="text-lg font-bold mb-8 section-heading">
						<i class="fas fa-user mr-2"></i>Principal Investigator Information
					</h2>

					<div class="grid grid-cols-1 md:grid-cols-2 gap-8">
						<!-- PI Name -->
						<div>
							<label class="block text-sm font-semibold mb-2 form-label">Name of P.I. (if applicable)</label>
							<div class="grid grid-cols-3 gap-2">
								<input
									type="text"
									bind:value={piFirstName}
									placeholder="First"
									class="px-3 py-2 border rounded-md focus:outline-none text-sm form-input"
								/>
								<input
									type="text"
									bind:value={piMiddleName}
									placeholder="MI"
									maxlength="2"
									class="px-3 py-2 border rounded-md focus:outline-none text-sm form-input"
								/>
								<input
									type="text"
									bind:value={piLastName}
									placeholder="Last"
									class="px-3 py-2 border rounded-md focus:outline-none text-sm form-input"
								/>
							</div>
							<div class="grid grid-cols-3 gap-2 mt-1 text-xs text-center helper-text">
								<span>First name</span>
								<span>MI</span>
								<span>Last name</span>
							</div>
						</div>

						<!-- PI Email -->
						<div>
							<label for="piEmail" class="block text-sm font-semibold mb-2 form-label">
								Email of P.I. (if applicable)
							</label>
							<input
								id="piEmail"
								type="email"
								bind:value={piEmail}
								class="w-full px-4 py-2 border rounded-md focus:outline-none text-sm form-input"
							/>
						</div>

						<!-- PI Publication Name -->
						<div>
							<label for="piPublicationName" class="block text-sm font-semibold mb-2 form-label">
								Name of P.I. as cited in publications (if applicable)
							</label>
							<div class="flex gap-2 items-start">
								<input
									id="piPublicationName"
									type="text"
									bind:value={piPublicationName}
									placeholder="e.g., Harris PA"
									class="flex-1 px-4 py-2 border rounded-md focus:outline-none text-sm form-input"
								/>
								<span class="text-xs mt-2 helper-text">(e.g., Harris PA)</span>
							</div>
						</div>

						<!-- IRB Number -->
						<div>
							<label for="irbNumber" class="block text-sm font-semibold mb-2 form-label">
								IRB number (if applicable)
							</label>
							<input
								id="irbNumber"
								type="text"
								bind:value={irbNumber}
								class="w-full px-4 py-2 border rounded-md focus:outline-none text-sm form-input"
							/>
						</div>
					</div>
				</div>
			{/if}

			<!-- Research Type Section (Conditional) -->
			{#if showResearchTypes}
				<div class="p-8 border-b animate-in fade-in duration-300 form-section">
					<h2 class="text-lg font-bold mb-8 section-heading">
						<i class="fas fa-flask mr-2"></i>Research Type
					</h2>

					<label class="block text-sm font-semibold mb-4 form-label">
						Please specify:
					</label>
					<div class="grid grid-cols-1 md:grid-cols-2 gap-3">
						{#each Object.entries(researchTypeLabels) as [key, label]}
							<label class="flex items-start gap-3 p-2 cursor-pointer hover:bg-gray-50 rounded transition-colors">
								<input
									type="checkbox"
									bind:checked={researchTypes[key]}
									class="w-4 h-4 rounded cursor-pointer shrink-0 mt-0.5 border"
								/>
								<span class="text-sm form-label">{label}</span>
							</label>
						{/each}
					</div>
				</div>
			{/if}

			<!-- Project Start Section -->
			<div class="p-8 border-b form-section">
				<h2 class="text-lg font-bold mb-8 section-heading">
					<i class="fas fa-rocket mr-2"></i>Start Project
				</h2>

				<p class="text-sm font-semibold mb-6 form-label">Start project from scratch or begin with a template?</p>

				<div class="space-y-4 mb-6">
					<!-- Option 1: Empty Project -->
					<label class="flex items-center gap-3 p-3 border rounded-md cursor-pointer hover:bg-gray-50 transition-colors radio-option" class:selected={startProjectType === 'empty'} class:border-2={startProjectType === 'empty'}>
						<input
							type="radio"
							name="startProjectType"
							value="empty"
							onchange={() => (startProjectType = 'empty')}
							checked={startProjectType === 'empty'}
							class="w-4 h-4 cursor-pointer border"
						/>
						<div>
							<p class="font-semibold text-sm form-label">Create an empty project (blank slate)</p>
							<p class="text-xs helper-text">Start with a clean slate and build your project from scratch</p>
						</div>
					</label>

					<!-- Option 2: Upload XML -->
					<label class="flex items-center gap-3 p-3 border rounded-md cursor-pointer hover:bg-gray-50 transition-colors radio-option" class:selected={startProjectType === 'upload'} class:border-2={startProjectType === 'upload'}>
						<input
							type="radio"
							name="startProjectType"
							value="upload"
							onchange={() => (startProjectType = 'upload')}
							checked={startProjectType === 'upload'}
							class="w-4 h-4 cursor-pointer border"
						/>
						<div>
							<p class="font-semibold text-sm form-label">Upload a REDCap project XML file (CDISC ODM format)</p>
							<p class="text-xs helper-text">Import configuration from an existing REDCap project file</p>
						</div>
					</label>

					<!-- Option 3: Use Template -->
					<label class="flex items-center gap-3 p-3 border rounded-md cursor-pointer hover:bg-gray-50 transition-colors radio-option" class:selected={startProjectType === 'template'} class:border-2={startProjectType === 'template'}>
						<input
							type="radio"
							name="startProjectType"
							value="template"
							onchange={() => (startProjectType = 'template')}
							checked={startProjectType === 'template'}
							class="w-4 h-4 cursor-pointer border"
						/>
						<div>
							<p class="font-semibold text-sm form-label">Use a template (choose one below)</p>
							<p class="text-xs helper-text">Start with a pre-built template with sample fields and forms</p>
						</div>
					</label>
				</div>

				<!-- Upload Section -->
				{#if startProjectType === 'upload'}
					<div class="p-4 border rounded-md mb-6 animate-in fade-in duration-300 upload-section">
						<label class="block">
							<span class="text-sm font-semibold mb-2 block form-label">Choose XML file to upload</span>
							<input
								type="file"
								accept=".xml"
								class="w-full px-4 py-2 border rounded-md focus:outline-none cursor-pointer text-sm form-input"
							/>
						</label>
						<p class="text-xs mt-2 helper-text">
							<i class="fas fa-info-circle mr-2"></i>Only CDISC ODM format XML files are supported
						</p>
					</div>
				{/if}

				<!-- Template Selection -->
				{#if startProjectType === 'template'}
					<div class="animate-in fade-in duration-300 p-4 border rounded-md template-section">
						<p class="text-sm font-semibold mb-3 form-label">
							<i class="fas fa-star text-pink-500 mr-2"></i>Choose a project template
						</p>
						<p class="text-xs mb-4 helper-text">(comes pre-filled with fields, forms/surveys, and other settings)</p>

						<!-- Template List -->
						<div class="space-y-2">
							{#each templates as template}
								<label class="flex items-start gap-3 p-3 border rounded-md cursor-pointer hover:bg-white transition-colors bg-white template-item" class:selected={selectedTemplate === template.id} class:border-2={selectedTemplate === template.id}>
									<input
										type="radio"
										name="template"
										value={template.id}
										onchange={() => (selectedTemplate = template.id)}
										checked={selectedTemplate === template.id}
										class="w-4 h-4 cursor-pointer mt-0.5 shrink-0 border"
									/>
									<div class="flex-1">
										<p class="text-sm font-medium" style="color: #EC4899;">{template.title}</p>
										<p class="text-xs mt-1 helper-text">{template.description}</p>
									</div>
								</label>
							{/each}
						</div>
					</div>
				{/if} 
			</div>
 
			<!-- Action Buttons -->
			<div class="p-8 border-t flex justify-end gap-3 action-buttons">
				<button
					onclick={handleCancel}
					class="px-6 py-2 border font-semibold rounded-md hover:opacity-80 transition-all text-sm btn-cancel"
				>
					Cancel
				</button>
				<button
					onclick={handleCreateProject}
					class="btn btn-primary"
				>
					CREATE PROJECT
				</button>
                  
			</div>
		</div>
		</div>
	</div>
</div>

<style>
	:global(body) {
		background-color: #F4F7FC;
	}
	
	:global(.page-bg) {
		background-color: #F4F7FC;
	}
	
	:global(.title-bar) {
		border-color: #E5E7EB;
	}
	
	:global(.page-title) {
		color: #3E4A60;
	}
	
	:global(.nav-text) {
		color: #3E4A60;
	}
	
	:global(.nav-link) {
		color: #032D7B;
	}
	
	:global(.nav-separator) {
		color: #9CA3AF;
	}
	
	:global(.section-heading) {
		color: #032D7B;
	}
	
	:global(.form-label) {
		color: #3E4A60;
	}
	
	:global(.form-input),
	:global(.form-select),
	:global(.form-textarea) {
		border-color: #E5E7EB;
		color: #3E4A60;
	}
	
	:global(.form-input:focus),
	:global(.form-select:focus),
	:global(.form-textarea:focus) {
		border-color: #4C5FD6 !important;
		box-shadow: 0 0 0 1px #4C5FD6 !important;
	}
	
	:global(.helper-text) {
		color: #9CA3AF;
	}
	
	:global(.form-card) {
		background-color: #FFFFFF;
		border: 1px solid #E5E7EB;
	}
	
	:global(.form-section) {
		border-color: #E5E7EB;
	}
	
	:global(input[type="checkbox"]),
	:global(input[type="radio"]) {
		accent-color: #032D7B;
		border-color: #E5E7EB;
	}
	
	:global(.radio-option) {
		border-color: #E5E7EB;
	}
	
	:global(.radio-option.selected) {
		border-color: #4C5FD6;
		background-color: #F0F4FF;
	}
	
	:global(.upload-section),
	:global(.template-section) {
		background-color: #F0F4FF;
		border-color: #4C5FD6;
	}
	
	:global(.template-item) {
		border-color: #E5E7EB;
	}
	
	:global(.template-item.selected) {
		border-color: #EC4899;
		background-color: #F9E6F0;
	}
	
	:global(.template-item p) {
		color: #EC4899;
	}
	
	:global(.action-buttons) {
		background-color: #F0F4FF;
		border-color: #E5E7EB;
	}
	
	:global(.btn-cancel) {
		border-color: #E5E7EB;
		color: #3E4A60;
	}
	
	:global(.btn-primary) {
		background-color: #032D7B;
		color: #FFFFFF;
	}
	
	:global(.btn-primary:hover) {
		opacity: 0.9;
	}
	
	:global(input[type="text"]:focus),
	:global(input[type="email"]:focus),
	:global(textarea:focus),
	:global(select:focus) {
		border-color: #4C5FD6 !important;
		box-shadow: 0 0 0 1px #4C5FD6 !important;
	}
	
	@keyframes fadeIn {
		from {
			opacity: 0;
		}
		to {
			opacity: 1;
		}
	}
	
	:global(.animate-in) {
		animation: fadeIn 0.3s ease-in-out;
	}
	
	:global(.fade-in) {
		animation: fadeIn 0.3s ease-in-out;
	}
	
	:global(.duration-300) {
		animation-duration: 0.3s;
	}
</style>
