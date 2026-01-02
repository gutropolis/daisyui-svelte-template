<script lang="ts">
	import { Min_PRESSURE_COHESIVE_SOIL } from "$lib/enums/piledatabase";

	 
    export let cohesivePressureType:string =""; 

</script>
 
        <div title="Cohesive Pressure Type" class="mb-3">
            {#if Min_PRESSURE_COHESIVE_SOIL.length > 0}   
                {#each Min_PRESSURE_COHESIVE_SOIL as item}
                <div class="flex ">
                    <div class="flex items-center h-5">
                            <input
                                id={item.id}
                                aria-describedby={item.name}
                                type="radio"
                                value={item.id}
                                name="cohesive_pressure_type"
                                bind:group={cohesivePressureType}
                                class="w-4 h-4 text-blue-600 bg-blue-100 border-gray-300"
                            />
                        
                    </div>
                    <div class="ms-2 text-sm mb-3">
                        <label for="freeearth" class="font-medium text-gray-900 dark:text-gray-300"
                            >{item.name}</label
                        >
                    </div>
                </div> 
                {/each}
            {/if}      
        </div> 