<!--
 Copyright (c) 2022. Ankit Patial.
 Unauthorized copying of this file, via any medium is strictly prohibited. Proprietary and confidential.
 Author: Ankit Patial
  -->
<script lang='ts'>
	import type Entity from '$lib/models/Entity';
	import Label from '$theme/components/form/Label.svelte';
	import { createEventDispatcher } from 'svelte';
	export let labelClass = ""; 
	export let cls = '';
	export let name: string;
	export let label: string = '';
	export let placeholder: string = '';
	export let value: any;
	export let options: [Entity];
	export let multiple = false;
	export let disabled = false;
	export let required = false;
	export let tooltip = '';
	export let orientation='';
	export let w = '';
	export let m = 'mb-3';
	export let toolTipEnable=false;
	export let toolTipText="";

	let style = ' text-gray-700  font-normal leading-tight focus:outline-none ' +
		'focus:bg-white focus:border-secondary';
	const dispatch = createEventDispatcher();
	let id: string = 'rd-' + Date.now(),
		changeTO;

	function change() {
		if (changeTO) clearTimeout(changeTO);
		changeTO = setTimeout(() => {
			dispatch('change', { name, value });
		}, 700);
	}
	if(toolTipEnable){
		labelClass=`${labelClass} flex items-center`;
	}
</script>

<div class='form-control {orientation === "horizontal" ? 'field-inline' : ''}  {w} {m}'>
	<Label uppercase {id} content={label} cls={labelClass}  {toolTipEnable} {toolTipText}>
		{#if $$slots.alt}
			<slot name='alt'></slot>
		{/if}
	</Label>
	<div class='{style} {cls}'>
		{#each options || [] as op}
			<label class='label cursor-pointer inline-flex justify-start mr-5'>
				<input
					type='radio'
					class='w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600 mr-2'
					name={name}
					value={op.id}
					bind:group={value}
					on:change={change}
					{disabled}
					{required}
				/>
				<span class='label-text'>{op.name}</span>
			</label>
		{/each}
	</div>
</div>


<style>
	/* device: tablet/ small screen */
@media (min-width: 640px) {
  
  .field-inline {
	  display: flex;
	  flex-direction: row;
	  column-gap: 1rem;
  }

  .field-inline div{
	  flex-grow: 1;
  }
}
</style>