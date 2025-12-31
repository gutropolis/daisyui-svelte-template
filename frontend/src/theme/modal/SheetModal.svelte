<script lang="ts">
	import Modal from '$theme/components/modal/Modal.svelte';
	import { createEventDispatcher } from 'svelte';
	import { getContextClient } from '@urql/svelte';
	import { CreatePileSheetMutation, CreateSoilMutation, UpdatePileSheetMutation, UpdateSoilMutation } from '$lib/gql/soil';
	import DropDown from '$theme/components/form/DropDown.svelte';
	import alerts from '$lib/stores/alerts';
	import type { PileSheet, Soil } from '$lib/models/PileDesign';  
	import { SOIL_TYPES } from '$lib/enums/piledatabase'; 
	import { handleGqlErr } from '$lib/utils/gqlfx';

	export let pileSheet: PileSheet = {
		slug: '', 
		name: '',  
        sectionModule: 0.0, 
        elasticity: 0.0,  
        allowableStress: 0.0, 
        momentOfInertia: 0.0, 
        maxiBendingMoment: 0.0, 
        upstand: 0.0, 
        areaSteel: 0.0, 
        weightPerMeter: 0.0, 
	};

	const options = { theme: 'snow' };
	const client = getContextClient();
	const dispatch = createEventDispatcher();

	let formId = 'add-sheet',
		busy = false,
		err,
		readOnly = false;

	let disabled = false;
	let title = 'Add Sheet';
	let okBtnText = 'Save';

	async function save() {
		busy = true;
		let mutation = pileSheet.slug ? UpdatePileSheetMutation : CreatePileSheetMutation;
		// Save the Connector
		const res = await client
			.mutation(mutation, {
				input: {
					slug: pileSheet.slug, 
					name: pileSheet.name,   
					sectionModule:pileSheet.sectionModule, 
					elasticity: pileSheet.elasticity, 
					allowableStress: pileSheet.allowableStress, 
					momentOfInertia: pileSheet.momentOfInertia, 
					maxiBendingMoment: pileSheet.maxiBendingMoment, 
					upstand: pileSheet.upstand, 
					areaSteel: pileSheet.areaSteel, 
					weightPerMeter: pileSheet.weightPerMeter,  
				}
			})
			.toPromise();

		busy = false;
		if (res.error) {
			let errMsg = handleGqlErr(res.error);
			alerts.error(title, errMsg);
			return false;
		}

		let result = pileSheet.slug ? res.data.updatePilesheet : res.data.createPilesheet;

		if (result.status) {
			pileSheet.slug = result.slug;
			alerts.success(title, result.message);
			dispatch('saved', { response: 'done' });
			return;
		} else {
			alerts.error(title, result.message);
			return;
		}
	}

	function cancel() {
		dispatch('cancel', { save: 'done' });
	}
</script>

<Modal
	open
	small
	{formId}
	{title}
	{okBtnText}
	on:cancel={cancel}
	contentScrolling={false}
	cls="overflow-y-visible"
	btnCls="text-white bg-blue-600 hover:text-blue-600 border border-blue-600 hover:bg-white focus:bg-white font-medium rounded text-sm px-4 py-2 text-center inline-flex items-center blue-btn duration-300 transform"
