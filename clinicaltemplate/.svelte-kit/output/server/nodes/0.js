

export const index = 0;
let component_cache;
export const component = async () => component_cache ??= (await import('../entries/pages/_layout.svelte.js')).default;
export const imports = ["_app/immutable/nodes/0.CSSI3CGZ.js","_app/immutable/chunks/O-IopRwW.js","_app/immutable/chunks/B0DI0EOH.js"];
export const stylesheets = ["_app/immutable/assets/layout.Ce7zo4Q0.css"];
export const fonts = [];
