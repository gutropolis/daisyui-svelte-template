

export const index = 1;
let component_cache;
export const component = async () => component_cache ??= (await import('../entries/fallbacks/error.svelte.js')).default;
export const imports = ["_app/immutable/nodes/1.CJ5YfhjG.js","_app/immutable/chunks/O-IopRwW.js","_app/immutable/chunks/B0DI0EOH.js"];
export const stylesheets = [];
export const fonts = [];
