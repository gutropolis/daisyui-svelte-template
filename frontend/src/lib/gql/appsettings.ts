import { gql } from '@urql/svelte';

export const GetAppSettings = gql`
  query abc($input: String){
  appSetting(type:$input)  
}
`;
export const UpdateAppSettings =gql`
mutation UpdateAppSettings($type:String!,$input:Map!) {
    updateAppSetting(type:$type, input:$input) {
      success
      message
    }
  }
  `