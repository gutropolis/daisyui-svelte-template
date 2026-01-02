<script lang="ts">
 
	import type { Project } from '$lib/models/Project'; 
	import DropDown from '$theme/components/form/DropDown.svelte';
	import Input from '$theme/components/form/Input.svelte';
	import NextPreviousBtn from '$theme/components/button/NextPreviousBtn.svelte';
	import { projectStore } from '$lib/stores/project';
	import { SaveProjectClientMutation } from '$lib/gql/projectclient';
	import { getContextClient } from '@urql/svelte';
	import { createEventDispatcher } from 'svelte';
	import { camelize } from '$lib/utils/string';
  
	//export let project:Project ;

	$: project = $projectStore; 
	let formId="project-add";
    let  busy = false, err, readOnly = false;
	
	const client = getContextClient();
	const dispatch = createEventDispatcher();
	
	async function save() {
		 
	}

	function inputCode(e) {
        let codeValue = camelize(e.target.value || '').toUpperCase();
        if (codeValue.length > 5) {
            codeValue = codeValue.substring(0, 8);
        }
        $projectStore.code = camelize(codeValue || '').toUpperCase();
    }

	$:if(project.name){
		console.log("Project>>Client",project.name)
	}
</script>
<div class="bg-white ">
	 
		
		<fieldset class="p-4">
			<legend class="text-sm font-medium text-gray-900  text-medium">Client Information</legend>
			 
				<form id={formId} class="w-full" on:submit|preventDefault={save}>
					 
						<div title="Name">
								<Input 
									orientation="horizontal"
									label="Client Name"
									type="text"
									on:keypress={inputCode} 
									required
									placeholder="Client Name"
									labelClass="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
									cls="block w-full rounded py-1.5 pr-[75px] ps-3 bg-slate-50 border border-gray-300 text-gray-900 text-sm focus:border-blue-600"
									bind:value={$projectStore.name}
								/>  
						</div>
						<div title="Office/Site">
						 	<Input 
							    orientation="horizontal"
								label="Site/Office"
								type="text"
								name="siteOffice" 
								required
								placeholder="Enter office/site"
								labelClass="block mb-2 mr-3 text-sm font-medium text-gray-900 dark:text-white"
								cls="block w-full rounded py-1.5 pr-[75px] ps-3 bg-slate-50 border border-gray-300 text-gray-900 text-sm focus:border-blue-600"
								bind:value={$projectStore.siteOffice}
							/>  
						</div>
	
					<div class="grid gap-3 mb-6 xsm:grid-cols-2">
						<div title="Code">
				    	<Input 
							orientation="horizontal"
							label="Code"
							type="text"
							name="code" 
							required
							disabled={true}
							placeholder="code"
							labelClass="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
							cls="block w-full rounded py-1.5 pr-[75px] ps-3 bg-slate-50 border border-gray-300 text-gray-900 text-sm focus:border-blue-600"
							bind:value={$projectStore.code}
						/>  
								 
								
								  
						</div>
						<div title="FAO">
						 
								<Input 
								    orientation="horizontal"
								    label="FAO"
									type="text"
									name="siteOffice" 
									required
									placeholder="Enter FAO"
									labelClass="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
									cls="block w-full rounded py-1.5 pr-[75px] ps-3 bg-slate-50 border border-gray-300 text-gray-900 text-sm focus:border-blue-600"
									bind:value={$projectStore.fao}
								/>  
						</div>
						<div title="Telephone">
								<Input 
								    orientation="horizontal"
									label="Tel:"
									type="text"
									name="telephone" 
									required
									placeholder="Enter telephone"
									labelClass="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
									cls="block w-full rounded py-1.5 pr-[75px] ps-3 bg-slate-50 border border-gray-300 text-gray-900 text-sm focus:border-blue-600"
									bind:value={$projectStore.tel}
								/>   
						</div>
						<div title="fax">
								<Input 
								    orientation="horizontal"
								    label="Fax"
									type="text"
									name="fax" 
									required
									placeholder="Enter fax"
									labelClass="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
									cls="block w-full rounded py-1.5 pr-[75px] ps-3 bg-slate-50 border border-gray-300 text-gray-900 text-sm focus:border-blue-600"
									bind:value={$projectStore.fax}
								/>    
						</div>
					</div>
	 
				</form>
				
				 
		</fieldset>
		<fieldset class="p-4">
			<legend class="text-sm font-medium text-gray-900  text-medium">Job Information</legend>
			 
				<form id={formId} class="w-full" on:submit|preventDefault={save}>
					 
						<div title="Job Title">
							<Input 
							    orientation="horizontal"
								label="Title"
								type="text"
								name="jobtitle" 
								required
								placeholder="Enter title"
								labelClass="block mb-2 mr-3 text-sm font-medium text-gray-900 dark:text-white"
								cls="block w-full rounded py-1.5 pr-[75px] ps-3 bg-slate-50 border border-gray-300 text-gray-900 text-sm focus:border-blue-600"
								bind:value={$projectStore.title}
							/>  
						</div>
						<div title="Office/Site">
						 	<Input 
							    orientation="horizontal"
								label="Note"
								type="text"
								name="note" 
								required
								placeholder="Enter note"
								labelClass="block mb-2 mr-2 text-sm font-medium text-gray-900 dark:text-white"
								cls="block w-full rounded py-1.5 pr-[75px] ps-3 bg-slate-50 border border-gray-300 text-gray-900 text-sm focus:border-blue-600"
								bind:value={$projectStore.note}
							/>  
						</div>
	
					<div class="grid gap-3 mb-6 xsm:grid-cols-2">
					 
						<div title="Designer">
						 
								<Input 
								    orientation="horizontal"
								    label="Designer"
									type="text"
									name="designer" 
									required
									placeholder="Enter Designer"
									labelClass="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
									cls="block w-full rounded py-1.5 pr-[75px] ps-3 bg-slate-50 border border-gray-300 text-gray-900 text-sm focus:border-blue-600"
									bind:value={$projectStore.jobDesigner}
								/>  
						</div>
						<div title="Job Reference">
								<Input 
								    orientation="horizontal"
									label="Ref:"
									type="text"
									name="reference" 
									required
									placeholder="Enter telephone"
									labelClass="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
									cls="block w-full rounded py-1.5 pr-[75px] ps-3 bg-slate-50 border border-gray-300 text-gray-900 text-sm focus:border-blue-600"
									bind:value={$projectStore.ref}
								/>   
						</div>
						 
					</div>
	 
				</form>
				
				 
		</fieldset> 
	
		 
		 
 
</div> 