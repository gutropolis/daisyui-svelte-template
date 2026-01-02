<script lang="ts">
  import { onDestroy, onMount } from 'svelte';
  import { browser } from '$app/environment';
	import { projectStore } from '$lib/stores/project';

  $: project = $projectStore; 
  console.log("Project >>>>>>>>>>",project);
  
  let pileHeightScalar = 1; // Initial pile height scale
  let waterDepthScalar = 1; // Initial water depth scale
  // Transform data into soilLayers format with depthStart, depthEnd, and color
  let depthStart = 0;
  // Excavation and pile parameters
  let excavationDepth = 10; // in meters
  let  passiveWaterDepth = 3; // Passive water depth
  let activeWaterDepth = 5; // Active water depth
  let surchargeValue = "Surcharge = 10 kN/m²"; // Surcharge value on top
  let totalDepth = excavationDepth; // Total depth of the pile

  // Soil layers (with color and depth in meters)
  let soilLayers = [];

  let canvas;
  let ctx;
  let waterDepthIcon;
  let surchargeIcon;

  // Define the aspect ratio
    const aspectRatio = 3 / 4; // Adjust as per your needs
  // Define 10 colors for soil layers
    const colors = ["#d3fffb", "#ff980078", "#b9a7a1", "#ffc1cc", "#c1caff", "#d1e2c4", "#fdd835", "#b39ddb", "#f48fb1", "#ce93d8"];
  // Resize handler to adjust the canvas size while maintaining the aspect ratio
  function resizeCanvas() {
    canvas.width = canvas.offsetWidth;
    canvas.height = canvas.width * aspectRatio; // Maintain the aspect ratio
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
    console.log("Excavation Depth",excavationDepth,"Passive WaterDepth",passiveWaterDepth,"active Water Depth",activeWaterDepth,"surchargeValue",surchargeValue,"totalDepth",totalDepth,)
    console.log("Pile Height",project);
  
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    const baseX = canvas.width / 2; // Center X position of the pile
    const baseY =80; // Start of the top of the excavation (top of the canvas)
    const pileHeight = excavationDepth * 50 * pileHeightScalar; // Pile height (50px per meter scaled)
    const toeLength = 50; // Length of the toe
    const pileWidth = 20; // Width of the pile

    // 1. Draw labels for Passive and Active sides
    ctx.fillStyle = 'black';
    ctx.font = '16px Arial';
    ctx.fillText("Passive Side", baseX - 200, baseY - 40);
    ctx.fillText("Active Side", baseX + 120, baseY - 40);

    // 2. Draw the soil layers on Passive Side
    let cumulativeDepth = baseY;
    let i =0;
    soilLayers.forEach(layer => { 
      i = i+1;
      let layerHeight = (layer.depthEnd - layer.depthStart) * 50 * pileHeightScalar; // Scaled height of the layer
      if(i===soilLayers.length){
        layerHeight = (excavationDepth - layer.depthStart) * 50 * pileHeightScalar; // Scaled height of the layer
      }
      if (cumulativeDepth >= baseY + (passiveWaterDepth * 50)) {
        ctx.fillStyle = layer.color;
        ctx.fillRect(baseX - 200, cumulativeDepth, 200, layerHeight); // Draw soil only on passive side
      }
      cumulativeDepth += layerHeight;
      
    });

    // 3. Draw the soil layers on Active Side and display soil names on the right
    i =0;
    cumulativeDepth = baseY;
    
    soilLayers.forEach(layer => {
      i = i+1;
      let layerHeight = (layer.depthEnd - layer.depthStart) * 50 * pileHeightScalar;
      if(i===soilLayers.length){
        layerHeight = (excavationDepth - layer.depthStart) * 50 * pileHeightScalar; // Scaled height of the layer
      }
      
        ctx.fillStyle = layer.color;
        ctx.fillRect(baseX, cumulativeDepth, 200, layerHeight); // Draw soil only on active side

        // Display soil name on the right side
        ctx.fillStyle = 'blue';
        ctx.font = '20px Arial';
        ctx.fillText(`${layer.name}`, canvas.width -200, cumulativeDepth + layerHeight /10);
        
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
        ctx.drawImage(waterImage, canvas.width - 360, activeWaterLevel - 3, 40, 40); // Adjust position
        // Add G.W.T label for active side
        ctx.fillStyle = 'black';
        ctx.font = '14px Arial';
        ctx.fillText(`G.W.T = ${activeWaterDepth}m`, canvas.width - 360, activeWaterLevel - 10);
      });
    }

  // Lifecycle hook to initialize the canvas and SVG images
  onMount(() => {
    ctx = canvas.getContext('2d');
    drawSheetPileDesign(); // Initial drawing
    resizeCanvas(); // Initial sizing
      if (browser) {
          // Resize canvas when the window is resized
          window.addEventListener('resize', resizeCanvas);
      }
    
  });

  // Cleanup on destroy
  onDestroy(() => {
      if (browser) {
          window.removeEventListener('resize', resizeCanvas); // Cleanup event listener
      }
    
  });

 
  // Redraw the canvas when sliders change
    $:if(project.excavation?.depth > 0 && project.soils?.length > 0){
      let depthStart = 0;
      console.log("Excavation Depth ",project.excavation?.depth);
      let data= project.soils;
      soilLayers = data.map((soil, index) => {
        const layer = {
          name: soil.name,
          depthStart: depthStart,
          depthEnd: depthStart + soil.depth,
          color: colors[index % colors.length] // Get color based on index
        };
        depthStart += soil.depth; // Update depthStart for the next layer
        return layer;
      });
      console.log("Changed Layers >>>>",soilLayers);
      drawSheetPileDesign();
    } 
</script> 
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
