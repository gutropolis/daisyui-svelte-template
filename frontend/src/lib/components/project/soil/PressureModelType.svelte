<script lang="ts">
	import { PRESSURE_MODEL_TYPE } from "$lib/enums/piledatabase";

	 
    export let modelType:string =""; 

</script>
 
        <div title="Pressure" class="mb-3">
            {#if PRESSURE_MODEL_TYPE.length > 0}   
                {#each PRESSURE_MODEL_TYPE as item}
                <div class="flex ">
                    <div class="flex items-center h-5">
                            <input
                                id={item.id}
                                aria-describedby={item.name}
                                type="radio"
                                value={item.id}
                                name="pressuremodel"
                                bind:group={modelType}
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