<script lang="ts">
    import type { ProjectExcavation } from '$lib/models/Project';
	import InputNumber from '$theme/components/form/InputNumber.svelte';
	import ExcavLevelTypes from '$lib/components/project/ExcavLevelTypes.svelte';
	import { CALCULATION_METHOD } from '$lib/enums/piledatabase';
	import { projectStore } from '$lib/stores/project';

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
		pressureModel:'', 
		cohesivePressureType:'', 
		applyPassiveSoft:'',
	};
	let projExcavation=$projectStore.excavation?$projectStore.excavation:defaultExcavation;
 
	 
	$:{
		$projectStore.excavation=projExcavation;
		console.log("Project Excavation", $projectStore)
	}
	
	
</script>

<div class="">
	<div class="grid gap-3 mb-3 xsm:grid-cols-2">
		<div title="Depth">
			<InputNumber  
				label="Depth(m))" 
				name="depth" 
				required
				placeholder="Depth"
				labelClass="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
				cls="block w-full rounded py-1.5 pr-[75px] ps-3 bg-slate-50 border border-gray-300 text-gray-900 text-sm focus:border-blue-600"
				bind:value={projExcavation.depth}
			/>  
			 
		</div>

		<div title="Active Water Depth">
			<InputNumber  
				label="Active Water Depth(m)" 
				name="activeWaterDepth" 
				required
				placeholder="Active Water Depth(m)"
				labelClass="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
				cls="block w-full rounded py-1.5 pr-[75px] ps-3 bg-slate-50 border border-gray-300 text-gray-900 text-sm focus:border-blue-600"
				bind:value={projExcavation.activeWaterDepth}
			/>  
			 
		</div>

		<div title="Passive Water Depth">
			<InputNumber  
				label="Passive Water Depth(m)" 
				name="passiveWaterDepth" 
				required
				placeholder="Passive Water Depth"
				labelClass="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
				cls="block w-full rounded py-1.5 pr-[75px] ps-3 bg-slate-50 border border-gray-300 text-gray-900 text-sm focus:border-blue-600"
				bind:value={projExcavation.passiveWaterDepth}
			/>  
			 
		</div>

		<div title="Surcharge">
			<InputNumber  
				label="Surcharge(kN/m<sup>2</sup>)" 
				name="surcharge" 
				required
				placeholder="Surcharge"
				labelClass="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
				cls="block w-full rounded py-1.5 pr-[75px] ps-3 bg-slate-50 border border-gray-300 text-gray-900 text-sm focus:border-blue-600"
				bind:value={projExcavation.surcharge}
			/>  
			 
		</div>

		<div title="Water Density">
			<InputNumber  
				label="Water Density(kN/m<sup>3</sup>)" 
				name="waterDensity" 
				required
				placeholder="Water Density"
				labelClass="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
				cls="block w-full rounded py-1.5 pr-[75px] ps-3 bg-slate-50 border border-gray-300 text-gray-900 text-sm focus:border-blue-600"
				bind:value={projExcavation.waterDensity}
			/>  
			 
		</div>

		<div title="Minimum Fluid Density">
			<InputNumber  
				label="Minimum Fluid Density (kN/m3)" 
				name="miniFluidDensity" 
				required
				placeholder="Minimum Fluid Density"
				labelClass="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
				cls="block w-full rounded py-1.5 pr-[75px] ps-3 bg-slate-50 border border-gray-300 text-gray-900 text-sm focus:border-blue-600"
				bind:value={projExcavation.miniFluidDensity}
			/>  
			 
			 
		</div>
	</div>

	<div>
		<fieldset class="p-4">
			<legend class="font-medium text-gray-900 px-2">Ground</legend>
			<div class="grid gap-3 xsm:grid-cols-3">
				
				<ExcavLevelTypes  bind:levelName={projExcavation.slopeType} /> 
				<div>
					<fieldset class="p-4">
						<div>
							<div class="mb-4" title="Beta Active">
								<InputNumber  
									label="Beta Active (degree)" 
									name="activeSlopeAngle" 
									required
									placeholder="0.0 <span class='text-gray-700 text-lg leading-none'>°</span>"
									labelClass="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
									cls="block w-full rounded py-1.5 pr-[75px] ps-3 bg-slate-50 border border-gray-300 text-gray-900 text-sm focus:border-blue-600"
									bind:value={projExcavation.activeSlopeAngle}
								/>  
								 
							</div>
							<div title="Beta Passive">
								<InputNumber  
									label="Beta Passive (degree)" 
									name="passiveSlopeAngle" 
									required
									placeholder="0.0 <span class='text-gray-700 text-lg leading-none'>°</span>"
									labelClass="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
									cls="block w-full rounded py-1.5 pr-[75px] ps-3 bg-slate-50 border border-gray-300 text-gray-900 text-sm focus:border-blue-600"
									bind:value={projExcavation.passiveSlopeAngle}
								/>  
								 
							</div>
		
						</div> 
					</fieldset>
				</div>
				<div>
					<fieldset class="p-4">
						<legend class="font-medium text-gray-900 px-2 text-medium">Method</legend>

						{#each CALCULATION_METHOD as method}
						<div class="flex mb-4">
						  <div class="flex items-center h-5">
							<input
						      name="calculateMethod"
							  id={method.id}
							  type="radio"
							  bind:group={projExcavation.calculationMethod}
							  value={method.id}
							  class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300"
							/>
						  </div>
						  <div class="ms-2 text-sm">
							<label for={method.id} class="font-medium text-gray-900 dark:text-gray-300">
							  {method.name}
							</label>
						  </div>
						</div>
					  {/each}
						 
					</fieldset>
				</div>
			</div>
		</fieldset>
	</div>
</div>
<div class="imagebox">

</div>
