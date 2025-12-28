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
	() => import('./nodes/31'),
	() => import('./nodes/32'),
	() => import('./nodes/33'),
	() => import('./nodes/34'),
	() => import('./nodes/35'),
	() => import('./nodes/36')
];

export const server_loads = [];

export const dictionary = {
		"/": [5],
		"/(public)/auth/2-step-verification": [29,[4]],
		"/(public)/auth/forgot-password": [30,[4]],
		"/(public)/auth/login": [31,[4]],
		"/(public)/auth/register": [32,[4]],
		"/(app)/dashboard": [6,[2]],
		"/demo": [33],
		"/demo/lucia": [~34],
		"/demo/lucia/login": [~35],
		"/demo/paraglide": [36],
		"/(app)/fieldcomment": [7,[2]],
		"/(app)/my-alerts": [8,[2]],
		"/(app)/myprojects": [9,[2]],
		"/(app)/project": [10,[2,3]],
		"/(app)/project/new": [11,[2,3]],
		"/(app)/project/setup": [12,[2,3]],
		"/(app)/project/[projectId]": [13,[2,3]],
		"/(app)/project/[projectId]/analysis": [14,[2,3]],
		"/(app)/project/[projectId]/dashboard": [15,[2,3]],
		"/(app)/project/[projectId]/data/status": [16,[2,3]],
		"/(app)/project/[projectId]/export": [17,[2,3]],
		"/(app)/project/[projectId]/setup2": [27,[2,3]],
		"/(app)/project/[projectId]/setup": [18,[2,3]],
		"/(app)/project/[projectId]/setup/bookmarks": [19,[2,3]],
		"/(app)/project/[projectId]/setup/define-events": [20,[2,3]],
		"/(app)/project/[projectId]/setup/design-instruments": [21,[2,3]],
		"/(app)/project/[projectId]/setup/optional-modules": [22,[2,3]],
		"/(app)/project/[projectId]/setup/production": [23,[2,3]],
		"/(app)/project/[projectId]/setup/settings": [24,[2,3]],
		"/(app)/project/[projectId]/setup/testing": [25,[2,3]],
		"/(app)/project/[projectId]/setup/user-rights": [26,[2,3]],
		"/(app)/reports": [28,[2]]
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