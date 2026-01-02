
import { gql } from '@urql/svelte';


export const QryMySoilSheets = gql`
query MySoilSheets{
    myExcavationSheets{
        
        name
        slug
        sectionModule
        elasticity
        allowableStress
        momentOfInertia
        maxiBendingMoment
        upstand
        areaSteel
        weightPerMeter
        status
    }
    myExcavationSoils{
        name
        slug
        type
        unitWeight
        effectiveUnitWeight
        cohesion
        adhesion
        internalFriction
        wallFrictionAngle
        kActive
        kPassive
        kAc
        kPc 
    }
}

`;

export const QryProject = gql`
    query ProjectById($code: String!) {
        projectById(code: $code) {
                    id
                    createdAt
                    code
                    name
                    siteOffice
                    fao
                    tel
                    fax
                    status
                    jobDesigner
                    title
                    ref
                    note
                    user{
                        id
                    }
                    projexcavation{
                        id
                        name
                        slug
                        depth
                        activeWaterDepth
                        passiveWaterDepth
                        surcharge
                        waterDensity
                        miniFluidDensity
                        slopeType
                        activeSlopeAngle
                        passiveSlopeAngle
                        calculationMethod
                        pressureModel
                        cohesivePressureType
                        penetrationTypes
                        applyPassiveSoft
                        depthPassiveSoft
                        applyRuleThumb
                        upstand
                        toe
                        fos
                        passiveSoilFactorCp
                        passiveSoilFactorKp
                        terzaghiM
                        terzaghiA
                        showWater
                        tensionCrackDepth
                        softPassiveThickness
                    
                    }
                    soilproject{
                        id
                        depth
                        name
                        
                        slug
                        type
                        unitWeight
                        effectiveUnitWeight
                        cohesion
                        adhesion
                        internalFriction
                        wallFrictionAngle
                        kActive
                        kPassive
                        kAc
                        kPc
                        orderBy
                    
                    }          
                    sheetproject{
                        id
                        name
                        sheetName
                        slug
                        sectionModule
                        elasticity
                        allowableStress
                        momentOfInertia
                        maxiBendingMoment
                        maxiAllowedDeflection
                        upstand
                        areaSteel
                        weightPerMeter
                    
                    } 
           
        }
         
    }   
`;