
import { gql } from '@urql/svelte';
// GraphQL Queries
	export const PERMISSIONS_QUERY = gql`
		query GetPermissions($page: Int, $limit: Int, $filterInput: FilterPermissionsInput) {
			permissions(page: $page, limit: $limit, filterInput: $filterInput) {
				success
				message
				data {
					id
					keyName
					name
					description
					icon
					featureId
					createdAt
					updatedAt
				}
				pagination {
					page
					limit
					total
					totalPages
					hasNext
					hasPrev
				}
			}
		}
	`;

	 

	export const CREATE_PERMISSION_MUTATION = gql`
		mutation CreatePermission($input: CreatePermissionInput!) {
			createPermission(input: $input) {
				success
				message
				data {
					id
					keyName
					name
					description
					icon
					featureId
					createdAt
					updatedAt
				}
			}
		}
	`;

	export const UPDATE_PERMISSION_MUTATION = gql`
		mutation UpdatePermission($id: Int!, $input: UpdatePermissionInput!) {
			updatePermission(id: $id, input: $input) {
				success
				message
				data {
					id
					keyName
					name
					description
					icon
					featureId
					createdAt
					updatedAt
				}
			}
		}
	`;

	export const DELETE_PERMISSION_MUTATION = gql`
		mutation DeletePermission($id: Int!) {
			deletePermission(id: $id) {
				success
				message
			}
		}
	`; 
 

 // GraphQL Queries
	export  const PLAN_FEATURES_QUERY = gql`
		query {
			planFeatures {
				success
				message
				data {
					id
					keyName
					name
					description
					createdAt
					updatedAt
				}
			}
		}
	`;

	export const CREATE_PLAN_FEATURE = gql`
		mutation CreatePlanFeature($input: CreatePlanFeatureInput!) {
			createPlanFeature(input: $input) {
				success
				message
				data {
					id
					keyName
					name
					description
					createdAt
					updatedAt
				}
			}
		}
	`;

	export const UPDATE_PLAN_FEATURE = gql`
		mutation UpdatePlanFeature($id: Int!, $input: UpdatePlanFeatureInput!) {
			updatePlanFeature(id: $id, input: $input) {
				success
				message
				data {
					id
					keyName
					name
					description
					createdAt
					updatedAt
				}
			}
		}
	`;

	export const DELETE_PLAN_FEATURE = gql`
		mutation DeletePlanFeature($id: Int!) {
			deletePlanFeature(id: $id) {
				success
				message
			}
		}
	`;


// GraphQL Queries
	export const PLANS_QUERY = gql`
		query GetPlans($page: Int, $limit: Int, $filterInput: FilterPlansInput) {
			plans(page: $page, limit: $limit, filterInput: $filterInput) {
				success
				message
				data {
					id
					slug
					name
					price
					durationDays
					maxUsers
					maxStudies
					maxStorageGb
					features
					createdAt
					updatedAt
				}
				pagination {
					page
					limit
					total
					totalPages
					hasNext
					hasPrev
				}
			}
		}
	`;

	export const DELETE_PLAN_MUTATION = gql`
		mutation DeletePlan($id: Int!) {
			deletePlan(id: $id) {
				success
				message
			}
		}
	`;


 

	export const CREATE_PLAN_MUTATION = gql`
		mutation CreatePlan($input: PlanInput!) {
			createPlan(input: $input) {
				success
				message
				data {
					id
					slug
					name
					price
					durationDays
					maxUsers
					maxStudies
					maxStorageGb
					features
					createdAt
					updatedAt
				}
			}
		}
	`;

    export const UPDATE_PLAN_MUTATION = gql`
		mutation UpdatePlan($id: Int!, $input: PlanInput!) {
			updatePlan(id: $id, input: $input) {
				success
				message
				data {
					id
					slug
					name
					price
					durationDays
					maxUsers
					maxStudies
					maxStorageGb
					features
					createdAt
					updatedAt
				}
			}
		}
	`;
export const GET_PLAN_QUERY = gql`
		query GetPlan($id: Int!) {
			plan(id: $id) {
				success
				message
				data {
					id
					slug
					name
					price
					durationDays
					maxUsers
					maxStudies
					maxStorageGb
					features
					createdAt
					updatedAt
				}
			}
		}
	`;

 