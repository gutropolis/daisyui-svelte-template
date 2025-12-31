<script lang="ts">
	import Modal from '$theme/components/modal/Modal.svelte';
	import { createEventDispatcher } from 'svelte';
	import { getContextClient } from '@urql/svelte';
	import { CreateSoilMutation, UpdateSoilMutation } from '$lib/gql/soil';
	import DropDown from '$theme/components/form/DropDown.svelte';
	import alerts from '$lib/stores/alerts';
	import type { PileSheet, Soil } from '$lib/models/PileDesign';  
	import { SOIL_TYPES } from '$lib/enums/piledatabase'; 
	import { handleGqlErr } from '$lib/utils/gqlfx';

	export let soil: Soil = {
		slug: '',
		type: '',
		name: '',
		unitWeight: 0.0,
		effectiveUnitWeight: 0.0,
		cohesion: 0.0,
		adhesion: 0.0,
		internalFriction: 0.0,
		wallFrictionAngle: 0.0,
		kActive: 0.0,
		kPassive: 0.0,
		kAc: 0.0,
		kPc: 0.0
	};

	const options = { theme: 'snow' };
	const client = getContextClient();
	const dispatch = createEventDispatcher();

	let formId = 'add-soil',
		busy = false,
		err,
		readOnly = false;

	let disabled = false;
	let title = 'Add Soil';
	let okBtnText = 'Save';

	async function save() {
		busy = true;
		let mutation = soil.slug ? UpdateSoilMutation : CreateSoilMutation;
		// Save the Connector
		const res = await client
			.mutation(mutation, {
				input: {
					slug: soil.slug,
					name: soil.name,
					type: soil.type,
					unitWeight: soil.unitWeight,
					effectiveUnitWeight: soil.effectiveUnitWeight,
					cohesion: soil.cohesion,
					adhesion: soil.adhesion,
					internalFriction: soil.internalFriction,
					wallFrictionAngle: soil.wallFrictionAngle,
					kActive: soil.kActive,
					kPassive: soil.kPassive,
					kAc: soil.kAc,
					kPc: soil.kPc
				}
			})
			.toPromise();

		busy = false;
		if (res.error) {
			let errMsg = handleGqlErr(res.error);
			alerts.error(title, errMsg);
			return false;
		}

		let result = soil.slug ? res.data.updateSoil : res.data.createSoil;

		if (result.status) {
			soil.slug = result.slug;
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
							bind:value={soil.name}
							class="block w-full rounded py-1.5 pr-7 ps-3 bg-slate-50 border border-gray-300 text-gray-900 text-sm focus:border-blue-600"
						/>
					</div>
					<div title="Submerged Density">
						<DropDown
							labelClass="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
							label="Type"
							cls="bg-slate-50 border border-gray-300 text-gray-900 text-sm rounded focus:border-s block w-full px-2.5 py-1.5"
							bind:value={soil.type}
							options={SOIL_TYPES}
						/>
					</div>
				</div>

				<div class="grid gap-3 mb-6 xsm:grid-cols-2">
					<div title="Unit Weight">
						<label for="" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Unit Weight</label>
						<div class="relative">
							<div
								class="pointer-events-none absolute inset-y-1 right-0 pt-0 items-center pr-3 leading-normal height-full"
							>
								<span class="text-gray-700 text-sm leading-normal">kN/m<sup>3</sup></span>
							</div>
							<input
								type="number"
								step="any"
								bind:value={soil.unitWeight}
								class="block w-full rounded py-1.5 pr-[75px] ps-3 bg-slate-50 border border-gray-300 text-gray-900 text-sm focus:border-blue-600"
							/>
						</div>
					</div>
					<div title="Effective Unit Weight">
						<label for="" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
							>Effective Unit Weight</label
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
								bind:value={soil.effectiveUnitWeight}
								class="block w-full rounded py-1.5 pr-[75px] ps-3 bg-slate-50 border border-gray-300 text-gray-900 text-sm focus:border-blue-600"
							/>
						</div>
					</div>
					<div title="Max. Bending moment">
						<label for="" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Adhesion (Ca)</label>
						<div class="relative">
							<div
								class="pointer-events-none absolute inset-y-1 right-0 pt-0 items-center pr-3 leading-normal height-full"
							>
								<span class="text-gray-700 text-sm leading-normal">(kN/m<sup>2</sup>)</span>
							</div>
							<input
								type="number"
								step="any"
								bind:value={soil.adhesion}
								class="block w-full rounded py-1.5 pr-[75px] ps-3 bg-slate-50 border border-gray-300 text-gray-900 text-sm focus:border-blue-600"
								placeholder="Max. Bending moment"
							/>
						</div>
					</div>
					<div title="Cohesion">
						<label for="" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Cohesion(C)</label>
						<div class="relative">
							<div
								class="pointer-events-none absolute inset-y-1 right-0 pt-0 items-center pr-3 leading-normal height-full"
							>
								<span class="text-gray-700 text-sm leading-normal">kN/m<sup>2</sup></span>
							</div>
							<input
								type="number"
								step="any"
								bind:value={soil.cohesion}
								class="block w-full rounded py-1.5 pr-[75px] ps-3 bg-slate-50 border border-gray-300 text-gray-900 text-sm focus:border-blue-600"
								placeholder="Cohesion"
							/>
						</div>
					</div>
				</div>

				<div class="grid gap-3 xsm:grid-cols-2">
					<div title="Angle of internal friction of soil">
						<label for="" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Internal friction</label>
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
								bind:value={soil.internalFriction}
								class="block w-full rounded py-1.5 pr-7 ps-3 bg-slate-50 border border-gray-300 text-gray-900 text-sm focus:border-blue-600"
								placeholder="Angle of internal friction of soil"
							/>
						</div>
					</div>
					<div title="Angle of friction of soil and plates">
						<label for="" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
							>Wall friction angle:</label
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
								bind:value={soil.wallFrictionAngle}
								class="block w-full rounded py-1.5 pr-[45px] ps-3 bg-slate-50 border border-gray-300 text-gray-900 text-sm focus:border-blue-600"
								placeholder="Angle of internal friction of soil"
							/>
						</div>
					</div>
					<div class="grid gap-3 mb-3 sm:grid-cols-2">
						<div title="Coefficient of active pressure for cohession soil">
							<label for="" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">K<sub>a</sub></label>
							<input
								type="number"
								step="any"
								bind:value={soil.kActive}
								class="bg-slate-50 border border-gray-300 text-gray-900 text-sm rounded focus:border-s block w-full px-2.5 py-1.5"
								placeholder="Coefficient of active pressure for cohession soil"
							/>
						</div>
						<div title="Coefficient of passive pressure for cohession soil" class="mb-3">
							<label for="" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">K<sub>p</sub></label>
							<input
								type="number"
								step="any"
								bind:value={soil.kPassive}
								class="bg-slate-50 border border-gray-300 text-gray-900 text-sm rounded focus:border-s block w-full px-2.5 py-1.5"
								placeholder="Coefficient of passive pressure for cohession soil"
							/>
						</div>
					</div>
					<div class="grid gap-3 sm:grid-cols-2">
						<div title="Coefficient of active pressure for cohesive soil">
							<label for="" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">K<sub>ac</sub></label>
							<input
								type="number"
								step="any"
								bind:value={soil.kAc}
								class="bg-slate-50 border border-gray-300 text-gray-900 text-sm rounded focus:border-s block w-full px-2.5 py-1.5"
								placeholder="Coefficient of active pressure for cohesive soil"
							/>
						</div>

						<div title="Coefficient of passive pressure for cohesive soil">
							<label for="" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">K<sub>pc</sub></label>
							<input
								type="number"
								step="any"
								bind:value={soil.kPc}
								class="bg-slate-50 border border-gray-300 text-gray-900 text-sm rounded focus:border-s block w-full px-2.5 py-1.5"
								placeholder="Coefficient of passive pressure for cohesive soil"
							/>
						</div>
					</div>
				</div>
			</form>
		</div>
	</div>
</Modal>
