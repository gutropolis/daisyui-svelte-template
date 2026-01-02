<script lang="ts">
	import IconActiveLevelGround from '$theme/icons/leveltype/IconActiveLevelGround.svelte';
  import IconActiveDownlevelGround from '$theme/icons/leveltype/IconActiveDownlevelGround.svelte';
  import IconActiveUpwardLevel from '$theme/icons/leveltype/IconActiveUpwardLevel.svelte';
  import IconPassiveBeta from '$theme/icons/leveltype/IconPassiveBeta.svelte';
  import IconPassiveDownSlope from '$theme/icons/leveltype/IconPassiveDownSlope.svelte';
  import IconPassiveUpwardSlope from '$theme/icons/leveltype/IconPassiveUpwardSlope.svelte';

	import type { ProjectExcavation } from '$lib/models/Project';
	import InputNumber from '$theme/components/form/InputNumber.svelte';
  const levelTypes = [
		
    { id: 'activeLevelGround', title: 'Active Level Ground', icon: IconActiveLevelGround,index:1 },
    { id: 'activeUpwardlevelGround', title: 'Active Upward Level Ground', icon: IconActiveUpwardLevel,index:2 },
    { id: 'activeDownwardlevelGround', title: 'Active Downward Level Ground', icon: IconActiveDownlevelGround ,index:3},
    { id: 'betaPassive', title: 'Beta Passive', icon: IconPassiveBeta ,index:4},
    { id: 'betaPassiveUpwardSlope', title: 'Beta Passive Upward Slope', icon: IconPassiveUpwardSlope,index:5 },
    { id: 'betaPassiveDownwardSlope', title: 'Beta Passive Downward Slope', icon: IconPassiveDownSlope,index:6 },
];
export let levelName:any ;
</script>
<div>
    <fieldset class="p-4">
      <legend class="font-medium text-gray-900 px-2 text-medium">Level Type</legend>
    
      <div class="grid grid-cols-3 gap-4">
          <!-- First row with three images -->
          {#if levelTypes.length > 0}   
            {#each levelTypes as level}
            <div class="custom-radio" class:selected={levelName === level.id}>
           
              <input
              
                type="radio"
                name="leveltype"
                aria-describedby={level.id}
                bind:group={levelName}
                id={level.id}
                value={level.id}

                required
              />
              <label for={level.id} title={level.title}>
                <!-- Render the correct icon from the object -->
                <svelte:component this={level.icon} />
               
              </label>
            </div>
            {/each}
          {/if}
      </div>
    </fieldset>
</div>
<style>
  /* Default custom-radio styles */
 

  /* Highlighted state */
  .custom-radio.selected {
    background-color: #cce7ff; /* Change to whatever color you want */
    border-color: #007bff;
  }
</style>