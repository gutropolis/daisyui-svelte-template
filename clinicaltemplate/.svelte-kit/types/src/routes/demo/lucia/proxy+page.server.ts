// @ts-nocheck
import * as auth from '$lib/server/auth';
import { fail, redirect } from '@sveltejs/kit';
import { getRequestEvent } from '$app/server';
import type { Actions, PageServerLoad } from './$types';

export const load = async () => {
	const user = requireLogin()
	return { user };
};

export const actions = {
	logout: async (event: import('./$types').RequestEvent) => {
		if (!event.locals.session) {
			return fail(401);
		}
		await auth.invalidateSession(event.locals.session.id);
		auth.deleteSessionTokenCookie(event);

		return redirect(302, '/demo/lucia/login');
	},
};

function requireLogin() {
  const { locals } = getRequestEvent();

  if (!locals.user) {
    return redirect(302, "/demo/lucia/login");
  }

  return locals.user;
}
;null as any as PageServerLoad;;null as any as Actions;