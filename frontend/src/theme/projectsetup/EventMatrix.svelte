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
	import Matrix from './EventMatrixComponents/Matrix.svelte';
	import ConfigEventCondition from './EventMatrixComponents/ConfigEventCondition.svelte';
	import ConfigRepeatableGroups from './EventMatrixComponents/ConfigRepeatableGroups.svelte';

	// Sample data - Events
	let events: Event[] = [
		{ id: 'screening', name: 'Screening' },
		{ id: 'baseline', name: 'Baseline' },
		{ id: 'visit1', name: 'Visit 1' },
		{ id: 'endofstudy', name: 'End of Study' }
	];

	// Sample data - Clinical Groups
	let clinicalGroups: ClinicalGroup[] = [
		{ id: 'mri', name: 'MRI' },
		{ id: 'ct', name: 'CT' },
		{ id: 'demographics', name: 'Demographics' }
	];

	// Matrix data - tracks which groups are used in which events
	let matrix: MatrixEntry[] = [
		{ eventId: 'screening', groupId: 'mri', selected: true },
		{ eventId: 'screening', groupId: 'ct', selected: false },
		{ eventId: 'screening', groupId: 'demographics', selected: true },
		{ eventId: 'baseline', groupId: 'mri', selected: false },
		{ eventId: 'baseline', groupId: 'ct', selected: true },
		{ eventId: 'baseline', groupId: 'demographics', selected: true },
		{ eventId: 'visit1', groupId: 'mri', selected: true },
		{ eventId: 'visit1', groupId: 'ct', selected: false },
		{ eventId: 'visit1', groupId: 'demographics', selected: true },
		{ eventId: 'endofstudy', groupId: 'mri', selected: true },
		{ eventId: 'endofstudy', groupId: 'ct', selected: false },
		{ eventId: 'endofstudy', groupId: 'demographics', selected: false }
	];

	let activeTab = 'matrix';

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

<div class="space-y-6">
	<div class="bg-white rounded-lg shadow">
		<div class="border-b border-gray-200">
			<div class="flex gap-4 px-6">
				<button
					on:click={() => (activeTab = 'matrix')}
					class="px-4 py-3 text-sm font-medium border-b-2 transition {activeTab === 'matrix'
						? 'text-blue-600 border-blue-600'
						: 'text-gray-600 border-transparent hover:text-gray-900'}"
				>
					Event Planner
				</button>
				<button
					on:click={() => (activeTab = 'conditions')}
					class="px-4 py-3 text-sm font-medium border-b-2 transition {activeTab === 'conditions'
						? 'text-blue-600 border-blue-600'
						: 'text-gray-600 border-transparent hover:text-gray-900'}"
				>
					Event Condition Groups
				</button>
				<button
					on:click={() => (activeTab = 'repeatable')}
					class="px-4 py-3 text-sm font-medium border-b-2 transition {activeTab === 'repeatable'
						? 'text-blue-600 border-blue-600'
						: 'text-gray-600 border-transparent hover:text-gray-900'}"
				>
					Repeatable Groups
				</button>
			</div>
		</div>

		<div class="p-6">
			{#if activeTab === 'matrix'}
				<Matrix {events} {clinicalGroups} bind:matrix />
			{:else if activeTab === 'conditions'}
				<ConfigEventCondition {events} {clinicalGroups} {matrix} />
			{:else if activeTab === 'repeatable'}
				<ConfigRepeatableGroups />
			{/if}
		</div>
	</div>
</div>
