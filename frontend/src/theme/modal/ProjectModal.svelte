<script lang="ts">
	import { createEventDispatcher } from 'svelte';
	import { getContextClient } from '@urql/svelte';
	
	import type { PileSheet, Soil as SoilInterface } from '$lib/models/PileDesign';
	import type { Project, ProjectExcavation, ProjectSheet } from '$lib/models/Project';
	import ModalLarge from './ModalLarge.svelte';
	import Client from '$lib/components/project/Client.svelte';
	import Excavation from '$lib/components/project/Excavation.svelte';
	import Soil from '$lib/components/project/Soil.svelte';
	import Wall from '$lib/components/project/Wall.svelte';
	import Support from '$lib/components/project/Support.svelte';
	import NextPreviousBtn from '../button/NextPreviousBtn.svelte';
	import IconClient from '$theme/icons/IconClient.svelte';
	import IconExcavation from '$theme/icons/IconExcavation.svelte';
	import IconSoil from '$theme/icons/IconSoil.svelte';
	import IconWall from '$theme/icons/IconWall.svelte';
	import IconSupport from '$theme/icons/IconSupport.svelte';
	import { projectStore, projCurrentStep } from '$lib/stores/project';
	import { saveProjClient, saveProjExcavation, saveProjSheet } from '$lib/utils/project';

	import { goto } from '$app/navigation';
	import { PATH } from '$lib/enums/path';
	import { QryMySoilSheets } from '$lib/gql/project';

	export let open = false;
	export let projSlug:string="";

    let soils: SoilInterface[] = [];
    let pileSheets: PileSheet[] = [];
	
	let projSheet: ProjectSheet = {
		sectionModule: '',
		elasticity: '',
		allowableStress: '',
		momentOfInertia: '',
		maxiBendingMoment: '',
		maxiAllowedDeflection: '',
		upstand: '',
		areaSteel: '',
		weightPerMeter: '',
		name: '',
		slug: ''
	};
	let projExcavation: ProjectExcavation = {
		depth: '',
		activeWaterDepth: 0.0,
		passiveWaterDepth: 0.0,
		surcharge: 0.0,
		waterDensity: 64.21,
		miniFluidDensity: 31.82,
		slopeType: '',
		activeSlopeAngle: 0.0,
		passiveSlopeAngle: 0.0,
		calculationMethod: 'k',
		penetrationTypes: '',
		applyRuleThumb: false,
		name: '',
		pressureModel: '',
		cohesivePressureType: '',
		applyPassiveSoft: false,
		slug: ''
	};
	/*
    let project: Project = { 
		code:'', name: '', siteOffice:'', fao:'', tel: '', fax: '', note: '', status: false, jobDesigner:'', title:'', ref:'', 
		sheet:projSheet,excavation:projExcavation
	};
    */
	const options = { theme: 'snow' };
	const client = getContextClient();
	const dispatch = createEventDispatcher();
	const triggers = [
		{ id: 'job', title: 'Client', icon: IconClient, index: 1 },
		{ id: 'excavation', title: 'Excavation', icon: IconExcavation, index: 2 },
		{ id: 'soil', title: 'Soil', icon: IconSoil, index: 3 },
		{ id: 'wall', title: 'Wall', icon: IconWall, index: 4 },
		{ id: 'support', title: 'Support', icon: IconSupport, index: 5 }
	];
	 
	let currentStep = $projCurrentStep,
		totalStep = triggers.length,
		selectedTab = 'job';
	let formId = 'add-edit-project',
		busy = false,
		err,
		readOnly = false;

	let disabled = false;
	let title = 'Manage Project';
	let okBtnText = 'Save';

	async function handleNext(e) {
		let currentTab = triggers[currentStep - 1].id;
		let project = $projectStore;
		console.log('PRoject ', project);
		console.log('Current Tab', currentTab, project?.id);
		let slug = '';

		if (currentTab === 'job') {

			slug = await saveProjClient(project, client);
			if(slug!=""){
				currentStep = e.detail.step;
				let url = PATH.MY_PROJECT_VIEW.replace(':id', slug);
				goto(url);
				return;
			}
			

		} else if ((currentTab === 'soil' || currentTab === 'excavation') && project.id != '') {
			console.log('Excavation Proj ID', project.id);
			let excavation = project.excavation;
			slug = await saveProjExcavation(project.id, excavation, client);
		} else if (currentTab === 'wall' && project.id != '') {
			console.log('Sheet Proj ID', project.id);
			let excavation = project.excavation;
			slug = await saveProjExcavation(project.id, excavation, client);
			let sheet = project.sheet;
			slug = await saveProjSheet(project.id, sheet, client);
		} else if (currentTab === 'support' && project.id != '') {
		}
		if (slug === '') {
			return;
		}

		console.log('SLUG FOR NEXT', slug);
		currentStep = e.detail.step;
		return;
	}
	async function loadSheetSoils(){
	 
		const res = await client.query(QryMySoilSheets, {  } ).toPromise();
		if(res.error) throw res.error;

		// project will be passed on to all pages under it
		pileSheets=res.data?.myExcavationSheets;
	    soils=res.data?.myExcavationSoils;
	}
	function handleBack(e) {
		currentStep = e.detail.step;
		return;
	}

	function cancel() {
		dispatch('cancel', { save: 'done' });
		
	}

	function handleTab(tabId: number) {
		currentStep = tabId;
		return;
	}
	$: if (currentStep) {
		selectedTab = triggers[currentStep - 1].id;
		console.log('Selected Current Tab', selectedTab);
	}

	$: project = $projectStore;

	$: if (project) {
		console.log('Model Project', project);
	}

	if(projSlug!=""){
            $projectStore.code=projSlug;
    }
	loadSheetSoils();
