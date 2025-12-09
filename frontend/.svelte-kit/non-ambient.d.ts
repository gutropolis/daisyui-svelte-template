
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
		RouteId(): "/(public)/(auth)" | "/(public)" | "/(app)" | "/" | "/(public)/(auth)/2-step-verification" | "/(app)/admin" | "/(app)/admin/permission" | "/(app)/admin/permission/Component" | "/(app)/admin/plan" | "/(app)/admin/plan/feature" | "/(app)/dashboard" | "/demo" | "/demo/lucia" | "/demo/lucia/login" | "/(app)/empty" | "/(public)/(auth)/forgot-password" | "/(public)/(auth)/login" | "/(app)/my-projects" | "/(app)/project" | "/(app)/project/new" | "/(public)/(auth)/register" | "/test-graphql";
		RouteParams(): {
			
		};
		LayoutParams(): {
			"/(public)/(auth)": Record<string, never>;
			"/(public)": Record<string, never>;
			"/(app)": Record<string, never>;
			"/": Record<string, never>;
			"/(public)/(auth)/2-step-verification": Record<string, never>;
			"/(app)/admin": Record<string, never>;
			"/(app)/admin/permission": Record<string, never>;
			"/(app)/admin/permission/Component": Record<string, never>;
			"/(app)/admin/plan": Record<string, never>;
			"/(app)/admin/plan/feature": Record<string, never>;
			"/(app)/dashboard": Record<string, never>;
			"/demo": Record<string, never>;
			"/demo/lucia": Record<string, never>;
			"/demo/lucia/login": Record<string, never>;
			"/(app)/empty": Record<string, never>;
			"/(public)/(auth)/forgot-password": Record<string, never>;
			"/(public)/(auth)/login": Record<string, never>;
			"/(app)/my-projects": Record<string, never>;
			"/(app)/project": Record<string, never>;
			"/(app)/project/new": Record<string, never>;
			"/(public)/(auth)/register": Record<string, never>;
			"/test-graphql": Record<string, never>
		};
		Pathname(): "/" | "/2-step-verification" | "/2-step-verification/" | "/admin" | "/admin/" | "/admin/permission" | "/admin/permission/" | "/admin/permission/Component" | "/admin/permission/Component/" | "/admin/plan" | "/admin/plan/" | "/admin/plan/feature" | "/admin/plan/feature/" | "/dashboard" | "/dashboard/" | "/demo" | "/demo/" | "/demo/lucia" | "/demo/lucia/" | "/demo/lucia/login" | "/demo/lucia/login/" | "/empty" | "/empty/" | "/forgot-password" | "/forgot-password/" | "/login" | "/login/" | "/my-projects" | "/my-projects/" | "/project" | "/project/" | "/project/new" | "/project/new/" | "/register" | "/register/" | "/test-graphql" | "/test-graphql/";
		ResolvedPathname(): `${"" | `/${string}`}${ReturnType<AppTypes['Pathname']>}`;
		Asset(): "/robots.txt" | string & {};
	}
}