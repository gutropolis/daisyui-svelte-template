<script lang="ts">
	import { PENETRATION_TYPES } from "$lib/enums/piledatabase";

	 
    export let penetrationType:string ="";
    export let isRuleThumb:boolean=false ;

</script>
<div>
    <fieldset class="p-4 pb-2 mt-3">
        <legend class="text-sm font-medium text-gray-900 px-2 text-medium">Penetration</legend>
        {#if PENETRATION_TYPES.length > 0}   
            {#each PENETRATION_TYPES as item}
                <div class="flex mb-3">
                    <div class="flex items-center h-5">
                        <input
                            id={item.id}
                            aria-describedby={item.name}
                            type="radio"
                            value={item.id}
                            name="penetration"
                            bind:group={penetrationType}
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
         
    
         
        <hr class="mb-3" />
        <div class="flex items-center">
            <input id="link-checkbox" type="checkbox"   bind:value={isRuleThumb}  class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600">
            <label for="link-checkbox" class="ms-2 text-sm font-medium text-gray-900 dark:text-gray-300">Rules of thumb</label>
        </div> 
     
    </fieldset>
</div>