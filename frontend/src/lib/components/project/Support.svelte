<script lang="ts">
	import IconPlus from '$theme/icons/IconPlus.svelte';
	import IconMinus from '$theme/icons/IconMinus.svelte';
    import { createEventDispatcher } from 'svelte';
	import SupportFrame from '$theme/framebox/SupportFrame.svelte';
	import IconShare from '$theme/icons/IconShare.svelte';
	import IconQuestion from '$theme/icons/IconQuestion.svelte';
    const dispatch = createEventDispatcher();
    let formItems = [
        { id:  Date.now(), 'support_depth': 0, 'load_model': '', 'support_type': '', 'strut_angle': '', 'share_load': false, 'strut_angle_check': false }
    ];

    function addForm() {
        formItems = [...formItems, { id: Date.now(), 'support_depth': 0, 'load_model': '', 'support_type': '', 'strut_angle': '', 'share_load': false, 'strut_angle_check': false }];
    }

  function removeForm(id: any) {
    formItems = formItems.filter(item => item.id !== id);
  }

  function handleChange(event:any, id: any) {
      
    const { name, value } = event.target;
    formItems = formItems.map(field =>
      field.id === id ? { ...field, [name]: value } : field
    );

    console.log(formItems)

    // Emit the form values to the parent component
    const changeEvent = new CustomEvent('formChange', { detail: formItems });
    dispatch('formChange', changeEvent);
  }
</script>


<div class="mb-3 grid gap-3  md:grid-cols-2">
    <div>
        <SupportFrame />
    </div>
    <div>
        <img src="" alt="support frame" />
    </div>
</div>

