/* Copyright (c) 2022. Ankit Patial.
 * Unauthorized copying of this file, via any medium is strictly prohibited. Proprietary and confidential.
 * Author: Ankit Patial
 */

import type { ROLE } from '$lib/enums/role';
import type{  ACCOUNT_STATUS  } from '$lib/enums/user';
import type { Subscription } from '$lib/models/Subscription';
 
export   interface User {
	id?:number; 
	uid?: string; 
	email?: string; 
	firstName?:string;
	lastName?:string; 
	fullName?:string;
	contact_number?:string; 
	company?:string;
	country?:string;
	password?:string;
	password2?:string;
	profileImage?:string; 
	status?:ACCOUNT_STATUS; 
	role?:string;
	avtar?(name: string): string;
	otp?:string;
	mySubscription?:Subscription
	 
	
} 
export interface UserBasic {
	id: string;
	name: string;
	email?: string;
	avtar?: string;
	isVerified?: string;
	status?:ACCOUNT_STATUS;
}

export interface Feature {
	id: number;
	keyName?: string;
	name: string;
	description?: string;
	createdAt?: string;
	updatedAt?: string;
}

export interface PermissionType {
	id: number;
	keyName: string;
	name: string;
	description?: string;
	icon?: string;
	featureId: number;
	feature?: Feature;
	createdAt?: string;
	updatedAt?: string;
}
 