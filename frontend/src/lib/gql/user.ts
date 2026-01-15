
import { gql } from '@urql/svelte';

export const QryMe= gql`
query Me {
        me  {
        
            id
            firstName
            lastName
            email 
            role
            fullName
            __typename      
        
        }
}`;

export const ALL_USERS_QUERY = gql`
    query AllUsers($search: String, $isActive: Boolean) {
        allUsers(search: $search, isActive: $isActive) {
            id
            firstName
            lastName
            email
            role
        }
    }
`;
 
export const UpdateHostProfile = gql`
  mutation UpdateHostProfile($input: UserInput!) {
    updateHostProfile(input: $input) {
      status
      message
      photo
       
    }
  }
`;
export const VerifyUserAccount = gql`
mutation VerifyAccount($slug: String!,$token: String!) {
    verifyAccount(slug: $slug,token: $token) {
        status
        message
     
  }
}
`; 
export const ForgetPasswordAccount = gql`
mutation ForgetPassword($email: String! ) {
    forgetPassword(email: $email ) {
        status  
    }
}
`; 
export const ResetPasswordMutation = gql`
mutation ResetPassword($slug: String!,$token: String!,$newPassword: String!,$password2: String!) {
    resetPassword(slug: $slug,token: $token,newPassword: $newPassword,password2: $password2) {
        status
        message
     
  }
}
`; 
 
 

  
export const RegisterUser= gql`
   mutation register(
        
        $contactNumber:String!,
        $email:String!,
        $firstName:String!,
        $lastName:String!,
        $password1:String!,
        $password2:String!,
    ) {
    register(  
        
        contactNumber: $contactNumber,
        email: $email,
        firstName: $firstName,
        lastName: $lastName,
        password1: $password1,
        password2: $password2
    ){ 
            success
            errors
            token 
            refreshToken
       }
           
   }`; 
 
 export const LoginUser= gql`
 mutation LoginAuth( 
      $email:String!, 
      $password:String!, 
  ) {
    tokenAuth(   
      email: $email, 
      password: $password, 
  ){ 
         
        token
        success
        errors
        user{
            id
            firstName
            lastName 
            email
            contactNumber
            role
        }
        refreshToken 
        __typename
        
     }
         
 }`; 
 

export const RefreshToken= gql`
mutation RefreshToken( 
     $refreshToken:String!   
 ) {
    refreshToken(   
        refreshToken: $refreshToken 
 ){ 
       payload 
       token
       refreshToken
    }
        
}`; 

export const UpdateCompany = gql`
mutation updateCompany($input: CreateCompanyInput!) {
    updateCompany(input: $input) {
        status
        message
    }
}`;

 
export const GenOTPMutation = gql`
mutation OtpEmailSend($email:String!,$type:String!) {
    otpEmailSend(email:$email,type:$type) {
        status
        message
    }
}`;
export const LoginWithOtpMutation = gql`
mutation LoginWithOtp($email:String!,$otp:String!) {
    loginWithOtp(email:$email,otp:$otp) {
        status
        message
    }
}`;


