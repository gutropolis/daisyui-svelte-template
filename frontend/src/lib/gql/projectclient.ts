import { gql } from '@urql/svelte';  
 
 

export const QryProjects = gql`
    query MyProjects($page: Int!, $perPage: Int!, $where: ProjectFilterInput,$orderBy:OrderByInput){
        myProjects(page: $page, perPage: $perPage, where: $where, orderBy: $orderBy){
            edges{
                jobDesigner
                id
                code
                name
                siteOffice
                tel
                fax
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
 export const SaveProjectClientMutation = gql`
    mutation SaveProjectClient($input: ProjectClientInput!) {
        saveProjectClient(input: $input) {
            status
            project{ 
                code,
                id 
            }
    }
}`; 

export const SaveProjExcavMutation = gql`
    mutation SaveProjectExcavation($input: ProjectExcavationInput!) {
        saveProjectExcavation(input: $input) {
            status
            msg
            excavation{ 
                slug 
            }
    }
}`; 

export const SaveProjectSheetMutation = gql`
    mutation SaveProjectSheet($input: ProjectSheetInput!) {
        saveProjectSheet(input: $input) {
            status
            msg
            sheet{ 
                slug 
            }
    }
}`; 

export const SaveProjectSoilMutation = gql`
    mutation SaveProjectSoil($input: ProjectSoilInput!) {
        saveProjectSoil(input: $input) {
            status
            msg
            soil{ 
                slug 
            }
    }
}`; 

export const RemoveSoilMutation = gql`
    mutation RemoveSoil($slug:String!,$projectId:ID!) {
        removeSoil(slug: $slug,projectId: $projectId) {
            status
            
    }
}`; 
 
 export const DesignPileSheetStrMut = gql`
    mutation DesignPileSheetStr( $projectCode:String!) {
        designPileSheetStr( projectCode: $projectCode) {
            status
            responseData  
        }
}`; 
 