/**
 * Resolves a project route by replacing [projectId] placeholder with the actual project ID
 * @param route - The route template containing [projectId]
 * @param projectId - The project ID to insert
 * @returns The resolved route string
 */
export function resolveProjectRoute(route: string, projectId: string): string {
	return route.replace('[projectId]', projectId);
}

/**
 * Alternative implementation that appends projectId to the route
 * Use this if routes are defined without [projectId] placeholder
 */
export function resolveProjectRouteAlt(route: string, projectId: string): string {
	return `${route}/${projectId}`;
}