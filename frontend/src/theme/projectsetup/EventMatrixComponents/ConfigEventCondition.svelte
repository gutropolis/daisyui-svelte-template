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

	export interface ConditionRule {
		id: string;
		event: string;
		form: string;
		field: string;
		operator: string;
		value: string;
	}

	export interface GroupCondition {
		id: string;
		groupId: string;
		groupName: string;
		logicOperator: 'any' | 'all';
		rules: ConditionRule[];
	}

	export interface EventNode {
		id: string;
		eventName: string;
		expanded: boolean;
		groupConditions: GroupCondition[];
	}
</script>

<script lang="ts">
	export let events: Event[] = [];
	export let clinicalGroups: ClinicalGroup[] = [];
	export let matrix: MatrixEntry[] = [];

	let eventNodes: EventNode[] = [
		{
			id: 'screening',
			eventName: 'Screening',
			expanded: true,
			groupConditions: [
				{
					id: 'gc1',
					groupId: 'demographics',
					groupName: 'Demographics',
					logicOperator: 'any',
					rules: [
						{ id: 'r1', event: 'screening', form: 'Demographics Form', field: 'Age', operator: '=', value: '18+' }
					]
				},
				{
					id: 'gc2',
					groupId: 'medicalhistory',
					groupName: 'Medical History',
					logicOperator: 'all',
					rules: []
				}
			]
		},
		{
			id: 'baseline',
			eventName: 'Baseline',
			expanded: false,
			groupConditions: [
				{
					id: 'gc3',
					groupId: 'vitals',
					groupName: 'Vitals',
					logicOperator: 'any',
					rules: []
				}
			]
		}
	];

	// Check if event-group relations exist
	$: hasRelations = matrix.some(m => m.selected);

	// Get selected event-group pairs
	$: selectedPairs = matrix.filter(m => m.selected);

	const toggleEvent = (eventId: string) => {
		const event = eventNodes.find(e => e.id === eventId);
		if (event) {
			event.expanded = !event.expanded;
			eventNodes = eventNodes;
		}
	};

	const addConditionRule = (eventId: string, groupConditionId: string) => {
		const eventNode = eventNodes.find(e => e.id === eventId);
		if (eventNode) {
			const groupCondition = eventNode.groupConditions.find(gc => gc.id === groupConditionId);
			if (groupCondition) {
				groupCondition.rules = [
					...groupCondition.rules,
					{ id: Date.now().toString(), event: '', form: '', field: '', operator: '=', value: '' }
				];
				eventNodes = eventNodes;
			}
		}
	};

	const removeConditionRule = (eventId: string, groupConditionId: string, ruleId: string) => {
		const eventNode = eventNodes.find(e => e.id === eventId);
		if (eventNode) {
			const groupCondition = eventNode.groupConditions.find(gc => gc.id === groupConditionId);
			if (groupCondition) {
				groupCondition.rules = groupCondition.rules.filter(r => r.id !== ruleId);
				eventNodes = eventNodes;
			}
		}
	};

	const getEventName = (eventId: string) => {
		return events.find(e => e.id === eventId)?.name || eventId;
	};

	const getGroupName = (groupId: string) => {
		return clinicalGroups.find(g => g.id === groupId)?.name || groupId;
	};

	const handleSave = () => {
		console.log('Conditions saved:', eventNodes);
	};
</script>

