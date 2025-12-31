<script lang="ts"> 
	import { createEventDispatcher } from 'svelte';
	import { getContextClient } from '@urql/svelte'; 
 
	const client = getContextClient();
	const dispatch = createEventDispatcher();

    export let currentStep =1;
    export let totalStep:number=1;

    let nextStep:number=0;;
    let  backStep:number=0;
    
    if(currentStep==1){
        nextStep=currentStep+1;
        backStep=currentStep;
    }
    
	async function handleNext() { 
        if(currentStep <  totalStep  ){
            nextStep=currentStep+1;
        } 
		dispatch('next', { step: nextStep });
		return;
	}

	function handleBack() {
        if(currentStep > 1   ){
            backStep=currentStep-1;
        } 
		dispatch('back', {step: backStep});
        return;
	}
</script>
<div class="mt-4 text-right">
    {#if currentStep > 1 }		
        <button on:click={()=>handleBack()}  class="text-red-600 bg-white hover:text-white border border-red-600 hover:bg-red-600 focus:bg-red-600 font-medium rounded text-sm px-4 py-1 text-center inline-flex items-center ms-3 outline-redbtn duration-300 transform">
            Back
        </button>
    {/if}
    
    {#if currentStep <  totalStep}		
        <button on:click={()=>handleNext()} disabled={currentStep == totalStep}  class="text-blue-600 bg-white hover:text-white border border-blue-600 hover:bg-blue-600 focus:bg-blue-600 font-medium rounded text-sm px-4 py-1 text-center inline-flex items-center ms-3 outline-bluebtn duration-300 transform">
            Next
        </button>
    {/if}
</div>