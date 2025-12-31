<script lang='ts'>
	import { createEventDispatcher } from 'svelte';
	import Label from '$theme/components/form/Label.svelte';

	export let label = '';
	export let name = '';
	export let required = false;
	export let disabled = false;
	export let value = false;
	export let tooltip = '';
	export let orientation='';

	const dispatch = createEventDispatcher();

	function changeVal(e) {
		if (disabled) return;
		value = e.target.checked;
		dispatch('change', value);
	}
</script>

<div class='form-control  {orientation === "horizontal" ? 'field-inline' : ''}  w-full mb-3'>
	{#if label}
		<Label uppercase content={label}>
		</Label>
	{/if}

	<input
		type='checkbox'
		class='toggle toggle-sm toggle-secondary'
		class:toggle-success={true}
		{name}
		{required}
		{disabled}
		checked={value}
		on:input={changeVal}
		on:keypress
		class:tooltip={!!tooltip} data-tip={tooltip}
	/>
</div>

