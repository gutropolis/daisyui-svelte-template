<script lang="ts">
 
	import type { Project } from '$lib/models/Project'; 
	import DropDown from '$theme/components/form/DropDown.svelte';
	import Input from '$theme/components/form/Input.svelte';
	import NextPreviousBtn from '$theme/components/button/NextPreviousBtn.svelte';
	import { projectStore } from '$lib/stores/project';
	import { SaveProjectClientMutation } from '$lib/gql/projectclient';
	import { getContextClient } from '@urql/svelte';
	import { createEventDispatcher } from 'svelte';
	import { camelize } from '$lib/utils/string';
	import SideBarSummery from '$lib/components/project/tools/SideBarSummery.svelte';
	import PileDesignCanvas from '$lib/components/project/wall/PileDesignCanvas.svelte';
   
	//export let project:Project ;
	let soilLayers = [
		{ name: "Topsoil", depthStart: 0, depthEnd: 3, color: "#d3fffb" },
		{ name: "Clay", depthStart: 3, depthEnd: 7, color: "#ff980078" },
		{ name: "Sand", depthStart: 7, depthEnd: 10, color: "#b9a7a1" }
	];
	$: project = $projectStore; 
	let formId="project-add";
    let  busy = false, err, readOnly = false;
	
	const client = getContextClient();
	const dispatch = createEventDispatcher();
	 
	$:if(project.name){
		console.log("Project>>Client",project.name)
	}
</script>
<div class=" flex w-full h-[680px] gap-4 ">
    <SideBarSummery on:manageProject /> 
	<div   class="flex-1   flex-col  border-1 h-full p-5 w-full  bg-white shadow-sm   rounded-lg" style="box-shadow: 0px 0px 4px 0px #00000033;display: inline-block;">
        
		<PileDesignCanvas   />
    </div>
</div>