<script> 
	import graph   from "$theme/images/graph.png"
	import SideBarSummery from "./SideBarSummery.svelte";
</script>

<div class=" flex w-full h-[680px] gap-4 ">
    <SideBarSummery on:manageProject /> 
	<div class="flex-1   flex-col  border-1 h-full p-5 w-full px-28  bg-white shadow-sm   rounded-lg" style="box-shadow: 0px 0px 4px 0px #00000033;">
       <div class="flex   h-[50%] items-end justify-center ">
        <img class="object-scale-down w-[50%] h-[90%]" src={graph} />
        <img class="object-scale-down w-[50%] h-[90%]" src={graph} />
       </div>
       <div class="flex  h-[50%] items-start justify-center">
        <img class="object-scale-down w-[50%] h-[90%]" src={graph} />
        <img class="object-scale-down w-[50%] h-[90%]" src={graph} />
       </div>
        
    </div>
</div>
