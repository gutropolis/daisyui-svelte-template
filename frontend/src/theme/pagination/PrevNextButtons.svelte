<script lang='ts'>

	import { createEventDispatcher } from 'svelte';
	import IconChevronLeft from '$theme/icons/IconChevronLeft.svelte';
	import IconChevronRight from '$theme/icons/IconChevronRight.svelte';

	export let hasPrevious = false;
	export let hasNext = false;

	const dispatch = createEventDispatcher();

	function previousPage() {
		dispatch('previous');
	}

	function nextPage() {
		dispatch('next');
	}
</script>

{#if hasNext || hasPrevious}
<nav class="flex items-center flex-column flex-wrap md:flex-row justify-between p-4" aria-label="Table navigation">
    <span class="text-sm font-normal text-gray-500 dark:text-gray-400 mb-4 md:mb-0 block w-full md:inline md:w-auto">
        Showing 
        <span class="font-semibold text-gray-900 dark:text-white">1-10</span> 
        of 
        <span class="font-semibold text-gray-900 dark:text-white">1000</span>
    </span>
    <ul class="inline-flex -space-x-px rtl:space-x-reverse text-sm h-8">
        <li>
            <button
                on:click={previousPage} 
                disabled={!hasPrevious} 
                class="flex items-center justify-center px-3 h-8 ms-0 leading-tight text-gray-500 bg-white border border-gray-300 rounded-s-lg hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white
                disabled:bg-gray-200 disabled:text-gray-400 disabled:dark:bg-gray-700 disabled:dark:text-gray-500"
            >
                Previous
            </button>
        </li>
        <li>
            <button
                on:click={nextPage} 
                disabled={!hasNext} 
                class="flex items-center justify-center px-3 h-8 leading-tight text-gray-500 bg-white border border-gray-300 rounded-e-lg hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white
                disabled:bg-gray-200 disabled:text-gray-400 disabled:dark:bg-gray-700 disabled:dark:text-gray-500"
            >
                Next
            </button>
        </li>
    </ul>
</nav>
	 
{/if}