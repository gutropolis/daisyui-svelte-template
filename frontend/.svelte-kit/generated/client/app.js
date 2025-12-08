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
	() => import('./nodes/17')
];

export const server_loads = [];

export const dictionary = {
		"/": [4],
		"/(public)/(auth)/2-step-verification": [10,[3]],
		"/(app)/admin": [5,[2]],
		"/(app)/dashboard": [6,[2]],
		"/demo": [14],
		"/demo/lucia": [~15],
		"/demo/lucia/login": [~16],
		"/(app)/empty": [7,[2]],
		"/(public)/(auth)/forgot-password": [11,[3]],
		"/(public)/(auth)/login": [12,[3]],
		"/(app)/my-projects": [8,[2]],
		"/(app)/project/new": [9,[2]],
		"/(public)/(auth)/register": [13,[3]],
		"/test-graphql": [17]
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