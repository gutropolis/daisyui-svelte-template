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

		let items = [
			//{ label: 'Dashboard', href: PATH.USER_DASHBOARD || '/', endsWith: 'dashboard', icon: IconDashboard },
			{ label: 'Projects', href: PATH.PROJECTS || '/', endsWith: 'projects', icon: IconProjects },
			{ label: 'Invited Project', href: PATH.PROJECTINVITATION  || '/', endsWith: 'projects', icon: IconUserPlus },
			{ label: 'Help', href:'#', icon: IconHelp }, 
+				{ label: 'Profile', href: PATH.USER_PROFILE || '/', endsWith: 'profile', icon: IconProfile },
+				{ label: 'Sign out', href: PATH.LOGIN , endsWith: '', icon: IconSignOut },
		];

		if(!projId){
			items = [
				//{ label: 'Dashboard', href: PATH.USER_DASHBOARD || '/', endsWith: 'dashboard', icon: IconDashboard },
				{ label: 'Projects', href: PATH.PROJECTS || '/', endsWith: 'projects', icon: IconProjects },
				{ label: 'Invited Project', href: PATH.PROJECTINVITATION  || '/', endsWith: 'projects', icon: IconUserPlus },
			];
			set(items);
			return;
		}

		let  result =0;
        if($authUser.role === ROLE.ADMIN){
			   result = 2
		}else{
			  result = isProjRoleHavePerm(projId , userRole,permission )
		}
		
		if(result === 0 ) {
			items=[];
		}else if(result == 2 ) {
			items=[];
			items.push({ label: 'Projects', href: PATH.PROJECT_VIEW.replace(':id', projId) || '/', endsWith: 'projects', icon: IconDashboard });
			items.push({ label: 'Setup', href: PATH.PROJECT_SETUP.replace(':id', projId).replace(':module', 'setup') || '/', endsWith: 'projects', icon: IconSetup });
 			 
			items.push({ label: 'Role & Permission', href: PATH.PROJECT_SETUP.replace(':id', projId).replace(':module', 'roles') || '/', endsWith: 'projects', icon: IconKey });
			items.push({ label: 'Users', href: PATH.PROJECT_SETUP.replace(':id', projId).replace(':module', 'users'), startsWith: 'users', icon: IconUsers });
			items.push({ label: 'Subjects', href: PATH.PROJECT_VIEW_SUBJECTS.replace(':id', projId) || '/', endsWith: 'projects', icon: IconSubjects });
+			items.push({ label: 'Data View', href: PATH.PROJECT_VIEW_DATAVIEW.replace(':id', projId) || '/', endsWith: 'projects', icon: IconDataView });
+			items.push({ label: 'Import/Export', href: PATH.PROJECT_VIEW_ImpExp.replace(':id', projId) || '/', endsWith: 'projects', icon: IconImportExport });
			items.push({ label: 'Upload', href: PATH.PROJECT_SITE_UPLOAD.replace(':id', projId) || '/', endsWith: 'upload', icon: IconUpload });
			
			items.push({ label: 'Review', href: PATH.PROJECT_REVIEW_IMG.replace(':id', projId) || '/', endsWith: 'projects', icon: IconImportExport });
			items.push({ label: 'Audit Logs', href: PATH.ADMIN_AUDIT_LOGS || '/', endsWith: 'auditlogs', icon: IconAudit }); 
			items.push({ label: 'Help', href:'#', icon: IconHelp });
			set(items);
			return;
		}else if(result == 1 ) {
			items=[];

			items.push({ label: 'Projects', href: PATH.PROJECT_VIEW.replace(':id', projId) || '/', endsWith: 'projects', icon: IconDashboard });
			if(permission['PROJECT_SETUP_DESIGN'] && permission['PROJECT_SETUP_DESIGN']===1){
				items.push({ label: 'Setup', href: PATH.PROJECT_SETUP.replace(':id', projId).replace(':module', 'setup') || '/', endsWith: 'projects', icon: IconSetup });
 			}
			if(permission['USER_RIGHT'] && permission['USER_RIGHT']===1){
				 items.push({ label: 'Users', href: PATH.PROJECT_SETUP.replace(':id', projId).replace(':module', 'users'), startsWith: 'users', icon: IconUsers });
			}
			if(permission['MANAGE_SITE'] && permission['MANAGE_SITE']===1){
				items.push({ label: 'Subjects', href: PATH.PROJECT_VIEW_SUBJECTS.replace(':id', projId) || '/', endsWith: 'projects', icon: IconSubjects });
 			}
			if(permission['IMPORT'] && permission['IMPORT']===1){
				items.push({ label: 'Data View', href: PATH.PROJECT_VIEW_DATAVIEW.replace(':id', projId) || '/', endsWith: 'projects', icon: IconDataView });
 			}
			
			if(permission['Export'] && permission['Export']===1){
				items.push({ label: 'Import/Export', href: PATH.PROJECT_VIEW_ImpExp.replace(':id', projId) || '/', endsWith: 'projects', icon: IconImportExport });
 			}

		    if(permission['REVIEW_IMG'] && permission['REVIEW_IMG']===1){
				items.push({ label: 'Review', href: PATH.PROJECT_REVIEW_IMG.replace(':id', projId) || '/', endsWith: 'projects', icon: IconImportExport });
 			}

		    
			items.push({ label: 'Upload', href: PATH.PROJECT_SITE_UPLOAD.replace(':id', projId) || '/', endsWith: 'upload', icon: IconUpload });
			items.push({ label: 'Audit Logs', href: PATH.ADMIN_AUDIT_LOGS || '/', endsWith: 'auditlogs', icon: IconAudit });
			set(items);
		}

		// You can now use the projId variable in your derived store logic
	},
	[] as Array<MenuItem>
);



