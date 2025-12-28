

export const index = 5;
let component_cache;
export const component = async () => component_cache ??= (await import('../entries/pages/(app)/dashboard/_page.svelte.js')).default;
export const imports = ["_app/immutable/nodes/5.D_GJnVwM.js","_app/immutable/chunks/O-IopRwW.js","_app/immutable/chunks/B0DI0EOH.js","_app/immutable/chunks/pgnebUR0.js"];
export const stylesheets = ["_app/immutable/assets/5.C_TwB3fj.css"];
export const fonts = [];
