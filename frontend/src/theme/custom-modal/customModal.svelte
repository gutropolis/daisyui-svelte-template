<!-- components/Modal.svelte -->
<script>
    export let isOpen = false;
    export let onClose;

    let activeTab = 'tab1';
</script>
  
  {#if isOpen}
    <div class="modal">
        
      <div class="modal-content">
        <div class="modal-title border-gray-300 border-b">
            <h3>Edit Information</h3>
            <span class="close" on:click={onClose}>&times;</span>
        </div>
        <slot />
        
        <!-- Add more divs for additional tab contents if needed -->
      </div>
    </div>
  {/if}
  
  <style>
    /* Modal styles */
    .modal {
      display: block;
      position: fixed;
      z-index: 45;
      left: 0;
      top: 0;
      width: 100%;
      height: 100%;
      overflow: auto;
      background-color: rgba(0, 0, 0, 0.5);
    }
  
    .modal-content {
      background-color: #fff;
      margin: 10px auto;
      padding: 0px;
      width: 80%;
      max-width: 768px;
    }

    .modal-content .modal-title{
        position: relative;
        padding: 15px 35px 15px 15px;
        border-bottom: solid 1px #d4d4d4;
    }

    .modal-content .modal-title .close{
        position: absolute;
        right: 10px;
        top: 8px;
    }
  
    .close {
      color: #aaa;
      float: right;
      font-size: 28px;
      font-weight: bold;
    }
  
    .close:hover,
    .close:focus {
      color: black;
      text-decoration: none;
      cursor: pointer;
    }
  
    /* Tab styles */
    .tab {
      overflow: hidden;
      border-bottom: 1px solid #ccc;
      margin-bottom: 15px;
    }
  
    .tab button {
      background-color: inherit;
      float: left;
      border: none;
      outline: none;
      cursor: pointer;
      padding: 14px 16px;
      transition: 0.3s;
      font-size: 17px;
    }
  
    .tab button:hover {
      background-color: #ddd;
    }
  
    .tab button.active {
      background-color: #ccc;
    }
  </style>
  