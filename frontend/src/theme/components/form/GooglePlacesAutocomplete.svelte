<script lang="ts">
  import { createEventDispatcher, afterUpdate, onMount } from "svelte";
  import IconSpin from "$theme/icons/IconSpin.svelte";
  import { GOOGLE_MAP_API } from "$lib/enums/setting"; 
  export let apiKey = GOOGLE_MAP_API; 
  export let options = undefined;

  export let labelClass = "";
  export let ref = undefined;
  export let labelText = "";
  export let name = "";
  export let placeholder = "";
  export let required = false;
  export let value = "";
  export let disabled = false;
  export let w = "w-auto";
  export let m = "mb-3";
  export let cls = "";

  let busy = false,
    dirty = false,
    err = "";
  let map;
  let marker;
  const dispatch = createEventDispatcher();
  const id = "txt-" + Date.now();
  const inputCls =
    "input w-full text-gray-700 border border-gray-300 leading-tight focus:outline-none " +
    "focus:bg-white focus:border-secondary";

  let inputField;
  $: selectedLocationName = value || "";

  onMount(() => {
    const script = document.createElement("script");
    script.src = `https://maps.googleapis.com/maps/api/js?key=${apiKey}&libraries=places`;
    script.async = true;
    script.defer = true;
    console.log("GOOGLE MAP URL", script.src);

    script.onload = () => {
      // Listen for place selection event
      const autocomplete = new google.maps.places.Autocomplete(
        inputField,
        options
      );

      const mapOptions = {
        center: { lat: 0, lng: 0 },
        zoom: 2,
      };
      map = new google.maps.Map(document.getElementById("map"), mapOptions);

      marker = new google.maps.Marker({
        position: { lat: 0, lng: 0 },
        map: map,
        draggable: true, // Enable marker dragging
      });

      autocomplete.addListener("place_changed", () => {
        busy = true;
        const place = autocomplete.getPlace();

        if (place.geometry && place.geometry.location) {
          const location = place.geometry.location;

          marker.setPosition(location);
          map.setCenter(location);
          map.setZoom(15);
        }
        // There are circumstances where the place_changed event fires, but we
        // were NOT given location data. I only want to propagate the event if we
        // truly received location data from Google.
        // See the `Type something, no suggestions, hit Enter` test case.
        if (hasLocationData(place)) {
          setSelectedLocation({
            place: place,
            text: inputField.value,
          });
        }
        busy = false;
      });

      marker.addListener("dragend", () => {
        const geocoder = new google.maps.Geocoder();
        geocoder.geocode(
          { location: marker.getPosition() },
          (results, status) => {
            if (status === "OK") {
              const place = results[0];
              // There are circumstances where the place_changed event fires, but we
              // were NOT given location data. I only want to propagate the event if we
              // truly received location data from Google.
              // See the `Type something, no suggestions, hit Enter` test case.
              if (hasLocationData(place)) {
                setSelectedLocation({
                  place: place,
                  text: inputField.value,
                });
              }
            } else {
              console.error(
                "Reverse geocode was not successful for the following reason:",
                status
              );
            }
          }
        );
      });

      dispatch("ready");
    };

    document.head.appendChild(script);
  });

  afterUpdate(() => {
    if (map && marker) {
      const geocoder = new google.maps.Geocoder();
      geocoder.geocode({ address: inputField }, (results, status) => {
        if (status === "OK") {
          const location = results[0].geometry.location;
          marker.setPosition(location);
          map.setCenter(location);
          map.setZoom(10);
        } else {
          console.error(
            "Geocode was not successful for the following reason:",
            status
          );
        }
      });
    }
  });

  function emptyLocationField() {
    inputField.value = "";
    onChange();
  }

  function hasLocationData(place) {
    const fieldsToLookFor = (options && options.fields) || ["geometry"];
    return place.hasOwnProperty(fieldsToLookFor[0]);
  }

  function onChange() {
    if (inputField.value === "") {
      setSelectedLocation(null);
    }
  }

  function onKeyDown(event) {
    const suggestionsAreVisible =
      document.getElementsByClassName("pac-item").length;

    if (event.key === "Enter" || event.key === "Tab") {
      if (suggestionsAreVisible) {
        const isSuggestionSelected =
          document.getElementsByClassName("pac-item-selected").length;
        if (!isSuggestionSelected) {
          selectFirstSuggestion();
        }
      } else if (doesNotMatchSelectedLocation(inputField.value)) {
        setTimeout(emptyLocationField, 10);
      }
    } else if (event.key === "Escape") {
      setTimeout(emptyLocationField, 10);
    }

    if (suggestionsAreVisible) {
      if (event.key === "Enter") {
        /* When suggestions are visible, don't let an 'Enter' submit a form (since
         * the user is interacting with the list of suggestions at the time, not
         * expecting their actions to affect the form as a whole). */
        event.preventDefault();
      }
    }
  }

  function selectFirstSuggestion() {
    // Simulate the 'down arrow' key in order to select the first suggestion:
    // https://developer.mozilla.org/en-US/docs/Web/Guide/Events/Creating_and_triggering_events
    const simulatedEvent = new KeyboardEvent("keydown", {
      key: "ArrowDown",
      code: "ArrowDown",
      keyCode: 40,
    });
    inputField.dispatchEvent(simulatedEvent);
  }

  function setSelectedLocation(data) {
    selectedLocationName = (data && data.text) || "";
    dispatch("place_changed", data);
  }

  function doesNotMatchSelectedLocation(value) {
    return selectedLocationName !== value;
  }
</script>

<div class="form-control {w} {m}">
  <label class="label p-0 {labelClass}" for={id}>
    {@html labelText}
  </label>
  <div class="tooltip-top">
    <input
      class="{inputCls} {cls}"
      {id}
      {name}
      {required}
      {disabled}
      bind:this={inputField}
      on:change={onChange}
      on:keydown={onKeyDown}
      {placeholder}
      {value}
      on:keypress
      on:focus
    />
    {#if busy}
      <div class="relative float-right -mt-10 mr-1">
        <IconSpin />
      </div>
    {/if}
  </div>
  {#if $$slots.desc}
    <label class="label p-0 mt-0.5">
      <span class="label-text-alt">
        <slot name="desc" />
      </span>
    </label>
  {/if}
</div>

<div id="map" class="map" />

<style>
  .map {
    height: 400px;
    width: 100%;
  }
  .details {
    margin-top: 16px;
    width: 100%;
    max-width: 400px;
  }
</style>
