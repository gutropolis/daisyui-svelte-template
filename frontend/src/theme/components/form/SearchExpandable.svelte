<script lang="ts">
	import {createEventDispatcher} from 'svelte';
	import IconSearch from '$theme/icons/IconSearch.svelte';

	const dispatch = createEventDispatcher();
	let search="";
	let timeOut;
	let searchlength:number  = 0;
	$:{
		searchlength = search.length;
	}
	// debounce type input
	function watch() {
		clearTimeout(timeOut);
		timeOut = setTimeout(() => {
			dispatch('search', {search});
		}, 400);
	}
</script>

<div class='relative text-right'>
		<span class='absolute right-0 mr-3 mt-[7px]'>
			<IconSearch />
		</span>
	<input
		type='text'
		placeholder='Seach...'
		class='input { searchlength > 0 ?"w-full pl-4" : "w-10 pl-0" }  pr-10 focus:pl-4 bg-transparent focus:w-full relative text-gray-700 border border-gray-300 leading-tight outline-none focus:outline-none focus:border-secondary transitionEffect'
		on:input={watch} bind:value={search}
	/>
</div>