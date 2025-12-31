<!-- InputField.svelte -->
<script>
    export let label = "";
    export let id = "";
    export let orientation = "vertical";
    export let type = "text";
  </script>
  
  <div class="mb-4 flex flex-col" class:horizontal={orientation === "horizontal"}>
    <label class="mb-1" for={id}>{label}</label>
    <input type={type} id={id} class="border rounded px-2 py-1" />
  </div>
  
  <style>
    .horizontal {
      display: flex;
      flex-direction: row;
      align-items: center;
    }
  </style>