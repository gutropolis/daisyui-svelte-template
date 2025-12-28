
// this file is generated — do not edit it


declare module "svelte/elements" {
	export interface HTMLAttributes<T> {
		'data-sveltekit-keepfocus'?: true | '' | 'off' | undefined | null;
		'data-sveltekit-noscroll'?: true | '' | 'off' | undefined | null;
		'data-sveltekit-preload-code'?:
			| true
			| ''
			| 'eager'
			| 'viewport'
			| 'hover'
			| 'tap'
			| 'off'
			| undefined
			| null;
		'data-sveltekit-preload-data'?: true | '' | 'hover' | 'tap' | 'off' | undefined | null;
		'data-sveltekit-reload'?: true | '' | 'off' | undefined | null;
		'data-sveltekit-replacestate'?: true | '' | 'off' | undefined | null;
	}
}

export {};


declare module "$app/types" {
	export interface AppTypes {
		RouteId(): "/(public)" | "/(app)" | "/" | "/(app)/admin" | "/(app)/admin/feature" | "/(app)/admin/permission" | "/(app)/admin/permission/Component" | "/(app)/admin/plan" | "/(app)/admin/plan/components" | "/(app)/admin/plan/new" | "/(app)/admin/plan/[id]" | "/(app)/admin/plan/[id]/edit" | "/(app)/admin/project" | "/(app)/admin/project/add" | "/(app)/admin/project/edit" | "/(public)/auth" | "/(public)/auth/2-step-verification" | "/(public)/auth/forgot-password" | "/(public)/auth/login" | "/(public)/auth/register" | "/(app)/dashboard2" | "/(app)/dashboard" | "/demo" | "/demo/lucia" | "/demo/lucia/login" | "/demo/paraglide" | "/(app)/fieldcomment" | "/(app)/my-alerts" | "/(app)/myprojects" | "/(app)/project" | "/(app)/project/new" | "/(app)/project/setup" | "/(app)/project/[projectId]" | "/(app)/project/[projectId]/analysis" | "/(app)/project/[projectId]/dashboard" | "/(app)/project/[projectId]/data" | "/(app)/project/[projectId]/data/status" | "/(app)/project/[projectId]/export" | "/(app)/project/[projectId]/setup2" | "/(app)/project/[projectId]/setup" | "/(app)/project/[projectId]/setup/bookmarks" | "/(app)/project/[projectId]/setup/define-events" | "/(app)/project/[projectId]/setup/design-instruments" | "/(app)/project/[projectId]/setup/optional-modules" | "/(app)/project/[projectId]/setup/production" | "/(app)/project/[projectId]/setup/settings" | "/(app)/project/[projectId]/setup/testing" | "/(app)/project/[projectId]/setup/user-rights" | "/(app)/reports";
		RouteParams(): {
			"/(app)/admin/plan/[id]": { id: string };
			"/(app)/admin/plan/[id]/edit": { id: string };
			"/(app)/project/[projectId]": { projectId: string };
			"/(app)/project/[projectId]/analysis": { projectId: string };
			"/(app)/project/[projectId]/dashboard": { projectId: string };
			"/(app)/project/[projectId]/data": { projectId: string };
			"/(app)/project/[projectId]/data/status": { projectId: string };
			"/(app)/project/[projectId]/export": { projectId: string };
			"/(app)/project/[projectId]/setup2": { projectId: string };
			"/(app)/project/[projectId]/setup": { projectId: string };
			"/(app)/project/[projectId]/setup/bookmarks": { projectId: string };
			"/(app)/project/[projectId]/setup/define-events": { projectId: string };
			"/(app)/project/[projectId]/setup/design-instruments": { projectId: string };
			"/(app)/project/[projectId]/setup/optional-modules": { projectId: string };
			"/(app)/project/[projectId]/setup/production": { projectId: string };
			"/(app)/project/[projectId]/setup/settings": { projectId: string };
			"/(app)/project/[projectId]/setup/testing": { projectId: string };
			"/(app)/project/[projectId]/setup/user-rights": { projectId: string }
		};
		LayoutParams(): {
			"/(public)": Record<string, never>;
			"/(app)": { id?: string; projectId?: string };
			"/": { id?: string; projectId?: string };
			"/(app)/admin": { id?: string };
			"/(app)/admin/feature": Record<string, never>;
			"/(app)/admin/permission": Record<string, never>;
			"/(app)/admin/permission/Component": Record<string, never>;
			"/(app)/admin/plan": { id?: string };
			"/(app)/admin/plan/components": Record<string, never>;
			"/(app)/admin/plan/new": Record<string, never>;
			"/(app)/admin/plan/[id]": { id: string };
			"/(app)/admin/plan/[id]/edit": { id: string };
			"/(app)/admin/project": Record<string, never>;
			"/(app)/admin/project/add": Record<string, never>;
			"/(app)/admin/project/edit": Record<string, never>;
			"/(public)/auth": Record<string, never>;
			"/(public)/auth/2-step-verification": Record<string, never>;
			"/(public)/auth/forgot-password": Record<string, never>;
			"/(public)/auth/login": Record<string, never>;
			"/(public)/auth/register": Record<string, never>;
			"/(app)/dashboard2": Record<string, never>;
			"/(app)/dashboard": Record<string, never>;
			"/demo": Record<string, never>;
			"/demo/lucia": Record<string, never>;
			"/demo/lucia/login": Record<string, never>;
			"/demo/paraglide": Record<string, never>;
			"/(app)/fieldcomment": Record<string, never>;
			"/(app)/my-alerts": Record<string, never>;
			"/(app)/myprojects": Record<string, never>;
			"/(app)/project": { projectId?: string };
			"/(app)/project/new": Record<string, never>;
			"/(app)/project/setup": Record<string, never>;
			"/(app)/project/[projectId]": { projectId: string };
			"/(app)/project/[projectId]/analysis": { projectId: string };
			"/(app)/project/[projectId]/dashboard": { projectId: string };
			"/(app)/project/[projectId]/data": { projectId: string };
			"/(app)/project/[projectId]/data/status": { projectId: string };
			"/(app)/project/[projectId]/export": { projectId: string };
			"/(app)/project/[projectId]/setup2": { projectId: string };
			"/(app)/project/[projectId]/setup": { projectId: string };
			"/(app)/project/[projectId]/setup/bookmarks": { projectId: string };
			"/(app)/project/[projectId]/setup/define-events": { projectId: string };
			"/(app)/project/[projectId]/setup/design-instruments": { projectId: string };
			"/(app)/project/[projectId]/setup/optional-modules": { projectId: string };
			"/(app)/project/[projectId]/setup/production": { projectId: string };
			"/(app)/project/[projectId]/setup/settings": { projectId: string };
			"/(app)/project/[projectId]/setup/testing": { projectId: string };
			"/(app)/project/[projectId]/setup/user-rights": { projectId: string };
			"/(app)/reports": Record<string, never>
		};
		Pathname(): "/" | "/admin" | "/admin/" | "/admin/feature" | "/admin/feature/" | "/admin/permission" | "/admin/permission/" | "/admin/permission/Component" | "/admin/permission/Component/" | "/admin/plan" | "/admin/plan/" | "/admin/plan/components" | "/admin/plan/components/" | "/admin/plan/new" | "/admin/plan/new/" | `/admin/plan/${string}` & {} | `/admin/plan/${string}/` & {} | `/admin/plan/${string}/edit` & {} | `/admin/plan/${string}/edit/` & {} | "/admin/project" | "/admin/project/" | "/admin/project/add" | "/admin/project/add/" | "/admin/project/edit" | "/admin/project/edit/" | "/auth" | "/auth/" | "/auth/2-step-verification" | "/auth/2-step-verification/" | "/auth/forgot-password" | "/auth/forgot-password/" | "/auth/login" | "/auth/login/" | "/auth/register" | "/auth/register/" | "/dashboard2" | "/dashboard2/" | "/dashboard" | "/dashboard/" | "/demo" | "/demo/" | "/demo/lucia" | "/demo/lucia/" | "/demo/lucia/login" | "/demo/lucia/login/" | "/demo/paraglide" | "/demo/paraglide/" | "/fieldcomment" | "/fieldcomment/" | "/my-alerts" | "/my-alerts/" | "/myprojects" | "/myprojects/" | "/project" | "/project/" | "/project/new" | "/project/new/" | "/project/setup" | "/project/setup/" | `/project/${string}` & {} | `/project/${string}/` & {} | `/project/${string}/analysis` & {} | `/project/${string}/analysis/` & {} | `/project/${string}/dashboard` & {} | `/project/${string}/dashboard/` & {} | `/project/${string}/data` & {} | `/project/${string}/data/` & {} | `/project/${string}/data/status` & {} | `/project/${string}/data/status/` & {} | `/project/${string}/export` & {} | `/project/${string}/export/` & {} | `/project/${string}/setup2` & {} | `/project/${string}/setup2/` & {} | `/project/${string}/setup` & {} | `/project/${string}/setup/` & {} | `/project/${string}/setup/bookmarks` & {} | `/project/${string}/setup/bookmarks/` & {} | `/project/${string}/setup/define-events` & {} | `/project/${string}/setup/define-events/` & {} | `/project/${string}/setup/design-instruments` & {} | `/project/${string}/setup/design-instruments/` & {} | `/project/${string}/setup/optional-modules` & {} | `/project/${string}/setup/optional-modules/` & {} | `/project/${string}/setup/production` & {} | `/project/${string}/setup/production/` & {} | `/project/${string}/setup/settings` & {} | `/project/${string}/setup/settings/` & {} | `/project/${string}/setup/testing` & {} | `/project/${string}/setup/testing/` & {} | `/project/${string}/setup/user-rights` & {} | `/project/${string}/setup/user-rights/` & {} | "/reports" | "/reports/";
		ResolvedPathname(): `${"" | `/${string}`}${ReturnType<AppTypes['Pathname']>}`;
		Asset(): "/robots.txt" | string & {};
	}
}