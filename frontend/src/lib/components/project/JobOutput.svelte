<script lang="ts">  
	import IconTabGraph from '$theme/icons/IconTabGraph.svelte';
	import IconSideElevation from '$theme/icons/IconSideElevation.svelte';
	import IconTable from '$theme/icons/IconTable.svelte';
	import IconInputOutput from '$theme/icons/IconInputOutput.svelte';
	import IconClient from '$theme/icons/IconClient.svelte';
    import { onMount } from 'svelte';
    import { writable } from 'svelte/store'; 
    import { cubicInOut } from 'svelte/easing';
    import { crossfade } from 'svelte/transition'; 
	import IconExcavation from '$theme/icons/IconExcavation.svelte';
	import InputOutput from '$lib/components/input-output/InputOutput.svelte';
	import SideElevation from '$lib/components/side-elevation/SideElevation.svelte';
 

    let className = '';
    export { className as class };

    const triggers = [
        { id: 'elevation', title: 'Elevation', icon: IconSideElevation },
        { id: 'table', title: 'Table', icon: IconTable },
        { id: 'io', title: 'Input/Ouput', icon: IconInputOutput },
        { id: 'excavation', title: 'Excavation', icon: IconExcavation },
        { id: 'graph', title: 'Graph', icon: IconTabGraph }
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
              <li class="me-2 inline-block align-top">
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
      <div class="bg-white p-3 shadow-md" id="elevationTabpanel">
          <SideElevation />
       </div>
      <div  class="bg-white p-3 shadow-md">
          
      </div>
      <div  class="bg-white p-3 shadow-md">
          
      </div>
      <div   class=" bg-white p-3 shadow-md">
          
      </div>
       
  </div>