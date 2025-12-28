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
	() => import('./nodes/36'),
	() => import('./nodes/37'),
	() => import('./nodes/38'),
	() => import('./nodes/39'),
	() => import('./nodes/40'),
	() => import('./nodes/41'),
	() => import('./nodes/42'),
	() => import('./nodes/43'),
	() => import('./nodes/44'),
	() => import('./nodes/45'),
	() => import('./nodes/46'),
	() => import('./nodes/47')
];

export const server_loads = [];

export const dictionary = {
		"/": [5],
		"/(app)/admin": [6,[2]],
		"/(app)/admin/feature": [7,[2]],
		"/(app)/admin/permission": [8,[2]],
		"/(app)/admin/plan": [9,[2]],
		"/(app)/admin/plan/new": [10,[2]],
		"/(app)/admin/plan/[id]": [11,[2]],
		"/(app)/admin/plan/[id]/edit": [12,[2]],
		"/(app)/admin/project": [13,[2]],
		"/(app)/admin/project/add": [14,[2]],
		"/(app)/admin/project/edit": [15,[2]],
		"/(public)/auth/2-step-verification": [40,[4]],
		"/(public)/auth/forgot-password": [41,[4]],
		"/(public)/auth/login": [42,[4]],
		"/(public)/auth/register": [43,[4]],
		"/(app)/dashboard2": [17,[2]],
		"/(app)/dashboard": [16,[2]],
		"/demo": [44],
		"/demo/lucia": [~45],
		"/demo/lucia/login": [~46],
		"/demo/paraglide": [47],
		"/(app)/fieldcomment": [18,[2]],
		"/(app)/my-alerts": [19,[2]],
		"/(app)/myprojects": [20,[2]],
		"/(app)/project": [21,[2,3]],
		"/(app)/project/new": [22,[2,3]],
		"/(app)/project/setup": [23,[2,3]],
		"/(app)/project/[projectId]": [24,[2,3]],
		"/(app)/project/[projectId]/analysis": [25,[2,3]],
		"/(app)/project/[projectId]/dashboard": [26,[2,3]],
		"/(app)/project/[projectId]/data/status": [27,[2,3]],
		"/(app)/project/[projectId]/export": [28,[2,3]],
		"/(app)/project/[projectId]/setup2": [38,[2,3]],
		"/(app)/project/[projectId]/setup": [29,[2,3]],
		"/(app)/project/[projectId]/setup/bookmarks": [30,[2,3]],
		"/(app)/project/[projectId]/setup/define-events": [31,[2,3]],
		"/(app)/project/[projectId]/setup/design-instruments": [32,[2,3]],
		"/(app)/project/[projectId]/setup/optional-modules": [33,[2,3]],
		"/(app)/project/[projectId]/setup/production": [34,[2,3]],
		"/(app)/project/[projectId]/setup/settings": [35,[2,3]],
		"/(app)/project/[projectId]/setup/testing": [36,[2,3]],
		"/(app)/project/[projectId]/setup/user-rights": [37,[2,3]],
		"/(app)/reports": [39,[2]]
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