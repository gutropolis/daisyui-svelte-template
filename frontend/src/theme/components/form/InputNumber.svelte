<script lang="ts">
  import Input from "$theme/components/form/Input.svelte";
  export let labelClass = "";
  export let w = 'w-auto';
  export let m = 'mb-3';
  export let cls = ''; 
  export let label = "";
  export let name = "";
  export let placeholder = "";
  export let required = false;
  export let value:string|number = "";
  export let disabled = false;
  export let min = 0;
  export let max = 10000;
  export let numberType = "";
  export let orientation = "";
  export let ref = undefined;
  export let toolTipEnable=false;
	export let toolTipText="";
  
  let step = "1";
  let maskOptions = undefined;

  if (numberType === "float") {
    //maskOptions={};
    step = "0.1";
  } else if (numberType === "integer") {
    step = "1";
    maskOptions = { mask: Number, min: Number(min), max: Number(max) };
  }
</script>

<Input
{labelClass}
{w}
{cls}

  type="number"
  {label}
  {name}
  {placeholder}
  {required}
  {disabled}
  {min}
  {max}
  {numberType}
  {orientation}
  {ref}
  {step}
  bind:value
  {maskOptions}
  {toolTipEnable} 
  {toolTipText}
  on:change
/>
