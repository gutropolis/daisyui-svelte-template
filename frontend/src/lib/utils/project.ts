import { SaveProjectClientMutation, SaveProjectSheetMutation, SaveProjectSoilMutation, SaveProjExcavMutation } from "$lib/gql/projectclient";
import type { Project, ProjectExcavation, ProjectSheet, ProjectSoil } from '$lib/models/Project';

import { Client  } from '@urql/svelte'; 
import { handleGqlErr } from '$lib/utils/gqlfx';
import alerts from '$lib/stores/alerts';  
//export let project:Project ;

 
 

export async function saveProjClient(project:Project,client:Client) {
    
    const title="Project Client";
    // Save the Connector
    const res = await client
        .mutation(SaveProjectClientMutation, {
            input: {
                code: project.code,
                name: project.name,
                siteOffice: project.siteOffice,
                fao: project.fao,
                tel: project.tel,
                fax: project.fax,
                note: project.note, 
                jobDesigner: project.jobDesigner,
                title: project.title,
                ref: project.ref,
            }
        })
        .toPromise();

     
    if (res.error) {
        const errMsg = handleGqlErr(res.error);
        alerts.error(title, errMsg);
        return "";
    }

    const result =res.data.saveProjectClient;

    if (result.status) {
        project.id = result.project.id;
        project.code = result.project.code;
        alerts.success(title, "Client Information Save Successfully!!");  
        return project.code;
    } else {
        alerts.error(title,  "Something is wrong. Please try again !!");
        return "";
    }
    return "";
}


export async function saveProjExcavation(projectID="",excavation:ProjectExcavation,client:Client) {
    
    const title="Project Excavation";
    // Save the Connector
    const res = await client
        .mutation(SaveProjExcavMutation, {
            input: {
                depth: excavation.depth,
                activeWaterDepth: excavation.activeWaterDepth,
                passiveWaterDepth: excavation.passiveWaterDepth,
                surcharge: excavation.surcharge,
                waterDensity: excavation.waterDensity,
                miniFluidDensity: excavation.miniFluidDensity,
                slopeType: excavation.slopeType,
                activeSlopeAngle:excavation.activeSlopeAngle,
                passiveSlopeAngle: excavation.passiveSlopeAngle,
                calculationMethod: excavation.calculationMethod?excavation.calculationMethod:'k',
                penetrationTypes: excavation.penetrationTypes ? excavation.penetrationTypes:"freeearth",
                applyRuleThumb: excavation.applyRuleThumb?excavation.applyRuleThumb:false,
                
                pressureModel: excavation.pressureModel,
                cohesivePressureType:excavation.cohesivePressureType?excavation.cohesivePressureType : "minifluidhead",
                terzaghiM: excavation.terzaghiM,
                terzaghiA: excavation.terzaghiA,
                showWater:excavation.showWater,
                tensionCrackDepth:excavation.tensionCrackDepth,
                applyPassiveSoft:excavation.applyPassiveSoft?excavation.applyPassiveSoft:false,
                softPassiveThickness:excavation.softPassiveThickness,
                passiveSoilFactorKp:excavation.passiveSoilFactorKp,
                passiveSoilFactorCp:excavation.passiveSoilFactorCp,
                upstand:excavation.upstand,
                toe:excavation.toe,
                fos:excavation.fos,
                slug:excavation.slug,
                projectID:projectID,
            }
        })
        .toPromise();

     
    if (res.error) {
        const errMsg = handleGqlErr(res.error);
        alerts.error(title, errMsg);
        return "";
    }

    const result =res.data.saveProjectExcavation;

    if (result.status) {
        excavation.slug = result.excavation.slug;
        alerts.success(title, result.msg);  
        return result.excavation.slug;
    } else {
        alerts.error(title, result.msg);
        return "";
    }
    return "";
}


export async function saveProjSheet(projectID="",sheet:ProjectSheet,client:Client) {
    
    const title="Project Sheet";
    console.log("Project Sheet",sheet);
    // Save the Connector
    const res = await client
        .mutation(SaveProjectSheetMutation, {
            input: {
                sectionModule: sheet.sectionModule,
                elasticity:  sheet.elasticity,
                allowableStress: sheet.allowableStress,
                momentOfInertia: sheet.momentOfInertia,
                maxiBendingMoment:  sheet.maxiBendingMoment,
                maxiAllowedDeflection: sheet.maxiAllowedDeflection,
                //upstand: sheet.upstand,
                //areaSteel:  sheet.areaSteel,
                //weightPerMeter: sheet.weightPerMeter,
                name: sheet.name,
                sheetName: sheet.sheetName,
                slug:sheet.slug,
                projectID:projectID,
            }
        })
        .toPromise();

     
    if (res.error) {
        const errMsg = handleGqlErr(res.error);
        alerts.error(title, errMsg);
        return "";
    }

    const result =res.data.saveProjectSheet;

    if (result.status) {
        sheet.slug = result.sheet.slug;
        alerts.success(title, result.msg);  
        return sheet.slug;
    } else {
        alerts.error(title, result.msg);
        return "";
    }
    return "";
}


export async function saveProjSoil(projectID="",order=1,soil:ProjectSoil,client:Client) {
    
    const title="Project Soil";
    console.log("saveProjSoil Soils ",soil);
   // Check if depth exists and is greater than 0
    if (soil.depth && parseFloat(soil.depth) <= 0) {
        alerts.error(title, "Please enter a valid depth greater than 0");
        return;
    }
    // Save the Connector
    const res = await client
        .mutation(SaveProjectSoilMutation, {
            input: {
                depth: soil.depth ? parseFloat(soil.depth):0,
                name: soil.name,
                type:soil.type,
                unitWeight:soil.unitWeight,
                effectiveUnitWeight:soil.effectiveUnitWeight,
                cohesion:soil.cohesion,
                adhesion:soil.adhesion,
                internalFriction:soil.internalFriction,
                wallFrictionAngle:soil.wallFrictionAngle,
                kActive:soil.kActive,
                kPassive:soil.kPassive,
                kAc:soil.kAc,
                kPc:soil.kPc,
                order: order,
                slug:soil.slug,
                projectID:projectID,
            }
        })
        .toPromise();

     
    if (res.error) {
        const errMsg = handleGqlErr(res.error);
        alerts.error(title, errMsg);
        return "";
    }

    const result =res.data.saveProjectSoil;

    if (result.status) {
        soil.slug = result.soil.slug;
        alerts.success(title, result.msg);  
        return soil.slug;
    } else {
        alerts.error(title, result.msg);
        return "";
    }
    return "";
}