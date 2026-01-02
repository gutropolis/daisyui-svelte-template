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
	import SideBarSummery from './SideBarSummery.svelte';
	import IconProject from '$theme/icons/IconProject.svelte';
	import IconDocument from '$theme/icons/IconDocument.svelte';
	import IconEdit from '$theme/icons/IconEdit.svelte';
  
	//export let project:Project ;

	$: project = $projectStore; 
	let formId="project-add";
    let  busy = false, err, readOnly = false;
	
	const client = getContextClient();
	const dispatch = createEventDispatcher();
    // Function to handle the button click
    function handleClick() {
        // Dispatch a custom event named 'editProject'
        dispatch("manageProject", { open: true});
    } 
	$:if(project.name){
		console.log("Project>>Client",project.name)
	}
</script>

<div class="   border-1 rounded-lg text-[#546680] bg-white shadow-sm  p-4  " style="box-shadow: 0px 0px 4px 0px #00000033;">
    {#if project.name && project.name!=""} 
        <div class="w-80   border-1 rounded-lg text-[#546680] bg-white shadow-sm p-2   " style="box-shadow: 0px 0px 4px 0px #00000033;">
            <span class="text-md font-semibold text-blue-500">DETAILS</span>
            <ul> 
                <li class="flex  gap-2">
                    <span class="font-semibold w-[30%] text-right">Client:</span>
                    <p class="w-[70%]">{project.name}</p>
                </li>
                <li class="flex  gap-2">
                    <span class="font-semibold  w-[30%] text-right">Site:</span>
                    <p>{project.siteOffice}</p>
                </li>
                <li class="flex  gap-2">
                    <span class="font-semibold w-[30%] text-right">Attn:</span>
                    <p>{project.jobDesigner}</p>
                </li>
                <li class="flex  gap-2">
                    <span class="font-semibold w-[30%] text-right">Tel:</span>
                    <p>{project.tel}</p>
                </li>
                <li class="flex  gap-2">
                    <span class="font-semibold w-[30%] text-right">Fax:</span>
                    <p>{project.fax}</p>
                </li>
                <hr class="border-t-2 border-blue-600 my-2" />
                <li class="flex  gap-2">
                    <span class="font-semibold w-[30%] text-right">Ref:</span>
                    <p>{project.ref}</p>
                </li>
                <li class="flex  gap-2">
                    <span class="font-semibold  w-[30%] text-right">Page:</span>
                    <p>3</p>
                </li>
                <li class="flex  gap-2">
                    <span class="font-semibold  w-[30%] text-right">Date:</span>
                    <p>1.2.24</p>
                </li>
                {#if project.sheet && project.sheet.sheetName!=""}
                    <hr class="border-t-2 border-blue-600 my-2" />
                    <li class="flex  gap-2">
                        <span class="font-semibold  w-[30%] text-right">Sheet:</span>
                        <p>{project.sheet?.sheetName}</p>
                    </li>
                    <li class="flex  gap-2">
                        <span class="font-semibold  w-[30%] text-right">Pressure:</span>
                        <p>{project.excavation?.pressureModel.toUpperCase()} (m={project.excavation?.terzaghiM}; a={project.excavation?.terzaghiA})</p>
                    </li>
                    <li class="flex  gap-2">
                        <span class="font-semibold  w-[30%] text-right">Toe:</span>
                        <p>{project.excavation?.toe}</p>
                    </li>
                    <hr class="border-t-2 border-blue-600 my-2" />
                {/if}    
            </ul>
            <div class="mt-4">
                <table class="w-full ">
                    <thead class="bg-blue-100">
                        <tr>
                            <th></th>
                            <th>MAXIMUM</th>
                            <th>d(m)</th>
                        </tr>
                    </thead>
                    <tbody class="bg-slate-100">
                        <tr>
                            <td> <span class=" ml-2 inline-block w-2 h-2 bg-black rounded-full"></span></td>
                            <td class=" ">70.3 kN/m3</td>
                            <td>0.00</td>
                        </tr>
                        <tr>
                            <td><span class="ml-2 inline-block w-2 h-2 border border-red-600"></span></td>
                            <td class="flex items-center">6402.9 kN/m/m</td>
                            <td>8.19</td>
                        </tr>
                        <tr>
                            <td>
                                <span class="ml-2 inline-block w-2 h-2 border border-green-600 transform rotate-45"
                                ></span>
                            </td>
                            <td class="flex items-center">449.2 kN/m</td>
                            <td>18.16</td>
                        </tr>
                        <tr>
                            <td><span class="ml-2 inline-block w-2 h-2 bg-purple-700 rounded-full"></span></td>
                            <td class="flex items-center">10745.3 mm</td>
                            <td>31.97</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            
        </div> 
    {/if}
    <button type="button" 
    class="w-full text-white bg-[#2557D6] hover:bg-[#2557D6]/90 focus:ring-4 focus:ring-[#2557D6]/50 focus:outline-none font-medium rounded-lg text-large px-5 py-2.5 text-center inline-flex justify-center items-center dark:focus:ring-[#2557D6]/50 mb-2 mt-6"
    on:click={handleClick}
    >
        <!-- SVG Icon for sheet pile -->
        <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
            <path stroke-linecap="round" stroke-linejoin="round" d="M2 12h20M2 6h20M2 18h20"></path>
        </svg>
        Edit Project
    </button>
      
        
</div>