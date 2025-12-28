import * as server from '../entries/pages/demo/lucia/login/_page.server.ts.js';

export const index = 30;
let component_cache;
export const component = async () => component_cache ??= (await import('../entries/pages/demo/lucia/login/_page.svelte.js')).default;
export { server };
export const server_id = "src/routes/demo/lucia/login/+page.server.ts";
export const imports = ["_app/immutable/nodes/30.DBu0TOIX.js","_app/immutable/chunks/O-IopRwW.js","_app/immutable/chunks/B0DI0EOH.js"];
export const stylesheets = [];
export const fonts = [];
