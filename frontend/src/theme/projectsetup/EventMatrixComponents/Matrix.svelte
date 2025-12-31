<script context="module" lang="ts">
	export interface Event {
		id: string;
		name: string;
	}

	export interface ClinicalGroup {
		id: string;
		name: string;
	}

	export interface MatrixEntry {
		eventId: string;
		groupId: string;
		selected: boolean;
	}
</script>

<script lang="ts">
	export let events: Event[] = [];
	export let clinicalGroups: ClinicalGroup[] = [];
	export let matrix: MatrixEntry[] = [];

	const getMatrixEntry = (eventId: string, groupId: string) => {
		return matrix.find(m => m.eventId === eventId && m.groupId === groupId);
	};

	const toggleSelection = (eventId: string, groupId: string) => {
		const entry = getMatrixEntry(eventId, groupId);
		if (entry) {
			entry.selected = !entry.selected;
			matrix = matrix;
		}
	};

	const deselectAll = () => {
		matrix = matrix.map(m => ({ ...m, selected: false }));
	};
</script>

<div class="w-full">
	<div class="bg-white rounded-lg">
		<div class="flex items-center justify-between mb-4">
            <h3 class="text-lg font-bold text-[#0b3a7a] flex items-center gap-2">
                <i class="fas fa-sliders-h"></i>
                Event Matrix
            </h3>
            <p></p>  
        </div>
		
		
		<!-- Event Matrix Information Box -->
		<div class="mb-6 p-4 bg-blue-50 border border-blue-200 rounded-lg">
			<div class="space-y-3">
				<div>
					<h4 class="font-semibold text-gray-900 text-sm mb-1">What is an Event Matrix?</h4>
					<p class="text-gray-700 text-sm">An Event Matrix is a table used in clinical trials to define which forms (CRFs/eCRFs) are collected at which visits, under what conditions. It maps study events to clinical form groups and data collection modalities.</p>
				</div>
				<div>
					<h4 class="font-semibold text-gray-900 text-sm mb-1">Purpose in Clinical Trials</h4>
					<ul class="text-gray-700 text-sm list-disc list-inside space-y-1">
						<li>Defines data collection schedule and requirements</li>
						<li>Ensures consistency across all study sites</li>
						<li>Specifies which CRFs/eCRFs are required at each visit</li>
						<li>Documents conditional data collection rules</li>
						<li>Manages repeatable visits and grouped events</li>
					</ul>
				</div>
				<div>
					<h4 class="font-semibold text-gray-900 text-sm mb-1">How to Assign and Use</h4>
					<ol class="text-gray-700 text-sm list-decimal list-inside space-y-1">
						<li>Check the boxes to assign forms to visits/events</li>
						<li>Use "Multi Event group" to create grouped event structures</li>
						<li>Use "Modality group" to define data collection methods (paper, electronic, etc.)</li>
						<li>Configure conditions for conditional data collection</li>
						<li>Set up repeatable groups for visits that repeat multiple times</li>
					</ol>
				</div>
			</div>
		</div>
		<div class="flex items-center justify-between mb-4">
			<button
				on:click={deselectAll}
				class="text-blue-600 text-sm font-semibold hover:text-blue-700"
			>
				Deselect all
			</button>
		</div>
		
		<div class="overflow-x-auto">
			<table class="w-full text-sm">
				<thead>
					<tr class="border-b-2 border-gray-300 bg-gray-50">
						<th class="text-left py-3 px-4 font-semibold text-gray-700">GROUP</th>
						{#each clinicalGroups as group (group.id)}
							<th class="text-center py-3 px-4 font-semibold text-[#0b3a7a]">
								<span>{group.name.toUpperCase()}</span>
							</th>
						{/each}
					</tr>
				</thead>
				<tbody>
					{#each events as event (event.id)}
						<tr class="border-b border-gray-100 hover:bg-gray-50">
							<td class="py-3 px-4 font-medium text-gray-700 flex items-center gap-2">
								<span>{event.name}</span>
								<i class="fas fa-layer-group text-xs text-gray-500" title="Multi Event group"></i>
								<i class="fas fa-hospital text-xs text-gray-500" title="Modality group"></i>
							</td>
							{#each clinicalGroups as group (group.id)}
								<td class="py-3 px-4 text-center">
									<input
										type="checkbox"
										checked={getMatrixEntry(event.id, group.id)?.selected || false}
										on:change={() => toggleSelection(event.id, group.id)}
										class="w-5 h-5 cursor-pointer accent-blue-600"
									/>
								</td>
							{/each}
						</tr>
					{/each}
				</tbody>
			</table>
		</div>

		<!-- Bottom Action Buttons -->
		<div class="flex items-center justify-between gap-3 mt-8 pt-6 border-t border-gray-200">
			<div class="flex items-center gap-4">
				<button
					class="flex items-center gap-2 text-gray-700 text-sm hover:text-gray-900 font-medium"
					title="Multi Event group configuration"
				>
					<i class="fas fa-layer-group text-sm"></i>
					<span>Multi Event group</span>
				</button>
				<button
					class="flex items-center gap-2 text-gray-700 text-sm hover:text-gray-900 font-medium"
					title="Modality group configuration"
				>
					<i class="fas fa-hospital text-sm"></i>
					<span>Modality group</span>
				</button>
			</div>
			<button
				class="flex items-center gap-2 px-4 py-2 bg-blue-600 text-white hover:bg-blue-700 rounded font-semibold text-sm transition-colors"
			>
				<span>Save</span>
			</button>
		</div>
	</div>
</div>