>
	<div class="grid grid-cols-12 gap-4">
		<div class="col-span-12">
			<form id={formId} class="w-full" on:submit|preventDefault={save}>
				<div class="grid gap-3 mb-6 md:grid-cols-2">
					<div title="Name">
						<label for="" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Name</label>
						<input
							type="text"
							maxlength="100"
							bind:value={pileSheet.name}
							class="block w-full rounded py-1.5 pr-7 ps-3 bg-slate-50 border border-gray-300 text-gray-900 text-sm focus:border-blue-600"
						/>
					</div>
					<div title="Section Module">
						<label for="" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Section Module</label>
						<div class="relative">
							<div
								class="pointer-events-none absolute inset-y-1 right-0 pt-0 items-center pr-3 leading-normal height-full"
							>
								<span class="text-gray-700 text-sm leading-normal">kN/m<sup>3</sup></span>
							</div>
							<input
								type="number"
								step="any"
								bind:value={pileSheet.sectionModule}
								class="block w-full rounded py-1.5 pr-[75px] ps-3 bg-slate-50 border border-gray-300 text-gray-900 text-sm focus:border-blue-600"
							/>
						</div>
					</div> 
				</div>

				<div class="grid gap-3 mb-6 xsm:grid-cols-2">
					<div title="Elasticity">
						<label for="" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Elasticity</label>
						<div class="relative">
							<div
								class="pointer-events-none absolute inset-y-1 right-0 pt-0 items-center pr-3 leading-normal height-full"
							>
								<span class="text-gray-700 text-sm leading-normal">kN/m<sup>3</sup></span>
							</div>
							<input
								type="number"
								step="any"
								bind:value={pileSheet.elasticity}
								class="block w-full rounded py-1.5 pr-[75px] ps-3 bg-slate-50 border border-gray-300 text-gray-900 text-sm focus:border-blue-600"
							/>
						</div>
					</div>
					<div title="Allowable Stress">
						<label for="" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
							>Allowable Stress</label
						>
						<div class="relative">
							<div
								class="pointer-events-none absolute inset-y-1 right-0 pt-0 items-center pr-3 leading-normal height-full"
							>
								<span class="text-gray-700 text-sm leading-normal">kN/m<sup>3</sup></span>
							</div>
							<input
								type="number"
								step="any"
								bind:value={pileSheet.allowableStress}
								class="block w-full rounded py-1.5 pr-[75px] ps-3 bg-slate-50 border border-gray-300 text-gray-900 text-sm focus:border-blue-600"
							/>
						</div>
					</div>
					<div title="Moment of Intertia">
						<label for="" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Moment of Intertia</label>
						<div class="relative">
							<div
								class="pointer-events-none absolute inset-y-1 right-0 pt-0 items-center pr-3 leading-normal height-full"
							>
								<span class="text-gray-700 text-sm leading-normal">(kN/m<sup>2</sup>)</span>
							</div>
							<input
								type="number"
								step="any"
								bind:value={pileSheet.momentOfInertia}
								class="block w-full rounded py-1.5 pr-[75px] ps-3 bg-slate-50 border border-gray-300 text-gray-900 text-sm focus:border-blue-600"
								placeholder="Max. Bending moment"
							/>
						</div>
					</div>
					<div title="Maxi Bending Moment">
						<label for="" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Maximum Bending Moment</label>
						<div class="relative">
							<div
								class="pointer-events-none absolute inset-y-1 right-0 pt-0 items-center pr-3 leading-normal height-full"
							>
								<span class="text-gray-700 text-sm leading-normal">kN/m<sup>2</sup></span>
							</div>
							<input
								type="number"
								step="any"
								bind:value={pileSheet.maxiBendingMoment}
								class="block w-full rounded py-1.5 pr-[75px] ps-3 bg-slate-50 border border-gray-300 text-gray-900 text-sm focus:border-blue-600"
								placeholder="Cohesion"
							/>
						</div>
					</div>
				</div>

				<div class="grid gap-3 xsm:grid-cols-2">
					<div title="Upstand">
						<label for="" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Upstand</label>
						<!-- <input type="number" class="bg-slate-50 border border-gray-300 text-gray-900 text-sm rounded focus:border-s block w-full px-2.5 py-1.5" /> -->
						<div class="relative">
							<div
								class="pointer-events-none absolute inset-y-0 right-0 pt-2 items-center pr-3 leading-none height-full"
							>
								<span class="text-gray-700 text-lg leading-none">°</span>
							</div>
							<input
								type="number"
								step="any"
								bind:value={pileSheet.upstand}
								class="block w-full rounded py-1.5 pr-7 ps-3 bg-slate-50 border border-gray-300 text-gray-900 text-sm focus:border-blue-600"
								placeholder="Angle of internal friction of soil"
							/>
						</div>
					</div>
					<div title="Area of Steel">
						<label for="" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
							>Area of Steel:</label
						>
						<!-- <input type="number" class="bg-slate-50 border border-gray-300 text-gray-900 text-sm rounded focus:border-s block w-full px-2.5 py-1.5" placeholder="Angle of friction of soil and plates" /> -->

						<div class="relative">
							<div
								class="pointer-events-none absolute inset-y-1 right-0 pt-0 items-center pr-3 leading-normal height-full"
							>
								<span class="text-gray-700 text-sm leading-normal">mm</span>
							</div>
							<input
								type="number"
								step="any"
								bind:value={pileSheet.areaSteel}
								class="block w-full rounded py-1.5 pr-[45px] ps-3 bg-slate-50 border border-gray-300 text-gray-900 text-sm focus:border-blue-600"
								placeholder="Angle of internal friction of soil"
							/>
						</div>
					</div>
					<div class="grid gap-3 mb-3 sm:grid-cols-2">
						<div title="Weight Per meter">
							<label for="" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Weight<sub>(m)</sub></label>
							<input
								type="number"
								step="any"
								bind:value={pileSheet.weightPerMeter}
								class="bg-slate-50 border border-gray-300 text-gray-900 text-sm rounded focus:border-s block w-full px-2.5 py-1.5"
								placeholder="Coefficient of active pressure for cohession soil"
							/>
						</div>
					 
					</div>
					 
				</div>
			</form>
		</div>
	</div>
</Modal>
