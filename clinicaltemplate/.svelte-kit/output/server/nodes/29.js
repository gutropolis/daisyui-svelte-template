import * as server from '../entries/pages/demo/lucia/_page.server.ts.js';

export const index = 29;
let component_cache;
export const component = async () => component_cache ??= (await import('../entries/pages/demo/lucia/_page.svelte.js')).default;
export { server };
export const server_id = "src/routes/demo/lucia/+page.server.ts";
export const imports = ["_app/immutable/nodes/29.Bci3V_vF.js","_app/immutable/chunks/O-IopRwW.js","_app/immutable/chunks/B0DI0EOH.js"];
export const stylesheets = [];
export const fonts = [];
