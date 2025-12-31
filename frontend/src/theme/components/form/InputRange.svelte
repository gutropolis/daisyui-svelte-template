<script lang='ts'>
	import Label from '$theme/components/form/Label.svelte';
	import { createEventDispatcher } from 'svelte';

	export let name = '';
	export let label = '';
	export let required = false;
	export let disabled = false;
	export let value = 0;
	export let min = '';
	export let max = '';
	export let tooltip = '';
	export let w = 'w-auto';
	export let m = 'mb-3';
  export let orientation='';
	export let ref=undefined;
	const dispatch = createEventDispatcher();
	const id = 'rng-' + Date.now();

	$:isTip = !!tooltip;
	$:tip = tooltip;

	function change(e) {
		dispatch('change', { name, value: e.target.value });
	}
</script>


<div class='form-control  {orientation === "horizontal" ? 'field-inline' : ''}  {w} {m}'>
	<Label uppercase {id} content={label}>
		{#if $$slots.alt}
			<slot name='alt'></slot>
		{/if}
	</Label>
	<div class='tooltip-top' class:tooltip={isTip} data-tip={tip}>
		<input
			class='range range-secondary range-xs'
			type='range'
			{name}
			{required}
			{disabled}
			{min}
			{max}
			{ref}
			bind:value
			class:tooltip={!!tooltip} data-tip={tooltip}
			on:keypress
			on:change={change}
		/>
	</div>
	{#if $$slots.desc}
		<label class='label p-0 mt-0.5'>
			<span class='label-text-alt'>
				<slot name='desc'></slot>
			</span>
		</label>
	{/if}
</div>


