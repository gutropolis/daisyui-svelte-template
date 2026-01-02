<script lang="ts"> 
	import IconSave from '$theme/icons/IconSave.svelte';
	import IconGraph from '$theme/icons/IconGraph.svelte';
	import IconClient from '$theme/icons/IconClient.svelte';
    import { onMount } from 'svelte';
    import { writable } from 'svelte/store'; 
    import { cubicInOut } from 'svelte/easing';
    import { crossfade } from 'svelte/transition';
    import Excavation from '$lib/components/project/Excavation.svelte'
    import Soil from '$lib/components/project/Soil.svelte'
    import Support from '$lib/components/project/Support.svelte'
    import Wall from '$lib/components/project/Wall.svelte'
	import IconExcavation from '$theme/icons/IconExcavation.svelte';
	import IconSoil from '$theme/icons/IconSoil.svelte';
	import IconWall from '$theme/icons/IconWall.svelte';
	import IconSupport from '$theme/icons/IconSupport.svelte';

   

    let className = '';
    export { className as class };

    const triggers = [
        { id: 'job', title: 'Job', icon: IconClient },
        { id: 'excavation', title: 'Excavation', icon: IconExcavation },
        { id: 'soil', title: 'Soil', icon: IconSoil },
        { id: 'wall', title: 'Wall', icon: IconWall },
        { id: 'support', title: 'Support', icon: IconSupport },
    ];

    const [send, receive] = crossfade({
        duration: 250,
        easing: cubicInOut,
    });

</script>

<div class="w-full pt-5"  >

  <div class="tabitem mb-5 shadow-md bg-white">
        <ul class="block -mb-px tablist overflow-x-auto whitespace-nowrap flex-nowrap">
        {#each triggers as triggerItem}
            <li class="me-2 inline-block align-top"
            >
            <button 
                type="button"  
                class="block px-3 py-3 border-b-2 border-transparent hover:text-blue-600 hover:border-blue-600 relative font-semibold text-sm"
               >
               <i class="inline-block me-2 align-middle"><svelte:component this={triggerItem.icon} /></i>
               {triggerItem.title}
               <!-- {#if $value === triggerItem.id}
                <div
                    in:send={{ key: 'test' }}
                    out:receive={{ key: 'sts' }}
                    class="absolute left-0 h-1 w-full bottom-0 rounded-0 bg-blue-600"
                />
                {/if} -->
            </button>
            </li>
        {/each}
            
        </ul>
    </div>
    <div   class="bg-white p-3 shadow-md">
        <Excavation />
     </div>
    <div   class="bg-white p-3 shadow-md">
        <Excavation />
    </div>
    <div   class="bg-white p-3 shadow-md">
        <Soil />
    </div>
    <div  class=" bg-white p-3 shadow-md">
        <Wall />
    </div>
    <div   class="bg-white p-3 shadow-md">
        <Support />
    </div>
</div>