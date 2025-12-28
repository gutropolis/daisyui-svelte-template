<script lang="ts">
	import { page } from '$app/stores';
	import { PROJECT_DETAIL_SETUP_ROUTE } from '$lib/enums/routes';
	import { resolveProjectRoute } from '$lib/utils/routes';

	interface User {
		id: number;
		name: string;
		email: string;
		role: 'Admin' | 'Designer' | 'Data Entry' | 'Viewer';
		dag?: string;
	}

	interface DAG {
		id: number;
		name: string;
		description: string;
		members: number;
	}

	let users: User[] = [
		{ id: 1, name: 'John Admin', email: 'john@example.com', role: 'Admin' },
		{ id: 2, name: 'Jane Designer', email: 'jane@example.com', role: 'Designer' },
		{ id: 3, name: 'Bob Entry', email: 'bob@example.com', role: 'Data Entry', dag: 'Site 1' }
	];

	let dags: DAG[] = [
		{ id: 1, name: 'Site 1', description: 'Primary research site', members: 3 },
		{ id: 2, name: 'Site 2', description: 'Secondary research site', members: 2 }
	];

	let showNewUserModal = false;
	let newUser = { name: '', email: '', role: 'Data Entry' as const };

	const addNewUser = () => {
		const user: User = {
			id: Math.max(...users.map(u => u.id), 0) + 1,
			...newUser
		};
		users = [...users, user];
		showNewUserModal = false;
		newUser = { name: '', email: '', role: 'Data Entry' };
	};

	const deleteUser = (id: number) => {
		users = users.filter(u => u.id !== id);
	};

	const getRoleColor = (role: string) => {
		switch (role) {
			case 'Admin':
				return 'bg-red-100 text-red-800';
			case 'Designer':
				return 'bg-blue-100 text-blue-800';
			case 'Data Entry':
				return 'bg-green-100 text-green-800';
			case 'Viewer':
				return 'bg-gray-100 text-gray-800';
			default:
				return 'bg-gray-100 text-gray-800';
		}
	};

	const projectId = $derived($page.params.projectId ?? '1');
	const setupOverviewRoute = $derived(resolveProjectRoute(PROJECT_DETAIL_SETUP_ROUTE, projectId));
</script>

