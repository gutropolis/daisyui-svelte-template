<script lang="ts">
    import { onDestroy, onMount } from 'svelte';
    import { projectStore } from '$lib/stores/project';

    $: project = $projectStore; 
    console.log("Project >>>>>>>>>>",project);

    let pileHeightScalar = 1; // Initial pile height scale
    let waterDepthScalar = 1; // Initial water depth scale
   
    let excavationDepth =   0; // in meters
    let passiveWaterDepth =   0; // Passive water depth
    let activeWaterDepth =  0; // Active water depth
    let surchargeValue = `Surcharge = 0 kN/m²` ; // Surcharge value on top
    let totalDepth = excavationDepth; // Total depth of the pile

    // Excavation and pile parameters
   
    
  
    // Soil layers (with color and depth in meters)
    let soilLayers = [
      { name: "Topsoil", depthStart: 0, depthEnd: 10, color: "#000000" },
      { name: "Clay", depthStart:10, depthEnd: 20, color: "#ff980078" },
      { name: "Sand", depthStart: 20, depthEnd: 25, color: "#b9a7a1" }
    ];
  
    let canvas;
    let ctx;
    let waterDepthIcon;
    let surchargeIcon;
  
    // Define the aspect ratio
    const aspectRatio = 3 / 4; // Adjust as per your needs
  
    // Resize handler to adjust the canvas size while maintaining the aspect ratio
    function resizeCanvas() {
      canvas.width = canvas.offsetWidth;
      canvas.height = canvas.width * 1.4; // Maintain the aspect ratio
      drawSheetPileDesign();
    }
  
    // Function to convert SVG to image
    function svgToImage(svgElement, callback) {
      const svgData = new XMLSerializer().serializeToString(svgElement);
      const svgBlob = new Blob([svgData], { type: "image/svg+xml;charset=utf-8" });
      const url = URL.createObjectURL(svgBlob);
      const img = new Image();
      img.onload = function () {
        URL.revokeObjectURL(url);
        callback(img);
      };
      img.src = url;
    }
  
    // Function to draw the design on the canvas
    function drawSheetPileDesign() {
      if (!ctx ||  project?.excavation?.depth === 0) return; // Ensure the context is ready
      
      excavationDepth = project.excavation.depth; // in meters
      passiveWaterDepth = project.excavation?.passiveWaterDepth ; // Passive water depth
      activeWaterDepth =project.excavation?.activeWaterDepth  ; // Active water depth
      surchargeValue = `Surcharge = ${project.excavation?.surcharge }kN/m²` ; // Surcharge value on top
      totalDepth = excavationDepth; // Total depth of the pile
     
      console.log("Pile Height",project);
      ctx.clearRect(0, 0, canvas.width, canvas.height);
  
      const baseX = canvas.width / 2; // Center X position of the pile
      const baseY = 100; // Start of the top of the excavation (top of the canvas)
      const pileHeight = excavationDepth * 50 * pileHeightScalar; // Pile height (50px per meter scaled)
      const toeLength = 50; // Length of the toe
      const pileWidth = 20; // Width of the pile
      
  
      // 1. Draw labels for Passive and Active sides
      ctx.fillStyle = 'black';
      ctx.font = '16px Arial';
      ctx.fillText("Passive Side", baseX - 200, baseY - 20);
      ctx.fillText("Active Side", baseX + 120, baseY - 50);
  
      // 2. Draw the soil layers on Passive Side
      let cumulativeDepth = baseY;
      soilLayers.forEach(layer => {
        const layerHeight = (layer.depthEnd - layer.depthStart) * 50 * pileHeightScalar; // Scaled height of the layer
        if (cumulativeDepth >= baseY + (passiveWaterDepth * 50)) {
          ctx.fillStyle = layer.color;
          ctx.fillRect(baseX - 200, cumulativeDepth, 200, layerHeight); // Draw soil only on passive side
        }
        cumulativeDepth += layerHeight;
      });
  
      // 3. Draw the soil layers on Active Side and display soil names on the right
      cumulativeDepth = baseY;
      soilLayers.forEach(layer => {
        const layerHeight = (layer.depthEnd - layer.depthStart) * 50 * pileHeightScalar;
        if (cumulativeDepth >= baseY + (activeWaterDepth * 50)) {
          ctx.fillStyle = layer.color;
          ctx.fillRect(baseX, cumulativeDepth, 200, layerHeight); // Draw soil only on active side
  
          // Display soil name on the right side
          ctx.fillStyle = 'black';
          ctx.font = '14px Arial';
          ctx.fillText(`${layer.name}`, canvas.width - 100, cumulativeDepth + layerHeight / 2);
        }
        cumulativeDepth += layerHeight;
      });
  
      // 4. Draw the sheet pile (stem and toe)
      ctx.fillStyle = 'green'; // Pile color
      ctx.fillRect(baseX - pileWidth / 2, baseY, pileWidth, pileHeight); // Vertical stem of the pile
      ctx.fillRect(baseX - pileWidth / 2 - toeLength, baseY + pileHeight, toeLength, 10); // Horizontal toe
  
      // 5. Draw the water levels on Passive and Active sides
      const passiveWaterLevel = baseY + (passiveWaterDepth * 50 * waterDepthScalar);
      const activeWaterLevel = baseY + (activeWaterDepth * 50 * waterDepthScalar);
  
      ctx.strokeStyle = 'blue';
      ctx.setLineDash([5, 5]); // Dashed line for water levels
  
      // Draw passive water level
      ctx.beginPath();
      ctx.moveTo(0, passiveWaterLevel);
      ctx.lineTo(baseX, passiveWaterLevel);
      ctx.stroke();
  
      // Draw active water level
      ctx.beginPath();
      ctx.moveTo(baseX, activeWaterLevel);
      ctx.lineTo(canvas.width, activeWaterLevel);
      ctx.stroke();
  
      // Reset line dash style
      ctx.setLineDash([]);
  
      // 6. Draw the surcharge (SVG icon)
      svgToImage(surchargeIcon, (surchargeImage) => {
        ctx.drawImage(surchargeImage, baseX + 100, baseY - 15, 80, 20); // Adjust position
      });
  
      // 7. Draw surcharge value label
      ctx.fillStyle = 'black';
      ctx.font = '14px Arial';
      ctx.fillText(surchargeValue, baseX + 100, baseY - 20);
  
      // 8. Draw the scale on the left (depth from 0 to 10m)
      ctx.strokeStyle = 'black';
      ctx.beginPath();
      ctx.moveTo(50, baseY);
      ctx.lineTo(50, baseY + pileHeight); // Scale starts at top and goes to the bottom of the pile
      ctx.stroke();
  
      ctx.font = '12px Arial';
      for (let i = 0; i <= totalDepth; i++) {
        const depthLabelY = baseY + i * 50 * pileHeightScalar;
        ctx.fillText(`${i}m`, 20, depthLabelY + 5);
        ctx.beginPath();
        ctx.moveTo(45, depthLabelY);
        ctx.lineTo(55, depthLabelY);
        ctx.stroke();
      }
  
      // 9. Draw the water depth icon and label over the dotted line for Passive Side
      svgToImage(waterDepthIcon, (waterImage) => {
        ctx.drawImage(waterImage, baseX - 250, passiveWaterLevel - 3, 40, 40); // Adjust position
        // Add G.W.T label for passive side
        ctx.fillStyle = 'black';
        ctx.font = '14px Arial';
        ctx.fillText(`G.W.T = ${passiveWaterDepth}m`, baseX - 250, passiveWaterLevel - 10);
      });
  
      // 10. Draw the water depth icon and label over the dotted line for Active Side
      svgToImage(waterDepthIcon, (waterImage) => {
        ctx.drawImage(waterImage, canvas.width - 190, activeWaterLevel - 3, 40, 40); // Adjust position
        // Add G.W.T label for active side
        ctx.fillStyle = 'black';
        ctx.font = '14px Arial';
        ctx.fillText(`G.W.T = ${activeWaterDepth}m`, canvas.width - 190, activeWaterLevel - 10);
      });
    }
  
    // Lifecycle hook to initialize the canvas and SVG images
    onMount(() => {
      ctx = canvas.getContext('2d');
      drawSheetPileDesign(); // Initial drawing
      resizeCanvas(); // Initial sizing
  
      // Resize canvas when the window is resized
      if (typeof window !== 'undefined') {
        window.addEventListener('resize', resizeCanvas);
      }
    });
  
    // Cleanup on destroy
    onDestroy(() => {
      if (typeof window !== 'undefined') {
        window.removeEventListener('resize', resizeCanvas); // Cleanup event listener
      }
    });
  
    // Redraw the canvas when sliders change
    $:if(project.excavation?.depth > 0){
      console.log("Excavation Depth ",project.excavation?.depth);
      drawSheetPileDesign();
    } 
  </script>
  
  <!-- Inputs for user interaction -->
  <div>
    <label for="pileHeightScalar">Pile Height Scalar: </label>
    <input type="range" min="1" max="2" step="0.1" bind:value={pileHeightScalar}>
    <span>{pileHeightScalar.toFixed(1)}</span> (Scale)
  </div>
  
  <div>
    <label for="waterDepthScalar">Water Depth Scalar: </label>
    <input type="range" min="1" max="2" step="0.1" bind:value={waterDepthScalar}>
    <span>{waterDepthScalar.toFixed(1)}</span> (Scale)
  </div>
  
  <!-- Canvas for drawing -->
  <canvas bind:this={canvas} style="width: 100%;"></canvas>
  
  <!-- Hidden SVG elements for Water Depth and Surcharge icons -->
  <svg id="waterDepthIconSvg" bind:this={waterDepthIcon} xmlns="http://www.w3.org/2000/svg" width="40" height="40" style="display:none">
    <g>
      <rect x="10" y="20" width="20" height="2" fill="blue" />
      <polygon points="20,0 10,20 30,20" fill="blue" />
      <line x1="10" y1="24" x2="30" y2="24" stroke="blue" stroke-width="2" />
      <line x1="15" y1="26" x2="25" y2="26" stroke="blue" stroke-width="2" />
    </g>
  </svg>
  
  <svg id="surchargeIconSvg" bind:this={surchargeIcon} xmlns="http://www.w3.org/2000/svg" width="80" height="20" style="display:none">
    <g>
      <rect x="10" y="0" width="60" height="4" fill="red" />
      <line x1="20" y1="4" x2="20" y2="15" stroke="black" stroke-width="2" />
      <line x1="30" y1="4" x2="30" y2="15" stroke="black" stroke-width="2" />
      <line x1="40" y1="4" x2="40" y2="15" stroke="black" stroke-width="2" />
      <line x1="50" y1="4" x2="50" y2="15" stroke="black" stroke-width="2" />
      <line x1="60" y1="4" x2="60" y2="15" stroke="black" stroke-width="2" />
    </g>
  </svg>
  
  <style>
    canvas {
      border: 1px solid black;
    }
  </style>
  