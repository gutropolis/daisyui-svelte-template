<!--
 Copyright (c) 2022. Ankit Patial.
 Unauthorized copying of this file, via any medium is strictly prohibited. Proprietary and confidential.
 Author: Ankit Patial
  -->

<script lang='ts'>
	import { breadCrumbs } from '$lib/stores/app';
	import IconHome from '$theme/icons/IconHome.svelte';
	import type Entity from '$lib/models/Entity';

	let options: [Entity], lastIdx;
	$: {
		options = $breadCrumbs || [];
		lastIdx = options.length - 1;
	}

</script>

<div class='breadcrumbs pt-0 text-sm block' style='overflow: initial'>
	{#if options?.length > 0}
		<ul class='text-gray-600'>
			<li>
				<a href='/' class='hover:text-secondary'>
					 
				</a>
			</li>
			{#each options as option, idx (option.id)}
				{#if idx < lastIdx }
					<li>
						<a class='font-bold hover:text-secondary capitalize' href={option.id}>{option.name}</a>
					</li>
				{:else }
					<li>{option.name}</li>
				{/if}
			{/each}
		</ul>
	{/if}
</div>

