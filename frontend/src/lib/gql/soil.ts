import { gql } from '@urql/svelte';  

export const QrySoils = gql`
    query Soils ($page: Int!, $perPage: Int!, $where: SoilFilterInput,$orderBy:OrderByInput){
        soils(page: $page, perPage: $perPage, where: $where, orderBy: $orderBy){
            edges{
                id
      			slug
                name
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
                status
        
            }
            totalCount
            hasNextPage
            hasPreviousPage
            totalPages
            nextPageNumber
            previousPageNumber 

        }
    }
    
`;
export const QrySoilDetail = gql`
    query SoilByID($slug:String!) {
        soilById(slug: $slug){
            id
            name
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
            status
        }
    }`;
 
export const CreateSoilMutation = gql`
  mutation CreateSoil($input: SoilInput!) {
    createSoil(input: $input) {
        status
        slug
        message
    }
  }
`; 
 
export const UpdateSoilMutation = gql`
  mutation UpdateSoil($input: SoilInput!) {
    updateSoil(input: $input) {
        status
        slug
        message
    }
  }
`;

 export const QryPileSheets = gql`
    query PileSheets ($page: Int!, $perPage: Int!, $where: PileSheetFilterInput,$orderBy:OrderByInput){
        pileSheets(page: $page, perPage: $perPage, where: $where, orderBy: $orderBy){
            edges{
                id
                slug
                name
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
            totalCount
            hasNextPage
            hasPreviousPage
            totalPages
            nextPageNumber
            previousPageNumber 
        }
    }
    
`;
export const QryPileSheetBySlug = gql`
    query PileheetById($slug:String!) {
        pilesheetById(slug: $slug){
                id
                name
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
    }`;
 
 
 export const CreatePileSheetMutation = gql`
 mutation CreatePilesheet($input: PileSheetInput!) {
    createPilesheet(input: $input) {
       status
       slug
       message
   }
 }
`; 

export const UpdatePileSheetMutation = gql`
 mutation UpdatePileSheet($input: PileSheetInput!) {
    updatePilesheet(input: $input) {
       status
       slug
       message
   }
 }
`;