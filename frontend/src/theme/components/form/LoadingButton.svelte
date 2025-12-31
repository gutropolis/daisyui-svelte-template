<script lang="ts">
    export let isLoading = false;
    export let type: 'submit' | 'button'   = 'submit'; 
    export let className="";
    export let label="Submit";

    let cls= isLoading?" isLoading":"";

  </script>
  
  <button
    class='{className} {cls}' 
    type={type} 
  >
    {#if isLoading}
      <svg class="animate-spin h-5 w-5 mr-3" viewBox="0 0 24 24">
        <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4" />
        <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 0012 20v-2a5.978 5.978 0 01-3.535-1.465l-1.414 1.414zM12 4V2a8 8 0 018 8h-2a6 6 0 00-6-6z" />
      </svg>
      Loading...
    {:else}
      {label}
    {/if}
    <slot>

    </slot>
   
  </button>
 