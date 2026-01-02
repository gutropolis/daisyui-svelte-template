/* Copyright (c) 2022. Ankit Patial.
 * Unauthorized copying of this file, via any medium is strictly prohibited. Proprietary and confidential.
 * Author: Ankit Patial
 */

/**
 * regular expression to wrap words stating with ':' []
 * e.g. /some/:id/other => /some/[:id]/other
 */
const wrapRegEx = /(:\w+)/gi;

export function routeMatch(href: string, routeId: string): boolean {
  if (!href || !routeId) return false;
  const route = href.replace(wrapRegEx, "[$1]").replace(":", "");
  return `/${routeId}`.startsWith(route);
}