</script>

<ModalLarge
	open
	small
	wide={true}
	{formId}
	{title}
	{okBtnText}
	on:cancel={cancel}
	contentScrolling={true}
	okBtnHidden={true}
	cancelBtnHidden={true}
	cls="overflow-y-visible"
	btnCls="text-white bg-blue-600 hover:text-blue-600 border border-blue-600 hover:bg-white focus:bg-white font-medium rounded text-sm px-4 py-2 text-center inline-flex items-center blue-btn duration-300 transform"
>
	<div class="w-full">
		<div class="tabitem mb-5 shadow-md bg-white">
			<ul class="block -mb-px tablist overflow-x-auto whitespace-nowrap flex-nowrap">
				{#each triggers as triggerItem}
					<li class="me-2 inline-block align-top">
						<button
							on:click={() => handleTab(triggerItem.index)}
							type="button"
							class="block px-3 py-3 border-b-2 border-transparent hover:text-blue-600 hover:border-blue-600 relative font-semibold text-sm"
						>
							<i class="inline-block me-2 align-middle"><svelte:component this={triggerItem.icon} /></i>
							{triggerItem.title}
								<!-- {#if $value === triggerItem.id}
									<div
										in:send={{ key: 'test' }}
										out:receive={{ key: 'sts' }}
										class="absolute left-0 h-1 w-full bottom-0 rounded-0 bg-blue-600"
									/>
								{/if} -->
						</button>
					</li>
				{/each}
			</ul>
		</div>
		{#if selectedTab === 'job'}
			<div class="bg-white p-3 shadow-md">
				<Client />
			</div>
		{:else if selectedTab === 'excavation'}
			<div class="bg-white p-3 shadow-md">
				<Excavation />
			</div>
		{:else if selectedTab === 'soil'}
			<div class="bg-white p-3 shadow-md">
				<Soil {soils} projectID={project.id} />
			</div>
		{:else if selectedTab === 'wall'}
			<div class=" bg-white p-3 shadow-md">
				<Wall {pileSheets} />
			</div>
		{:else if selectedTab === 'support'}
			<div class="bg-white p-3 shadow-md">
				<Support />
			</div>
		{/if}
		<NextPreviousBtn on:back={handleBack} on:next={handleNext} {currentStep} {totalStep} />
	</div>
</ModalLarge>
