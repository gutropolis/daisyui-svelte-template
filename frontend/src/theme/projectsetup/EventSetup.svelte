<script lang="ts">
	interface Event {
		id: number;
		title: string;
		apiIdentifier: string;
		description: string;
	}

	let events: Event[] = [
		{
			id: 1,
			title: 'Screening',
			apiIdentifier: 'screening',
			description: 'Initial patient screening visit'
		},
		{
			id: 2,
			title: 'Baseline',
			apiIdentifier: 'baseline',
			description: 'Baseline data collection at the start of the study'
		},
		{
			id: 3,
			title: 'Week 4 Visit',
			apiIdentifier: 'week_4',
			description: 'Follow-up visit at 4 weeks'
		}
	];

	let showModal = false;
	let isEditing = false;
	let editingId: number | null = null;
	let successMessage = '';

	let formData = {
		title: '',
		apiIdentifier: '',
		description: ''
	};

	const openAddModal = () => {
		isEditing = false;
		editingId = null;
		formData = {
			title: '',
			apiIdentifier: '',
			description: ''
		};
		showModal = true;
	};

	const openEditModal = (event: Event) => {
		isEditing = true;
		editingId = event.id;
		formData = {
			title: event.title,
			apiIdentifier: event.apiIdentifier,
			description: event.description
		};
		showModal = true;
	};

	const closeModal = () => {
		showModal = false;
		formData = {
			title: '',
			apiIdentifier: '',
			description: ''
		};
	};

	const saveEvent = () => {
		if (!formData.title || !formData.apiIdentifier) {
			alert('Please fill in all required fields');
			return;
		}

		if (isEditing && editingId !== null) {
			// Update existing event
			const index = events.findIndex(e => e.id === editingId);
			if (index !== -1) {
				events[index] = {
					...events[index],
					title: formData.title,
					apiIdentifier: formData.apiIdentifier,
					description: formData.description
				};
			}
			successMessage = 'Event updated successfully!';
		} else {
			// Add new event
			const newEvent: Event = {
				id: Math.max(...events.map(e => e.id), 0) + 1,
				title: formData.title,
				apiIdentifier: formData.apiIdentifier,
				description: formData.description
			};
			events = [...events, newEvent];
			successMessage = 'Event added successfully!';
		}

		closeModal();
		setTimeout(() => {
			successMessage = '';
		}, 3000);
	};

	const deleteEvent = (id: number) => {
		if (confirm('Are you sure you want to delete this event?')) {
			events = events.filter(e => e.id !== id);
			successMessage = 'Event deleted successfully!';
			setTimeout(() => {
				successMessage = '';
			}, 3000);
		}
	};
</script>

