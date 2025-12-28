<script lang="ts">
	import { onMount } from 'svelte';
	import { page } from '$app/stores';
	import { PROJECT_DETAIL_SETUP_ROUTE } from '$lib/enums/routes';
	import { resolveProjectRoute } from '$lib/utils/routes';

	interface Event {
		id: number;
		name: string;
		description: string;
		dayOffset: number;
		repeatable: boolean;
	}

	interface Form {
		id: number;
		name: string;
	}

	let events: Event[] = [
		{ id: 1, name: 'Baseline', description: 'Initial assessment', dayOffset: 0, repeatable: false },
		{ id: 2, name: 'Follow-up Week 4', description: '4-week follow-up visit', dayOffset: 28, repeatable: false }
	];

	let forms: Form[] = [
		{ id: 1, name: 'Baseline Assessment' },
		{ id: 2, name: 'Vitals' },
		{ id: 3, name: 'Lab Results' }
	];

	let eventFormAssignments: { [key: number]: number[] } = {
		1: [1, 2],
		2: [2, 3]
	};

	 let showNewEventModal = false;
	let newEventName = '';
	let newEventDescription = '';
	let newEventDayOffset = 0;

	const addNewEvent = () => {
		const newEvent: Event = {
			id: Math.max(...events.map(e => e.id), 0) + 1,
			name: newEventName,
			description: newEventDescription,
			dayOffset: newEventDayOffset,
			repeatable: false
		};
		events = [...events, newEvent];
		eventFormAssignments[newEvent.id] = [];
		showNewEventModal = false;
		newEventName = '';
		newEventDescription = '';
		newEventDayOffset = 0;
	};

	 const projectId = $derived($page.params.projectId ?? '1');
	 const setupOverviewRoute = $derived(resolveProjectRoute(PROJECT_DETAIL_SETUP_ROUTE, projectId));

	 const toggleFormAssignment = (eventId: number, formId: number) => {
		const assignments = eventFormAssignments[eventId] || [];
		if (assignments.includes(formId)) {
			eventFormAssignments[eventId] = assignments.filter(f => f !== formId);
		} else {
			eventFormAssignments[eventId] = [...assignments, formId];
		}
	};

	const deleteEvent = (id: number) => {
		events = events.filter(e => e.id !== id);
		delete eventFormAssignments[id];
	};
</script>

