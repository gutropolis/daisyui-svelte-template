<script lang="ts">
	import IconWall from '$theme/icons/IconWall.svelte';
	import IconTrash from '$theme/icons/IconTrash.svelte';
	import IconNew from '$theme/icons/IconNew.svelte';
	import IconSoil from '$theme/icons/IconSoil.svelte';
    import IconEdit from '$theme/icons/IconEdit.svelte';
    import IconSave from '$theme/icons/IconSave.svelte';
    import { onMount } from 'svelte';
    import { writable } from 'svelte/store'; 
    import Excavation from '$lib/components/project/Excavation.svelte'
    import Soil from '$lib/components/project/Soil.svelte'
    import Support from '$lib/components/project/Support.svelte'
    import Wall from '$lib/components/project/Wall.svelte'
	import { assets } from '$app/paths';

    let route = 'addSheet'

</script>
<style>
     
    .accordion .accordion-item {
        padding: 2px;
    }
</style>
    
<div class="w-full pt-5">
    <div class="breadcrumb text-sm text-gray-400">
            
    
        <nav class="flex" aria-label="Breadcrumb">
            <ol class="inline-flex items-center space-x-1 md:space-x-2 rtl:space-x-reverse">
            <li class="inline-flex items-center">
                <a href="#" class="inline-flex items-center text-sm font-medium text-gray-700 hover:text-blue-600 dark:text-gray-400 dark:hover:text-white">
                <svg class="w-3 h-3 me-2.5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 20 20">
                    <path d="m19.707 9.293-2-2-7-7a1 1 0 0 0-1.414 0l-7 7-2 2a1 1 0 0 0 1.414 1.414L2 10.414V18a2 2 0 0 0 2 2h3a1 1 0 0 0 1-1v-4a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v4a1 1 0 0 0 1 1h3a2 2 0 0 0 2-2v-7.586l.293.293a1 1 0 0 0 1.414-1.414Z"/>
                </svg>
                Home
                </a>
            </li>
            <li>
                <div class="flex items-center">
                <svg class="rtl:rotate-180 w-3 h-3 text-gray-400 mx-1" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 6 10">
                    <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m1 9 4-4-4-4"/>
                </svg>
                <a href="#" class="ms-1 text-sm font-medium text-gray-700 hover:text-blue-600 md:ms-2 dark:text-gray-400 dark:hover:text-white">Database</a>
                </div>
            </li>
            <li aria-current="page">
                <div class="flex items-center">
                <svg class="rtl:rotate-180 w-3 h-3 text-gray-400 mx-1" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 6 10">
                    <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m1 9 4-4-4-4"/>
                </svg>
                <span class="ms-1 text-sm font-medium text-gray-500 md:ms-2 dark:text-gray-400">Client</span>
                </div>
            </li>
            </ol>
        </nav>
  
    </div>
    <div class="w-full mt-6  shadow-md">
        <div class="flex items-center justify-between w-full font-medium text-left group-first:rounded-t border-s border-e group-first:border-t border-b border-gray-200 px-5 py-3 accordion-item bg-white">
            <span class="text-base flex gap-2 accordion-header">
                <i class="inline mt-0.5">
                    <svg width="16" height="16" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path
                            d="M1.66667 0H14.3333C15.252 0 16 0.747333 16 1.66667V16H0V1.66667C0 0.747333 0.747999 0 1.66667 0ZM0.666666 1.66667V4H4V0.666667H1.66667C1.11533 0.666667 0.666666 1.11533 0.666666 1.66667ZM11.3333 12V8.66667H4.66667V12H11.3333ZM11.3333 4V0.666667H4.66667V4H11.3333ZM8.66667 4.66667V8H15.3333V4.66667H8.66667ZM12 8.66667V12H15.3333V8.66667H12ZM4 8.66667H0.666666V12H4V8.66667ZM8 8V4.66667H0.666666V8H8ZM14.3333 0.666667H12V4H15.3333V1.66667C15.3333 1.11533 14.8847 0.666667 14.3333 0.666667ZM15.3333 12.6667H8.66667V15.3333H15.3333V12.6667ZM8 15.3333V12.6667H0.666666V15.3333H8Z"
                            fill="#4D4D4D"
                        ></path>
                    </svg>
                    <!---->
                </i>
                <span class="text-gray-700">Profile Information:</span>
            </span>
        </div>
        <div class="bg-white p-6">
        <form method="post" enctype="multipart/form-data">
            
            <fieldset class="p-4">
                <legend class="text-sm font-medium text-gray-900 px-2 text-medium">Account Information</legend>
                <div class="grid gap-3 mb-3 md:grid-cols-2"><!----></div>
                <div class="grid gap-3 mb-3 md:grid-cols-2">
                    
                    
                    
                </div>
            </fieldset>
            
            <fieldset class="p-4">
                <legend class="text-sm font-medium text-gray-900 px-2 text-medium">Profile Information</legend>
                <div class="grid gap-3 mb-3 md:grid-cols-2"><!----></div>
                <div class="grid gap-3 mb-3 md:grid-cols-2">
                    
                    
                    
                </div>
            </fieldset>
            <!---->
            <div class="text-right mt-3">
                <button
                    class="text-blue-600 bg-white hover:text-white border border-blue-600 hover:bg-blue-600 focus:bg-blue-600 font-medium rounded text-sm px-6 py-2 text-center inline-flex items-center me-2 outline-bluebtn duration-300 transform"
                >
                    <svg width="16" height="16" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <g clip-path="url(#clip0_49_583)">
                            <path
                                d="M8 6.66675C7.47258 6.66675 6.95701 6.82315 6.51848 7.11616C6.07995 7.40918 5.73815 7.82566 5.53632 8.31293C5.33449 8.80019 5.28168 9.33637 5.38457 9.85366C5.48747 10.3709 5.74144 10.8461 6.11438 11.219C6.48732 11.592 6.96248 11.8459 7.47976 11.9488C7.99704 12.0517 8.53322 11.9989 9.02049 11.7971C9.50776 11.5953 9.92424 11.2535 10.2173 10.8149C10.5103 10.3764 10.6667 9.86083 10.6667 9.33341C10.6667 8.62617 10.3857 7.94789 9.88562 7.4478C9.38552 6.9477 8.70724 6.66675 8 6.66675ZM8 10.6667C7.73629 10.6667 7.47851 10.5885 7.25924 10.442C7.03997 10.2955 6.86908 10.0873 6.76816 9.84366C6.66724 9.60002 6.64084 9.33194 6.69229 9.07329C6.74373 8.81465 6.87072 8.57708 7.05719 8.39061C7.24366 8.20414 7.48124 8.07715 7.73988 8.0257C7.99852 7.97425 8.26661 8.00066 8.51024 8.10158C8.75388 8.20249 8.96212 8.37339 9.10863 8.59265C9.25514 8.81192 9.33333 9.06971 9.33333 9.33341C9.33333 9.68704 9.19286 10.0262 8.94281 10.2762C8.69276 10.5263 8.35362 10.6667 8 10.6667Z"
                                fill="#003A91"
                            ></path>
                            <path
                                d="M15.024 2.74801L13.252 0.976013C12.9432 0.665575 12.576 0.419466 12.1714 0.251935C11.7669 0.0844031 11.3332 -0.00122304 10.8953 1.31975e-05H3.33333C2.4496 0.00107177 1.60237 0.352601 0.97748 0.977493C0.352588 1.60239 0.00105857 2.44962 0 3.33335L0 12.6667C0.00105857 13.5504 0.352588 14.3976 0.97748 15.0225C1.60237 15.6474 2.4496 15.999 3.33333 16H12.6667C13.5504 15.999 14.3976 15.6474 15.0225 15.0225C15.6474 14.3976 15.9989 13.5504 16 12.6667V5.10468C16.0012 4.66684 15.9156 4.2331 15.7481 3.82858C15.5805 3.42405 15.3344 3.05678 15.024 2.74801ZM11.3333 1.38668V2.00001C11.3333 2.53045 11.1226 3.03915 10.7475 3.41423C10.3725 3.7893 9.86377 4.00001 9.33333 4.00001H6.66667C6.13623 4.00001 5.62753 3.7893 5.25245 3.41423C4.87738 3.03915 4.66667 2.53045 4.66667 2.00001V1.33335H10.8953C11.0429 1.33466 11.1898 1.35255 11.3333 1.38668ZM14.6667 12.6667C14.6667 13.1971 14.456 13.7058 14.0809 14.0809C13.7058 14.456 13.1971 14.6667 12.6667 14.6667H3.33333C2.8029 14.6667 2.29419 14.456 1.91912 14.0809C1.54405 13.7058 1.33333 13.1971 1.33333 12.6667V3.33335C1.33333 2.80291 1.54405 2.29421 1.91912 1.91913C2.29419 1.54406 2.8029 1.33335 3.33333 1.33335V2.00001C3.33439 2.88374 3.68592 3.73097 4.31081 4.35587C4.93571 4.98076 5.78294 5.33229 6.66667 5.33335H9.33333C10.1717 5.33074 10.9781 5.01179 11.5914 4.44026C12.2047 3.86872 12.5797 3.08674 12.6413 2.25068L14.0813 3.69068C14.455 4.0666 14.6653 4.57468 14.6667 5.10468V12.6667Z"
                                fill="#003A91"
                            ></path>
                        </g>
                        <defs>
                            <clipPath id="clip0_49_583"><rect width="16" height="16" fill="white"></rect></clipPath>
                        </defs>
                    </svg>
                    <!---->
                    <span class="ms-3">Save Changes</span>
                </button>
            </div>
        </form>
        </div>
    </div>
</div>