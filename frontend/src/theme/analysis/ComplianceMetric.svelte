<script lang="ts">
	export let title: string;
	export let description: string;
	export let value: number;
	export let progress: number;
	export let status: 'compliant' | 'warning' | 'non-compliant';
</script>

<div class="space-y-2">
	<div class="flex items-start justify-between">
		<div>
			<p class="font-semibold text-gray-900 text-sm">{title}</p>
			<p class="text-xs text-gray-500">{description}</p>
		</div>
		<p
			class="text-lg font-bold"
			class:text-green-600={status === 'compliant'}
			class:text-amber-600={status === 'warning'}
			class:text-red-600={status === 'non-compliant'}
		>
			{value}%
		</p>
	</div>
	<div class="w-full bg-gray-200 rounded-full h-2 overflow-hidden">
		<div
			class="h-full transition-all"
			class:bg-green-600={status === 'compliant'}
			class:bg-amber-500={status === 'warning'}
			class:bg-red-600={status === 'non-compliant'}
			style="width: {progress}%"
		></div>
	</div>
	<p class="text-xs font-semibold mt-1" class:text-green-600={status === 'compliant'} class:text-amber-600={status === 'warning'} class:text-red-600={status === 'non-compliant'}>
		{status.replace('-', ' ').toUpperCase()}
	</p>
</div>
