<script lang="ts">
	interface ProjectData {
		title: string;
		purpose: string;
		useSurveys: boolean;
		useLongitudinal: boolean;
		useMyCap: boolean;
		notes: string;
	}

	let projectData: ProjectData = {
		title: 'Diabetes Study 2025',
		purpose: 'Clinical research on diabetes management',
		useSurveys: true,
		useLongitudinal: true,
		useMyCap: false,
		notes: ''
	};

	let isSaving = false;

	const saveSettings = async () => {
		isSaving = true;
		await new Promise(resolve => setTimeout(resolve, 1000));
		isSaving = false;
		alert('Project settings saved successfully!');
	};
</script>

<div class="space-y-6">
	<!-- Project Configuration Card -->
	<div class="bg-white rounded-lg shadow p-6">
		<h2 class="text-xl font-bold text-gray-800 mb-6 flex items-center gap-2">
			<i class="fas fa-folder text-[#0b3a7a]"></i>
			Project Configuration
		</h2>

		<form on:submit|preventDefault={saveSettings} class="space-y-6">
			<!-- Project Title -->
			<div>
				<label class="block text-sm font-semibold text-gray-700 mb-2">
					Project Title
					<span class="text-red-500">*</span>
				</label>
				<input
					type="text"
					bind:value={projectData.title}
					class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-[#0b3a7a] focus:border-transparent outline-none"
					placeholder="Enter project title"
				/>
				<p class="text-xs text-gray-500 mt-1">The name of your research project</p>
			</div>

			<!-- Project Purpose -->
			<div>
				<label class="block text-sm font-semibold text-gray-700 mb-2">
					Project Purpose
					<span class="text-red-500">*</span>
				</label>
				<textarea
					bind:value={projectData.purpose}
					class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-[#0b3a7a] focus:border-transparent outline-none"
					placeholder="Describe the purpose of your project"
					rows="3"
				></textarea>
				<p class="text-xs text-gray-500 mt-1">Brief description of the project's objectives</p>
			</div>

			<!-- Feature Toggles -->
			<div class="border-t pt-6">
				<h3 class="text-lg font-semibold text-gray-800 mb-4">Enable Features</h3>

				<!-- Use Surveys Toggle -->
				<div class="flex items-center justify-between p-4 bg-gray-50 rounded-lg mb-4">
					<div class="flex items-start gap-3">
						<div class="mt-1">
							<i class="fas fa-check-circle text-green-500 text-lg"></i>
						</div>
						<div>
							<p class="font-semibold text-gray-800">Use surveys in this project?</p>
							<p class="text-sm text-gray-600 mt-1">
								Allow participants to complete surveys online
								<a href="#" class="text-[#0b3a7a] hover:underline ml-1">?</a>
							</p>
						</div>
					</div>
					<label class="relative inline-flex items-center cursor-pointer">
						<input
							type="checkbox"
							bind:checked={projectData.useSurveys}
							class="sr-only peer"
						/>
						<div class="w-11 h-6 bg-gray-300 peer-focus:outline-none peer-focus:ring-4 peer-focus:ring-[#0b3a7a]/30 rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:bg-[#0b3a7a]"></div>
					</label>
				</div>

				<!-- Use Longitudinal Toggle -->
				<div class="flex items-center justify-between p-4 bg-gray-50 rounded-lg mb-4">
					<div class="flex items-start gap-3">
						<div class="mt-1">
							<i class="fas fa-check-circle text-green-500 text-lg"></i>
						</div>
						<div>
							<p class="font-semibold text-gray-800">Use longitudinal data collection with defined events?</p>
							<p class="text-sm text-gray-600 mt-1">
								Schedule multiple visits/events for participants
								<a href="#" class="text-[#0b3a7a] hover:underline ml-1">?</a>
							</p>
						</div>
					</div>
					<label class="relative inline-flex items-center cursor-pointer">
						<input
							type="checkbox"
							bind:checked={projectData.useLongitudinal}
							class="sr-only peer"
						/>
						<div class="w-11 h-6 bg-gray-300 peer-focus:outline-none peer-focus:ring-4 peer-focus:ring-[#0b3a7a]/30 rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:bg-[#0b3a7a]"></div>
					</label>
				</div>

				<!-- Use MyCap Toggle -->
				<div class="flex items-center justify-between p-4 bg-gray-50 rounded-lg">
					<div class="flex items-start gap-3">
						<div class="mt-1">
							<i class="fas fa-times-circle text-red-500 text-lg"></i>
						</div>
						<div>
							<p class="font-semibold text-gray-800">Use the MyCap participant-facing mobile app?</p>
							<p class="text-sm text-gray-600 mt-1">
								Allow participants to access forms via mobile app
								<a href="#" class="text-[#0b3a7a] hover:underline ml-1">?</a>
							</p>
							<a href="#" class="text-[#0b3a7a] hover:underline text-sm mt-2 inline-block">Learn more about MyCap</a>
						</div>
					</div>
					<label class="relative inline-flex items-center cursor-pointer">
						<input
							type="checkbox"
							bind:checked={projectData.useMyCap}
							class="sr-only peer"
						/>
						<div class="w-11 h-6 bg-gray-300 peer-focus:outline-none peer-focus:ring-4 peer-focus:ring-[#0b3a7a]/30 rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:bg-[#0b3a7a]"></div>
					</label>
				</div>
			</div>

			<!-- Notes Section -->
			<div class="border-t pt-6">
				<label class="block text-sm font-semibold text-gray-700 mb-2">Notes</label>
				<textarea
					bind:value={projectData.notes}
					class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-[#0b3a7a] focus:border-transparent outline-none"
					placeholder="Add any additional notes or comments"
					rows="3"
				></textarea>
			</div>

			<!-- Action Buttons -->
			<div class="flex gap-4 justify-end border-t pt-6">
				<button
					type="button"
					class="px-6 py-2 border border-gray-300 text-gray-700 rounded-lg hover:bg-gray-50 font-medium transition-colors"
				>
					Cancel
				</button>
				<button
					type="submit"
					disabled={isSaving}
					class="px-6 py-2 bg-[#0b3a7a] text-white rounded-lg hover:bg-[#082654] font-medium transition-colors disabled:opacity-50"
				>
					{#if isSaving}
						<i class="fas fa-spinner fa-spin mr-2"></i>Saving...
					{:else}
						<i class="fas fa-save mr-2"></i>Save Settings
					{/if}
				</button>
			</div>
		</form>
	</div>

	<!-- Help Section -->
	<div class="bg-[#0b3a7a]/5 rounded-lg shadow p-6 border border-[#0b3a7a]/10">
		<h3 class="text-lg font-bold text-gray-800 mb-3 flex items-center gap-2">
			<i class="fas fa-info-circle text-[#0b3a7a]"></i>
			Quick Help
		</h3>
		<ul class="space-y-2 text-sm text-gray-700">
			<li class="flex gap-2">
				<span class="text-[#0b3a7a] font-bold">•</span>
				<span><strong>Surveys:</strong> Enable if you want participants to complete online forms</span>
			</li>
			<li class="flex gap-2">
				<span class="text-[#0b3a7a] font-bold">•</span>
				<span><strong>Longitudinal:</strong> Use this for multi-visit studies with scheduled events</span>
			</li>
			<li class="flex gap-2">
				<span class="text-[#0b3a7a] font-bold">•</span>
				<span><strong>MyCap:</strong> Mobile app access for remote data collection</span>
			</li>
		</ul>
	</div>
</div>

