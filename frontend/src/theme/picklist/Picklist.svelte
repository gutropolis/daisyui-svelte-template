<script lang="ts">
    import { createEventDispatcher } from 'svelte';
	import type { Soil as SoilInterface } from '$lib/models/PileDesign';  
	import { projectStore } from '$lib/stores/project'; 
    
    export let soils: SoilInterface[] = [];
    const dispatch = createEventDispatcher();

    // Function to dispatch the remove event
	function removeSoil(slug: string) {
        dispatch('remove', { slug });
    }
    function editSoil(slug: string) {
        dispatch('edit', { slug });
    }
</script>

<div class="overflow-x-auto">
    <table class="min-w-full table-auto border-collapse">
        <thead class="bg-gray-200">
            <tr>
                <th class="px-4 py-2 text-left font-bold border-b">m</th>
                <th class="px-4 py-2 text-left font-bold border-b">Passive Side</th>
                <th class="px-4 py-2 text-left font-bold border-b">Action</th> <!-- New column for the action -->
            </tr>
        </thead>
        <tbody>
            {#if soils.length > 0}
                {#each soils as soil}
                    
                        <tr class="hover:bg-gray-100"> <!-- Row hover effect -->
                            <td class="border-b px-4 py-2">{soil.depth}m</td>
                            <td class="border-b px-4 py-2">{soil.name} {soil.slug}</td>
                            <td class="border-b px-4 py-2 text-right">
                                <button on:click={() => removeSoil(soil.slug)} class="text-red-500 hover:text-red-700">
                                    <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                                        <path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" />
                                    </svg>
                                </button>
                                <button on:click={() => editSoil(soil.slug)} class="text-red-500 hover:text-red-700">
                                    <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                                        <path stroke-linecap="round" stroke-linejoin="round" d="M12 20h9m-5.5-3.5l5-5-3-3-5 5m1.5 1.5l-7.5 7.5-2.5 1 1-2.5L14 8.5z" />
                                      </svg>
                                </button>
                            </td>
                        </tr>
                     
                {/each}
            {:else}
                <tr class="hover:bg-gray-100">
                    <td class="border-b px-4 py-2" colspan="3">No soil is chosen</td>
                </tr>
            {/if}
        </tbody>
    </table>
</div>
