<script lang='ts'>
	import { createEventDispatcher, onDestroy, onMount } from 'svelte';
	import IconSpin from '$theme/icons/IconSpin.svelte';
	import Label from '$theme/components/form/Label.svelte';

	export let labelClass = "";
	export let ref = undefined;
	export let label = '';
	export let name = '';
	export let type: 'text' | 'email' | 'password' = 'text';
	export let placeholder = '';
	export let required = false;
	export let value = '';
	export let disabled = false;
	export let focus = false;
	export let autocomplete = 'off';
	export let maskOptions: object | undefined = undefined;
	export let min = undefined;
	export let max = undefined;
	export let maxlength = undefined;
	export let w = 'w-auto';
	export let m = 'mb-3';
	export let cls = '';
	export let step='';
	export let orientation='';
	export let toolTipEnable=false;
	export let toolTipText="";
	export let validate: (val: any) => Promise<string> = () => {
		return Promise.resolve('');
	};

	const dispatch = createEventDispatcher();
	const id = 'txt-' + Date.now()+Math.random();
	const inputCls = '  w-full text-gray-700 border border-gray-300 leading-tight focus:outline-none ' +
		'focus:bg-white focus:border-secondary';
	let imask, busy = false, dirty = false, err = '', timeOut, changeTO, IMaskLib;

	if(toolTipEnable){
		labelClass=`${labelClass} flex items-center`;
	}

	$:isTip = !!err;
	$:isTipErr = !!err;
	$:tip = err;
	$:if (value) {
		doValidate(value);
	}
	$:if (imask) imask.value = (value || '').toString();

	onMount(async () => {
		if (focus) ref.focus();
		if (maskOptions) {
			const { default: IMask } = await import('imask');
			IMaskLib = IMask;
			imask = new IMaskLib(ref, maskOptions);
			imask.on('accept', () => {  // accept | complete
				setValue(imask.value); // imask.unmaskedValue'
			});
		}
	});

	onDestroy(() => {
		imask && imask.destroy();
	});

	function changeVal(e) {
		if (disabled) return;

		const val = (type === 'number' || type === 'range') ? Number(e.target.value) : e.target.value;
		if (!maskOptions) {
			setValue(val);
		}

		if (changeTO) clearTimeout(changeTO);
		changeTO = setTimeout(() => {
			dispatch('change', { name, value: val });
		}, 700);
	}

	function setValue(val) {
		value = val;
	}

	function doValidate(value) {
		if (timeOut) clearTimeout(timeOut);
		timeOut = setTimeout(() => {
			busy = true;
			err = '';
			validate(value)
				.then((errMsg) => {
					busy = false;
					err = errMsg;
				})
				.catch((ex) => {
					busy = false;
					err = ex.message || ex;
				});
		}, 500);
	}

</script>

<div class='form-control  {orientation === "horizontal" ? 'field-inline' : ''} {w} {m}'>
	<Label uppercase {id} content={label} cls={labelClass}  {toolTipEnable} {toolTipText}>
		{#if $$slots.alt}
			<slot name='alt'></slot>
		{/if}
	</Label>
	<div class='tooltip-top' class:tooltip={isTip} class:tooltip-error={isTipErr} data-tip={tip}>
		{#if $$slots.group}
			<label class='input-group'>
				<input
					class='{inputCls} {cls}'
					class:input-error={isTipErr}
					bind:this={ref}
					{id}
					{name}
					{type}
					{required}
					{placeholder}
					{value}
					{disabled}
					{autocomplete}
					{min}
					{max}
					{maxlength}
					{step}
					on:input={changeVal}
					on:keypress
					on:focus
				/>
				<slot name='group'></slot>
			</label>
		{:else}
			<input
				class='{inputCls} {cls}'
				class:input-error={isTipErr}
				bind:this={ref}
				id={id}
				{name}
				{type}
				{required}
				{placeholder}
				{value}
				{disabled}
				{min}
				{max}
				{maxlength}
				{step}
				{autocomplete}
				on:input={changeVal}
				on:keypress
				on:focus
			/>
		{/if}
		{#if (busy)}
			<div class='relative float-right -mt-10 mr-1'>
				<IconSpin />
			</div>
		{/if}
	</div>
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