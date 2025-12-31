<script lang="ts">
	export let title: string;
	export let description: string;
	export let targetDate: string;
	export let status: 'completed' | 'in-progress' | 'pending';
	export let completedDate: string | undefined = undefined;
	export let category: string;
</script>

<div class="flex gap-4">
	<!-- Timeline dot and line -->
	<div class="flex flex-col items-center">
		<div
			class="w-4 h-4 rounded-full border-2 border-gray-200 flex items-center justify-center text-white text-xs"
			class:bg-green-500={status === 'completed'}
			class:bg-blue-500={status === 'in-progress'}
			class:bg-gray-400={status === 'pending'}
		>
			{#if status === 'completed'}
				<svg xmlns="http://www.w3.org/2000/svg" class="w-2 h-2" viewBox="0 0 24 24" fill="currentColor">
					<path d="M5 13l4 4L19 7" />
				</svg>
			{:else if status === 'in-progress'}
				<div class="w-2 h-2 rounded-full bg-white"></div>
			{/if}
		</div>
		<slot name="line" />
	</div>

	<!-- Content -->
	<div class="pb-4 flex-1">
		<div class="flex items-start justify-between">
			<div>
				<h4 class="font-semibold text-gray-900">{title}</h4>
				<p class="text-sm text-gray-600 mt-1">{description}</p>
			</div>
			{#if status === 'completed' && completedDate}
				<span class="text-xs text-green-600 font-semibold whitespace-nowrap ml-4">Completed: {completedDate}</span>
			{:else if targetDate}
				<span class="text-xs text-gray-500 whitespace-nowrap ml-4">Target: {targetDate}</span>
			{/if}
		</div>
		<div class="flex gap-2 mt-2">
			<span class="inline-block px-2 py-1 bg-gray-100 text-xs text-gray-600 rounded capitalize">
				{category}
			</span>
		</div>
	</div>
</div>
