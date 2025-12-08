<script lang="ts">
	import { graphqlClient } from '$lib/graphql/client';
	import { gql } from 'graphql-request';

	let testResult = $state<any>(null);
	let loading = $state(false);
	let error = $state<string | null>(null);
	let rawResponse = $state<string>('');

	async function testConnection() {
		loading = true;
		error = null;
		testResult = null;
		rawResponse = '';

		try {
			console.log('🧪 Testing GraphQL connection...');
			const query = gql`
				query {
					hello
				}
			`;

			const response = await graphqlClient.request(query);
			console.log('✅ GraphQL response:', response);
			testResult = response;
			rawResponse = JSON.stringify(response, null, 2);
		} catch (err) {
			console.error('❌ GraphQL test error:', err);
			error = err instanceof Error ? err.message : String(err);
			rawResponse = JSON.stringify(err, null, 2);
		} finally {
			loading = false;
		}
	}

	async function testLogin() {
		loading = true;
		error = null;
		testResult = null;
		rawResponse = '';

		try {
			console.log('🧪 Testing login mutation...');
			const mutation = gql`
				mutation Login($email: String!, $password: String!) {
					login(email: $email, password: $password) {
						success
						message
						token {
							accessToken
							refreshToken
							tokenType
						}
					}
				}
			`;

			const response = await graphqlClient.request(mutation, {
				email: 'user@example.com',
				password: '123456'
			});
			console.log('✅ Login response:', response);
			testResult = response;
			rawResponse = JSON.stringify(response, null, 2);
		} catch (err) {
			console.error('❌ Login test error:', err);
			error = err instanceof Error ? err.message : String(err);
			rawResponse = JSON.stringify(err, null, 2);
		} finally {
			loading = false;
		}
	}
</script>

