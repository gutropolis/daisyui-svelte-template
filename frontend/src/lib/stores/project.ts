// store.ts
import type { Project, ProjectExcavation, ProjectSheet, ProjectSoil, SheetPileDesign } from '$lib/models/Project';
import { writable } from 'svelte/store';


let projSheet: ProjectSheet={ 
        
    sectionModule:"",
    elasticity: "",
    allowableStress:"",
    momentOfInertia:"",
    maxiBendingMoment:"",
    maxiAllowedDeflection:"",
    //upstand:"",
    //areaSteel:"",
    //weightPerMeter:"",
    name:"",
    slug:"",
}
let projExcavation: ProjectExcavation ={ 
    depth:"",  
    activeWaterDepth:0.0,  
    passiveWaterDepth:0.0,  
    surcharge:0.0, 
    waterDensity:0.0,  
    miniFluidDensity:0.0,
    slopeType:"", 
    activeSlopeAngle:0.0,
    passiveSlopeAngle:0.0,
    calculationMethod: "k" ,
    penetrationTypes:"freeearth",
    applyRuleThumb:false,
    name:"",
    pressureModel:"rankin",
    cohesivePressureType:"minifluidhead", 

    terzaghiM:0,
    terzaghiA :0,
    showWater:false,
    tensionCrackDepth:0,
    applyPassiveSoft:false,
    softPassiveThickness:0,
    slug:"",

};
let soil:ProjectSoil= {
    depth:"", 
    name:"", 
    slug:"", 
    type:"", 
    unitWeight:"", 
    effectiveUnitWeight:"", 
    cohesion:"", 
    adhesion:"", 
    internalFriction:"", 
    wallFrictionAngle:"", 
    kActive:"", 
    kPassive:"", 
    kAc:"", 
    kPc:"",  
}
// Initialize with a default value or null
const defaultProject: Project = {
    id: undefined,
    code: '',
    name: '',
    siteOffice: '',
    fao: '',
    tel: '',
    fax: '',
    note: '',
    status: false,
    jobDesigner: '',
    title: '',
    ref: '',
    excavation: projExcavation,
    soils: [],
    sheet: projSheet
};


// Initialize with a default value or null
const defaultSheetPileDesign: SheetPileDesign = {
  id: undefined,
  code: '',
  name: '',
  siteOffice: '',
  fao: '',
  tel: '',
  fax: '',
  note: '',
  status: false,
  jobDesigner: '',
  title: '',
  ref: '',
  excavation: projExcavation,
  soils: [],

  rotatingPointDredge:'',
  maxShearForceAtDepth: '', 
  maxShearForce: '',
  shearForceAtRotation: '',

  maxBendingMomentDepth:'',
  maxBendingMoment: '',
  
  zeroShearForceDistance: '',
  totalPressureAtRotation: '',
  totalDistance: '',
  passiveLiteralPressureZeroShearForce: '',
  depthOfPile: '',
  toe: '',
  otherAdditionalInfo: '', // Add more fields as needed
  pressure: '',
  pressureDepth: '',
};



export const projCurrentStep = writable<number>(1);
export const projectStore = writable<Project>(defaultProject);
export const pileDesignStore = writable<SheetPileDesign>(defaultSheetPileDesign);
// Common function to update the excavation object
export function updateExcavation(updates) {
  projectStore.update(project => {
    project.excavation = {
      ...project.excavation, // Spread existing excavation data
      ...updates, // Merge updates into excavation
    };
    return project;
  });
}