<!--
  -  Copyright (c) 2022 - 2023.  Ankit Patial.
  -  Unauthorized copying of this file, via any medium is strictly prohibited. Proprietary and confidential.
  -  Author: Ankit Patial
  -->

<script lang='ts'>
	export let content = '';
	export let uppercase = false;
	export let id = '';
	export let cls = '';
	export let toolTipEnable=false;
	export let toolTipText=""; 
	import IconQuestionMarkCircle from '$theme/icons/IconQuestionMarkCircle.svelte';
</script>

<label class='label p-0 {cls}' for={id} >
	<span >
		{@html content} 
		{#if toolTipEnable }
			<div class="tooltip tooltip-right ml-2" data-tip={toolTipText} >
				<IconQuestionMarkCircle />
			</div>
		{/if}
	</span>
	<span class="label-text-alt">
		<slot></slot>
	</span>
</label>