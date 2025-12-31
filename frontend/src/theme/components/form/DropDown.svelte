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
	export let name = '';
	export let label = '';
	export let placeholder: string = '';
	export let value: any;
	export let options: [Entity];
	export let multiple = false;
	export let disabled = false;
	export let required = false;
	export let tooltip = '';
	export let labelTop = false;
	export let w = 'w-full';
	export let m = 'mb-3';
	export let cls = '';
	export let orientation='';
	export let ref = undefined;
	export let toolTipEnable=false;
	export let toolTipText="";

	const dispatch = createEventDispatcher();

	let id: string = 'ddl-' + Date.now();
	let style = 'text-gray-700 border border-gray-300 font-normal leading-tight focus:outline-none ' +
		'focus:bg-white focus:border-secondary';

	if (multiple && !Array.isArray(value)) {
		value = [].concat(value);
	}

	function change() {
		dispatch('change', { name, value });
	}
	if(toolTipEnable){
		labelClass=`${labelClass} flex items-center`;
	}
</script>

<div
	class='form-control {orientation === "horizontal" ? 'field-inline' : ''} {w} {m} tooltip-top'
	class:tooltip={!!tooltip}
	class:labelTop={labelTop}
	data-tip={tooltip}
>

	<Label   {id} content={label} cls={labelClass} {toolTipEnable} {toolTipText}>
		{#if $$slots.alt}
			<slot name='alt'></slot>
		{/if}
		
	</Label>


	{#if multiple}
			<select multiple {id} class='{style} {cls}' bind:this={ref} bind:value={value} {disabled} {required} on:change={change}>
			{#if placeholder}
				<option disabled>{placeholder}</option>
			{/if}
			{#each (options || []) as option}
				<option value={option.id}>{option.name}</option>
			{/each}
		</select>
	{:else }
		<select id={id} class='{style} {cls}' bind:value={value} {disabled} {required} on:change={change}>
			{#if placeholder}
				<option disabled>{placeholder}</option>
			{/if}
			{#each (options || []) as option}
				<option value={option.id}>{option.name}</option>
			{/each}
		</select>
	{/if}

	{#if $$slots.desc}
		<label class='label p-0 mt-0.5'>
			<span class='label-text-alt'>
				<slot name='desc'></slot>
			</span>
		</label>
	{/if}
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