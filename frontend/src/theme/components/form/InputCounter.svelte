<script lang="ts">
  import type Entity from '$lib/models/Entity';
  import Label from '$theme/components/form/Label.svelte'; 
  import IconUpSide from '$theme/icons/IconUpSide.svelte';
  import IconDownSide from '$theme/icons/IconDownSide.svelte'; 
  import { createEventDispatcher, onDestroy, onMount } from 'svelte';
  import IconSpin from '$theme/icons/IconSpin.svelte'; 
  export let labelClass = ""; 
	export let ref = undefined;
	export let label = '';
	export let name = '';
	export let type = 'text';
	export let placeholder = '0';
	export let required = false;
	export let value = 0;
	export let disabled = false;
	export let focus = false;
	export let autocomplete = 'off'; 
	export let maxlength = undefined;
	export let w = 'w-auto';
	export let m = 'mb-3';
	export let cls = '';
	export let step='';
	export let orientation='';
 

	const dispatch = createEventDispatcher();
	const id = 'txt-' + Date.now();
	const inputCls = 'px-2 text-center  border-r-1  border-l-1 border-gray-300 appearance-none outline-none text-gray-800 w-full bg-transparent ';
	let imask, busy = false, dirty = false, err = '', timeOut, changeTO;
	
	function changeVal(e) {
		if (disabled) return;

		const val = Number(e.target.value);  
		if (changeTO) clearTimeout(changeTO);
		changeTO = setTimeout(() => {
			dispatch('change', { name, value: val });
		}, 700);
	}
 
  function handleDecrement(){  
    if(value >  0){ 
      value=value-1;
    } 
  } 
  function handleIncrement(){   
      value=value+1; 
  } 
</script>
<div
	class='form-control {orientation === "horizontal" ? 'field-inline' : ''} {w} {m} tooltip-top' 
	 
>

	<Label   {id} content={label} cls={labelClass}>
		{#if $$slots.alt}
			<slot name='alt'></slot>
		{/if}
	</Label>


    <div class="my-2 p-1 bg-white    {cls}">
        <div
          class="h-10 w-28 bg-gray-50 flex border file:rounded items-center mt-1 "
        >
            <button
              tabindex="-1"
              for="show_more"
              class="cursor-pointer outline-none focus:outline-none   transition-all text-gray-500 hover:text-blue-600 border-r-0"
              on:click|preventDefault={()=>handleDecrement()}
            >
              <IconUpSide />
            </button>
            <input
                class='{inputCls}' 
                bind:this={ref}
                id={id}
                {name}
                {type}
                {required}
                {placeholder}
                {value}
                {disabled} 
                {maxlength}
                {step}
                {autocomplete}  
                on:keypress
                on:focus
                on:input={changeVal}
              />  
            <button
              tabindex="-1"
              for="show_more"
              class="cursor-pointer outline-none focus:outline-none border-l border-gray-200 transition-all text-gray-500 hover:text-blue-600 border-l-0"
              on:click|preventDefault={()=>handleIncrement()}
              >
              <IconDownSide />
            </button>
      </div>
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