/* Copyright (c) 2022. Ankit Patial.
 * Unauthorized copying of this file, via any medium is strictly prohibited. Proprietary and confidential.
 * Author: Ankit Patial
 */

import { derived, writable } from 'svelte/store';
import type {User} from '$lib/models/User';
import type Entity from '$lib/models/Entity';
import { PATH } from '$lib/enums/path';
import { ROLE } from '$lib/enums/role';

export const authUserBusy = writable<boolean>(false);

export const authUser = writable<User | undefined>(undefined);

export const authRole = derived(authUser, ($u) => {
    return $u?.role || ROLE.NONE;
});

export const storeProjID = writable<string>("");
export const storeSubjID = writable<string>("");
export const authUserDashboard = derived(authUser, ($user) => {
	switch ($user?.role) {
		case ROLE.ADMIN:
			//return PATH.ADMIN_DASHBOARD;
			return PATH.ADMIN_PROJECTS

		default:
			return PATH.PROJECTS
			//return PATH.USER_DASHBOARD;
	}
});

export const breadCrumbs = writable<Array<Entity>>([
	{
		id: PATH.HOME,
		name: 'Home'
	},
	{
		id: PATH.ADMIN_PROJECTS,
		name: 'Project'
	},
	{
		id: PATH.ADMIN_CONNECTORS,
		name: 'Connectors'
	}

]);

export const drawAppSidebar = writable<boolean>(false);
