<script lang="ts">
	import { enhance } from '$app/forms';

	let { form } = $props();

	let projectTitle = $state('');
	let projectPurpose = $state('');
	let projectNotes = $state('');
	let assignToFolder = $state(false);
	let startOption = $state('empty');
	let loading = $state(false);

	// Principal Investigator fields
	let piFirstName = $state('');
	let piMiddleInitial = $state('');
	let piLastName = $state('');
	let piEmail = $state('');
	let piPublicationName = $state('');
	let irbNumber = $state('');

	// Research Type
	let researchType = $state('');

	// File upload
	let xmlFile: File | null = $state(null);

	// Template selection
	let selectedTemplate = $state('');

	function handleSubmit() {
		loading = true;
	}

	function handleFileChange(event: Event) {
		const input = event.target as HTMLInputElement;
		if (input.files && input.files[0]) {
			xmlFile = input.files[0];
		}
	}
</script>

<div class="container mx-auto px-4 py-8 max-w-4xl">
	<!-- Page Header -->
	<div class="mb-6">
		<h1 class="text-2xl font-bold text-primary mb-2">
			<span class="text-3xl mr-2">+</span> Create a new REDCap Project
		</h1>
		<p class="text-sm text-gray-600">
			You may begin the creation of a new REDCap project on your own by completing the form below
			and clicking the Create Project button at the bottom.
		</p>
	</div>

	<!-- Main Form Card -->
	<form
		method="POST"
		action="?/createProject"
		use:enhance
		onsubmit={handleSubmit}
		class="space-y-6"
	>
		<!-- Basic Information Section -->
		<div class="card bg-white shadow">
			<div class="card-body">
				<h2 class="text-lg text-primary mb-4 flex items-center gap-2">
					<svg
						xmlns="http://www.w3.org/2000/svg"
						fill="none"
						viewBox="0 0 24 24"
						stroke-width="1.5"
						stroke="currentColor"
						class="w-5 h-5"
					>
						<path
							stroke-linecap="round"
							stroke-linejoin="round"
							d="M11.25 11.25l.041-.02a.75.75 0 011.063.852l-.708 2.836a.75.75 0 001.063.853l.041-.021M21 12a9 9 0 11-18 0 9 9 0 0118 0zm-9-3.75h.008v.008H12V8.25z"
						/>
					</svg>
					Basic Information
				</h2>

				<div class="grid grid-cols-1 md:grid-cols-2 gap-6">
					<!-- Project Title -->
					<div class="form-control">
						<label class="label" for="projectTitle">
							<span class="label-text font-medium">Project title</span>
						</label>
						<input
							id="projectTitle"
							type="text"
							name="projectTitle"
							placeholder="e.g., REDCap Basics 2019"
							bind:value={projectTitle}
							class="input input-bordered w-full"
							required
						/>
						<label class="label">
							<span class="label-text-alt text-gray-500"
								>Title to be displayed on project webpage</span
							>
						</label>
					</div>

					<!-- Purpose of Project -->
					<div class="form-control">
						<label class="label" for="projectPurpose">
							<span class="label-text font-medium">Purpose of this project</span>
						</label>
						<select
							id="projectPurpose"
							name="projectPurpose"
							bind:value={projectPurpose}
							class="select select-bordered w-full"
							required
						>
							<option value="" disabled selected></option>
							<option value="practice">Practice / Just for fun</option>
							<option value="operational">Operational Support</option>
							<option value="research">Research</option>
							<option value="quality">Quality Improvement</option>
							<option value="other">Other</option>
						</select>
						<label class="label">
							<span class="label-text-alt text-gray-500">How will it be used?</span>
						</label>
					</div>
				</div>

				<!-- Project Notes -->
				<div class="form-control mt-4">
					<label class="label" for="projectNotes">
						<span class="label-text font-medium">Project notes (optional)</span>
					</label>
					<textarea
						id="projectNotes"
						name="projectNotes"
						placeholder="Comments describing the project's use or purpose that are displayed on the My Projects page."
						bind:value={projectNotes}
						class="textarea textarea-bordered h-24 w-full"
					></textarea>
				</div>

				<!-- Assign to Folder -->
				<div class="form-control mt-4">
					<label class="label cursor-pointer justify-start gap-3">
						<input
							type="checkbox"
							name="assignToFolder"
							bind:checked={assignToFolder}
							class="checkbox checkbox-sm"
						/>
						<span class="label-text">Assign project to a Project Folder?</span>
					</label>
				</div>
			</div>
		</div>

		<!-- Principal Investigator Information (shown only for Research) -->
		{#if projectPurpose === 'research'}
			<div class="card bg-white shadow">
				<div class="card-body">
					<h2 class="text-lg text-primary mb-4 flex items-center gap-2">
						<svg
							xmlns="http://www.w3.org/2000/svg"
							fill="none"
							viewBox="0 0 24 24"
							stroke-width="1.5"
							stroke="currentColor"
							class="w-5 h-5"
						>
							<path
								stroke-linecap="round"
								stroke-linejoin="round"
								d="M15.75 6a3.75 3.75 0 11-7.5 0 3.75 3.75 0 017.5 0zM4.501 20.118a7.5 7.5 0 0114.998 0A17.933 17.933 0 0112 21.75c-2.676 0-5.216-.584-7.499-1.632z"
							/>
						</svg>
						Principal Investigator Information
					</h2>

					<div class="grid grid-cols-1 md:grid-cols-2 gap-6">
						<!-- PI Name -->
						<div class="form-control">
							<label class="label" for="piFirstName">
								<span class="label-text font-medium">Name of P.I. (if applicable)</span>
							</label>
							<div class="grid grid-cols-6 gap-2">
								<input
									id="piFirstName"
									type="text"
									name="piFirstName"
									placeholder="First"
									bind:value={piFirstName}
									class="input input-bordered input-sm col-span-2"
								/>
								<input
									type="text"
									name="piMiddleInitial"
									placeholder="MI"
									bind:value={piMiddleInitial}
									class="input input-bordered input-sm col-span-1"
									maxlength="2"
								/>
								<input
									type="text"
									name="piLastName"
									placeholder="Last"
									bind:value={piLastName}
									class="input input-bordered input-sm col-span-3"
								/>
							</div>
							<label class="label">
								<span class="label-text-alt text-gray-500">First name</span>
								<span class="label-text-alt text-gray-500">MI</span>
								<span class="label-text-alt text-gray-500">Last name</span>
							</label>
						</div>

						<!-- PI Email -->
						<div class="form-control">
							<label class="label" for="piEmail">
								<span class="label-text font-medium">Email of P.I. (if applicable)</span>
							</label>
							<input
								id="piEmail"
								type="email"
								name="piEmail"
								bind:value={piEmail}
								class="input input-bordered w-full"
							/>
						</div>

						<!-- PI Publication Name -->
						<div class="form-control">
							<label class="label" for="piPublicationName">
								<span class="label-text font-medium"
									>Name of P.I., as cited in publications (if applicable)</span
								>
							</label>
							<input
								id="piPublicationName"
								type="text"
								name="piPublicationName"
								placeholder="e.g., Harris PA"
								bind:value={piPublicationName}
								class="input input-bordered w-full"
							/>
						</div>

						<!-- IRB Number -->
						<div class="form-control">
							<label class="label" for="irbNumber">
								<span class="label-text font-medium">IRB number (if applicable)</span>
							</label>
							<input
								id="irbNumber"
								type="text"
								name="irbNumber"
								placeholder="e.g., Harris PA"
								bind:value={irbNumber}
								class="input input-bordered w-full"
							/>
						</div>
					</div>
				</div>
			</div>

			<!-- Research Type -->
			<div class="card bg-white shadow">
				<div class="card-body">
					<h2 class="text-lg text-primary mb-4 flex items-center gap-2">
						<svg
							xmlns="http://www.w3.org/2000/svg"
							fill="none"
							viewBox="0 0 24 24"
							stroke-width="1.5"
							stroke="currentColor"
							class="w-5 h-5"
						>
							<path
								stroke-linecap="round"
								stroke-linejoin="round"
								d="M9.75 3.104v5.714a2.25 2.25 0 01-.659 1.591L5 14.5M9.75 3.104c-.251.023-.501.05-.75.082m.75-.082a24.301 24.301 0 014.5 0m0 0v5.714c0 .597.237 1.17.659 1.591L19.8 15.3M14.25 3.104c.251.023.501.05.75.082M19.8 15.3l-1.57.393A9.065 9.065 0 0112 15a9.065 9.065 0 00-6.23-.693L5 14.5m14.8.8l1.402 1.402c1.232 1.232.65 3.318-1.067 3.611A48.309 48.309 0 0112 21c-2.773 0-5.491-.235-8.135-.687-1.718-.293-2.3-2.379-1.067-3.61L5 14.5"
							/>
						</svg>
						Research Type
					</h2>

					<p class="text-sm text-gray-700 mb-4">Please specify:</p>

					<div class="grid grid-cols-1 md:grid-cols-2 gap-2">
						<label class="flex items-start gap-3 cursor-pointer">
							<input
								type="checkbox"
								name="researchType"
								value="basic"
								class="checkbox checkbox-sm mt-1"
							/>
							<span class="label-text">Basic or bench research</span>
						</label>

						<label class="flex items-start gap-3 cursor-pointer">
							<input
								type="checkbox"
								name="researchType"
								value="clinical"
								class="checkbox checkbox-sm mt-1"
							/>
							<span class="label-text">Clinical research study or trial</span>
						</label>

						<label class="flex items-start gap-3 cursor-pointer">
							<input
								type="checkbox"
								name="researchType"
								value="translational1"
								class="checkbox checkbox-sm mt-1"
							/>
							<span class="label-text text-sm"
								>Translational research 1 (applying discoveries to the development of trials and
								studies in humans)</span
							>
						</label>

						<label class="flex items-start gap-3 cursor-pointer">
							<input
								type="checkbox"
								name="researchType"
								value="translational2"
								class="checkbox checkbox-sm mt-1"
							/>
							<span class="label-text text-sm"
								>Translational research 2 (enhancing adoption of research findings and best
								practices into the community)</span
							>
						</label>

						<label class="flex items-start gap-3 cursor-pointer">
							<input
								type="checkbox"
								name="researchType"
								value="behavioral"
								class="checkbox checkbox-sm mt-1"
							/>
							<span class="label-text">Behavioral or psychosocial research study</span>
						</label>

						<label class="flex items-start gap-3 cursor-pointer">
							<input
								type="checkbox"
								name="researchType"
								value="epidemiology"
								class="checkbox checkbox-sm mt-1"
							/>
							<span class="label-text">Epidemiology</span>
						</label>

						<label class="flex items-start gap-3 cursor-pointer">
							<input
								type="checkbox"
								name="researchType"
								value="repository"
								class="checkbox checkbox-sm mt-1"
							/>
							<span class="label-text text-sm"
								>Repository (developing a data or specimen repository for future use by
								investigators)</span
							>
						</label>

						<label class="flex items-start gap-3 cursor-pointer">
							<input
								type="checkbox"
								name="researchType"
								value="other"
								class="checkbox checkbox-sm mt-1"
							/>
							<span class="label-text">Other</span>
						</label>
					</div>
				</div>
			</div>
		{/if}

		<!-- Start Project Section -->
		<div class="card bg-white shadow">
			<div class="card-body">
				<h2 class="text-lg text-primary mb-4 flex items-center gap-2">
					<svg
						xmlns="http://www.w3.org/2000/svg"
						fill="none"
						viewBox="0 0 24 24"
						stroke-width="1.5"
						stroke="currentColor"
						class="w-5 h-5"
					>
						<path
							stroke-linecap="round"
							stroke-linejoin="round"
							d="M15.59 14.37a6 6 0 01-5.84 7.38v-4.8m5.84-2.58a14.98 14.98 0 006.16-12.12A14.98 14.98 0 009.631 8.41m5.96 5.96a14.926 14.926 0 01-5.841 2.58m-.119-8.54a6 6 0 00-7.381 5.84h4.8m2.581-5.84a14.927 14.927 0 00-2.58 5.84m2.699 2.7c-.103.021-.207.041-.311.06a15.09 15.09 0 01-2.448-2.448 14.9 14.9 0 01.06-.312m-2.24 2.39a4.493 4.493 0 00-1.757 4.306 4.493 4.493 0 004.306-1.758M16.5 9a1.5 1.5 0 11-3 0 1.5 1.5 0 013 0z"
						/>
					</svg>
					Start Project
				</h2>

				<p class="text-sm text-gray-700 mb-4">
					Start project from scratch or begin with a template?
				</p>

				<div class="space-y-3">
					<!-- Empty Project Option -->
					<label
						class="flex items-start gap-3 p-4 border-2 rounded-lg cursor-pointer transition-colors hover:border-primary"
						class:border-primary={startOption === 'empty'}
						class:bg-primary={startOption === 'empty'}
						class:bg-opacity-5={startOption === 'empty'}
					>
						<input
							type="radio"
							name="startOption"
							value="empty"
							bind:group={startOption}
							class="radio radio-primary mt-1"
						/>
						<div class="flex-1">
							<div class="font-medium text-gray-900">Create an empty project (blank slate)</div>
							<div class="text-sm text-gray-500">
								Start with a clean slate and build your project from scratch
							</div>
						</div>
					</label>

					<!-- Upload XML Option -->
					<label
						class="flex items-start gap-3 p-4 border-2 rounded-lg cursor-pointer transition-colors hover:border-primary"
						class:border-primary={startOption === 'upload'}
						class:bg-primary={startOption === 'upload'}
						class:bg-opacity-5={startOption === 'upload'}
					>
						<input
							type="radio"
							name="startOption"
							value="upload"
							bind:group={startOption}
							class="radio radio-primary mt-1"
						/>
						<div class="flex-1">
							<div class="font-medium text-gray-900">
								Upload a REDCap project XML file (CDISC ODM format)
							</div>
							<div class="text-sm text-gray-500">
								Import configuration from an existing REDCap project file
							</div>
						</div>
					</label>

					<!-- Template Option -->
					<label
						class="flex items-start gap-3 p-4 border-2 rounded-lg cursor-pointer transition-colors hover:border-primary"
						class:border-primary={startOption === 'template'}
						class:bg-primary={startOption === 'template'}
						class:bg-opacity-5={startOption === 'template'}
					>
						<input
							type="radio"
							name="startOption"
							value="template"
							bind:group={startOption}
							class="radio radio-primary mt-1"
						/>
						<div class="flex-1">
							<div class="font-medium text-gray-900">Use a template (choose one below)</div>
							<div class="text-sm text-gray-500">
								Start with a pre-built template with sample fields and forms
							</div>
						</div>
					</label>
				</div>

				<!-- File Upload Section (shown when upload is selected) -->
				{#if startOption === 'upload'}
					<div class="mt-6 p-4 bg-blue-50 border-2 border-blue-200 rounded-lg">
						<h3 class="font-medium text-gray-900 mb-3">Choose XML file to upload</h3>
						<div class="form-control">
							<input
								type="file"
								accept=".xml"
								onchange={handleFileChange}
								class="file-input file-input-bordered file-input-primary w-full"
							/>
							{#if xmlFile}
								<label class="label">
									<span class="label-text-alt text-success">Selected: {xmlFile.name}</span>
								</label>
							{/if}
						</div>
						<div class="alert alert-info mt-3">
							<svg
								xmlns="http://www.w3.org/2000/svg"
								fill="none"
								viewBox="0 0 24 24"
								class="stroke-current shrink-0 w-5 h-5"
							>
								<path
									stroke-linecap="round"
									stroke-linejoin="round"
									stroke-width="2"
									d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
								></path>
							</svg>
							<span class="text-sm">Only CDISC ODM format XML files are supported</span>
						</div>
					</div>
				{/if}

				<!-- Template Selection (shown when template is selected) -->
				{#if startOption === 'template'}
					<div class="mt-6 p-4 bg-blue-50 border-2 border-blue-200 rounded-lg">
						<h3 class="font-medium text-primary mb-2 flex items-center gap-2">
							<svg
								xmlns="http://www.w3.org/2000/svg"
								fill="none"
								viewBox="0 0 24 24"
								stroke-width="1.5"
								stroke="currentColor"
								class="w-5 h-5"
							>
								<path
									stroke-linecap="round"
									stroke-linejoin="round"
									d="M11.48 3.499a.562.562 0 011.04 0l2.125 5.111a.563.563 0 00.475.345l5.518.442c.499.04.701.663.321.988l-4.204 3.602a.563.563 0 00-.182.557l1.285 5.385a.562.562 0 01-.84.61l-4.725-2.885a.563.563 0 00-.586 0L6.982 20.54a.562.562 0 01-.84-.61l1.285-5.386a.562.562 0 00-.182-.557l-4.204-3.602a.563.563 0 01.321-.988l5.518-.442a.563.563 0 00.475-.345L11.48 3.5z"
								/>
							</svg>
							Choose a project template
						</h3>
						<p class="text-sm text-gray-600 mb-4">
							(comes pre-filled with fields, forms/surveys, and other settings)
						</p>

						<div class="space-y-2">
							<!-- Basic Demography -->
							<label
								class="flex items-start gap-3 p-3 border rounded-lg cursor-pointer hover:bg-white transition-colors"
								class:bg-white={selectedTemplate === 'demographics'}
								class:border-pink-400={selectedTemplate === 'demographics'}
							>
								<input
									type="radio"
									name="template"
									value="demographics"
									bind:group={selectedTemplate}
									class="radio radio-sm radio-secondary mt-1"
								/>
								<div class="flex-1">
									<div class="font-medium text-gray-900">Basic Demography</div>
									<div class="text-sm text-gray-600">
										Contains a single data collection instrument to capture basic demographic
										information.
									</div>
								</div>
							</label>

							<!-- CAMH Data Dictionary -->
							<label
								class="flex items-start gap-3 p-3 border rounded-lg cursor-pointer hover:bg-white transition-colors"
								class:bg-white={selectedTemplate === 'camh'}
								class:border-pink-400={selectedTemplate === 'camh'}
							>
								<input
									type="radio"
									name="template"
									value="camh"
									bind:group={selectedTemplate}
									class="radio radio-sm radio-secondary mt-1"
								/>
								<div class="flex-1">
									<div class="font-medium text-gray-900">CAMH Data Dictionary</div>
									<div class="text-sm text-gray-600">
										Collaborative effort of CAMH researchers Contains a lot of measures used in CAMH
										studies for internal use only
									</div>
								</div>
							</label>

							<!-- Classic Database -->
							<label
								class="flex items-start gap-3 p-3 border rounded-lg cursor-pointer hover:bg-white transition-colors"
								class:bg-white={selectedTemplate === 'classic'}
								class:border-pink-400={selectedTemplate === 'classic'}
							>
								<input
									type="radio"
									name="template"
									value="classic"
									bind:group={selectedTemplate}
									class="radio radio-sm radio-secondary mt-1"
								/>
								<div class="flex-1">
									<div class="font-medium text-gray-900">Classic Database</div>
									<div class="text-sm text-gray-600">
										Contains six data entry forms, including forms for demography and baseline data,
										three monthly data forms, and concludes with a completion data form.
									</div>
								</div>
							</label>

							<!-- Common Data Elements -->
							<label
								class="flex items-start gap-3 p-3 border rounded-lg cursor-pointer hover:bg-white transition-colors"
								class:bg-white={selectedTemplate === 'common'}
								class:border-pink-400={selectedTemplate === 'common'}
							>
								<input
									type="radio"
									name="template"
									value="common"
									bind:group={selectedTemplate}
									class="radio radio-sm radio-secondary mt-1"
								/>
								<div class="flex-1">
									<div class="font-medium text-gray-900">Common Data Elements</div>
									<div class="text-sm text-gray-600">
										Contains: Subject Enrollment and Informed Consent, Demographic Form, QIDS-SR,
										GAD7, PSQI, WHOQOL, Sheehan Disability, Standard values codes and formats for
										common response categories.
									</div>
								</div>
							</label>
						</div>
					</div>
				{/if}
			</div>
		</div>

		<!-- Form Actions -->
		<div class="flex justify-end gap-3">
			<a href="/project" class="btn btn-ghost">Cancel</a>
			<button type="submit" class="btn btn-primary" disabled={loading}>
				{#if loading}
					<span class="loading loading-spinner loading-sm"></span>
					Creating...
				{:else}
					CREATE PROJECT
				{/if}
			</button>
		</div>
	</form>
</div>

<style lang="postcss">
	.card {
		border-radius: 0.5rem;
	}

	.input:focus,
	.select:focus,
	.textarea:focus {
		border-color: #6366f1;
		outline: none;
		box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.1);
	}

	.btn-primary {
		background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%);
		border: none;
		color: white;
		font-weight: 600;
		letter-spacing: 0.025em;
	}

	.btn-primary:hover:not(:disabled) {
		opacity: 0.9;
	}

	.btn-primary:disabled {
		opacity: 0.6;
		cursor: not-allowed;
	}

	.radio-primary:checked {
		background-color: #6366f1;
		border-color: #6366f1;
	}

	.checkbox:checked {
		background-color: #6366f1;
		border-color: #6366f1;
	}
</style>
