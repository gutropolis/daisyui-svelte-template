// if you want to generate a static html file
// for your page.
// Documentation: https://kit.svelte.dev/docs/page-options#prerender
export const prerender = 'auto' 
// if you want to Generate a SPA
// you have to set ssr to false.
// This is not the case (so set as true or comment the line)
// Documentation: https://kit.svelte.dev/docs/page-options#ssr
export const ssr = true;

// How to manage the trailing slashes in the URLs
// the URL for about page witll be /about with 'ignore' (default)
// the URL for about page witll be /about/ with 'always'
// https://kit.svelte.dev/docs/page-options#trailingslash 
export const trailingSlash = 'always'


import { browser } from '$app/environment';
import { goto } from '$app/navigation';
import client from '$lib/gql/client';
import { QryMe } from '$lib/gql/user';
 
 
export async function load({ params }: any) {
	if (!browser) {
		return {
			authUser: undefined
		};
	}
	const res = await client().query(QryMe, {  }).toPromise();
	if(res.error) {
		return {
			authUser: undefined
		};
	}

	// project will be passed on to all pages under it
	return {
	  	authUser:res.data?.me ,
	 
	};
}