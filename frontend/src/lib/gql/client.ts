// src/urqlClient.js
import { createClient, cacheExchange, CombinedError, errorExchange, fetchExchange, type Operation } from '@urql/svelte';
import { goto } from "$app/navigation";
import { authToken,refreshToken, setTokens, clearTokens } from '$lib/stores/authStore';
import alerts from '$lib/stores/alerts';
import { GRAPHQL_PATH, PATH } from '$lib/enums/path';
import { authExchange , } from "@urql/exchange-auth";
import { RefreshToken } from "$lib/gql/user";
const refreshAuth = async ({ authState }) => {
    console.log("Clear Token");
    if (!authState) {
        clearTokens();
        return null;
    }

    const refresh = localStorage.getItem('refreshToken');

    if (authState.token && refresh) {
        const tokenPayload = JSON.parse(atob(authState.token.split('.')[1]));
        const tokenExpiry = tokenPayload.exp * 1000;
        const currentTime = Date.now();

        // Check if the token is close to expiring
        if (tokenExpiry - currentTime > 120000) {
            return { token: authState.token };
        }

        console.log('Fetching new token...');
        console.log('GRAPHQL_PATH:', GRAPHQL_PATH);

        try {
            const response = await fetch(GRAPHQL_PATH, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    query: `
                        mutation RefreshToken($refreshToken: String!) {
                            refreshToken(refreshToken: $refreshToken) {
                                token
                                refreshToken
                            }
                        }
                    `,
                    variables: { refreshToken: refresh },
                }),
            });

            console.log('Response received:', response);

            if (!response.ok) {
                console.error('Non-200 response:', response.statusText);
                clearTokens();
                return null;
            }

            const data = await response.json();
            console.log('Parsed data:', data);

            if (data.errors) {
                console.error('GraphQL errors:', data.errors);
                clearTokens();
                return null;
            }

            const newToken = data.data.refreshToken.token;
            const newRefreshToken = data.data.refreshToken.refreshToken;
            setTokens(newToken, newRefreshToken);

            return { token: newToken };
        } catch (error) {
            console.error('Fetch error:', error);
            clearTokens();
            return null;
        }
    }

    return null;
};

 
export default function() {
    let client = createClient({
        url: GRAPHQL_PATH,
        exchanges: [
            cacheExchange,
            errorExchange({
                onError: error => {
                    console.log('ERROR!!!', error);
                    if (error.graphQLErrors) {
						console.log("error.graphQLErrors",error.graphQLErrors,"error.message",error.message)
						if (error.message.includes('[GraphQL] ent')) {
							error.message = error.message.replace('[GraphQL] ent', 'DB Error');
						} else if (error.message.includes('[GraphQL] ')) {
							
							let message = error.message.replace('[GraphQL] ', '');

							// Check if the message contains an array of errors
							const arrayPart = message.match(/\[(.*?)\]/);
							
							if (arrayPart && arrayPart[1]) {
								// Convert the extracted string to an array
								const errorsArray = arrayPart[1]
								.split("', '")
								.map(str => str.replace(/['\[\]]/g, '')); // Remove any remaining single quotes or brackets
							
								// Iterate over the array items and build the error message
								let s = '';
								errorsArray.forEach(error => {
								s += '<span> ' + error+'</span>';
								});
								error.message = s;
							}



						}
					}
                    
                    const isAuthError = error.graphQLErrors.some(e => e.extensions?.code === 'FORBIDDEN' || e.extensions?.code === 'UNAUTHENTICATED');
                    if (isAuthError) {
                        clearTokens();
                       
						alerts.push({
							type: 'warning',
							title: 'Session',
							body: 'Session is expired, please login again'
						});
                        goto(PATH.LOGIN);
                    }
                },
            }),
            authExchange(async utils => {
                   
                return {
                  addAuthToOperation(operation) {
                    console.log("addAuthToOperation");
                    const token = localStorage.getItem('authToken');

                    if (!token) {
                        return operation;
                    }
                
                    const fetchOptions = {
                        ...operation.context.fetchOptions,
                        headers: {
                            ...operation.context.fetchOptions?.headers,
                            'Authorization': `Bearer ${token}`,
                        },
                    };
                
                    return {
                        ...operation,
                        context: {
                            ...operation.context,
                            fetchOptions,
                        },
                    };
                  },
                  // ...
                  didAuthError(error, _operation) {
                    console.log("didAuthError");
                    return error.graphQLErrors.some(e => e.extensions?.code === 'FORBIDDEN' || e.extensions?.code === 'UNAUTHENTICATED');
                  },

                  // ...
                  async refreshAuth() {
                    console.log("refreshAuth");
                    const result = await utils.mutate(RefreshToken, { refreshToken });
              
                    if (result.data?.refreshLogin) {
                      // Update our local variables and write to our storage
                      let token = result.data.refreshLogin.token;
                      let refreshToken = result.data.refreshLogin.refreshToken;
                      localStorage.setItem('token', token);
                      localStorage.setItem('refreshToken', refreshToken);
                    } else {
                      // This is where auth has gone wrong and we need to clean up and redirect to a login page
                      localStorage.clear();
                       
                    }
                  },
                willAuthError(operation) {
                    console.log("willAuthError");
                    const token = localStorage.getItem('authToken');

                    if (!token) {
                        return false;
                    }
                    console.log("Check token Validation");
                    // Check whether `token` JWT is expired
                    const tokenPayload = JSON.parse(atob(token.split('.')[1]));
                    const tokenExpiry = tokenPayload.exp * 1000;
                    const currentTime = Date.now();
                    const timeRemaining = tokenExpiry - currentTime;
                
                    return timeRemaining < 120000;
                 },

                };
              }),
            fetchExchange,
        ],
    });

    return client;
}
