<!-- MapAutocomplete.svelte -->
<script lang="ts">
    import { createEventDispatcher, onMount } from 'svelte'
    export let apiKey = 'AIzaSyDBEsN-alxNVwkCozkhtBAxSwzW_bmRCr4';
    export let options = undefined
    export let placeholder = undefined
    export let value = ''

    let autoComplete;
    let autocompleteInput;

    const dispatch = createEventDispatcher()



    onMount(() => {
      const script = document.createElement('script');
      script.src = `https://maps.googleapis.com/maps/api/js?key=${apiKey}&libraries=places`;
      script.async = true;
      script.defer = true;
      console.log("GOOGLE MAP URL",script.src)
      
      script.onload = () => {
        // Initialize the Google Places Autocomplete
        autoComplete = new google.maps.places.Autocomplete(autocompleteInput);
        
        // Listen for place selection event
        autoComplete.addListener('place_changed', () => {
          const place = autoComplete.getPlace(); 
          // Do something with the selected place
          console.log('Selected place:', place);
        });
      };
      
      document.head.appendChild(script);
    });
  </script> 
 
    <div class="autocomplete-wrapper">
      <input
        bind:this={autocompleteInput}
        class="autocomplete-input"
        type="text"
        placeholder="Enter a location"
      />
    </div>
 