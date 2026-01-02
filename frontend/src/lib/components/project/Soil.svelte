<script lang="ts">
	import type Entity from '$lib/models/Entity';
    import type { Soil as SoilInterface  } from '$lib/models/PileDesign';  
	import type { ProjectExcavation, ProjectSoil } from '$lib/models/Project';
	import { projectStore } from '$lib/stores/project';
	import DropDown from '$theme/components/form/DropDown.svelte';
    import IconPlus from '$theme/icons/IconPlus.svelte';
	import Picklist from '$theme/picklist/Picklist.svelte';
	import { getContextClient } from '@urql/svelte';
	import CohesivePressureType from './soil/CohesivePressureType.svelte';
	import PressureModelType from './soil/PressureModelType.svelte';
	import SoilLayer from './soil/SoilLayer.svelte';
	import { createEventDispatcher } from 'svelte';
	import { RemoveSoilMutation } from '$lib/gql/projectclient';
	import { handleGqlErr } from '$lib/utils/gqlfx';
	import alerts from '$lib/stores/alerts';
    
    export let soils:SoilInterface[]=[];
    export let projectID:string="";

    const dispatch = createEventDispatcher();
	const client = getContextClient();
    
    let soilSlug= "";
    let projSoils:SoilInterface[]=[]; 
    let soil:ProjectSoil= {
            depth:"", 
            name:"", 
            slug:"", 
            type:"", 
            unitWeight:"", 
            effectiveUnitWeight:"", 
            cohesion:"", 
            adhesion:"", 
            internalFriction:"", 
            wallFrictionAngle:"", 
            kActive:"", 
            kPassive:"", 
            kAc:"", 
            kPc:"",  
            orderBy:0,
        }

    let defaultExcavation: ProjectExcavation = { 
		depth:"",  
		activeWaterDepth:0.0,  
		passiveWaterDepth:0.0,  
		surcharge:0.0, 
		waterDensity:0.0,  
		miniFluidDensity:0.0,
		slopeType:"", 
		activeSlopeAngle:0.0,
		passiveSlopeAngle:0.0,
		calculationMethod: "k" ,
		penetrationTypes:"",
		applyRuleThumb:false,
		name:'', 
		pressureModel:'', 
		cohesivePressureType:'', 

		terzaghiM:0,
        terzaghiA :0,
        showWater:false,
        tensionCrackDepth:0,
        applyPassiveSoft:false,
        softPassiveThickness:0
	};
	let projExcavation=$projectStore.excavation?$projectStore.excavation:defaultExcavation;
    
    function handleSaveSoil(e){
        // Step 1: Get soil with all info
        let projSoil = e.detail.soilInfo;

        // Step 2: Fetch all soils from store
        let projSoils = $projectStore.soils ? $projectStore.soils : [];

        // Step 3: Check if projSoil has no slug, generate one
        if (!projSoil.slug || projSoil.slug === "") {
            projSoil.slug = (new Date().getTime()).toString(36);  // Generate slug
        }

        // Step 4: Check if projSoil.slug exists in projSoils
        let existingSoilIndex = projSoils.findIndex(soil => soil.slug === projSoil.slug);

        if (existingSoilIndex !== -1) {
            // Overwrite the existing soil if slug matches
            projSoils[existingSoilIndex] = projSoil;
        } else {
            // Otherwise, add the new soil
            projSoils = projSoils.concat(projSoil);  // Add new soil object
        }

        // Update the store with the new soils array
        $projectStore.soils = [...projSoils];

        // Optionally reset soilSlug
        let soilSlug = "";
    }
    async function handleRemoveSoil(e){

        let slugToRemove=e.detail.slug;
        console.log("Handle Remove",projSoils,slugToRemove)
        if(projSoils.length  > 0 ){
            projSoils = projSoils.filter(soil => soil.slug !== slugToRemove);
            $projectStore.soils=projSoils;
            await removeSoil(slugToRemove)  
        }
       
        soilSlug="";
    }
    function handleEditSoil(e){
        console.log("handle edit soil ",e.detail);
        soilSlug=e.detail.slug;
        soil = filterSoilsBySlug(projSoils,soilSlug);
        console.log("Soil Slug for Edit",soilSlug);
         
    }
    
	
    async function removeSoil(slug:string="") {
    
        const title="Project Soil";
        // Save the Connector
        const res = await client
            .mutation(RemoveSoilMutation, { projectId:projectID,slug:slug})
            .toPromise();

        
        if (res.error) {
            const errMsg = handleGqlErr(res.error);
            alerts.error(title, errMsg);
            return "";
        }

        const result =res.data.removeSoil;

        if (result.status) { 
            alerts.success(title,"Soil have removed successfully!!");  
            return soil.slug;
        }  
        return "";
    } 

    function filterSoilsBySlug(projSoils, slug) {
        return projSoils.find(soil => soil.slug === slug);
    }

	$:{
		$projectStore.excavation=projExcavation;
        projSoils=$projectStore.soils?$projectStore.soils:[] ;
		console.log("Project Excavation", $projectStore)
	}
	
