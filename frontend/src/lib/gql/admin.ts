
import { gql } from '@urql/svelte';
 
export const SaveAdminProject = gql`
    mutation SaveAdminProject($input: ProjectInput!) {
        saveAdminProject(input: $input)
    }`;

export const UpdateAdminProject = gql`
    mutation UpdateAdminProject($input: ProjectShortInput!) {
        updateAdminProject(input: $input)
    }`;

export const QryEmailTemplates = gql`
    query emailTemplates(
        $page: PageInput!
        $where: EmailTemplateWhereInput
        $orderBy: EmailTemplateOrder
    ) {
        emailTemplates(
            page: $page
            where: $where
            orderBy: $orderBy
        ) {
            totalCount
            pageInfo {
                hasPreviousPage
                hasNextPage
                startCursor
                endCursor
            }
            edges {
                node {
                    id 
                    code 
                    title 
                    subject 
                    body 
                    sms_body 
                    type  
                    from   
                }
            }
        }
    }
    
`;
export const SaveEmailTemplate = gql`
    mutation saveEmailTemplate($input: EmailTemplateInput!) {
        saveEmailTemplate(input: $input)
    }`;

export const UpdateEmailTemplate = gql`
    mutation updateEmailTemplate($input: EmailTemplateInput!) {
        updateEmailTemplate(input: $input)
    }`;
export const DeleteEmailTemplate = gql`
mutation DeleteEmailTemplate($input: EmailTemplateInput!) {
    DeleteEmailTemplate(input: $input)
}`;
