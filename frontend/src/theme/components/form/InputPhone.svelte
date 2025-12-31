<script lang='ts'>
	import Input from '$theme/components/form/Input.svelte';

	export let label = '';
	export let name = '';
	export let placeholder = '';
	export let required = false;
	export let value = '';
	export let disabled = false;
	export let orientation='';
	export let ref=undefined;
</script>

<Input
	type='text'
	{label}
	{name}
	{placeholder}
	{required}
	{disabled}
	{orientation}
	{ref}
	bind:value={value}
	maskOptions={{ mask: '(000) 000-0000' }}
/>

