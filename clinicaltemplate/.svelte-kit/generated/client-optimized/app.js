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
	() => import('./nodes/26'),
	() => import('./nodes/27'),
	() => import('./nodes/28'),
	() => import('./nodes/29'),
	() => import('./nodes/30'),
	() => import('./nodes/31')
];

export const server_loads = [];

export const dictionary = {
		"/": [4],
		"/(app)/dashboard": [5,[2]],
		"/demo": [28],
		"/demo/lucia": [~29],
		"/demo/lucia/login": [~30],
		"/demo/paraglide": [31],
		"/(app)/fieldcomment": [6,[2]],
		"/(app)/my-alerts": [7,[2]],
		"/(app)/myprojects": [8,[2]],
		"/(app)/project": [9,[2,3]],
		"/(app)/project/new": [10,[2,3]],
		"/(app)/project/setup": [11,[2,3]],
		"/(app)/project/[projectId]": [12,[2,3]],
		"/(app)/project/[projectId]/analysis": [13,[2,3]],
		"/(app)/project/[projectId]/dashboard": [14,[2,3]],
		"/(app)/project/[projectId]/data/status": [15,[2,3]],
		"/(app)/project/[projectId]/export": [16,[2,3]],
		"/(app)/project/[projectId]/setup2": [26,[2,3]],
		"/(app)/project/[projectId]/setup": [17,[2,3]],
		"/(app)/project/[projectId]/setup/bookmarks": [18,[2,3]],
		"/(app)/project/[projectId]/setup/define-events": [19,[2,3]],
		"/(app)/project/[projectId]/setup/design-instruments": [20,[2,3]],
		"/(app)/project/[projectId]/setup/optional-modules": [21,[2,3]],
		"/(app)/project/[projectId]/setup/production": [22,[2,3]],
		"/(app)/project/[projectId]/setup/settings": [23,[2,3]],
		"/(app)/project/[projectId]/setup/testing": [24,[2,3]],
		"/(app)/project/[projectId]/setup/user-rights": [25,[2,3]],
		"/(app)/reports": [27,[2]]
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