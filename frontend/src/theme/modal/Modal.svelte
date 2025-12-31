<!--
  - Copyright (c) 2022. SimSaw Software Private Limited.
  - Unauthorized copying of this file, via any medium is strictly prohibited. Proprietary and confidential.
  - Author: Ankit Patial
  - Dated:  02/05/22, 6:07 PM
  -->

<script lang='ts'>
	import { createEventDispatcher } from 'svelte';
	import { portal } from '$lib/actions/portal';

	import SubTitle from '$theme/components/title/SubTitle.svelte';

	export let open = false;
	export let busy = false;
	export let title;
	export let okBtnHidden = false;
	export let cancelBtnHidden = false;
	export let okBtnText = 'OK';
	export let cancelBtnText = 'CANCEL';
	export let contentScrolling = true;
	export let cls = '';
	export let btnCls='btn btn-secondary w-36';
	export let inlineCss = '';
	export let formId = '';
	export let wide = false;
	export let small = false;
	const dispatch = createEventDispatcher();

	function ok() {
		dispatch('ok');
	}

	function cancel() {
		dispatch('cancel');
	}

	function escKeyPress({ code }) {
		if (code === 'Escape') {
			cancel();
		}
	}

</script>

<svelte:window on:keyup={escKeyPress} />

<div use:portal={'modals'} class='modal'   class:modal-open={open}>
	<div class='modal-box p-4 bg-white {(wide? "w-11/12 max-w-5xl": (small? "max-w-lg": "max-w-2xl"))} {cls}' style={inlineCss}>
		<SubTitle cls='mb-2'>{title}</SubTitle>
		<div class='pt-4 whitespace-normal' class:contentScrolling={contentScrolling}>
			<slot></slot>
		</div>
		<div class='modal-action mt-4'>
			<slot name='actions'>
				{#if !okBtnHidden}
					{#if (formId)}
						<button form={formId} class={btnCls} disabled={busy}>
							{okBtnText}
						</button>
					{:else}
						<button class={btnCls} on:click|preventDefault={ok} disabled={busy}>
							{okBtnText}
						</button>
					{/if}
				{/if}
				{#if !cancelBtnHidden}
					<button
						class='text-red-600 bg-white hover:text-white border border-red-600 hover:bg-red-600 focus:bg-red-600 font-medium rounded text-sm px-4 py-1 text-center inline-flex items-center ms-3 outline-redbtn duration-300 transform'
						on:click|preventDefault={cancel}
						class:loading={busy}
						disabled={busy}
					>
						{cancelBtnText}
					</button>
				{/if}
			</slot>
		</div>
	</div>
</div>

<style>
	.contentScrolling{
			max-height: calc(100vh - 14rem);
			overflow-y: auto;
	}
</style>