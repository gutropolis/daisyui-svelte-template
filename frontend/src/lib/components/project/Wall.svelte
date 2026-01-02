
<script lang="ts">
    import type { ProjectExcavation, ProjectSheet,Project } from '$lib/models/Project';
	import InputNumber from '$theme/components/form/InputNumber.svelte';
	import ExcavLevelTypes from '$lib/components/project/ExcavLevelTypes.svelte';
	import { CALCULATION_METHOD, K_P_C_TYPES } from '$lib/enums/piledatabase';
	import type { PileSheet } from '$lib/models/PileDesign';
	import type Entity from '$lib/models/Entity';
    import { PENETRATION_TYPES } from "$lib/enums/piledatabase";
	import DropDown from '$theme/components/form/DropDown.svelte';
	import PenetrationType from './wall/PenetrationType.svelte';
	import { projectStore, updateExcavation } from '$lib/stores/project';
    export let pileSheets:PileSheet[]=[];
	 let defaultProjSheet: ProjectSheet={ 
        
        sectionModule:"",
        elasticity: "",
        allowableStress:"",
        momentOfInertia:"",
        maxiBendingMoment:"",
        maxiAllowedDeflection:"",
        upstand:"",
        areaSteel:"",
        weightPerMeter:"",
        name:"",
        slug:"",
        sheetName:""
    }
    let defaultExcavation:ProjectExcavation={
         
		penetrationTypes:"",
		applyRuleThumb:false,
        upstand:0,
        applyPassiveSoft:false, 
        toe:0, // optional, FloatField
        fos: 0, // optional, FloatField
        passiveSoilFactorCp: +1,
        passiveSoilFactorKp:""
    }
    let projSheet =$projectStore.sheet?$projectStore.sheet:defaultProjSheet; 
    let excavation=$projectStore.excavation?$projectStore.excavation:defaultExcavation;
    let SHEET_TYPES:Entity[]=[];
	 
    if(pileSheets.length > 0){
        SHEET_TYPES = pileSheets.map((sheet, index) => {
            return {
                id: sheet.slug, // use slug as id
                name: sheet.name, // use name for name field
                selected: index === 0 ? true : false // select the first one as default
            };
        });
    }
    
    function handleChange(e){
         
         let objSelSheet = filterSoilsBySlug(pileSheets, e.detail.value);
         projSheet.name=e.detail.value;
         projSheet.sheetName=objSelSheet.name;
         projSheet.sectionModule=objSelSheet.sectionModule;
         projSheet.elasticity=objSelSheet.elasticity;
         projSheet.allowableStress=objSelSheet.allowableStress;
         projSheet.momentOfInertia=objSelSheet.momentOfInertia;
         projSheet.maxiBendingMoment=objSelSheet.maxiBendingMoment;
         projSheet.maxiAllowedDeflection=objSelSheet.maxiAllowedDeflection;
         
         

         console.log("CHANGE VALUE",e.detail.value,projSheet );
    }
    // Function to filter soils based on slug
    function filterSoilsBySlug(pileSheets, slug) {
        return pileSheets.find(projSheet => projSheet.slug === slug);
    }
    $:{
		$projectStore.sheet=projSheet;
        updateExcavation(excavation);
		console.log("Project Excavation", $projectStore)
	}
        
