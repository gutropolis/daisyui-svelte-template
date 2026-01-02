<script lang="ts">

 	import Graph from "$lib/components/project/tools/Graph.svelte";
	import InputOutput from "$lib/components/project/tools/InputOutput.svelte";
	import SideElevation from "$lib/components/project/tools/SideElevation.svelte";
	import Table from "$lib/components/project/tools/Table.svelte";
	import IconGraph from "$theme/icons/IconGraph.svelte";
	import IconInputOutput from "$theme/icons/IconInputOutput.svelte";
	import IconSideElevation from "$theme/icons/IconSideElevation.svelte";
	import IconTable from "$theme/icons/IconTable.svelte";
	import Output from "./Output.svelte";
    let items = [{
			label: "Side Elevation",
			value: 1,
			component: SideElevation,
			icon: IconSideElevation
		},
		{
			label: "Input",
			value: 2,
			component: InputOutput,
			icon: IconInputOutput
		},
		{
			label: "Output",
			value: 3,
			component: Output,
			icon: IconInputOutput
		},
		{
			label: "Graph",
			value: 4,
			component: Graph,
			icon: IconGraph
		},
		{
			label: "Table",
			value: 5,
			component: Table,
			icon: IconTable
		}
	] 
    export let activeTabValue = 1;
  
    const handleClick = tabValue => () => (activeTabValue = tabValue);
    $:{
        console.log(activeTabValue)
    }

  </script>
  
 <div class="  border-5 border-[#4C5FD6] rounded-lg w-auto  text-md mt-4    ">
    <ul class="flex justify-end w-full h-8 items-center  ">
        {#each items as item}
    <li  class={activeTabValue === item.value ? 'active bg-[#4C5FD6] text-white rounded-3xl  shadow-xl z-10 mb-9  ' : 'rounded-3xl bg-[#FFFFFF] text-blue-900 shadow-xl z-10 mb-9'} style="box-shadow: -2px 0px 4px 0px #0000001A;">
                <span class=" flex  gap-2    px-4 font-medium py-1  cursor-pointer " on:click={handleClick(item.value)}>
                    <svelte:component this={item.icon}/>
                    {item.label}</span>
            </li>
        {/each}
        </ul>
        {#each items as item}
            {#if activeTabValue == item.value}
            <div class="w-full px-4 pb-4">
                <svelte:component this={item.component} on:manageProject/>
            </div>
            {/if}
        {/each}
 </div>
 