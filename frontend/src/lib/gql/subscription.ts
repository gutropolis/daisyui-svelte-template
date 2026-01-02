import { gql } from '@urql/svelte';
export const QryMe= gql`
query Me {
        me  {
        
            id
            firstName
            lastName
            slug
            email
            company
            contactNumber
            role
            __typename      
        
        }
}`;
export const QryPlans = gql`
    query Plans {
        plans{
            id
            slug
            planName
            maxUsers
            price
            description
            durationDays
            isActive
            features{
                name
                description
            }
        }
    }
    
`;
export const QryPlanDetail = gql`
    query PlanById($slug: String!) {
        planById(slug: $slug){
            id
            slug
            planName
            maxUsers
            price
            description
            durationDays
            isActive
            features{
                name
                description
            }
        }
    }`;

export const CreateStripeOrder = gql`
  mutation MakeStripeOrder($input: PaymentInput!) {
    makeStripeOrder(input: $input) {
      status
      message 
    }
  }
`;

export const CreatePaymentIntent = gql`
  mutation InitiatePayment($input: PaymentIntentInput!) {
    initiatePayment(input: $input) {
      status
      message
      intentId
    }
  }
`; 