<div class="container mx-auto py-8 px-4">
	<h1 class="text-3xl font-bold mb-8">🔍 GraphQL Network Debug Test</h1>

	<!-- Instructions -->
	<div class="alert alert-info mb-6">
		<div>
			<h3 class="font-bold">How to use this page:</h3>
			<ol class="list-decimal list-inside mt-2">
				<li>Open Browser DevTools: Press <kbd>F12</kbd></li>
				<li>Go to <strong>Network</strong> tab</li>
				<li>Click the buttons below</li>
				<li>In Network tab, look for requests to <code>localhost:8000/graphql</code></li>
				<li>Click on the request and check <strong>Response</strong> tab</li>
				<li>Also check <strong>Console</strong> tab for detailed logs</li>
			</ol>
		</div>
	</div>

	<!-- Status Info -->
	<div class="card bg-white shadow-lg mb-6">
		<div class="card-body">
			<h2 class="card-title">Connection Info</h2>
			<div class="space-y-2">
				<p><strong>API URL:</strong> <code class="bg-gray-200 px-2 py-1">{import.meta.env.VITE_GRAPHQL_API_URL || 'http://localhost:8000/graphql'}</code></p>
				<p><strong>Browser:</strong> <code class="bg-gray-200 px-2 py-1">{typeof window !== 'undefined' ? 'Connected' : 'SSR Mode'}</code></p>
				<p><strong>Status:</strong> Ready to test</p>
			</div>
		</div>
	</div>

	<!-- Test Buttons -->
	<div class="flex flex-wrap gap-4 mb-6">
		<button onclick={testConnection} disabled={loading} class="btn btn-primary">
			{#if loading}
				<span class="loading loading-spinner loading-sm"></span>
			{/if}
			Test Connection (Simple Query)
		</button>

		<button onclick={testLogin} disabled={loading} class="btn btn-secondary">
			{#if loading}
				<span class="loading loading-spinner loading-sm"></span>
			{/if}
			Test Login (user@example.com / 123456)
		</button>

		<a href="/auth/login" class="btn btn-ghost">Back to Login</a>
		<a href="/test-graphql" class="btn btn-outline">Clear Results</a>
	</div>

	<!-- Error Display -->
	{#if error}
		<div class="alert alert-error mb-6">
			<div>
				<h3 class="font-bold">❌ Error</h3>
				<p class="text-sm">{error}</p>
			</div>
		</div>
	{/if}

	<!-- Result Display -->
	{#if rawResponse}
		<div class="card bg-white shadow-lg">
			<div class="card-body">
				<h2 class="card-title">Response</h2>
				<div class="divider">Raw JSON</div>
				<pre class="bg-gray-100 p-4 rounded overflow-auto text-sm max-h-96"><code>{rawResponse}</code></pre>
				
				{#if testResult}
					<div class="divider">Parsed Result</div>
					<pre class="bg-green-50 p-4 rounded overflow-auto text-sm"><code>{JSON.stringify(testResult, null, 2)}</code></pre>
				{/if}
			</div>
		</div>
	{/if}

	<!-- Debug Instructions -->
	<div class="card bg-blue-50 shadow-lg mt-8">
		<div class="card-body">
			<h2 class="card-title">📊 What to Look For in Network Tab</h2>
			<div class="space-y-3">
				<div>
					<h3 class="font-bold">1. Find the GraphQL Request</h3>
					<p class="text-sm">Look for a POST request to <code class="bg-blue-100 px-2 py-1">http://localhost:8000/graphql</code></p>
				</div>
				<div>
					<h3 class="font-bold">2. Check Request Details</h3>
					<p class="text-sm">Click the request → <strong>Headers</strong> tab → Should see GraphQL query in Request body</p>
				</div>
				<div>
					<h3 class="font-bold">3. Check Response</h3>
					<p class="text-sm">Click the request → <strong>Response</strong> tab → Should see JSON with <code class="bg-blue-100 px-2 py-1">"data"</code> or <code class="bg-blue-100 px-2 py-1">"errors"</code></p>
				</div>
				<div>
					<h3 class="font-bold">4. Success Response Example</h3>
					<pre class="bg-gray-100 p-2 rounded text-xs overflow-auto"><code>{`{
  "data": {
    "hello": "Welcome to DaisyUI Healthcare GraphQL API!"
  }
}`}</code></pre>
				</div>
				<div>
					<h3 class="font-bold">5. Error Response Example</h3>
					<pre class="bg-gray-100 p-2 rounded text-xs overflow-auto"><code>{`{
  "errors": [
    {
      "message": "Connection refused",
      "extensions": { ... }
    }
  ]
}`}</code></pre>
				</div>
			</div>
		</div>
	</div>

	<!-- Console Instructions -->
	<div class="card bg-purple-50 shadow-lg mt-6">
		<div class="card-body">
			<h2 class="card-title">🖥️ Console Tab Guide</h2>
			<div class="space-y-2">
				<p class="text-sm"><strong>When you click a test button, you'll see in Console:</strong></p>
				<pre class="bg-gray-100 p-2 rounded text-xs overflow-auto"><code>{`🔗 GraphQL Client initialized with URL: http://localhost:8000/graphql
📤 GraphQL Request: { operation: 'Login', variables: {...}, ... }
✅ GraphQL Response: { data: {...}, ... }
📝 Form submitted with: { email: 'user@example.com' }
📤 Login result: { success: true/false, message: '...', ... }`}</code></pre>
				<p class="text-sm mt-2"><strong>Common errors in Console:</strong></p>
				<ul class="list-disc list-inside text-sm">
					<li>❌ GraphQL Error: "Cannot POST /graphql" → Backend not running</li>
					<li>❌ GraphQL Error: "Failed to fetch" → Network/CORS issue</li>
					<li>❌ GraphQL Error: "Invalid email or password" → User doesn't exist</li>
				</ul>
			</div>
		</div>
	</div>

	<!-- Troubleshooting -->
	<div class="card bg-yellow-50 shadow-lg mt-6">
		<div class="card-body">
			<h2 class="card-title">⚠️ Troubleshooting</h2>
			<div class="space-y-2">
				<p><strong>If no network request appears:</strong></p>
				<ul class="list-disc list-inside text-sm">
					<li>Check Console for JavaScript errors</li>
					<li>Make sure form validation passed (not empty fields)</li>
					<li>Ensure .env.local is set correctly</li>
				</ul>
				<p class="mt-2"><strong>If request shows 404 or 500 error:</strong></p>
				<ul class="list-disc list-inside text-sm">
					<li>Backend is not running on port 8000</li>
					<li>GraphQL route not configured in FastAPI</li>
					<li>Check backend terminal for Python errors</li>
				</ul>
				<p class="mt-2"><strong>If request shows CORS error:</strong></p>
				<ul class="list-disc list-inside text-sm">
					<li>Backend CORS configuration is wrong</li>
					<li>Frontend URL not allowed in backend CORS settings</li>
				</ul>
			</div>
		</div>
	</div>
</div>

<style>
	code {
		font-family: 'Courier New', monospace;
	}
	
	kbd {
		background: #f3f4f6;
		border: 1px solid #d1d5db;
		border-radius: 0.25rem;
		padding: 0.25rem 0.5rem;
		font-size: 0.875rem;
	}
</style>
