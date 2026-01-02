<script lang="ts">
    import { createEventDispatcher } from 'svelte';
	import type Entity from '$lib/models/Entity';
    import type { Soil as SoilInterface  } from '$lib/models/PileDesign';  
	import type { ProjectSoil } from '$lib/models/Project';
	import DropDown from '$theme/components/form/DropDown.svelte'; 
	import InputNumber from '$theme/components/form/InputNumber.svelte';
	import { saveProjSoil } from '$lib/utils/project';
	import { getContextClient } from '@urql/svelte';
	import { projectStore } from '$lib/stores/project';
 
    export let soils:SoilInterface[]=[];
    export let projectID:string="";
    export let slug:string="";
    const client = getContextClient();
	const dispatch = createEventDispatcher();
     
    let order= $projectStore?.soils?$projectStore?.soils.length +1 :0
    export let soil:ProjectSoil= {
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
        orderBy:1
    }
    let SOIL_TYPES:Entity[]=[]; 
    if(soils.length > 0){
        SOIL_TYPES = soils.map((soil, index) => {
            return {
                id: soil.slug, // use slug as id
                name: soil.name, // use name for name field
                selected: index === 0 ? true : false // select the first one as default
            };
        });
    }

    function resetSoil(){
        soil = {
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
            orderBy:0,slug
        }
    }

    async function handleSave(){
        console.log("Excavation Proj ID", projectID);
         
		let slug = await saveProjSoil(projectID,order,soil,client) 
        console.log("handleSave",slug);
        if(slug && slug!=""){
            soil.slug= slug;
            dispatch('save', { soilInfo:soil });
            resetSoil();
        }
        return;
       
    }

  
    function handleChange(e){
         console.log("CHANGE VALUE",e.detail.value,soils);
         soil = filterSoilsBySlug(soils, e.detail.value);
         if(soil){
            
         }
    }
    // Function to filter soils based on slug
    function filterSoilsBySlug(soils, slug) {
        return soils.find(soil => soil.slug === slug);
    }
    
    $:if(slug!=""){
       // soil = filterSoilsBySlug(soils,slug);
    }

    $:{
		 
		console.log("Project Soil Layer", soil);
	}
   
