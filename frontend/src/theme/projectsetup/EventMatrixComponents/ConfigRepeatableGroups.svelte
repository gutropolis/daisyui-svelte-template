<script lang="ts">
	interface GroupConfig {
		id: string;
		name: string;
		isRepeatableGroup: boolean;
		repeatableGroupName: string;
	}

	interface EventNode {
		id: string;
		eventName: string;
		expanded: boolean;
		groups: GroupConfig[];
	}

	let eventNodes: EventNode[] = [
		{
			id: 'screening',
			eventName: 'Screening',
			expanded: true,
			groups: [
				{ id: 'g1', name: 'Demographics', isRepeatableGroup: false, repeatableGroupName: '' },
				{ id: 'g2', name: 'Medical History', isRepeatableGroup: false, repeatableGroupName: '' },
				{ id: 'g3', name: 'Consent', isRepeatableGroup: true, repeatableGroupName: 'Consent Group' }
			]
		},
		{
			id: 'baseline',
			eventName: 'Baseline',
			expanded: true,
			groups: [
				{ id: 'g4', name: 'Demographics', isRepeatableGroup: true, repeatableGroupName: 'Baseline Demographics' },
				{ id: 'g5', name: 'Vitals', isRepeatableGroup: false, repeatableGroupName: '' }
			]
		},
		{
			id: 'visit1',
			eventName: 'Visit 1',
			expanded: false,
			groups: [
				{ id: 'g6', name: 'Follow-up', isRepeatableGroup: true, repeatableGroupName: 'Follow-up Visit' },
				{ id: 'g7', name: 'Labs', isRepeatableGroup: false, repeatableGroupName: '' }
			]
		},
		{
			id: 'endofstudy',
			eventName: 'End of Study',
			expanded: false,
			groups: [
				{ id: 'g8', name: 'Final Assessment', isRepeatableGroup: false, repeatableGroupName: '' },
				{ id: 'g9', name: 'Safety', isRepeatableGroup: false, repeatableGroupName: '' }
			]
		}
	];

	const toggleEvent = (eventId: string) => {
		const event = eventNodes.find(e => e.id === eventId);
		if (event) {
			event.expanded = !event.expanded;
			eventNodes = eventNodes;
		}
	};

	const handleSave = () => {
		console.log('Repeatable groups saved:', eventNodes);
	};
</script>

<div class="bg-white rounded-lg">
	<div class="mb-6">
		<h3 class="text-lg font-bold text-[#0b3a7a] flex items-center gap-2">
			<i class="fas fa-repeat"></i>
			Manage Repeatable Groups
		</h3>
	</div>

	<!-- Information Box -->
	<div class="mb-6 p-4 bg-green-50 border border-green-200 rounded-lg">
		<div class="space-y-3">
			<div>
				<h4 class="font-semibold text-gray-900 text-sm mb-1">What are Repeatable Groups?</h4>
				<p class="text-gray-700 text-sm">An excellent way to collect repeating data is to use repeatable instruments/events. This is sometimes called one-to-many data collection. You can specify a data collection instrument to be infinitely repeatable, which means that an instrument can be repeated over and over again (a different number of times for each record) even without enabling REDCap's longitudinal module.</p>
			</div>
			<div>
				<h4 class="font-semibold text-gray-900 text-sm mb-1">Configuration</h4>
				<p class="text-gray-700 text-sm">For each group within an event, you can specify whether it is repeatable and provide a custom label for the repeatable group.</p>
			</div>
		</div>
	</div>

	<!-- Tree Structure -->
	<div class="space-y-2 max-h-96 overflow-y-auto border border-gray-200 rounded-lg p-4 bg-gray-50">
		{#each eventNodes as event (event.id)}
			<div class="space-y-1">
				<!-- Event Node (Parent) -->
				<button
					on:click={() => toggleEvent(event.id)}
					class="w-full flex items-center gap-3 px-3 py-2 bg-white border border-gray-200 rounded hover:bg-gray-50 transition-colors text-left"
				>
					<i class={`fas fa-chevron-right transition-transform ${event.expanded ? 'rotate-90' : ''}`}></i>
					<i class="fas fa-calendar text-gray-500"></i>
					<span class="font-semibold text-gray-800">{event.eventName}</span>
				</button>

				<!-- Group Nodes (Children) -->
				{#if event.expanded}
					<div class="ml-6 space-y-2">
						{#each event.groups as group (group.id)}
							<div class="space-y-2 p-3 bg-white border border-gray-200 rounded">
								<!-- Group Header -->
								<div class="flex items-center gap-2">
									<i class="fas fa-folder text-blue-500"></i>
									<span class="font-medium text-gray-800 flex-1">{group.name}</span>
								</div>

								<!-- Repeatable Group Checkbox -->
								<div class="flex items-center gap-3 ml-6">
									<input
										type="checkbox"
										id={`repeatable-${group.id}`}
										bind:checked={group.isRepeatableGroup}
										class="w-4 h-4 cursor-pointer accent-blue-600"
									/>
									<label for={`repeatable-${group.id}`} class="text-sm text-gray-700 font-medium cursor-pointer flex-1">
										Is Repeatable Group
									</label>
								</div>

								<!-- Repeatable Group Name Input -->
								{#if group.isRepeatableGroup}
									<div class="ml-6">
										<label for={`name-${group.id}`} class="block text-xs font-medium text-gray-600 mb-1">
											Repeatable Group Name
										</label>
										<input
											id={`name-${group.id}`}
											type="text"
											bind:value={group.repeatableGroupName}
											placeholder="e.g. [visit_date], [weight] kg"
											class="w-full px-3 py-2 border border-gray-300 rounded text-sm bg-white text-gray-700 placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-blue-500"
										/>
										<p class="text-xs text-gray-500 mt-1">Example: [visit_date], [weight] kg</p>
									</div>
								{/if}
							</div>
						{/each}
					</div>
				{/if}
			</div>
		{/each}
	</div>

	<!-- Bottom Action Bar -->
	<div class="flex items-center justify-between mt-6 pt-4">
		<div class="text-gray-600 text-sm font-medium">
			Saved
		</div>
		<button
			on:click={handleSave}
			class="px-6 py-2 bg-blue-600 text-white rounded font-semibold hover:bg-blue-700 transition-colors"
		>
			SAVE
		</button>
	</div>
</div>
