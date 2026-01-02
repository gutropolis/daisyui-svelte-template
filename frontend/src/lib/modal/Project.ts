export interface Project {
    id?: number|string;
    code?: string; // 8 characters max
    name?: string; // 50 characters max
    siteOffice?: string; // Optional, 30 characters max
    fao?: string; // Optional, 30 characters max
    tel?: string; // Optional, 20 characters max
    fax?: string; // Optional, 20 characters max
    note?: string; // Optional, 256 characters max
    status?: boolean;
    jobDesigner?: string; // Optional, 50 characters max
    title?: string; // Optional, 50 characters max
    ref?: string; // Optional, 50 characters max
    excavation?: ProjectExcavation; // Assuming ProjectExcavation is defined elsewhere
    soils?: ProjectSoil[]; // Assuming ProjectSoil is defined elsewhere
    sheet?: ProjectSheet; // Assuming ProjectSheet is defined elsewhere
  }
 
  export interface ProjectExcavation {
    name: string; // max length 250
    slug?: string; // optional, unique
    depth?: number|string; // optional, FloatField
    activeWaterDepth?: number|string; // optional, FloatField
    passiveWaterDepth?: number|string; // optional, FloatField
    surcharge?: number|string; // optional, FloatField
    waterDensity?: number|string; // optional, FloatField
    miniFluidDensity?: number|string; // optional, FloatField
    slopeType?: string; // optional, FloatField
    activeSlopeAngle?: number; // optional, FloatField
    passiveSlopeAngle?: number; // optional, FloatField
    calculationMethod: string; // choices field, max length 5
    pressureModel: string; // choices field, max length 10
    cohesivePressureType: string; // choices field, max length 20
    penetrationTypes: string; // choices field, max length 10 
    depthPassiveSoft?: number; // optional, FloatField
    applyRuleThumb: boolean; // BooleanField
    upstand?: number|string; // optional, FloatField
    toe?: number|string; // optional, FloatField
    fos?: number|string; // optional, FloatField
    passiveSoilFactorCp?: number|string;  // optional, FloatField
    passiveSoilFactorKp?: number|string;  // optional, FloatField

    terzaghiM?:number|string;
    terzaghiA ?:number|string;
    showWater?:boolean;
    tensionCrackDepth?:number|string;
    applyPassiveSoft?:boolean;
    softPassiveThickness?:number|string;

  }
 

  export interface ProjectSoil {
    depth: number|string;
    name: string; 
    slug?: string;
    type: string;
    unitWeight?: number|string;
    effectiveUnitWeight?: number|string;
    cohesion?: number|string;
    adhesion?: number|string;
    internalFriction?: number|string;
    wallFrictionAngle?: number|string;
    kActive?: number|string;
    kPassive?: number|string;
    kAc?: number|string;
    kPc?: number|string;
    orderBy: number;
  }

  export interface ProjectSheet {
    name: string;  
    slug: string;  
    sectionModule?: number|string;  
    elasticity?: number|string;  
    allowableStress?: number|string;  
    momentOfInertia?: number|string;  
    maxiBendingMoment?: number|string; 
    maxiAllowedDeflection?:number|string; 
    upstand?: number|string; 
    areaSteel?: number|string; 
    weightPerMeter?: number|string; 
    sheetName?:string;
  }



  export interface ProjectSoil {
    depth: number|string;
    name: string; 
    slug?: string;
    type: string;
    unitWeight?: number|string;
    effectiveUnitWeight?: number|string;
    cohesion?: number|string;
    adhesion?: number|string;
    internalFriction?: number|string;
    wallFrictionAngle?: number|string;
    kActive?: number|string;
    kPassive?: number|string;
    kAc?: number|string;
    kPc?: number|string;
    orderBy: number;
  }
 
  export interface DesignSoil extends ProjectSoil {
    // Additional properties
    kdiff?: number | string;
    topDepth?: number | string;
    bottomDepth?: number | string;
    literalEarthPressureTop?: number | string;
    literalEarthPressureBottom?: number | string;
    topVerticalPressure?: number | string;
    bottomVerticalPressure?: number | string;
    topForce?: number | string;
    bottomForce?: number | string;
    
  }

  export interface SheetPileDesign {
    id?: number|string;
    code?: string; // 8 characters max
    name?: string; // 50 characters max
    siteOffice?: string; // Optional, 30 characters max
    fao?: string; // Optional, 30 characters max
    tel?: string; // Optional, 20 characters max
    fax?: string; // Optional, 20 characters max
    note?: string; // Optional, 256 characters max
    status?: boolean;
    jobDesigner?: string; // Optional, 50 characters max
    title?: string; // Optional, 50 characters max
    ref?: string; // Optional, 50 characters max
    excavation?: ProjectExcavation; // Assuming ProjectExcavation is defined elsewhere
    
    rotatingPointDredge?: number | string;
    maxShearForceAtDepth?: number | string;
    maxShearForce?: number | string;
    shearForceAtRotation?: number | string;
    
    maxBendingMoment?: number | string;
    maxBendingMomentDepth?: number | string;
    
    zeroShearForceDistance?: number | string;
    totalPressureAtRotation?: number | string;
    totalDistance?: number | string;
    passiveLiteralPressureZeroShearForce?: number | string;
    depthOfPile?: number | string;
    toe?: number | string;
    otherAdditionalInfo?:  number | string; // Add more fields as needed
    soils?: DesignSoil[]; // Assuming ProjectSoil is defined elsewhere
    pressure?: number | string;
    pressureDepth?: number | string;
  }