export interface QuickLink {
	label: string;
	href: string;
	icon: string;
	accent?: boolean;
}

export interface MenuItem {
	label: string;
	href: string;
	icon?: string;
	description?: string;
	prefix?: string;
}

export interface MenuSection {
	title: string;
	badge?: string;
	subtitle?: string;
	items: MenuItem[];
	action?: {
		label: string;
		href: string;
	};
}

export interface ContactAction {
	label: string;
	href: string;
	icon: string;
}