/*
 *  Copyright (c) 2022 - 2022.  Ankit Patial.
 *  Unauthorized copying of this file, via any medium is strictly prohibited. Proprietary and confidential.
 *  Author: Ankit Patial
 */

import { writable } from 'svelte/store';

export interface Data {
	count: number;
	items: Array<any>;
	isLoadMore: boolean;
	hasPrevious: boolean;
	hasNext: boolean;
	previousPageNumber: undefined | number;
	nextPageNumber: undefined | number;
	totalPages: undefined | number;
	totalCount: undefined | number; 
	error: undefined | string;
}

export interface Params {
	[key: string]: any;
}

export default class DataLoader {
	private after: string | undefined;
	private first: number | undefined;
	private before: string | undefined;
	private last: number | undefined;
     
	private page:number|undefined=1;

	private readonly client: any;
	private readonly qry: any;
	private readonly limit: number;
	private readonly dataFieldName: string;
	private readonly data: Data;
	private readonly params: Params;

	public delay: number = 300;
	public where: object;
	 
	public isAsc: boolean;
	public orderField: string;

	public store: any;
	public loading: any;

	constructor(client: any, qry: any, dataFieldName: string, limit: number) {
		this.client = client;
		this.qry = qry;
		this.limit = limit;
		this.first = limit;
		this.dataFieldName = dataFieldName;

		// public fields
		this.where = {};
		this.isAsc = true;
		this.orderField = 'created_at';

		this.params = {};
		this.data = {
			isLoadMore: false,
			count: 0,
			items: [],
			hasPrevious: false,
			hasNext: false,
			previousPageNumber: undefined,
			nextPageNumber: undefined,
			totalPages:0,
			error: undefined
		};

		// store
		this.store = writable(this.data);
		this.loading = writable(false);
	}

	async load(resetPage = true) {
		this.loading.set(true);

		const p = {
			...this.params,
			 
			page:this.page ? this.page:1 ,
			perPage:this.limit,
			where: this.where,
			orderBy: { direction: this.isAsc ? 'ASC' : 'DESC', field: this.orderField }
		};
		console.log("P",p);

		const r = await this.client.query(this.qry, p, { requestPolicy: 'network-only' }).toPromise();
        console.log("R",r)
		// Delay the setting of data so that it prevents too quick updates
		await new Promise(r=>setTimeout(r, this.delay));

		this.loading.set(false);

		if (r.err) {
			this.data.error = r.err.message;
			return;
		}
	 
		const {hasNextPage,hasPreviousPage, nextPageNumber,previousPageNumber,edges,totalCount, totalPages } = (r.data || {})[this.dataFieldName] || {};
        console.log("Edges",edges )
		this.data.count = totalCount || 0;
		this.data.previousPageNumber =  previousPageNumber;
		this.data.nextPageNumber =  nextPageNumber;
		this.data.hasPrevious = hasPreviousPage;
		this.data.hasNext =  hasNextPage;
		this.data.totalPages=totalPages;

		

		if (this.data.isLoadMore) {
			this.data.isLoadMore = false;
			// Directly concatenate `edges` to `this.data.items`
			this.data.items = this.data.items.concat(edges || []);
		} else {
			// Assign `edges` directly if not loading more
			this.data.items = edges || [];
		}

		this.store.set(this.data);
	}

	nextPage = () => {
		//this.after = this.data.nextPageNumber;
		//this.first = this.limit;
		//this.before = undefined;
		//this.last = undefined;
		this.page= this.data.nextPageNumber;
		return this.load(false);
	};

	previousPage = () => {
		//this.after = undefined;
		//this.first = undefined;
		//this.before = this.data.previousPageNumber;
		//this.last = this.limit;
		this.page= this.data.previousPageNumber;
		return this.load(false);
	};

	loadMore = () => {
		this.data.isLoadMore = true; 
		//this.after = this.data.nextPageNumber;
		//this.first = this.limit;
		//this.before = undefined;
		//this.last = undefined; 
		this.page= this.data.nextPageNumber;
		return this.load(false);
	};

	setParam = (name: string, value: any) => {
		this.params[name] = value;
	};
}