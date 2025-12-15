import * as universal_hooks from '../../../src/hooks.ts';

export { matchers } from './matchers.js';

export const nodes = [
	() => import('./nodes/0'),
	() => import('./nodes/1'),
	() => import('./nodes/2'),
	() => import('./nodes/3'),
	() => import('./nodes/4'),
	() => import('./nodes/5'),
	() => import('./nodes/6'),
	() => import('./nodes/7'),
	() => import('./nodes/8'),
	() => import('./nodes/9'),
	() => import('./nodes/10'),
	() => import('./nodes/11'),
	() => import('./nodes/12'),
	() => import('./nodes/13'),
	() => import('./nodes/14'),
	() => import('./nodes/15'),
	() => import('./nodes/16'),
	() => import('./nodes/17'),
	() => import('./nodes/18'),
	() => import('./nodes/19'),
	() => import('./nodes/20'),
	() => import('./nodes/21'),
	() => import('./nodes/22'),
	() => import('./nodes/23'),
	() => import('./nodes/24'),
	() => import('./nodes/25'),
	() => import('./nodes/26')
];

export const server_loads = [];

export const dictionary = {
		"/": [4],
		"/(public)/(auth)/2-step-verification": [19,[3]],
		"/(app)/admin": [5,[2]],
		"/(app)/admin/feature": [6,[2]],
		"/(app)/admin/permission": [7,[2]],
		"/(app)/admin/plan": [8,[2]],
		"/(app)/admin/plan/new": [9,[2]],
		"/(app)/admin/plan/[id]": [10,[2]],
		"/(app)/admin/plan/[id]/edit": [11,[2]],
		"/(app)/admin/project": [12,[2]],
		"/(app)/admin/project/add": [13,[2]],
		"/(app)/admin/project/edit": [14,[2]],
		"/(app)/dashboard": [15,[2]],
		"/demo": [23],
		"/demo/lucia": [~24],
		"/demo/lucia/login": [~25],
		"/(app)/empty": [16,[2]],
		"/(public)/(auth)/forgot-password": [20,[3]],
		"/(public)/(auth)/login": [21,[3]],
		"/(app)/my-projects": [17,[2]],
		"/(app)/project/new": [18,[2]],
		"/(public)/(auth)/register": [22,[3]],
		"/test-graphql": [26]
	};

export const hooks = {
	handleError: (({ error }) => { console.error(error) }),
	
	reroute: universal_hooks.reroute || (() => {}),
	transport: universal_hooks.transport || {}
};

export const decoders = Object.fromEntries(Object.entries(hooks.transport).map(([k, v]) => [k, v.decode]));
export const encoders = Object.fromEntries(Object.entries(hooks.transport).map(([k, v]) => [k, v.encode]));

export const hash = false;

export const decode = (type, value) => decoders[type](value);

export { default as root } from '../root.js';