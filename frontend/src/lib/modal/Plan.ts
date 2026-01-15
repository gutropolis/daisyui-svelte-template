
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



export interface Plan {
	id: number;
	slug: string;
	name: string;
	price: string;
	durationDays: number;
	maxUsers: number | null;
	maxStudies: number | null;
	maxStorageGb: number | null;
	features: number[];
	createdAt: string;
	updatedAt: string;
}