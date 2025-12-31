<script lang="ts">
	import TimelineEvent from './TimelineEvent.svelte';

	interface TimelineEvent {
		id: string;
		title: string;
		description: string;
		date: string;
		category: 'Planning' | 'Regulatory' | 'Enrollment' | 'Data Management';
		status: 'completed' | 'in-progress' | 'pending';
		targetDate?: string;
	}

	const timelineEvents: TimelineEvent[] = [
		{
			id: '1',
			title: 'Protocol Finalization',
			description: 'Complete and approve clinical trial protocol',
			date: '28/11/2023',
			category: 'Planning',
			status: 'completed',
			targetDate: '1/12/2023'
		},
		{
			id: '2',
			title: 'IRB Approval',
			description: 'Obtain institutional Review Board approval',
			date: '12/1/2024',
			category: 'Regulatory',
			status: 'completed',
			targetDate: '15/1/2024'
		},
		{
			id: '3',
			title: 'First Patient in',
			description: 'Enroll first patient in the study',
			date: '3/2/2024',
			category: 'Enrollment',
			status: 'completed',
			targetDate: '1/2/2024'
		},
		{
			id: '4',
			title: '50% Enrollment',
			description: 'Reach 50% of target enrollment',
			date: '',
			category: 'Enrollment',
			status: 'in-progress',
			targetDate: '1/6/2024'
		},
		{
			id: '5',
			title: 'Database Lock',
			description: 'Lock clinical database for analysis',
			date: '',
			category: 'Data Management',
			status: 'pending',
			targetDate: '15/1/2025'
		}
	];
</script>

<div class="space-y-6">
	<!-- Trial Info Cards -->
	<div class="grid grid-cols-3 gap-6">
		<div class="bg-white rounded-lg border border-gray-200 p-6">
			<h3 class="font-bold text-gray-900 mb-4">Trial Information</h3>
			<div class="space-y-3">
				<div>
					<p class="text-xs text-gray-500 uppercase tracking-wide font-semibold">Phase</p>
					<p class="text-base font-bold text-gray-900 mt-1">Phase II</p>
				</div>
				<div>
					<p class="text-xs text-gray-500 uppercase tracking-wide font-semibold">Therapeutic Area</p>
					<p class="text-base font-bold text-gray-900 mt-1">Oncology</p>
				</div>
				<div>
					<p class="text-xs text-gray-500 uppercase tracking-wide font-semibold">Sponsor</p>
					<p class="text-base font-bold text-gray-900 mt-1">BioPharma Inc.</p>
				</div>
				<div>
					<p class="text-xs text-gray-500 uppercase tracking-wide font-semibold">Start Date</p>
					<p class="text-base font-bold text-gray-900 mt-1">15/1/2024</p>
				</div>
			</div>
		</div>

		<div class="bg-white rounded-lg border border-gray-200 p-6">
			<h3 class="font-bold text-gray-900 mb-4">Enrollment Progress</h3>
			<div class="space-y-3">
				<div>
					<p class="text-xs text-gray-500 uppercase tracking-wide font-semibold">Current</p>
					<p class="text-base font-bold text-gray-900 mt-1">87 patients</p>
				</div>
				<div>
					<p class="text-xs text-gray-500 uppercase tracking-wide font-semibold">Target</p>
					<p class="text-base font-bold text-gray-900 mt-1">150 patients</p>
				</div>
				<div>
					<p class="text-xs text-gray-500 uppercase tracking-wide font-semibold">Progress</p>
					<p class="text-base font-bold text-gray-900 mt-1">58%</p>
					<div class="w-full bg-gray-200 rounded-full h-2 mt-2 overflow-hidden">
						<div class="bg-[#0b3a7a] h-full" style="width: 58%"></div>
					</div>
				</div>
			</div>
		</div>

		<div></div>
	</div>

	<!-- Timeline -->
	<div class="bg-white rounded-lg border border-gray-200 p-6">
		<h3 class="font-bold text-gray-900 mb-6">Milestone Timeline</h3>
		<div class="space-y-4">
			{#each timelineEvents as event, idx}
				<TimelineEvent
					title={event.title}
					description={event.description}
					status={event.status}
					targetDate={event.targetDate || ''}
					completedDate={event.date}
					category={event.category}
				>
					<svelte:fragment slot="line">
						{#if idx < timelineEvents.length - 1}
							<div class="w-0.5 h-16 bg-gray-200 mt-2"></div>
						{/if}
					</svelte:fragment>
				</TimelineEvent>
			{/each}
		</div>
	</div>
</div>
