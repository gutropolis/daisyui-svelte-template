<!--
 Copyright (c) 2022. Ankit Patial.
 Unauthorized copying of this file, via any medium is strictly prohibited. Proprietary and confidential.
 Author: Ankit Patial
  -->
<script lang='ts'>
	import flatpickr from 'flatpickr';
	import '$lib/components/form/DatePicker.css';
	import IconCalendar from '$lib/theme/icons/IconCalendar.svelte';
	import { createEventDispatcher, onDestroy  } from 'svelte';
	import Label from '$lib/components/form/Label.svelte';

	export let labelClass = "";
	export let ref = undefined;
	export let id: string = 'txt-' + Date.now();
	export let label = '';
	export let name = '';
	export let placeholder = '';
	export let required = false;
	export let value: Date | undefined;
	export let disabled = false;
	export let className = 'mb-3 relative';
	export let format='Y-m-d';
	export let orientation='';
	export let cls = '';
	export let w = 'w-auto';
	export let m = 'mb-3';
	export let toolTipEnable=false;
	export let toolTipText="";

	let pickr, busy = false, dirty = false, err = '', timeOut, changeTO;

	const inputCls = 'w-full bg-transparent text-gray-700 border border-gray-300 leading-tight focus:outline-none focus:bg-transparent focus:border-secondary z-10';
	const dispatch = createEventDispatcher();
	let datetimeFormatAtt: { altInput?: boolean,altFormat?:string, defaultDate: Date | undefined; dateFormat: string; enableTime: boolean,noCalendar?:boolean } = {
		altInput:false  ,
		altFormat: ''  ,
		defaultDate: value,
		enableTime: false,
		dateFormat:format,
		noCalendar: false,
	}

	$:if (format==='d-M-Y'){
		datetimeFormatAtt = { defaultDate: value, enableTime: false, dateFormat:format }
	}else if (format==='Y-m-d H:i'){
		datetimeFormatAtt = { defaultDate: value, enableTime: true, dateFormat:format }
	}else if (format==='Y-m-d'){
		datetimeFormatAtt = { altInput: true, altFormat: "F j, Y", defaultDate: value, enableTime: false, dateFormat:format }
	}else if (format==='H:i'){
		datetimeFormatAtt = { altInput: true, altFormat: "H:i", defaultDate: value, enableTime: true, dateFormat:format,noCalendar:true }
	}

	if(toolTipEnable){
		labelClass=`${labelClass} flex items-center`;
	}

	$: if (ref) {
		pickr = flatpickr(ref, datetimeFormatAtt);
	}

	 
	function changeVal(e) {
		if (disabled) return;

		const val =  e.target.value;
	 

		if (changeTO) clearTimeout(changeTO);
		changeTO = setTimeout(() => {
			dispatch('change', { name, value: val });
			value=val;
		}, 700);
	}
	onDestroy(() => {
		if (pickr) {
			pickr.destroy();
		}
	});

	function focus() {
		pickr.jumpToDate(value || new Date());
	}
</script>

<div class='flex flex-wrap {orientation === "horizontal" ? 'field-inline' : ''}   {w} {m}'>
	<Label uppercase {id} content={label}  cls={labelClass} {toolTipEnable} {toolTipText}>
		{#if $$slots.alt}
			<slot name='alt'></slot>
		{/if}
	</Label>

	{#if $$slots.group}
		<label class='input-group'>
			<div class='relative text-right'>
			<span class='absolute right-0 mr-3 mt-[7px] bg-white z-20'>
				<IconCalendar />
			</span>
				<input
					id={id}
					class='{inputCls} {w}'
					bind:this={ref}
					{name}
					{required}
					{placeholder}
					{disabled}
					on:input={changeVal}
					on:focus={focus}
				/>
				<slot name='helptext'></slot>
			</div>
			<slot name='group'></slot>
		</label>
	{:else }
		<div class=' {cls} relative text-right'>
		<span class='absolute right-0 mr-3 mt-[7px] bg-white z-20'>
			<IconCalendar />
		</span>
			<input
				{id}
				class='{inputCls} {w}'
				bind:this={ref}
				{name}
				{required}
				{placeholder}
				{disabled}
				on:input={changeVal}
				on:focus={focus}
			/>
			<slot name='helptext'></slot>
		</div>
	{/if}


</div>