<div class="p-6 space-y-6">
	<!-- Header -->
	<div>
		<a href={setupOverviewRoute} class="flex items-center gap-2 text-[#0b3a7a] hover:text-[#082654] text-sm font-medium mb-4">
			<i class="fas fa-arrow-left"></i>Back to Setup
		</a>
		<h1 class="text-3xl font-bold text-gray-800 mb-2">User Rights and Permissions</h1>
		<p class="text-gray-600">Manage team access, roles, and Data Access Groups (DAGs)</p>
	</div>

	<!-- Add User Button -->
	<button
		on:click={() => (showNewUserModal = true)}
		class="px-4 py-2 bg-[#0b3a7a] text-white rounded-lg hover:bg-[#082654] font-medium transition-colors flex items-center gap-2"
	>
		<i class="fas fa-user-plus"></i>
		Add User
	</button>

	<!-- Users Table -->
	<div class="bg-white rounded-lg shadow overflow-hidden">
		<div class="p-6 border-b border-gray-200">
			<h2 class="text-xl font-bold text-gray-800">Project Users ({users.length})</h2>
		</div>

		<div class="overflow-x-auto">
			<table class="w-full text-sm">
				<thead class="bg-gray-50 border-b border-gray-200">
					<tr>
						<th class="px-6 py-3 text-left font-semibold text-gray-700">Name</th>
						<th class="px-6 py-3 text-left font-semibold text-gray-700">Email</th>
						<th class="px-6 py-3 text-left font-semibold text-gray-700">Role</th>
						<th class="px-6 py-3 text-left font-semibold text-gray-700">DAG</th>
						<th class="px-6 py-3 text-left font-semibold text-gray-700">Actions</th>
					</tr>
				</thead>
				<tbody class="divide-y divide-gray-200">
					{#each users as user (user.id)}
						<tr class="hover:bg-gray-50 transition-colors">
							<td class="px-6 py-3 font-medium text-gray-800">{user.name}</td>
							<td class="px-6 py-3 text-gray-600">{user.email}</td>
							<td class="px-6 py-3">
								<span class="px-3 py-1 rounded-full text-xs font-medium {getRoleColor(user.role)}">
									{user.role}
								</span>
							</td>
							<td class="px-6 py-3 text-gray-600">
								{user.dag ? user.dag : '—'}
							</td>
							<td class="px-6 py-3">
							<button class="px-3 py-1 bg-[#0b3a7a]/5 text-[#0b3a7a] rounded hover:bg-[#0b3a7a]/10 text-xs font-medium transition-colors mr-2">
								<i class="fas fa-pen-square"></i> Edit
							</button>
								<button
									on:click={() => deleteUser(user.id)}
									class="px-3 py-1 bg-red-50 text-red-600 rounded hover:bg-red-100 text-xs font-medium transition-colors"
								>
									<i class="fas fa-trash"></i> Remove
								</button>
							</td>
						</tr>
					{/each}
				</tbody>
			</table>
		</div>
	</div>

	<!-- Role Reference -->
	<div class="bg-[#0b3a7a]/5 rounded-lg shadow p-6 border border-[#0b3a7a]/10">
		<h3 class="text-lg font-bold text-gray-800 mb-4 flex items-center gap-2">
			<i class="fas fa-info-circle text-[#0b3a7a]"></i>
			Role Permissions
		</h3>
		<div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-sm">
			<div>
				<p class="font-semibold text-red-800 mb-1">Admin</p>
				<p class="text-gray-700">Full access including design, data entry, and user management</p>
			</div>
			<div>
				<p class="font-semibold text-blue-800 mb-1">Designer</p>
				<p class="text-gray-700">Can design forms and events, but not enter data</p>
			</div>
			<div>
				<p class="font-semibold text-green-800 mb-1">Data Entry</p>
				<p class="text-gray-700">Can only enter and edit assigned records</p>
			</div>
			<div>
				<p class="font-semibold text-gray-800 mb-1">Viewer</p>
				<p class="text-gray-700">Read-only access to project data</p>
			</div>
		</div>
	</div>

	<!-- Data Access Groups -->
	<div class="bg-white rounded-lg shadow overflow-hidden">
		<div class="p-6 border-b border-gray-200">
			<h2 class="text-xl font-bold text-gray-800 flex items-center gap-2">
				<i class="fas fa-sitemap text-purple-600"></i>
				Data Access Groups (DAGs)
			</h2>
			<p class="text-sm text-gray-600 mt-1">Organize users by research sites or departments</p>
		</div>

		<div class="grid grid-cols-1 md:grid-cols-2 gap-4 p-6">
			{#each dags as dag (dag.id)}
				<div class="border border-gray-200 rounded-lg p-4 hover:shadow-md transition-shadow">
					<div class="flex items-start justify-between mb-2">
						<h3 class="font-bold text-gray-800">{dag.name}</h3>
						<button class="px-2 py-1 bg-red-50 text-red-600 rounded hover:bg-red-100 text-xs">
							<i class="fas fa-trash"></i>
						</button>
					</div>
					<p class="text-sm text-gray-600">{dag.description}</p>
					<p class="text-xs text-gray-500 mt-2">
						<i class="fas fa-users mr-1"></i>
						{dag.members} members
					</p>
				</div>
			{/each}
		</div>

		<div class="p-6 border-t border-gray-200">
			<button class="px-4 py-2 bg-green-600 text-white rounded-lg hover:bg-green-700 font-medium transition-colors flex items-center gap-2">
				<i class="fas fa-plus"></i>
				Create New DAG
			</button>
		</div>
	</div>

	<!-- New User Modal -->
	{#if showNewUserModal}
		<div class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
			<div class="bg-white rounded-lg shadow-xl p-6 max-w-md w-full mx-4">
				<h2 class="text-xl font-bold text-gray-800 mb-4">Add New User</h2>

				<div class="space-y-4">
					<div>
						<label class="block text-sm font-medium text-gray-700 mb-1">Name</label>
						<input
							type="text"
							bind:value={newUser.name}
							class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-[#0b3a7a] outline-none"
							placeholder="Full name"
						/>
					</div>

					<div>
						<label class="block text-sm font-medium text-gray-700 mb-1">Email</label>
						<input
							type="email"
							bind:value={newUser.email}
							class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-[#0b3a7a] outline-none"
							placeholder="user@example.com"
						/>
					</div>

					<div>
						<label class="block text-sm font-medium text-gray-700 mb-1">Role</label>
						<select
							bind:value={newUser.role}
							class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-[#0b3a7a] outline-none"
						>
							<option value="Data Entry">Data Entry</option>
							<option value="Designer">Designer</option>
							<option value="Admin">Admin</option>
							<option value="Viewer">Viewer</option>
						</select>
					</div>
				</div>

				<div class="flex gap-2 justify-end mt-6 border-t pt-4">
					<button
						on:click={() => (showNewUserModal = false)}
						class="px-4 py-2 border border-gray-300 text-gray-700 rounded-lg hover:bg-gray-50 font-medium transition-colors"
					>
						Cancel
					</button>
					<button
						on:click={addNewUser}
						class="px-4 py-2 bg-[#0b3a7a] text-white rounded-lg hover:bg-[#082654] font-medium transition-colors"
					>
						Add User
					</button>
				</div>
			</div>
		</div>
	{/if}
</div>
