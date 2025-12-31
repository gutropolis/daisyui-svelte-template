<script lang="ts">
	import StatsCard from './StatsCard.svelte';

	interface EnrollmentMetric {
		title: string;
		current: number;
		target: number;
		progress: number;
	}

	interface Site {
		name: string;
		location: string;
		enrolled: number;
		target: number;
	}

	const enrollmentMetrics: EnrollmentMetric[] = [
		{ title: 'Trial Enrollment Progress', current: 87, target: 150, progress: 58 }
	];

	const sites: Site[] = [
		{ name: 'City General Hospital', location: 'New York, USA', enrolled: 32, target: 50 },
		{ name: 'University Medical Center', location: 'Boston, USA', enrolled: 28, target: 40 }
	];
</script>

<div class="space-y-6">
	<!-- Summary Stats -->
	<div class="grid grid-cols-4 gap-4">
		<StatsCard title="Total Patients" value="3" icon="users" variant="primary" />
		<StatsCard title="Active Patients" value="2" icon="check" variant="success" />
		<StatsCard title="Completed" value="1" icon="checkmark" variant="success" />
		<StatsCard title="Adverse Events" value="1" icon="alert" variant="danger" />
	</div>

	<!-- Enrollment Progress Section -->
	<div class="grid grid-cols-2 gap-6">
		<!-- Trial Enrollment Progress -->
		<div class="bg-white rounded-lg border border-gray-200 p-6">
			<h3 class="font-bold text-gray-900 mb-4">Trial Enrollment Progress</h3>
			<p class="text-sm text-gray-600 mb-6">Current enrollment status by trial</p>
			{#each enrollmentMetrics as metric}
				<div class="space-y-3">
					<div>
						<div class="flex items-center justify-between mb-2">
							<p class="font-semibold text-gray-900 text-sm">{metric.title}</p>
							<p class="text-sm font-bold text-gray-900">{metric.current}/{metric.target}</p>
						</div>
						<div class="w-full bg-gray-200 rounded-full h-2 overflow-hidden">
							<div class="bg-[#0b3a7a] h-full" style="width: {metric.progress}%"></div>
						</div>
					</div>
				</div>
			{/each}
		</div>

		<!-- Site Performance -->
		<div class="bg-white rounded-lg border border-gray-200 p-6">
			<h3 class="font-bold text-gray-900 mb-4">Site Performance</h3>
			<p class="text-sm text-gray-600 mb-6">Enrollment by trial site</p>
			<div class="space-y-4">
				{#each sites as site}
					<div class="border-b border-gray-100 pb-4 last:border-b-0">
						<p class="font-semibold text-gray-900">{site.name}</p>
						<p class="text-xs text-gray-600">{site.location}</p>
						<div class="mt-2">
							<div class="flex items-center justify-between mb-1">
								<p class="text-xs text-gray-500">Site Progress</p>
								<p class="text-sm font-bold text-gray-900">{site.enrolled}/{site.target}</p>
							</div>
							<div class="w-full bg-gray-200 rounded-full h-2 overflow-hidden">
								<div class="bg-green-500 h-full" style="width: {(site.enrolled / site.target) * 100}%"></div>
							</div>
						</div>
					</div>
				{/each}
			</div>
		</div>
	</div>
</div>