<div class="p-6 space-y-6">
	<!-- Header -->
	<div>
		<a href={setupOverviewRoute} class="flex items-center gap-2 text-[#0b3a7a] hover:text-[#082654] text-sm font-medium mb-4">
			<i class="fas fa-arrow-left"></i>Back to Setup
		</a>
		<h1 class="text-3xl font-bold text-gray-800 mb-2">Define Your Events</h1>
		<p class="text-gray-600">Create events and assign instruments to them for scheduling and data collection</p>
	</div>

	<!-- Create Event Button -->
	<div class="flex gap-3">
		<button
			on:click={() => (showNewEventModal = true)}
			class="px-4 py-2 bg-[#0b3a7a] text-white rounded-lg hover:bg-[#082654] font-medium transition-colors flex items-center gap-2"
		>
			<i class="fas fa-plus"></i>
			Define My Events
		</button>
		<button class="px-4 py-2 bg-gray-600 text-white rounded-lg hover:bg-gray-700 font-medium transition-colors flex items-center gap-2">
			<i class="fas fa-check"></i>
			Designate Instruments for My Events
		</button>
	</div>

	<!-- Events List with Form Assignment -->
	<div class="space-y-4">
		{#each events as event (event.id)}
			<div class="bg-white rounded-lg shadow p-6">
				<div class="flex items-start justify-between mb-4">
					<div>
						<h3 class="text-lg font-bold text-gray-800">{event.name}</h3>
						<p class="text-sm text-gray-600">{event.description}</p>
						<p class="text-xs text-gray-500 mt-1">Day offset: {event.dayOffset}</p>
					</div>
					<button
						on:click={() => deleteEvent(event.id)}
						class="px-3 py-1 bg-red-50 text-red-600 rounded hover:bg-red-100 text-xs font-medium transition-colors"
					>
						<i class="fas fa-trash"></i> Delete
					</button>
				</div>

				<!-- Form Assignment -->
				<div class="border-t pt-4">
					<p class="text-sm font-semibold text-gray-700 mb-3">Assign Instruments:</p>
					<div class="space-y-2">
						{#each forms as form (form.id)}
							<label class="flex items-center gap-3 cursor-pointer p-2 hover:bg-gray-50 rounded">
								<input
									type="checkbox"
									checked={eventFormAssignments[event.id]?.includes(form.id) ?? false}
									on:change={() => toggleFormAssignment(event.id, form.id)}
									class="w-4 h-4 rounded border-gray-300 text-[#0b3a7a] focus:ring-[#0b3a7a]"
								/>
								<span class="text-gray-700">{form.name}</span>
							</label>
						{/each}
					</div>
				</div>

				<!-- Repeatability -->
				<div class="border-t pt-4 mt-4">
					<label class="flex items-center gap-3 cursor-pointer">
						<input
							type="checkbox"
							bind:checked={event.repeatable}
							class="w-4 h-4 rounded border-gray-300 text-[#0b3a7a] focus:ring-[#0b3a7a]"
						/>
						<span class="text-sm font-medium text-gray-700">Mark as repeatable event</span>
					</label>
				</div>
			</div>
		{/each}
	</div>

	<!-- Event Matrix View -->
	<div class="bg-white rounded-lg shadow overflow-hidden">
		<div class="p-6 border-b border-gray-200">
			<h2 class="text-xl font-bold text-gray-800">Event Matrix</h2>
			<p class="text-sm text-gray-600 mt-1">Overview of event-to-instrument assignments</p>
		</div>

		<div class="overflow-x-auto">
			<table class="w-full text-sm">
				<thead class="bg-gray-50 border-b border-gray-200">
					<tr>
						<th class="px-6 py-3 text-left font-semibold text-gray-700">Event Name</th>
						{#each forms as form (form.id)}
							<th class="px-6 py-3 text-center font-semibold text-gray-700">{form.name}</th>
						{/each}
					</tr>
				</thead>
				<tbody class="divide-y divide-gray-200">
					{#each events as event (event.id)}
						<tr class="hover:bg-gray-50">
							<td class="px-6 py-3 font-medium text-gray-800">{event.name}</td>
							{#each forms as form (form.id)}
								<td class="px-6 py-3 text-center">
									{#if eventFormAssignments[event.id]?.includes(form.id)}
										<i class="fas fa-check text-green-600 text-lg"></i>
									{:else}
										<span class="text-gray-300">—</span>
									{/if}
								</td>
							{/each}
						</tr>
					{/each}
				</tbody>
			</table>
		</div>
	</div>

	<!-- New Event Modal -->
	{#if showNewEventModal}
		<div class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
			<div class="bg-white rounded-lg shadow-xl p-6 max-w-md w-full mx-4">
				<h2 class="text-xl font-bold text-gray-800 mb-4">Create New Event</h2>

			<div class="space-y-4">
				<div>
					<label class="block text-sm font-medium text-gray-700 mb-1">Event Name</label>
					<input
						type="text"
						bind:value={newEventName}
						class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-[#0b3a7a] outline-none"
						placeholder="e.g., Baseline Visit"
					/>
				</div>

				<div>
					<label class="block text-sm font-medium text-gray-700 mb-1">Description</label>
					<input
						type="text"
						bind:value={newEventDescription}
						class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-[#0b3a7a] outline-none"
						placeholder="e.g., Initial assessment"
					/>
				</div>

				<div>
					<label class="block text-sm font-medium text-gray-700 mb-1">Day Offset</label>
					<input
						type="number"
						bind:value={newEventDayOffset}
						class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-[#0b3a7a] outline-none"
						placeholder="0"
					/>
				</div>
			</div>				<div class="flex gap-2 justify-end mt-6 border-t pt-4">
					<button
						on:click={() => (showNewEventModal = false)}
						class="px-4 py-2 border border-gray-300 text-gray-700 rounded-lg hover:bg-gray-50 font-medium transition-colors"
					>
						Cancel
					</button>
					<button
						on:click={addNewEvent}
						class="px-4 py-2 bg-[#0b3a7a] text-white rounded-lg hover:bg-[#082654] font-medium transition-colors"
					>
						Create Event
					</button>
				</div>
			</div>
		</div>
	{/if}
</div>