</script>
{#if  projectID!=""}
    <div class="flex flex-col md:flex-row">
        <div class="w-full md:w-1/2 p-2"> <!-- First column -->
            <div class="mb-6">
                <Picklist soils={projSoils} on:edit={handleEditSoil} on:remove={handleRemoveSoil} />
            </div>
            {#if soils.length > 0  }
                <SoilLayer {projectID} {soils} {soil}  slug={soilSlug} on:save={handleSaveSoil}   />
            {/if}
            
        </div>
        <div class="w-full md:w-1/2 p-2"> <!-- Second column -->
            <fieldset class="p-4 pb-2 ">
                <legend class="text-sm font-medium text-gray-900 px-2 text-medium">Pressure Model</legend>
                <PressureModelType bind:modelType={projExcavation.pressureModel} />
                <hr class="mb-2" />
                <div class="grid gap-2 mb-3 xsm:grid-cols-2">
                    <div title="m">
                        <label for="" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                            >m</label
                        >
                        <input type="number" bind:value={projExcavation.terzaghiM}  class="bg-slate-50 border border-gray-300 text-gray-900 text-sm rounded focus:border-s block w-full px-2.5 py-1.5" placeholder="m" />
                    </div>
                    <div title="a">
                        <label for="" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                            >a</label
                        >
                        <input type="number"  bind:value={projExcavation.terzaghiA}  class="bg-slate-50 border border-gray-300 text-gray-900 text-sm rounded focus:border-s block w-full px-2.5 py-1.5" placeholder="a" />
                    </div>
                </div>
            </fieldset>
            
            <fieldset class="p-4  pb-2 mt-4">
                <legend class="text-sm font-medium text-gray-900 px-2 text-medium">Cohesive Soil (Min. Press)</legend>
                
                <CohesivePressureType bind:cohesivePressureType={projExcavation.cohesivePressureType} />
                    <hr class="my-2" />
                    <div class="grid gap-3 mb-3 xsm:grid-cols-2">
                        <div class="flex items-center">
                            <input id="bordered-checkbox-1"   bind:value={projExcavation.showWater} type="checkbox"  name="bordered-checkbox" class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600">
                            <label for="bordered-checkbox-1" class="w-full ms-2 text-sm font-medium text-gray-900 dark:text-gray-300">Show Water</label>
                        </div>
                        <div title="Tension">
                            <label for="" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                                >Tension Crack (t)</label>
                            <div class="relative w-full">
                                <div class="pointer-events-none absolute inset-y-1 right-0 pt-0 items-center pr-3 leading-normal height-full">
                                    <span class="text-gray-700 text-sm leading-normal">m</span>
                                </div>
                                <input type="number"  bind:value={projExcavation.tensionCrackDepth}  class="bg-slate-50 border border-gray-300 text-gray-900 text-sm rounded focus:border-s block w-full ps-2.5 py-1.5 pe-7" placeholder="Tension" />
                            </div>
                    </div>
                </div> 
            </fieldset>

            <fieldset class="p-4  pb-2 mt-4">
                <legend class="text-sm font-medium text-gray-900 px-2 text-medium">Passive Softening</legend>
                <div class="grid gap-3 mb-3 sm:grid-cols-2">
                    
                    <div title="Passive softening thickness">
                        <label for="" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                            >Passive softening thickness</label
                        >
                        <div class="flex"> 
                            
                            <div data-dropdown-toggle="dropdown" class="flex-shrink-0 z-10 inline-flex items-center px-2.5 py-1.5 text-sm font-medium text-center text-gray-900 bg-gray-100 border border-gray-300 rounded-s-lg hover:bg-gray-200 focus:ring-4 focus:outline-none focus:ring-gray-100 dark:bg-gray-700 dark:hover:bg-gray-600 dark:focus:ring-gray-700 dark:text-white dark:border-gray-600" role="button">
                                <div class="flex items-center">
                                    <input id="applyPassive" type="checkbox"  bind:value={projExcavation.applyPassiveSoft}  name="bordered-checkbox" class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600">
                                    <label for="applyPassive" class="w-full ms-2 text-sm font-medium text-gray-900 dark:text-gray-300">Apply</label>
                                </div>
                            </div>
                            <div class="relative w-full">
                                <input type="number" class="bg-slate-50 border border-gray-300 text-gray-900 text-sm rounded focus:border-s block w-full px-2.5 py-1.5" placeholder="Passive softening thickness"  bind:value={projExcavation.softPassiveThickness}  />
                                
                            </div>
                        </div>
                    </div>
                </div> 
            </fieldset>
        </div>
    </div>
    <div class="grid gap-3 md:grid-cols-2">

    </div>

{/if}