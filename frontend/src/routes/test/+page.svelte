<script lang="ts">
	import { onMount } from 'svelte';
	import { GRAPHQL_PATH } from '$lib/enums/path';

	let user: any = null;
	let loading = true;
	let error: string | null = null;
	let debugInfo: string = '';

	const token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6Imd1dHJvcG9saXNAZ21haWwuY29tIiwiZXhwIjoxNzY3MzY4MDEwLCJvcmlnSWF0IjoxNzY3MzY3NzEwfQ.ywshXk3nGKZyxYTw3GObz8yISTzI68kWUxfMxfAKTt4';

	onMount(async () => {
		try {
			debugInfo = `GRAPHQL_PATH: ${GRAPHQL_PATH}\nToken: ${token}\n`;

			const requestOptions = {
				method: 'POST',
				headers: {
					'Content-Type': 'application/json',
					'Authorization': `Bearer ${token}`
				},
				body: JSON.stringify({
					query: `
						query Me {
							me {
								id
								firstName
								lastName
								slug
								email
								company
								contactNumber
								role
								__typename
							}
						}
					`,
					operationName: 'Me',
					variables: {}
				}),
				credentials: 'include'
			};

			debugInfo += `Request headers: ${JSON.stringify(requestOptions.headers)}\n`;
			console.log('Sending request with:', requestOptions);

			const response = await fetch(GRAPHQL_PATH, requestOptions);

			debugInfo += `Response status: ${response.status}\n`;
			debugInfo += `Response headers: ${JSON.stringify(Object.fromEntries(response.headers))}\n`;

			if (!response.ok) {
				throw new Error(`HTTP error! status: ${response.status}`);
			}

			const data = await response.json();
			debugInfo += `Response data: ${JSON.stringify(data)}\n`;
			console.log('GraphQL response:', data);

			if (data.errors) {
				error = data.errors.map((e: any) => e.message).join(', ');
			} else if (data.data?.me === null) {
				error = 'User data is null. Token may be invalid or user does not exist.';
			} else {
				user = data.data?.me;
			}
		} catch (err: any) {
			error = err.message || 'Failed to fetch user data';
			debugInfo += `Error: ${error}\n`;
		} finally {
			loading = false;
		}
	});
</script>

<div class="container mx-auto p-4">
	<h1 class="text-2xl font-bold mb-4">Test Page - User Authentication</h1>

	{#if loading}
		<p>Loading...</p>
	{:else if error}
		<p class="text-red-500">Error: {error}</p>
	{:else if user}
		<div class="bg-green-100 p-4 rounded">
			<h2 class="text-xl font-semibold">User Data:</h2>
			<ul class="mt-2">
				<li><strong>ID:</strong> {user.id}</li>
				<li><strong>First Name:</strong> {user.firstName}</li>
				<li><strong>Last Name:</strong> {user.lastName}</li>
				<li><strong>Slug:</strong> {user.slug}</li>
				<li><strong>Email:</strong> {user.email}</li>
				<li><strong>Company:</strong> {user.company}</li>
				<li><strong>Contact Number:</strong> {user.contactNumber}</li>
				<li><strong>Role:</strong> {user.role}</li>
				<li><strong>__typename:</strong> {user.__typename}</li>
			</ul>
		</div>
	{:else}
		<p class="text-yellow-500">No user data found. Please log in.</p>
	{/if}

	<div class="mt-8 p-4 bg-gray-200 rounded">
		<h3 class="text-lg font-bold mb-2">Debug Info:</h3>
		<pre class="text-xs whitespace-pre-wrap">{debugInfo}</pre>
	</div>

	<div class="mt-4">
		<a href="/auth/login" class="btn btn-primary">Login</a>
		<a href="/" class="btn btn-secondary ml-2">Home</a>
	</div>
</div>