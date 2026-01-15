import { gql } from '@urql/svelte';

export const SUBSCRIPTIONS_QUERY = gql`
	query Subscriptions($userId: ID, $status: String) {
		subscriptions(userId: $userId, status: $status) {
			id
			startDate
			endDate
			status
			paidStatus
			autoRenew
			createdAt
			updatedAt
			plan {
				id
				slug
				name
				price
				durationDays
			}
			user {
				id
				firstName
				lastName
				email
			}
		}
	}
`;

export const CREATE_SUBSCRIPTION_MUTATION = gql`
	mutation CreateSubscription($input: SubscriptionInput!) {
		createSubscription(input: $input) {
			subscription {
				id
				status
				startDate
				endDate
			}
		}
	}
`;