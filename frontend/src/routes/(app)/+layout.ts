import { redirect } from '@sveltejs/kit';
import type { LayoutLoad } from './$types';

export const load: LayoutLoad = ({ url }) => {
	// This will be handled on the client side by the layout component
	// For server-side, we can't check auth here without session
	// The layout component handles the redirect on client
	return {};
};