/*
 *  Copyright (c) 2022 - 2022.  Ankit Patial.
 *  Unauthorized copying of this file, via any medium is strictly prohibited. Proprietary and confidential.
 *  Author: Ankit Patial
 */

import { derived } from 'svelte/store';
import { authUser, storeProjID } from '$lib/stores/app';
import { PATH } from '$lib/enums/path';

import IconUsers from '$lib/icons/IconUsers.svelte';
import IconDashboard from '$lib/icons/IconDashboard.svelte';
import IconProjects from '$lib/icons/IconProjects.svelte';
import IconAudit from '$lib/icons/IconClock.svelte';
import IconSubjects from '$lib/icons/IconSubjects.svelte';
import IconDataView from '$lib/icons/IconDataView.svelte';
import IconImportExport from '$lib/icons/IconImportExport.svelte';
import IconSetup from '$lib/icons/IconSetup.svelte';
import IconGroup from '$lib/icons/IconGroup.svelte';
import IconQueue from '$lib/icons/IconQueue.svelte';
import IconUserPlus from '$lib/icons/IconUserPlus.svelte';
import IconKey from '$lib/icons/IconKey.svelte';
import IconClinic from '$lib/icons/IconClinic.svelte';
import {projectRoleStore,projPermStore} from "$lib/stores/project.js";
import {isProjRoleHavePerm} from "$lib/utils/project";
import { ROLE } from '$lib/enums/role';
import IconList from '$lib/icons/IconList.svelte';

import IconUpload from "$lib/icons/IconUpload.svelte";
import IconHelp from '$lib/icons/IconHelp.svelte';
import IconProfile from '$lib/icons/IconProfile.svelte';
import IconSignOut from '$lib/icons/IconSignOut.svelte';
import IconSpin from '$lib/icons/IconSpin.svelte';

export interface MenuItem {
	label: string;
	href: string;
	startsWith?: string;
	endsWith?: string;
	icon: any;
}

export const menuItems = derived(
	[authUser, storeProjID,projectRoleStore,projPermStore], // Include $projID as a dependency
	([$authUser, $storeProjID,$projectRoleStore,$projPermStore], set) => {
		const user = $authUser;
		console.log("MENU STORE ",$authUser);
		const projId = $storeProjID; // Access the value from $projID
		const userRole =$projectRoleStore;
		const permission =$projPermStore;
		console.log("Menu Items",permission)
		if (!user) {
			set([]);
			return;
		}

		let subitems =[
			{ label: 'General', href: PATH.ADMIN_SETTINGS_GENERAL  || '/', endsWith: 'emailtemplates', icon: IconList	 },
			{ label: 'Email Templates', href: PATH.ADMIN_EMAIL_TEMPLATES  || '/', endsWith: 'emailtemplates', icon: IconUserPlus },
			{ label: 'Payment',  href: PATH.ADMIN_SETTINGS_PAYMENT  || '/', endsWith: 'users', icon: IconHelp },
            { label: 'System',  href: PATH.ADMIN_SETTINGS_SYSTEM  || '/', endsWith: 'users', icon: IconHelp },
            { label: 'Add ons',  href: PATH.ADMIN_SETTINGS_ADDONS  || '/', endsWith: 'users', icon: IconHelp },
			{ label: 'Package',  href: PATH.ADMIN_SETTINGS_PACKAGE  || '/', endsWith: 'users', icon: IconHelp },
           
        ]
		let subitems2 =[
			{ label: 'license Feature ', href: PATH.ADMIN_LICENSE_FEATURE  || '/', endsWith: 'emailtemplates', icon: IconList	 },
			{ label: 'Product  ', href: PATH.ADMIN_LICENSE_PRODUCT  || '/', endsWith: 'emailtemplates', icon: IconList	 },
			 
        ]
		let items = [
				//{ label: 'Dashboard', href: PATH.USER_DASHBOARD || '/', endsWith: 'dashboard', icon: IconDashboard },
				{ label: 'Projects', href: PATH.ADMIN_PROJECTS || '/', endsWith: 'projects', icon: IconProjects },
				{ label: 'Users', href: PATH.ADMIN_USERS  || '/', endsWith: 'users', icon: IconUserPlus },
 				{ label: 'Settings' , icon: IconSetup  ,sub: subitems }, 
				{ label: 'license' , icon: IconSetup  ,sub: subitems2 },
				 { label: 'Audit Logs', href: PATH.ADMIN_AUDIT_LOGS || '/', endsWith: 'auditlogs', icon: IconAudit },
			
			];
			set(items);
			return;
		 

		// let  result =0;
        // if($authUser.role === ROLE.ADMIN){
		// 	   result = 2
		// }else{
		// 	  result = isProjRoleHavePerm(projId , userRole,permission )
		// }
		 

		// You can now use the projId variable in your derived store logic
	},
	[] as Array<MenuItem>
);



