import { createClient, cacheExchange, errorExchange, fetchExchange } from '@urql/svelte';
import { goto } from '$app/navigation';
import { get } from 'svelte/store';
import { refreshToken, setTokens, clearTokens } from '$lib/stores/authStore';
import alerts from '$lib/stores/alerts';
import { GRAPHQL_PATH, PATH } from '$lib/enums/path';
import { authExchange } from '@urql/exchange-auth';
import { RefreshToken } from '$lib/gql/user';

export default createClient({
	url: GRAPHQL_PATH,
	exchanges: [
		cacheExchange,
		errorExchange({
			onError: (error) => {
				console.log('ERROR!!!', error);
				if (error.graphQLErrors) {
					console.log('error.graphQLErrors', error.graphQLErrors, 'error.message', error.message);
					if (error.message.includes('[GraphQL] ent')) {
						error.message = error.message.replace('[GraphQL] ent', 'DB Error');
					} else if (error.message.includes('[GraphQL] ')) {
						let message = error.message.replace('[GraphQL] ', '');

						// Check if the message contains an array of errors
						const arrayPart = message.match(/\[(.*?)\]/);

						if (arrayPart && arrayPart[1]) {
							// Convert the extracted string to an array
							const errorsArray = arrayPart[1].split("', '").map((str) => str.replace(/['\[\]]/g, '')); // Remove any remaining single quotes or brackets

							// Iterate over the array items and build the error message
							let s = '';
							errorsArray.forEach((error) => {
								s += '<span> ' + error + '</span>';
							});
							error.message = s;
						}
					}
				}

				const isAuthError = error.graphQLErrors.some(
					(e) => e.extensions?.code === 'FORBIDDEN' || e.extensions?.code === 'UNAUTHENTICATED'
				);
				if (isAuthError) {
					clearTokens();

					alerts.push({
						type: 'warning',
						title: 'Session',
						body: 'Session is expired, please login again'
					});
					goto(PATH.LOGIN);
				}
			}
		}),
		authExchange(async (utils) => {
			return {
				addAuthToOperation(operation) {
					console.log('addAuthToOperation');
					const token = localStorage.getItem('authToken');
					console.log('Token from localStorage:', token);
					if (!token) {
						return operation;
					}

					const fetchOptions = {
						...operation.context.fetchOptions,
						headers: {
							...operation.context.fetchOptions?.headers,
							Authorization: `JWT ${token}`
						},
						credentials: 'include'
					};

					return {
						...operation,
						context: {
							...operation.context,
							fetchOptions
						}
					};
				},

				didAuthError(error, _operation) {
					console.log('didAuthError');
					return error.graphQLErrors.some(
						(e) => e.extensions?.code === 'FORBIDDEN' || e.extensions?.code === 'UNAUTHENTICATED'
					);
				},

				async refreshAuth() {
					console.log('refreshAuth');
					const result = await utils.mutate(RefreshToken, { refreshToken: get(refreshToken) });

					if (result.data?.refreshToken) {
						// Update our local variables and write to storage
						const newToken = result.data.refreshToken.token;
						const newRefreshToken = result.data.refreshToken.refreshToken;
						setTokens(newToken, newRefreshToken);
					} else {
						// This is where auth has gone wrong and we need to clean up
						clearTokens();
					}
				},

				willAuthError(operation) {
					console.log('willAuthError');
					const token = localStorage.getItem('authToken');

					if (!token) {
						return false;
					}
					console.log('Check token Validation');
					// Check whether `token` JWT is expired
					const tokenPayload = JSON.parse(atob(token.split('.')[1]));
					const tokenExpiry = tokenPayload.exp * 1000;
					const currentTime = Date.now();
					const timeRemaining = tokenExpiry - currentTime;

					return timeRemaining < 120000;
				}
			};
		}),
		fetchExchange
	]
});
