<script lang="ts">
     import type { Soil as SoilInterface  } from '$lib/models/PileDesign';  
	import type { Project, ProjectSheet } from '$lib/models/Project'; 
	import DropDown from '$theme/components/form/DropDown.svelte';
	import Input from '$theme/components/form/Input.svelte';
	import NextPreviousBtn from '$theme/components/button/NextPreviousBtn.svelte';
	import { projectStore,pileDesignStore } from '$lib/stores/project';
	import { SaveProjectClientMutation } from '$lib/gql/projectclient';
	import { getContextClient } from '@urql/svelte';
	import { createEventDispatcher } from 'svelte';
	import { camelize } from '$lib/utils/string';
	import SideBarSummery from './SideBarSummery.svelte';
	import PileDesignCanvas from '../wall/PileDesignCanvas.svelte';
  
	//export let project:Project ;
    let projSoils:SoilInterface[]=[]; 
    let sheet:ProjectSheet[]=[]; 
	let soilLayers = [
		{ name: "Topsoil", depthStart: 0, depthEnd: 3, color: "#d3fffb" },
		{ name: "Clay", depthStart: 3, depthEnd: 7, color: "#ff980078" },
		{ name: "Sand", depthStart: 7, depthEnd: 10, color: "#b9a7a1" }
	];
	$: project = $pileDesignStore; 
    projSoils=$pileDesignStore.soils?$pileDesignStore.soils:[] ;
    sheet=$pileDesignStore.sheet;
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
	<div class="flex-1   flex-col  border-1 h-full p-5 w-full  bg-white shadow-sm   rounded-lg" style="box-shadow: 0px 0px 4px 0px #00000033;">
        <!-- Step 1 : Make first row with-->
        <div class="space-y-4">
            <div class="w-full mb-5">
                <h3 class="border-b text-blue-600 border-b-gray-300 font-semibold pb-3">Input Data</h3>
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 mt-5">
                    <div class="col-span-1 md:col-span-1">
                        <table class="w-full text-sm text-left   text-gray-500">
                            <tbody>
                                <tr>
                                    <th class="text-right px-2 py-1">Depth of excavation</th>
                                    <td class="px-2 py-1">{project.excavation?.depth} m</td>
                                </tr>
                                <tr>
                                    <th class="text-right px-2 py-1">Surcharge</th>
                                    <td class="px-2 py-1">{project.excavation?.surcharge} kN<sup>2</sup>/m</td>
                                </tr>
                                <tr>
                                    <th class="text-right px-2 py-1">Slope (active)</th>
                                    <td class="px-2 py-1">-{project.excavation?.activeSlopeAngle} degree</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                    <div  class="col-span-1 md:col-span-1">
                        <table class="w-full text-sm text-left   text-gray-500">
                            <tbody>
                                <tr>
                                    <th class="text-right px-2 py-1">Depth of Active Water</th>
                                    <td class="px-2 py-1">{project.excavation?.activeWaterDepth}  m</td>
                                </tr>
                                <tr>
                                    <th class="text-right px-2 py-1">Depth of Passive Water</th>
                                    <td class="px-2 py-1">{project.excavation?.passiveWaterDepth} m</td>
                                </tr>
                                <tr>
                                    <th class="text-right px-2 py-1">Water Density</th>
                                    <td class="px-2 py-1">{project.excavation?.waterDensity} kN/m<sup>2</sup></td>
                                </tr>
                                <tr>
                                    <th class="text-right px-2 py-1">Minimum Fluid Density</th>
                                    <td class="px-2 py-1">{project.excavation?.miniFluidDensity} kN/m<sup>2</sup></td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
                {#if projSoils.length > 0} 
                <h3 class="border-b text-blue-600 border-b-gray-300 font-semibold pb-3">Soil Calculations</h3>
                <div class="grid grid-cols-1 sm:grid-cols-1 gap-4 mt-5">
                    <div class="col-span-1 md:col-span-1"> 
                                    {#each projSoils as soil}
                                    <div>
                                        <div class="border-b p-4 dark:border-gray-600">
                                            <h6 class="uppercase dark:text-gray-300">Layer: {soil.soilName}</h6>
                                        </div>
                                        <div class="grid grid-cols-1 md:grid-cols-12 gap-6">
                                            <div class="col-span-12  ">
                                                <table class=" w-full text-sm text-left rtl:text-right text-gray-500">
                                                    <tbody>
                                                        <tr>
                                                            <th scope="col" class="text-right px-2 py-1" title="Depth">Depth (m)</th>
                                                            <td class="px-2 py-1">{soil.depth} m</td>
                                                            <th class="text-right px-2 py-1">Soil Name</th>
                                                            <td class="px-2 py-1">{soil.soilName}</td>
                                                            <th scope="col" class="text-right px-2 py-3" title="γ"><span class="lowercase">γ</span> (kN/m<sup>3</sup>)</th>
                                                            <td class="px-2 py-1">{soil.unitWeight}</td>
                                                            <th scope="col" class="text-right px-2 py-3" title="γ"><span class="lowercase">γ<sub>1</sub></span> (kN/m<sup>3</sup>)</th>
                                                            <td class="px-2 py-1">{soil.effectiveUnitWeight}</td>
                                                        </tr>
                                                        
                                                    
                                                        <tr>
                                                            <th scope="col" class="text-right px-2 py-3" title="γ">C (kN/m<sup>2</sup>)</th>
                                                            <td class="px-2 py-1">{soil.cohesion}</td>
                                                            <th scope="col" class="text-right px-2 py-3" title="γ">C<sub>a</sub> (kN/m<sup>2</sup>)</th>
                                                            <td class="px-2 py-1">{soil.adhesion}</td>
                                                            <th scope="col" class="text-right px-2 py-3" title="γ">φ  (degree)</th>
                                                            <td class="px-2 py-1">{soil.internalFriction}</td>
                                                            <th scope="col" class="text-right px-2 py-3" title="γ"><span class="lowercase">δ</span> (degree)</th>
                                                            <td class="px-2 py-1">{soil.wallFrictionAngle}</td>
                                                        </tr> 
                                                        <tr>
                                                            <th scope="col" class="text-right px-2 py-3" title="γ">K<sub>a</sub></th>
                                                            <td class="px-2 py-1">{soil.kActive}</td>
                                                            <th scope="col" class="text-right px-2 py-3" title="γ">K<sub>ac</sub> </th>
                                                            <td class="px-2 py-1">{soil.kAc}</td>
                                                            <th scope="col" class="text-right px-2 py-3" title="γ">K<sub>p</sub></th>
                                                            <td class="px-2 py-1">{soil.kPassive}</td>
                                                            <th scope="col" class="text-right px-2 py-3" title="γ">K<sub>pc</sub></th>
                                                            <td class="px-2 py-1">{soil.kPc}</td>
                                                        </tr> 
                                                    </tbody>
                                                </table>
                                            </div>
                                            <div class="col-span-12  ">
                                                <h3 class="border-b text-black-600 border-b-gray-300 font-semibold pb-3">Calculations</h3>
                                                <table class="w-full text-sm text-left   text-gray-500">
                                                     
                                                    <tbody>
                                                        <tr class="bg-white border-b">
                                                            <th class=" px-2 py-1 text-blue-600 uppercase">Top Depth:</th>
                                                            <td class="px-2 py-1">{soil?.topDepth}</td>
                                                            <th class=" px-2 py-1 text-blue-600 uppercase">Bottom Depth:</th>
                                                            <td class="px-2 py-1">{soil?.bottomDepth}</td>
                                                            <td></td>
                                                            <td></td>
                                                        </tr>
                                                        <tr class="bg-white border-b">
                                                            <th class=" px-2 py-1 text-blue-600 uppercase">Top Earth Pressure:</th>
                                                            <td class="px-2 py-1">{soil?.literalEarthPressureTop}</td>
                                                            <th class=" px-2 py-1 text-blue-600 uppercase">Top vertical Pressure:</th>
                                                            <td class="px-2 py-1">{soil?.topVerticalPressure}</td>
                                                            <th class=" px-2 py-1 text-blue-600 uppercase">Top Force:</th>
                                                            <td class="px-2 py-1">{soil?.topForce}</td>
                                                        </tr>
                                                        <tr class="bg-white border-b">
                                                            <th class=" px-2 py-1 text-blue-600 uppercase">Bottom Earth Pressure:</th>
                                                            <td class="px-2 py-1">{soil?.literalEarthPressureBottom}</td>
                                                            <th class=" px-2 py-1 text-blue-600 uppercase">Bottom vertical Pressure:</th>
                                                            <td class="px-2 py-1">{soil?.bottomVerticalPressure}</td>
                                                            <th class=" px-2 py-1 text-blue-600 uppercase">Bottom Force:</th>
                                                            <td class="px-2 py-1">{soil?.bottomForce}</td>
                                                        </tr>
                                                        
                                                        
                                                    </tbody>
                                                </table>
                                            </div>
                                        </div>
                                        
                                            
                                         
                                   </div>
                                    {/each} 
                    </div>
                
                </div>
                {/if}  
              
            </div>

            <div class="w-full mb-5" >
                <h3 class="border-b text-blue-600 border-b-gray-300 font-semibold pb-3">Solutions</h3>
                <div class="mt-4">
                    <h6 class="text-sm font-semibold ">Sheet</h6>
                </div>
                <div class="relative overflow-x-auto sm:rounded mt-3 whitespace-nowrap">
                    <table class="w-full text-sm text-left rtl:text-right text-gray-500 ">
                        <thead class="text-xs w-full text-blue-600 uppercase   border-b border-gray-300   ">
                            <tr>
                                <th scope="col" class="px-2 py-3">Sheet</th>
                                <th scope="col" class="px-2 py-3">I(cm<sub>2</sub>/m)</th>
                                <th scope="col" class="px-2 py-3">E (kN/m<sup>2</sup>)</th>
                                <th scope="col" class="px-2 py-3">Z (cm<sup>3</sup>/m)</th>
                                <th scope="col" class="px-2 py-3">F (N/mm<sup>2</sup>)</th>
                                <th scope="col" class="px-2 py-3">Maximum Bending Moment(kNm/m)</th>
                                <th scope="col" class="px-2 py-3">upstand(m)</th>
                                <th scope="col" class="px-2 py-3">Toe(m)</th>
                                <th scope="col" class="px-2 py-3">Pile Length (m)</th> 
                            </tr>
                        </thead>
                        <tbody>
                            <tr class="bg-white border-b">
                                <td class="px-2 py-2">{sheet?.sheetName}</td>
                                <td class="px-2 py-2">{sheet?.momentOfInertia}</td>
                                <td class="px-2 py-2">{sheet?.elasticity}</td>
                                <td class="px-2 py-2">{sheet?.sectionModule}</td>
                                <td class="px-2 py-2">{sheet?.allowableStress}</td>
                                <td class="px-2 py-2">{sheet?.maxiBendingMoment}</td>
                                <td class="px-2 py-2">{sheet?.upstand}</td>
                                <td class="px-2 py-2">{project?.toe}</td>
                                <td class="px-2 py-2">{project?.depthOfPile}</td>
                            </tr>
                        </tbody>
                    </table>
                </div>

                <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 mt-5">
                    <div class="col-span-1 md:col-span-1">
                        <h6 class="text-sm font-semibold mb-4">Support</h6>
                        <table class="w-full text-sm text-left   text-gray-500">
                            <thead class="text-xs w-full text-blue-600 uppercase   border-b border-gray-300   ">
                                <tr>
                                    <th>Depth(m)</th>
                                    <th>Type</th>
                                    <th>Linear Load</th>
                                    <th>Strut Angle</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr class="bg-white border-b">
                                    <td class=" px-2 py-1">3.66</td>
                                    <td class="px-2 py-1">Water</td>
                                    <td class="px-2 py-1">93.1</td>
                                    <td class="px-2 py-1">0.0</td>
                                </tr>
                                <tr class="bg-white border-b">
                                    <td class=" px-2 py-1">3.66</td>
                                    <td class="px-2 py-1">Water</td>
                                    <td class="px-2 py-1">93.1</td>
                                    <td class="px-2 py-1">0.0</td>
                                </tr>
                                <tr class="bg-white border-b">
                                    <td class=" px-2 py-1">3.66</td>
                                    <td class="px-2 py-1">Water</td>
                                    <td class="px-2 py-1">93.1</td>
                                    <td class="px-2 py-1">0.0</td>
                                </tr>
                                <tr class="bg-white border-b">
                                    <td class=" px-2 py-1">3.66</td>
                                    <td class="px-2 py-1">Water</td>
                                    <td class="px-2 py-1">93.1</td>
                                    <td class="px-2 py-1">0.0</td>
                                </tr>
                                
                            </tbody>
                        </table>
                    </div>
                    <div  class="col-span-1 md:col-span-1">
                        <h6 class="text-sm font-semibold mb-4">Maxima</h6>
                        <table class="w-full text-sm text-left   text-gray-500">
                            <thead class="text-xs w-full text-blue-600 uppercase   border-b border-gray-300   ">
                                <tr>
                                    <th> </th>
                                    <th>Maxima</th>
                                    <th>Depth</th> 
                                </tr>
                            </thead>
                            <tbody>
                                <tr class="bg-white border-b">
                                    <th class=" px-2 py-1 text-blue-600 uppercase">Bending Moment</th>
                                    <td class="px-2 py-1">{project?.maxBendingMoment}</td>
                                    <td class="px-2 py-1">{project?.maxBendingMomentDepth}</td> 
                                </tr>
                                <tr class="bg-white border-b">
                                    <th class=" px-2 py-1 text-blue-600 uppercase">Deflection</th>
                                    <td class="px-2 py-1">703928.2mm</td>
                                    <td class="px-2 py-1">71.05m</td> 
                                </tr>
                                <tr class="bg-white border-b">
                                    <th class=" px-2 py-1 text-blue-600 uppercase">Pressure</th>
                                    <td class="px-2 py-1">{project?.pressure} KN/m<sub>2</sub></td>
                                    <td class="px-2 py-1">{project?.pressureDepth}</td> 
                                </tr>
                                <tr class="bg-white border-b">
                                    <th class=" px-2 py-1 text-blue-600 uppercase">Shear Force</th>
                                    <td class="px-2 py-1">{project?.shearForceAtRotation} KN/m</td>
                                    <td class="px-2 py-1">{project?.rotatingPointDredge}m</td> 
                                </tr>
                                
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>