<div class="bg-white rounded-lg">
	<div class="mb-4">
		<h3 class="text-lg font-bold text-[#0b3a7a] flex items-center gap-2">
			<i class="fas fa-sliders-h"></i>
			Event Group Conditions
		</h3>
	</div>

	<!-- Event Group Conditions Information Box -->
	<div class="mb-6 p-4 bg-purple-50 border border-purple-200 rounded-lg">
		<div class="space-y-3">
			<div>
				<h4 class="font-semibold text-gray-900 text-sm mb-1">What are Event Group Conditions?</h4>
				<p class="text-gray-700 text-sm">Event Group Conditions define the logic and rules for when specific forms or data collection groups should be collected during study events. They control conditional data capture based on patient responses or study parameters.</p>
			</div>
			<div>
				<h4 class="font-semibold text-gray-900 text-sm mb-1">How to Create Conditions</h4>
				<ol class="text-gray-700 text-sm list-decimal list-inside space-y-1">
					<li>Expand an Event to view its Groups</li>
					<li>Expand a Group to view or add Condition Rules</li>
					<li>Choose "Any" or "All" to determine rule matching logic</li>
					<li>Add IF rules by specifying Event, Form, Field, Operator, and Value</li>
					<li>Click SAVE to apply the conditions</li>
				</ol>
			</div>
		</div>
	</div>

	{#if !hasRelations}
		<div class="p-6 bg-red-50 border border-red-200 rounded-lg text-center">
			<i class="fas fa-info-circle text-red-500 text-2xl mb-2 block"></i>
			<p class="text-gray-700 font-medium mb-1">No Event-Group Relations Found</p>
			<p class="text-gray-600 text-sm">Please configure event-group relations in the Event Matrix first before setting up conditions.</p>
		</div>
	{:else}
		<!-- Tree Structure -->
		<div class="space-y-2 max-h-[500px] overflow-y-auto border border-gray-200 rounded-lg p-4 bg-gray-50">
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
						<div class="ml-6 space-y-1">
							{#each event.groupConditions as groupCondition (groupCondition.id)}
								<div class="space-y-1">
									<!-- Group Header -->
									<div class="flex items-center gap-2 px-3 py-2 bg-white border border-gray-200 rounded hover:bg-blue-50 transition-colors">
										<i class="fas fa-folder text-blue-500"></i>
										<span class="font-medium text-gray-800 flex-1">{groupCondition.groupName}</span>
										<span class="text-xs text-gray-500 bg-gray-100 px-2 py-1 rounded">{groupCondition.rules.length} rules</span>
									</div>

									<!-- Condition Rules Section -->
									<div class="ml-6 space-y-2">
										<!-- Logic Operator Selector -->
										<div class="bg-white p-3 border border-gray-200 rounded">
											<div class="flex items-center gap-2 mb-3">
												<span class="text-sm font-semibold text-gray-700">this group when</span>
												<select
													bind:value={groupCondition.logicOperator}
													class="px-2 py-1 border border-gray-300 rounded text-sm bg-white"
												>
													<option value="any">Any</option>
													<option value="all">All</option>
												</select>
												<span class="text-sm text-gray-700">of following rules match</span>
												<button
													on:click={() => addConditionRule(event.id, groupCondition.id)}
													class="text-blue-600 text-xs font-semibold hover:text-blue-700 ml-auto flex items-center gap-1"
												>
													<i class="fas fa-plus"></i>
													ADD NEW IF
												</button>
											</div>

											<!-- Condition Rules -->
											{#if groupCondition.rules.length === 0}
												<p class="text-gray-500 text-sm italic">No rules configured</p>
											{:else}
												<div class="space-y-2">
													{#each groupCondition.rules as rule, index (rule.id)}
														<div class="flex items-center gap-2 text-sm">
															<span class="font-semibold text-gray-600 w-12">
																{index === 0 ? 'IF' : '------'}
															</span>
															<select class="px-2 py-1 border border-gray-300 rounded text-xs bg-white flex-1">
																<option>Choose Event</option>
																{#each events as evt (evt.id)}
																	<option value={evt.id}>{evt.name}</option>
																{/each}
															</select>
															<select class="px-2 py-1 border border-gray-300 rounded text-xs bg-white flex-1 text-gray-400">
																<option>Choose Form</option>
															</select>
															<select class="px-2 py-1 border border-gray-300 rounded text-xs bg-white flex-1 text-gray-400">
																<option>Choose Field</option>
															</select>
															<select class="px-2 py-1 border border-gray-300 rounded text-xs bg-white">
																<option>=</option>
																<option>!=</option>
																<option>&gt;</option>
																<option>&lt;</option>
															</select>
															<input
																type="text"
																placeholder="Value"
																class="px-2 py-1 border border-gray-300 rounded text-xs bg-white flex-1"
															/>
															<button
																on:click={() => removeConditionRule(event.id, groupCondition.id, rule.id)}
																class="text-red-500 hover:text-red-700 p-1"
																title="Delete rule"
															>
																<i class="fas fa-trash text-xs"></i>
															</button>
														</div>
													{/each}
												</div>
											{/if}
										</div>
									</div>
								</div>
							{/each}
						</div>
					{/if}
				</div>
			{/each}
		</div>

		<!-- Bottom Action Bar -->
		<div class="flex items-center justify-end gap-3 mt-6 pt-4 border-t border-gray-200">
			<button
				on:click={handleSave}
				class="px-6 py-2 bg-[#0b3a7a] text-white rounded font-semibold hover:bg-[#0a2f65] transition-colors"
			>
				SAVE
			</button>
		</div>
	{/if}
</div>
