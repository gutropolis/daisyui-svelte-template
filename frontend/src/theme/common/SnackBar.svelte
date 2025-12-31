<script lang='ts'>
	import alerts from '$lib/stores/alerts';
	import type Alert from '$lib/modal/Alert';
	import { humanize } from '$lib/utils/string';
	import {slide} from 'svelte/transition';
	import {quintOut} from 'svelte/easing';
	import IconCancel from '$theme/icons/IconCancel.svelte';

	let messages: [Alert] | undefined;

	$:messages = ($alerts || []) as [Alert];
	 
</script>
 
{#if (messages.length > 0)}
	<div class='toast toast-right'>
		{#each messages as msg,i}
			 
				<div class="w-96">
					<div class="absolute right-5 mt-1">
						<button class="btn btn-ghost btn-sm" on:click={() => alerts.remove(msg.id)}>
							<IconCancel/>
						</button>
					</div>
					<div class='alert alert-{msg.type} shadow-lg'  > 
						<div>
							<div>
								{#if msg.type === 'success'}
									<svg xmlns='http://www.w3.org/2000/svg' class='stroke-current flex-shrink-0 h-6 w-6' fill='none'
											viewBox='0 0 24 24'>
										<path stroke-linecap='round' stroke-linejoin='round' stroke-width='2'
													d='M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z' />
									</svg>
								{:else if msg.type === 'warning'}
									<svg xmlns='http://www.w3.org/2000/svg' class='stroke-current flex-shrink-0 h-6 w-6' fill='none'
											viewBox='0 0 24 24'>
										<path stroke-linecap='round' stroke-linejoin='round' stroke-width='2'
													d='M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z' />
									</svg>
								{:else if msg.type === 'error'}
									<svg xmlns='http://www.w3.org/2000/svg' class='stroke-current flex-shrink-0 h-6 w-6' fill='none'
											viewBox='0 0 24 24'>
										<path stroke-linecap='round' stroke-linejoin='round' stroke-width='2'
													d='M10 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2m7-2a9 9 0 11-18 0 9 9 0 0118 0z' />
									</svg>
								{:else }
									<svg xmlns='http://www.w3.org/2000/svg' fill='none' viewBox='0 0 24 24'
											class='stroke-current flex-shrink-0 w-6 h-6'>
										<path stroke-linecap='round' stroke-linejoin='round' stroke-width='2'
													d='M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z'></path>
									</svg>
								{/if}
							</div>
							<div>
								<h3 class="font-bold text-lg">{ msg.title || humanize(msg.type)}</h3>
								<div class="text-lg whitespace-pre-wrap">{@html msg.body}</div>
							</div>
						</div>
					</div>
				</div>
			 
		{/each}
	</div>
{/if}