</script>
<fieldset class="p-4 pb-2">
    <legend class="text-sm font-medium text-gray-900 px-2 text-medium">Sheet Information</legend>
    <div class="grid gap-3 mb-3 xsm:grid-cols-2">
      
            <div title="Sheet Name">
                <DropDown 
                orientation="horizontal"
                label='Name:' 
                labelClass="block  pt-2  text-sm font-medium text-gray-900 dark:text-white"
                cls="bg-slate-50 border border-gray-300 text-gray-900 text-sm rounded focus:border-s block w-full px-2.5 py-1.5"
                bind:value={projSheet.name} 
                options={SHEET_TYPES} 
                on:change={handleChange}

                /> 
            </div>
        
       
            <div title="Section modules of sheet">
                <InputNumber  
                    orientation="horizontal"
                    label="Z:" 
                    name="section_module" 
                    required
                   
                    labelClass="block pt-2 text-sm font-medium text-gray-900 dark:text-white"
                    cls="block w-full rounded py-1.5 pr-[75px] ps-3 bg-slate-50 border border-gray-300 text-gray-900 text-sm focus:border-blue-600"
                    bind:value={projSheet.sectionModule}
                />   
            </div>
         
   
   
            
            <div title="Moment of inertia of sheet">
                <InputNumber  
                    orientation="horizontal"
                    label="I:" 
                    name="momentOfInertia" 
                    required 
                    labelClass="block pt-2 pr-9 text-sm font-medium text-gray-900 dark:text-white"
                    cls="block w-full rounded py-1.5 pr-[75px] ps-3 bg-slate-50 border border-gray-300 text-gray-900 text-sm focus:border-blue-600"
                    bind:value={projSheet.momentOfInertia}
                />
                
            </div>
        
         
            <div title="Stress">
                <InputNumber  
                    orientation="horizontal"
                    label="Stress" 
                    name="stress" 
                    required 
                    labelClass="block pt-2 pr-9 text-sm font-medium text-gray-900 dark:text-white"
                    cls="block w-full rounded py-1.5 pr-[75px] ps-3 bg-slate-50 border border-gray-300 text-gray-900 text-sm focus:border-blue-600"
                    bind:value={projSheet.allowableStress}
                />
                 
            
            <div title="Young’s Modules of sheet">
                <InputNumber  
                    orientation="horizontal"
                    label="E" 
                    name="young_module" 
                    required 
                    labelClass="block pt-2 pr-9 text-sm font-medium text-gray-900 dark:text-white"
                    cls="block w-full rounded py-1.5 pr-[75px] ps-3 bg-slate-50 border border-gray-300 text-gray-900 text-sm focus:border-blue-600"
                    bind:value={projSheet.elasticity}
                />
                 
            </div>
        </div>
        
        <div title="Cohesion">
                <InputNumber  
                    placeholder="Max. Bending moment" 
                    label="Max. Bending moment (kNm/m)" 
                    name="max_bending_moment" 
                    required 
                    labelClass="block pt-2 pr-9 text-sm font-medium text-gray-900 dark:text-white"
                    cls="block w-full rounded py-1.5 pr-[75px] ps-3 bg-slate-50 border border-gray-300 text-gray-900 text-sm focus:border-blue-600"
                    bind:value={projSheet.maxiBendingMoment}
                />
           
        </div>
        <div title="Max. Allowed Deflection">
            <InputNumber  
                    placeholder="Max. allowed defelction" 
                    label="Max. allowed defelction (mm)" 
                    name="max_allowed_deflection" 
                    required 
                    labelClass="block pt-2 pr-9 text-sm font-medium text-gray-900 dark:text-white"
                    cls="block w-full rounded py-1.5 pr-[75px] ps-3 bg-slate-50 border border-gray-300 text-gray-900 text-sm focus:border-blue-600"
                    bind:value={projSheet.maxiAllowedDeflection}
                />
            
        </div>
    </div>
</fieldset>

