export interface Pagination {
	after?: string;
	first?: number|undefined;
	before?: undefined;
	last?:   number|undefined;
}

export interface CursorPageInfo {
	startCursor?: undefined,
	endCursor ?: undefined,
	hasNextPage?: boolean,
	hasPreviousPage?:boolean,
}