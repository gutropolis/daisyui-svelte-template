 

import { browser } from '$app/environment'; 
import client from '$lib/gql/client';
import { QryMe } from '$lib/gql/user';
import { clearTokens } from '$lib/stores/authStore';
 
 
export async function load({ params }: any) {
	if (!browser) {
		return {
			authUser: undefined
		};
	}

	try {
		const res = await client.query(QryMe, {}).toPromise();
		console.log('Layout Load Me Query Result:', res);

		if (res.error) {
			console.error('QryMe Error:', res.error);
			clearTokens();
			return {
				authUser: undefined
			};
		}

		if (!res.data?.me) {
			console.warn('No user data returned from QryMe');
			clearTokens();
			return {
				authUser: undefined
			};
		}

		 
		// User data will be passed on to all pages under it
		return {
			authUser: res.data.me
		};
	} catch (error) {
		console.error('Layout load error:', error);
		clearTokens();
		return {
			authUser: undefined
		};
	}
}