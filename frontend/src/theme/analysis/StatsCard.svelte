<script lang="ts">
	export let title: string;
	export let value: string | number;
	export let icon: 'folder' | 'check' | 'hourglass' | 'document' | 'users' | 'checkmark' | 'alert' | 'eye';
	export let variant: 'primary' | 'success' | 'warning' | 'danger' = 'primary';
</script>

<div class="bg-white rounded-lg border border-gray-200 p-5 flex items-center justify-between">
	<div>
		<p class="text-xs text-gray-500 font-semibold uppercase tracking-wide">{title}</p>
		<p class="text-3xl font-bold mt-3" class:text-blue-600={variant === 'primary'} class:text-green-600={variant === 'success'} class:text-amber-600={variant === 'warning'} class:text-red-600={variant === 'danger'}>
			{value}
		</p>
	</div>
	<div
		class="w-12 h-12 rounded-md flex items-center justify-center"
		class:bg-blue-50={variant === 'primary'}
		class:bg-green-50={variant === 'success'}
		class:bg-amber-50={variant === 'warning'}
		class:bg-red-50={variant === 'danger'}
	>
		{#if icon === 'folder'}
			<svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6" class:text-blue-400={variant === 'primary'} class:text-green-400={variant === 'success'} class:text-amber-400={variant === 'warning'} class:text-red-400={variant === 'danger'} fill="none" viewBox="0 0 24 24" stroke="currentColor">
				<path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M3 7a2 2 0 012-2h4l2 2h6a2 2 0 012 2v7a2 2 0 01-2 2H5a2 2 0 01-2-2V7z" />
			</svg>
		{:else if icon === 'check'}
			<svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6" class:text-green-400={variant === 'success'} fill="currentColor" viewBox="0 0 24 24">
				<path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41L9 16.17z" />
			</svg>
		{:else if icon === 'checkmark'}
			<svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6" class:text-green-400={variant === 'success'} fill="currentColor" viewBox="0 0 24 24">
				<path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z" />
			</svg>
		{:else if icon === 'hourglass'}
			<svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6" class:text-amber-400={variant === 'warning'} fill="currentColor" viewBox="0 0 24 24">
				<path d="M6 2h12v6h-12V2zm0 8h12v2H6v-2zm0 4h12v2H6v-2zm12 4H6v2h12v-2z" />
			</svg>
		{:else if icon === 'document'}
			<svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6" class:text-blue-400={variant === 'primary'} fill="currentColor" viewBox="0 0 24 24">
				<path d="M14 2H6a2 2 0 00-2 2v16a2 2 0 002 2h12a2 2 0 002-2V8l-8-6z" />
			</svg>
		{:else if icon === 'users'}
			<svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6" class:text-blue-400={variant === 'primary'} fill="currentColor" viewBox="0 0 24 24">
				<path d="M16 11c1.66 0 2.99-1.34 2.99-3S17.66 5 16 5c-1.66 0-3 1.34-3 3s1.34 3 3 3zm-8 0c1.66 0 2.99-1.34 2.99-3S9.66 5 8 5C6.34 5 5 6.34 5 8s1.34 3 3 3zm0 2c-2.33 0-7 1.17-7 3.5V19h14v-2.5c0-2.33-4.67-3.5-7-3.5zm8 0c-.29 0-.62.02-.97.05 1.16.84 1.97 1.97 1.97 3.45V19h6v-2.5c0-2.33-4.67-3.5-7-3.5z" />
			</svg>
		{:else if icon === 'alert'}
			<svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6" class:text-red-400={variant === 'danger'} fill="currentColor" viewBox="0 0 24 24">
				<path d="M1 21h22L12 2 1 21zm12-3h-2v-2h2v2zm0-4h-2v-4h2v4z" />
			</svg>
		{:else if icon === 'eye'}
			<svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6" class:text-purple-400={variant === 'danger'} fill="currentColor" viewBox="0 0 24 24">
				<path d="M12 4.5C7 4.5 2.73 7.61 1 12c1.73 4.39 6 7.5 11 7.5s9.27-3.11 11-7.5c-1.73-4.39-6-7.5-11-7.5zM12 17c-2.76 0-5-2.24-5-5s2.24-5 5-5 5 2.24 5 5-2.24 5-5 5zm0-8c-1.66 0-3 1.34-3 3s1.34 3 3 3 3-1.34 3-3-1.34-3-3-3z" />
			</svg>
		{/if}
	</div>
</div>
