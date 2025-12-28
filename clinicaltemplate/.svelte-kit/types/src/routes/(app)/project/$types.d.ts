import type * as Kit from '@sveltejs/kit';

type Expand<T> = T extends infer O ? { [K in keyof O]: O[K] } : never;
// @ts-ignore
type MatcherParam<M> = M extends (param : string) => param is infer U ? U extends string ? U : string : string;
type RouteParams = {  };
type RouteId = '/(app)/project';
type MaybeWithVoid<T> = {} extends T ? T | void : T;
export type RequiredKeys<T> = { [K in keyof T]-?: {} extends { [P in K]: T[K] } ? never : K; }[keyof T];
type OutputDataShape<T> = MaybeWithVoid<Omit<App.PageData, RequiredKeys<T>> & Partial<Pick<App.PageData, keyof T & keyof App.PageData>> & Record<string, any>>
type EnsureDefined<T> = T extends null | undefined ? {} : T;
type OptionalUnion<U extends Record<string, any>, A extends keyof U = U extends U ? keyof U : never> = U extends unknown ? { [P in Exclude<A, keyof U>]?: never } & U : never;
export type Snapshot<T = any> = Kit.Snapshot<T>;
type PageParentData = Omit<Omit<EnsureDefined<import('../../$types.js').LayoutData>, keyof import('../$types.js').LayoutData> & EnsureDefined<import('../$types.js').LayoutData>, keyof LayoutData> & EnsureDefined<LayoutData>;
type LayoutRouteId = RouteId | "/(app)/project" | "/(app)/project/new" | "/(app)/project/setup" | "/(app)/project/[projectId]" | "/(app)/project/[projectId]/analysis" | "/(app)/project/[projectId]/dashboard" | "/(app)/project/[projectId]/data/status" | "/(app)/project/[projectId]/export" | "/(app)/project/[projectId]/setup" | "/(app)/project/[projectId]/setup/bookmarks" | "/(app)/project/[projectId]/setup/define-events" | "/(app)/project/[projectId]/setup/design-instruments" | "/(app)/project/[projectId]/setup/optional-modules" | "/(app)/project/[projectId]/setup/production" | "/(app)/project/[projectId]/setup/settings" | "/(app)/project/[projectId]/setup/testing" | "/(app)/project/[projectId]/setup/user-rights" | "/(app)/project/[projectId]/setup2"
type LayoutParams = RouteParams & { projectId?: string }
type LayoutParentData = Omit<EnsureDefined<import('../../$types.js').LayoutData>, keyof import('../$types.js').LayoutData> & EnsureDefined<import('../$types.js').LayoutData>;

export type PageServerData = null;
export type PageData = Expand<PageParentData>;
export type PageProps = { params: RouteParams; data: PageData }
export type LayoutServerData = null;
export type LayoutData = Expand<LayoutParentData>;
export type LayoutProps = { params: LayoutParams; data: LayoutData; children: import("svelte").Snippet }