<div class="grid gap-3 mb-3 sm:grid-cols-4 xsm:grid-cols-2">
    <PenetrationType 
      bind:penetrationType={excavation.penetrationTypes}
      bind:isRuleThumb={excavation.applyRuleThumb}
    />
    <div>
        <fieldset class="p-4 pb-2 mt-3">
            <legend class="text-sm font-medium text-gray-900 px-2 text-medium">Analysis Method</legend>
            <div class="flex mb-3">
                <div class="flex items-center h-5">
                    <input
                        id="grosspressure"
                        aria-describedby="analysis"
                        type="radio"
                        value=""
                        name="analysis"
                        class="w-4 h-4 text-blue-600 bg-blue-100 border-gray-300"
                    />
                </div>
                <div class="ms-2 text-sm ">
                    <label for="analysis" class="font-medium text-gray-900 dark:text-gray-300"> 
                        Gross Pressure (CP2) 
                    </label>
                </div>
            </div>
        
            <div class="flex mb-3">
                <div class="flex items-center h-5">
                    <input
                        id="netpressure"
                        aria-describedby="netpressure"
                        type="radio"
                        value=""
                        name="analysis"
                        class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300"
                    />
                </div>
                <div class="ms-2 text-sm">
                    <label for="netpressure" class="font-medium text-gray-900 dark:text-gray-300"
                        >Net Pressure (BSPH)</label
                    > 
                </div>
            </div>
            <div class="flex mb-3">
                <div class="flex items-center h-5">
                    <input
                        id="burlandpotts"
                        aria-describedby="burlandpotts"
                        type="radio"
                        value=""
                        name="analysis"
                        class="w-4 h-4 text-blue-600 bg-blue-100 border-gray-300"
                    />
                </div>
                <div class="ms-2 text-sm">
                    <label for="defineFos" class="font-medium text-gray-900 dark:text-gray-300"
                        >Burland Potts</label
                    >
                </div>
            </div> 
        </fieldset>
    </div>
    <div>
        <fieldset class="p-4 pb-2 mt-3">
            <legend class="text-sm font-medium text-gray-900 px-2 text-medium">Miscellaneous</legend>
            <div title="Upstand" class="mb-3">
                <label for="" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"> 
                    Upstand (m)
                </label>
                <!-- <input type="number" class="bg-slate-50 border border-gray-300 text-gray-900 text-sm rounded focus:border-s block w-full px-2.5 py-1.5" placeholder="Upstand" /> -->
                <div  class="relative">
                    <div class="pointer-events-none absolute inset-y-1 right-0 pt-0 items-center pr-3 leading-normal height-full">
                        <span class="text-gray-700 text-sm leading-normal">m<sup>2</sup></span>
                    </div>
                    <input bind:value={excavation.upstand} placeholder="Upstand" type="number" class="block w-full rounded  py-1.5 pr-7 ps-3  bg-slate-50 border border-gray-300 text-gray-900 text-sm focus:border-blue-600" />
                </div>
            </div>
            <div title="Toe" class="mb-3">
                <label for="" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                    >Toe</label>
               
                <div  class="relative">
                    <div class="pointer-events-none absolute inset-y-1 right-0 pt-0 items-center pr-3 leading-normal height-full">
                        <span class="text-gray-700 text-sm leading-normal">m<sup>2</sup></span>
                    </div>
                    <input bind:value={excavation.toe}  placeholder="Toe" type="number" class="block w-full rounded  py-1.5 pr-7 ps-3  bg-slate-50 border border-gray-300 text-gray-900 text-sm focus:border-blue-600" />
                </div>
            </div>
            <div title="Factor of safety" class="mb-3">
                <label for="" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                    >Factor of safety (FOS)</label
                >
                <input  bind:value={excavation.fos}   type="number" class="bg-slate-50 border border-gray-300 text-gray-900 text-sm rounded focus:border-s block w-full px-2.5 py-1.5" placeholder="Factor of safety" />
            </div>
            <div title="Rowe's moment reduction factor" class="mb-3">
                <label for="" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                    >Rowe's moment reduction factor (R)</label
                >
                <input type="text" class="bg-slate-50 border border-gray-300 text-gray-900 text-sm rounded focus:border-s block w-full px-2.5 py-1.5" placeholder="Rowe's moment reduction factor" />
            </div> 
        </fieldset>
    </div>
    <div>
        <fieldset class="p-4 pb-2 mt-3">
            <legend class="text-sm font-medium text-gray-900 px-2 text-medium">Passive Soil Factor</legend>
            <div class="grid gap-3 mb-3 grid-cols-1">
                <div title="Kp">
                     
                    <DropDown 
                    orientation="horizontal"
                    label='Kp:' 
                    labelClass="block  pt-2  text-sm font-medium text-gray-900 dark:text-white"
                    cls="bg-slate-50 border border-gray-300 text-gray-900 text-sm rounded focus:border-s block w-full px-2.5 py-1.5"
                    bind:value={excavation.passiveSoilFactorKp} 
                    options={K_P_C_TYPES} 
                    /> 
                     
                </div>
        
                
              
             
                <div title="C">{excavation.passiveSoilFactorCp} 
                    <DropDown 
                    orientation="horizontal"
                    label='Cp:' 
                    labelClass="block  pt-2  text-sm font-medium text-gray-900 dark:text-white"
                    cls="bg-slate-50 border border-gray-300 text-gray-900 text-sm rounded focus:border-s block w-full px-2.5 py-1.5"
                    bind:value={excavation.passiveSoilFactorCp} 
                    options={K_P_C_TYPES} 
                    />  
                </div>
                 
            </div>
         
        </fieldset>
    </div>

</div>