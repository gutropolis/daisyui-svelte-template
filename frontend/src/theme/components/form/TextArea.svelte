<!--
 Copyright (c) 2022. Ankit Patial.
 Unauthorized copying of this file, via any medium is strictly prohibited. Proprietary and confidential.
 Author: Ankit Patial
  -->
<script lang='ts'>
	import Label from '$theme/components/form/Label.svelte';
	import { createEventDispatcher } from 'svelte';

	export let labelClass = "";
	export let name = '';
	export let label = '';
	export let placeholder = '';
	export let required = false;
	export let value = '';
	export let disabled = false;
	export let focus = false;
	export let w = '';
	export let m = ''
	export let ref=undefined;
	export let orientation=undefined;
	export let cls = '';
	export let toolTipEnable=false;
	export let toolTipText="";

	const dispatch = createEventDispatcher();
	let inputCls =
		'textarea  text-gray-700 border border-gray-300  ';
	let id: string = 'ta-' + Date.now(),
		changeTO;

	function changeVal(e) {
		if (disabled) return;
		value = e.target.value;

		if (changeTO) clearTimeout(changeTO);
		changeTO = setTimeout(() => {
			dispatch('change', { name, value });
		}, 700);

	}

	if(toolTipEnable){
		labelClass=`${labelClass} flex items-center`;
	}
</script>

<div class='form-control   w-full mb-0 grid md:grid-cols-3 md:gap-x-4  {orientation === "horizontal" ? 'field-inline' : ''} {w} {m}'>
	<Label uppercase {id} content={label} cls={labelClass} {toolTipEnable} {toolTipText}>
		{#if $$slots.alt}
			<slot name='alt'></slot>
		{/if}
	</Label>
 

		<textarea
			bind:this={ref}
			class='{inputCls} {cls}'
			id={id}
			{required}
			{placeholder}
			{value}
			{disabled}
			on:input={changeVal}
			on:keypress
			on:change
			on:mouseup
		></textarea> 
	 
</div>