</script>
<fieldset class="p-4 pb-2">
    <legend class="text-sm font-medium text-gray-900 px-2 text-medium">Selected Layer</legend>
   
    <div class="grid gap-3 mb-4 md:grid-cols-1">
		<div title="Name">
            <DropDown 
                orientation="horizontal"
                label='Name:' 
                labelClass="block  pt-2 pr-8 text-sm font-medium text-gray-900 dark:text-white"
                cls="bg-slate-50 border border-gray-300 text-gray-900 text-sm rounded focus:border-s block w-full px-2.5 py-1.5"
                bind:value={slug}
                options={SOIL_TYPES} 
                on:change={handleChange}

                /> 
			 
		</div> 
    </div>
    <div class="grid gap-3 mb-6 md:grid-cols-1">
        <div title="Depth">
			<InputNumber  
                orientation="horizontal"
				label="Depth(m))" 
				name="depth" 
				required
				placeholder="Depth"
				labelClass="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
				cls="block w-full rounded py-1.5 pr-[75px] ps-3 bg-slate-50 border border-gray-300 text-gray-900 text-sm focus:border-blue-600"
				bind:value={soil.depth}
			/>  
			 
		</div>
    </div> 
    <div class="grid gap-3 mb-6 xsm:grid-cols-2">
        
        <div title="Bulk Denisty">
			<label for="" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
				>γ (Unit Weight)</label
			>
            <div  class="relative">
                <div class="pointer-events-none absolute inset-y-1 right-0 pt-0 items-center pr-3 leading-normal height-full">
                    <span class="text-gray-700 text-sm leading-normal">kN/m<sup>3</sup></span>
                  </div>
                  <input bind:value={soil.unitWeight} type="number" class="block w-full rounded  py-1.5 pr-[75px] ps-3  bg-slate-50 border border-gray-300 text-gray-900 text-sm focus:border-blue-600" />
            </div>
		</div>
        <div title="Submerged Density">
			<label for="" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
				>γ' (Submerged Density)</label
			>
            <div  class="relative">
                <div class="pointer-events-none absolute inset-y-1 right-0 pt-0 items-center pr-3 leading-normal height-full">
                    <span class="text-gray-700 text-sm leading-normal">kN/m<sup>3</sup></span>
                  </div>
                  <input bind:value={soil.effectiveUnitWeight} type="number" class="block w-full rounded  py-1.5 pr-[75px] ps-3  bg-slate-50 border border-gray-300 text-gray-900 text-sm focus:border-blue-600" />
            </div>
		</div>
        <div title="Cohesion">
			<label for="" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
				>Cohesion(C)</label
			>
            <div  class="relative">
                <div class="pointer-events-none absolute inset-y-1 right-0 pt-0 items-center pr-3 leading-normal height-full">
                    <span class="text-gray-700 text-sm leading-normal">kN/m<sup>2</sup></span>
                  </div>
                  <input  bind:value={soil.cohesion}  type="number" class="block w-full rounded  py-1.5 pr-[75px] ps-3  bg-slate-50 border border-gray-300 text-gray-900 text-sm focus:border-blue-600" placeholder="Cohesion" />
            </div>
		</div>
        <div title="Max. Bending moment">
			<label for="" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
				>Adhesion(Ca)</label> 
            <div  class="relative">
                <div class="pointer-events-none absolute inset-y-1 right-0 pt-0 items-center pr-3 leading-normal height-full">
                    <span class="text-gray-700 text-sm leading-normal">(kN/m<sup>2</sup>)</span>
                  </div>
                  <input  bind:value={soil.adhesion}  type="number" class="block w-full rounded  py-1.5 pr-[75px] ps-3  bg-slate-50 border border-gray-300 text-gray-900 text-sm focus:border-blue-600" placeholder="Max. Bending moment" />
            </div>
		</div>
    </div>

    <div class="grid gap-3 xsm:grid-cols-2">
        <div title="Angle of internal friction of soil">
			<label for="" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
				>Internal friction angle (ϕ)</label
			>
            <!-- <input type="number" class="bg-slate-50 border border-gray-300 text-gray-900 text-sm rounded focus:border-s block w-full px-2.5 py-1.5" /> -->
            <div class="relative">
                <div class="pointer-events-none absolute inset-y-0 right-0 pt-2 items-center pr-3 leading-none height-full">
                    <span class="text-gray-700 text-lg leading-none">°</span>
                  </div>
                  <input   bind:value={soil.internalFriction} type="number" name="price" id="price" class="block w-full rounded  py-1.5 pr-7 ps-3  bg-slate-50 border border-gray-300 text-gray-900 text-sm focus:border-blue-600"  placeholder="Angle of internal friction of soil" />
            </div>
		</div>
        <div title="Angle of friction of soil and plates">
			<label for="" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
				>Wall friction angle (δ)</label
			>
            <!-- <input type="number" class="bg-slate-50 border border-gray-300 text-gray-900 text-sm rounded focus:border-s block w-full px-2.5 py-1.5" placeholder="Angle of friction of soil and plates" /> -->

            <div class="relative">
                <div class="pointer-events-none absolute inset-y-1 right-0 pt-0 items-center pr-3 leading-normal height-full">
                    <span class="text-gray-700 text-sm leading-normal">mm</span>
                  </div>
                  <input  bind:value={soil.wallFrictionAngle} type="number" name="price" id="price" class="block w-full rounded  py-1.5 pr-[45px] ps-3  bg-slate-50 border border-gray-300 text-gray-900 text-sm focus:border-blue-600"  placeholder="Wall friction angle (δ)" />
            </div>
		</div>
        <div class="grid gap-3 mb-3 sm:grid-cols-2">
            <div title="Coefficient of active pressure for cohession soil">
                <label for="" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                    >K<sub>a</sub></label
                >
                <input  bind:value={soil.kActive}  type="number" class="bg-slate-50 border border-gray-300 text-gray-900 text-sm rounded focus:border-s block w-full px-2.5 py-1.5" placeholder="Coefficient of active pressure for cohession soil" />
            </div>
            <div title="Coefficient of passive pressure for cohession soil" class="mb-3">
                <label for="" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                    >K<sub>p</sub></label
                >
                <input  bind:value={soil.kPassive}  type="number" class="bg-slate-50 border border-gray-300 text-gray-900 text-sm rounded focus:border-s block w-full px-2.5 py-1.5" placeholder="Coefficient of passive pressure for cohession soil" />
            </div>
        </div>
        <div class="grid gap-3 sm:grid-cols-2">
            
            <div title="Coefficient of active pressure for cohesive soil">
                <label for="" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                    >K<sub>ac</sub></label
                >
                <input  bind:value={soil.kAc}  type="number" class="bg-slate-50 border border-gray-300 text-gray-900 text-sm rounded focus:border-s block w-full px-2.5 py-1.5" placeholder="Coefficient of active pressure for cohesive soil" />
            </div>
            <div title="Coefficient of passive pressure for cohesive soil">
                <label for="" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                    >K<sub>pc</sub></label
                >
                <input  bind:value={soil.kPc}   type="number" class="bg-slate-50 border border-gray-300 text-gray-900 text-sm rounded focus:border-s block w-full px-2.5 py-1.5" placeholder="Coefficient of passive pressure for cohesive soil" />
            </div>
        </div>
    </div>
    <div class="mt-4 text-right">
        <button  on:click={()=>handleSave()}   class="text-blue-600 bg-white hover:text-white border border-blue-600 hover:bg-blue-600 focus:bg-blue-600 font-medium rounded text-sm px-4 py-1 text-center inline-flex items-center ms-3 outline-bluebtn duration-300 transform">
            Add Soil
        </button>
        
    </div>
</fieldset>