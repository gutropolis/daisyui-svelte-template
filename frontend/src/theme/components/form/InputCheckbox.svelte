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
	export let w = ' ';
	export let m = 'mb-3';
	export let orientation='';
	export let ref=undefined;
	export let toolTipEnable=false;
	export let toolTipText="";
	const dispatch = createEventDispatcher();
	let id: string = 'chk-' + Date.now(),
		changeTO;

	if (multiple && !Array.isArray(value)) {
		value = [].concat(value);
	}
	if(toolTipEnable){
		labelClass=`${labelClass} flex items-center`;
	}

	function change() {
		if (changeTO) clearTimeout(changeTO);
		changeTO = setTimeout(() => {
			dispatch('change', { name, value });
		}, 700);
	}
</script>

{#if multiple}
	<div class='form-control class:field-inline ={orientation === "horizontal"} {w} {m}'>
		<Label uppercase {id} content={label}  {toolTipEnable} {toolTipText}>
			{#if $$slots.alt}
				<slot name='alt'></slot>
			{/if}
		</Label>
		{#each options || [] as op}
			<label class='label cursor-pointer inline-flex justify-start'>
				<input
					type='checkbox'
					class='checkbox checkbox-sm checkbox-secondary mr-2'
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
{:else }
	<div class='form-control {w} {m}'>
		<label class='label cursor-pointer inline-flex justify-start'>
			<input
				type='checkbox'
				class='checkbox checkbox-sm checkbox-secondary mr-2'
				bind:checked={value}
				on:change={change}
				{disabled}
				{required}
				{ref}
			/>
			<span class='label-text'>{label}</span>
		</label>
	</div>
{/if}