<div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
	<!-- Success Message -->
	{#if successMessage}
		<div class="col-span-1 lg:col-span-2 bg-green-50 border border-green-200 rounded-lg p-4 flex items-center gap-3">
			<i class="fas fa-check-circle text-green-600 text-lg"></i>
			<p class="text-green-700 font-medium">{successMessage}</p>
		</div>
	{/if}

	<!-- Main Content Area -->
	<div class="lg:col-span-2 space-y-6">
		<!-- Events Listing Section -->
		<div class="bg-white rounded-lg shadow p-6">
		<div class="flex items-center justify-between mb-6">
			<h2 class="text-xl font-bold text-gray-800 flex items-center gap-2">
				<i class="fas fa-calendar text-[#0b3a7a]"></i>
				Project Events
			</h2>
			<button
				on:click={openAddModal}
				class="px-4 py-2 bg-[#0b3a7a] text-white rounded-lg hover:bg-[#082654] font-medium transition-colors flex items-center gap-2"
			>
				<i class="fas fa-plus"></i>
				Add New Event
			</button>
		</div>

		{#if events.length === 0}
			<div class="text-center py-12">
				<i class="fas fa-inbox text-4xl text-gray-300 mb-4 block"></i>
				<p class="text-gray-600 font-medium">No events created yet</p>
				<p class="text-gray-400 text-sm">Click "Add New Event" to create your first event</p>
			</div>
		{:else}
			<div class="space-y-3">
				{#each events as event (event.id)}
					<div class="flex items-center justify-between p-4 bg-gray-50 rounded-lg border border-gray-200 hover:border-[#0b3a7a]/30 transition-colors">
						<div class="flex-1">
							<h3 class="font-semibold text-gray-800">{event.title}</h3>
							<p class="text-sm text-gray-600 mt-1">{event.description}</p>
							<p class="text-xs text-gray-500 mt-2 font-mono">API ID: {event.apiIdentifier}</p>
						</div>
						<div class="flex gap-2">
							<button
								on:click={() => openEditModal(event)}
								class="p-2 rounded-lg hover:bg-gray-200 text-[#0b3a7a] transition-colors"
								title="Edit Event"
							>
								<i class="fas fa-pen-square text-lg"></i>
							</button>
							<button
								on:click={() => deleteEvent(event.id)}
								class="p-2 rounded-lg hover:bg-red-100 text-red-500 transition-colors"
								title="Delete Event"
							>
								<i class="fas fa-trash text-lg"></i>
							</button>
						</div>
					</div>
				{/each}
			</div>
		{/if}
		</div>
	</div>

	<!-- Sidebar with Information -->
	<div class="lg:col-span-1">
		<div class="bg-[#0b3a7a]/5 rounded-lg p-5 border border-[#0b3a7a]/10 sticky top-4 space-y-6">
			<!-- What are Events -->
			<div>
				<h3 class="text-sm font-bold text-gray-800 mb-2 flex items-center gap-2">
					<i class="fas fa-info-circle text-[#0b3a7a]"></i>
					What are Events?
				</h3>
				<p class="text-xs text-gray-700 leading-relaxed">
					Events represent key moments or visits in your clinical study. Each event can contain multiple forms and data collection points. Events help organize the timeline of your study visits.
				</p>
			</div>

			<!-- Why Events Matter -->
			<div>
				<h3 class="text-sm font-bold text-gray-800 mb-2 flex items-center gap-2">
					<i class="fas fa-question-circle text-[#0b3a7a]"></i>
					Why Events Matter
				</h3>
				<ul class="text-xs text-gray-700 space-y-1.5 leading-relaxed">
					<li class="flex gap-2">
						<span class="text-[#0b3a7a] font-semibold">•</span>
						<span><strong>Organization:</strong> Structure data collection around study visits</span>
					</li>
					<li class="flex gap-2">
						<span class="text-[#0b3a7a] font-semibold">•</span>
						<span><strong>Workflow:</strong> Define which forms are completed at each visit</span>
					</li>
					<li class="flex gap-2">
						<span class="text-[#0b3a7a] font-semibold">•</span>
						<span><strong>Tracking:</strong> Monitor participant progress through study milestones</span>
					</li>
					<li class="flex gap-2">
						<span class="text-[#0b3a7a] font-semibold">•</span>
						<span><strong>Timing:</strong> Enforce study protocols and visit windows</span>
					</li>
				</ul>
			</div>

			<!-- Event Components -->
			<div>
				<h3 class="text-sm font-bold text-gray-800 mb-2 flex items-center gap-2">
					<i class="fas fa-layer-group text-[#0b3a7a]"></i>
					Event Components
				</h3>
				<ul class="text-xs text-gray-700 space-y-1.5">
					<li class="flex gap-2">
						<span class="text-[#0b3a7a]">•</span>
						<span><strong>Title:</strong> Display name of the event (e.g., "Screening", "Baseline")</span>
					</li>
					<li class="flex gap-2">
						<span class="text-[#0b3a7a]">•</span>
						<span><strong>API Identifier:</strong> Unique code for system integration</span>
					</li>
					<li class="flex gap-2">
						<span class="text-[#0b3a7a]">•</span>
						<span><strong>Description:</strong> Details about the event purpose and timing</span>
					</li>
				</ul>
			</div>

			<!-- API Identifier -->
			<div>
				<h3 class="text-sm font-bold text-gray-800 mb-2 flex items-center gap-2">
					<i class="fas fa-key text-[#0b3a7a]"></i>
					API Identifier (Must be Unique)
				</h3>
				<p class="text-xs text-gray-700 leading-relaxed mb-2">
					A unique identifier used in API calls and system references. Each event must have a distinct identifier.
				</p>
				<div class="bg-white border border-gray-300 rounded p-2.5 text-xs">
					<p class="text-gray-600 mb-1"><strong>Examples:</strong></p>
					<p class="font-mono text-gray-700 text-xs">screening, baseline, week_4</p>
					<p class="text-gray-600 text-xs mt-2 leading-relaxed">
						✓ Use lowercase letters, numbers, and underscores<br/>
						✓ No spaces or special characters<br/>
						✓ Must be unique across all events
					</p>
				</div>
			</div>

			<!-- Event Timing -->
			<div>
				<h3 class="text-sm font-bold text-gray-800 mb-2 flex items-center gap-2">
					<i class="fas fa-calendar text-[#0b3a7a]"></i>
					Event Timing & Planning
				</h3>
				<p class="text-xs text-gray-700 leading-relaxed mb-2">
					Define your event sequence based on your study protocol:
				</p>
				<ul class="text-xs text-gray-700 space-y-1">
					<li class="flex gap-2"><span class="text-[#0b3a7a]">→</span> <span><strong>Screening:</strong> Initial eligibility assessment</span></li>
					<li class="flex gap-2"><span class="text-[#0b3a7a]">→</span> <span><strong>Baseline:</strong> Start of study data collection</span></li>
					<li class="flex gap-2"><span class="text-[#0b3a7a]">→</span> <span><strong>Follow-ups:</strong> Regular visit intervals</span></li>
					<li class="flex gap-2"><span class="text-[#0b3a7a]">→</span> <span><strong>Final:</strong> Study completion visit</span></li>
				</ul>
			</div>

			<!-- Best Practices -->
			<div class="bg-white rounded p-3 border border-gray-200">
				<h4 class="text-xs font-semibold text-gray-800 mb-2 flex items-center gap-2">
					<i class="fas fa-lightbulb text-yellow-500"></i>
					Best Practices
				</h4>
				<ul class="text-xs text-gray-700 space-y-1">
					<li class="flex gap-2">
						<span class="text-[#0b3a7a]">→</span>
						<span>Use clear, descriptive event names</span>
					</li>
					<li class="flex gap-2">
						<span class="text-[#0b3a7a]">→</span>
						<span>Use consistent naming for API identifiers</span>
					</li>
					<li class="flex gap-2">
						<span class="text-[#0b3a7a]">→</span>
						<span>Document expected visit timelines</span>
					</li>
					<li class="flex gap-2">
						<span class="text-[#0b3a7a]">→</span>
						<span>Plan events in chronological order</span>
					</li>
				</ul>
			</div>
		</div>
	</div>
</div>

<!-- Modal Overlay -->
{#if showModal}
	<div class="fixed inset-0 bg-black/50 flex items-center justify-center z-50">
		<div class="bg-white rounded-lg shadow-lg p-8 max-w-md w-full mx-4">
			<h2 class="text-xl font-bold text-gray-800 mb-6">
				{isEditing ? 'Edit Event' : 'Add New Event'}
			</h2>

			<form on:submit|preventDefault={saveEvent} class="space-y-4">
				<!-- Title -->
				<div>
					<label class="block text-sm font-medium text-gray-700 mb-2">
						Title
						<span class="text-red-500">*</span>
					</label>
					<input
						type="text"
						bind:value={formData.title}
						class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-[#0b3a7a] focus:border-transparent outline-none"
						placeholder="Enter event title"
					/>
				</div>

				<!-- API Level Identifier -->
				<div>
					<label class="block text-sm font-medium text-gray-700 mb-2">
						API Level Identifier
						<span class="text-red-500">*</span>
					</label>
					<input
						type="text"
						bind:value={formData.apiIdentifier}
						class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-[#0b3a7a] focus:border-transparent outline-none"
						placeholder="e.g. screening, baseline, week_4"
					/>
					<p class="text-xs text-gray-500 mt-1">Unique identifier for API calls</p>
				</div>

				<!-- Description -->
				<div>
					<label class="block text-sm font-medium text-gray-700 mb-2">Description</label>
					<textarea
						bind:value={formData.description}
						class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-[#0b3a7a] focus:border-transparent outline-none"
						placeholder="Enter event description"
						rows="4"
					></textarea>
				</div>

				<!-- Buttons -->
				<div class="flex gap-3 justify-end mt-6 pt-4 border-t">
					<button
						type="button"
						on:click={closeModal}
						class="px-6 py-2 border border-gray-300 text-gray-700 rounded-lg hover:bg-gray-50 font-medium transition-colors"
					>
						CANCEL
					</button>
					<button
						type="submit"
						class="px-6 py-2 bg-[#0b3a7a] text-white rounded-lg hover:bg-[#082654] font-medium transition-colors"
					>
						SAVE
					</button>
				</div>
			</form>
		</div>
	</div>
{/if}

<style>
	:global(body.modal-open) {
		overflow: hidden;
	}
</style>