<div class="">
    
    <div class="grid gap-3 md:grid-cols-2">
        <fieldset class="p-4 relative mb-3">
            <legend  class="text-sm font-medium text-gray-900 px-2 text-medium">Selected Frame</legend>
            <div title="Name" class="mb-3">
                <label for="" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                    >Name</label
                >
                <input type="text"  name="load_model" class="bg-slate-50 border border-gray-300 text-gray-900 text-sm rounded focus:border-s block w-full px-2.5 py-1.5" />
            </div>
            <div class="grid gap-3 md:grid-cols-3 w-100">
                <div class="flex flex-col justify-end" title="support type">
                    <label for="" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">
                       Support Type
                    </label>
                    <select class="bg-slate-50 border border-gray-300 text-gray-900 text-sm rounded-e focus:border-s block w-full px-2.5 py-1.5" name="support_type">
                        <option></option>
                        <option>Water</option>
                        <option>Brace</option>
                    </select>
                </div>
                <div class="flex flex-col justify-end">
                    <div class="flex items-center">
                        <input  id="{'shareload'}" type="checkbox" name="share_load" class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded-s focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600">
                        <label for="{'shareload'}" class="w-full ms-2 text-sm font-medium text-gray-900 dark:text-gray-300">Share Load</label>
                    </div>
                </div>
               
                <div class="mt-2 text-right">
                    <button class="text-blue-700 border border-gray-300 hover:bg-blue-600 hover:border-blue-600 rounded text-sm p-2.5 text-center inline-flex items-center bg-white duration-300 transform outline-bluebtn" title="Share">
                        <IconShare />
                    </button>
                    <button class="text-blue-700 border border-gray-300 hover:bg-blue-600 hover:border-blue-600 rounded text-sm p-2.5 text-center inline-flex items-center bg-white duration-300 transform outline-bluebtn" title="remove">
                        <IconMinus />
                    </button>
                    
                </div>
            </div>
        </fieldset>
        <fieldset class="p-4 relative mb-3">
            <legend  class="text-sm font-medium text-gray-900 px-2 text-medium">Strut</legend>
            <div title="Angle">
                <label class="block mb-2 text-sm font-medium text-gray-900">Angle</label>
                <div  class="relative">
                    <div class="pointer-events-none absolute inset-y-1 right-0 pt-0 items-center pr-3 leading-normal height-full">
                        <span class="text-gray-700 text-sm leading-normal">O</span>
                    </div>
                    <input  type="number" class="block w-full rounded  py-1.5 pr-7 ps-2  bg-slate-50 border border-gray-300 text-gray-900 text-sm focus:border-blue-600" />
                </div>
            </div>
            <div  class="grid gap-3 md:grid-cols-2 mt-3">
                <div class="flex items-center">
                    <input  id="{'anchor'}" type="checkbox" name="strut_anchor" class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded-s focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600">
                    <label for="{'anchor'}" class="w-full ms-2 text-sm font-medium text-gray-900 dark:text-gray-300">Anchor</label>
                </div>
                <div class=" text-right">
                    <button class="text-blue-700 border border-gray-300 hover:bg-blue-600 hover:border-blue-600 rounded text-sm p-2.5 text-center inline-flex items-center bg-white duration-300 transform outline-bluebtn" title="Share">
                        <IconShare />
                    </button>
                </div>
            </div>
        </fieldset>
    </div>
    <div class="grid gap-3 md:grid-cols-3">
        <fieldset class="p-4 relative mb-3">
            <legend  class="text-sm font-medium text-gray-900 px-2 text-medium">Load Model</legend>
            <div class="flex mb-2">
                <div class="flex items-center">
                    <input
                        id="areadisturbution"
                        type="radio"
                        value=""
                        name="loadmodel"
                        class="w-4 h-4 text-blue-600 bg-blue-100 border-gray-300"
                    />
                </div>
                <div class="ms-2 text-sm">
                    <label for="areadisturbution" class="font-medium text-gray-900 dark:text-gray-300"
                        >Modified K value</label
                    >
                </div>
            </div>

            <div class="flex mb-3">
                <div class="flex items-center">
                    <input
                        id="hingemethod"
                        type="radio"
                        value=""
                        name="loadmodel"
                        class="w-4 h-4 text-blue-600 bg-blue-100 border-gray-300"
                    />
                </div>
                <div class="ms-2 text-sm">
                    <label for="hingemethod" class="font-medium text-gray-900 dark:text-gray-300"
                        >Hinge Method</label
                    >
                </div>
            </div>

            <div class="flex mb-3">
                <div class="flex items-center">
                    <input
                        id="rigidwall"
                        type="radio"
                        value=""
                        name="loadmodel"
                        class="w-4 h-4 text-blue-600 bg-blue-100 border-gray-300"
                    />
                </div>
                <div class="ms-2 text-sm">
                    <label for="rigidwall" class="font-medium text-gray-900 dark:text-gray-300"
                        >Rigid Wall</label
                    >
                </div>
            </div>

            <div class="flex mb-3">
                <div class="flex items-center">
                    <input
                        id="elasticsearch"
                        type="checkbox"
                        value=""
                        name="elasticsearch"
                        class="w-4 h-4 text-blue-600 bg-blue-100 border-gray-300"
                    />
                </div>
                <div class="ms-2 text-sm">
                    <label for="elasticsearch" class="font-medium text-gray-900 dark:text-gray-300"> 
                        Elastic Search </label>
                </div>
            </div>

            <div>
                <div  class="relative">
                    <div class="pointer-events-none absolute inset-y-1 right-0 pt-0 items-center pr-3 leading-normal height-full">
                        <span class="text-gray-700 text-sm leading-normal">P<sub>x</sub></span>
                    </div>
                    <input  type="number" class="block w-full rounded  py-1.5 pr-12 ps-2  bg-slate-50 border border-gray-300 text-gray-900 text-sm focus:border-blue-600" />
                </div>
            </div>
        </fieldset>

        <fieldset class="p-4 relative mb-3">
            <legend  class="text-sm font-medium text-gray-900 px-2 text-medium">Find Supports</legend>
            
            <div class="text-end">
                <button>
                    <IconQuestion />
                </button>
            </div> 
            <div title="Max. Top Support Depth" class="mb-2">
                <label class="block mb-2 text-sm font-medium text-gray-900">Max. Top Support Depth</label>
                <div  class="relative">
                    <div class="pointer-events-none absolute inset-y-1 right-0 pt-0 items-center pr-3 leading-normal height-full">
                        <span class="text-gray-700 text-sm leading-normal">m</span>
                    </div>
                    <input  type="number" class="block w-full rounded  py-1.5 pr-7 ps-2  bg-slate-50 border border-gray-300 text-gray-900 text-sm focus:border-blue-600" />
                </div>
            </div>

            <div title="Minimum Clearence" class="mb-2">
                <label class="block mb-2 text-sm font-medium text-gray-900">Minimum Clearence</label>
                <div  class="relative">
                    <div class="pointer-events-none absolute inset-y-1 right-0 pt-0 items-center pr-3 leading-normal height-full">
                        <span class="text-gray-700 text-sm leading-normal">m</span>
                    </div>
                    <input  type="number" class="block w-full rounded  py-1.5 pr-7 ps-2  bg-slate-50 border border-gray-300 text-gray-900 text-sm focus:border-blue-600" />
                </div>
            </div>

            <div title="SWL">
                <label class="block mb-2 text-sm font-medium text-gray-900">SWL</label>
                <div  class="relative">
                    <div class="pointer-events-none absolute inset-y-1 right-0 pt-0 items-center pr-3 leading-normal height-full">
                        <span class="text-gray-700 text-sm leading-normal">kN/m</span>
                    </div>
                    <input  type="number" class="block w-full rounded  py-1.5 pr-12 ps-2  bg-slate-50 border border-gray-300 text-gray-900 text-sm focus:border-blue-600" />
                </div>
            </div>
           
        </fieldset>
        <fieldset class="p-4 relative">
            <div class="flex mb-3">
                <div class="flex items-center">
                    <input
                        id="scaleframe"
                        type="checkbox"
                        value=""
                        name="scaleframe"
                        class="w-4 h-4 text-blue-600 bg-blue-100 border-gray-300"
                    />
                </div>
                <div class="ms-2 text-sm">
                    <label for="scaleframe" class="font-medium text-gray-900 dark:text-gray-300"> 
                        Scale Frame </label>
                </div>
            </div>

            <div class="flex mb-3">
                <div class="flex items-center">
                    <input
                        id="showframedescription"
                        type="checkbox"
                        value=""
                        name="showframedescription"
                        class="w-4 h-4 text-blue-600 bg-blue-100 border-gray-300"
                    />
                </div>
                <div class="ms-2 text-sm">
                    <label for="showframedescription" class="font-medium text-gray-900 dark:text-gray-300"> 
                        Show Frame Description </label>
                </div>
            </div>

            <div class="flex mb-3">
                <div class="flex items-center">
                    <input
                        id="concretelowestframe"
                        type="checkbox"
                        value=""
                        name="concretelowestframe"
                        class="w-4 h-4 text-blue-600 bg-blue-100 border-gray-300"
                    />
                </div>
                <div class="ms-2 text-sm">
                    <label for="concretelowestframe" class="font-medium text-gray-900 dark:text-gray-300"> 
                        Concrete Lowest Frame </label>
                </div>
            </div>
        </fieldset>
    </div>

</div>

 