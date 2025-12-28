<script lang="ts">
	import { page } from '$app/stores';
	import { PROJECT_DETAIL_SETUP_ROUTE } from '$lib/enums/routes';
	import { resolveProjectRoute } from '$lib/utils/routes';
	interface Bookmark {
		id: number;
		name: string;
		url: string;
		description: string;
		icon: string;
		roles: string[];
		target: '_blank' | '_self';
	}

	let bookmarks: Bookmark[] = [
		{
			id: 1,
			name: 'NIH Grant Information',
			url: 'https://grants.nih.gov',
			description: 'Official NIH grants portal and resources',
			icon: 'fa-external-link-alt',
			roles: ['Admin', 'Designer'],
			target: '_blank'
		},
		{
			id: 2,
			name: 'Data Dictionary',
			url: '#/docs/dictionary',
			description: 'Project data dictionary and field definitions',
			icon: 'fa-book',
			roles: ['Admin', 'Designer', 'Data Entry'],
			target: '_self'
		},
		{
			id: 3,
			name: 'Quality Control Dashboard',
			url: '#/dashboard/qc',
			description: 'Data quality and validation metrics',
			icon: 'fa-chart-bar',
			roles: ['Admin', 'Designer'],
			target: '_self'
		}
	];

	let showBookmarkModal = false;
	let newBookmark = {
		name: '',
		url: '',
		description: '',
		icon: 'fa-link',
		roles: [] as string[]
	};

	const availableRoles = ['Admin', 'Designer', 'Data Entry', 'Viewer'];
	const projectId = $derived($page.params.projectId ?? '1');
	const setupOverviewRoute = $derived(resolveProjectRoute(PROJECT_DETAIL_SETUP_ROUTE, projectId));

	const addBookmark = () => {
		const bookmark: Bookmark = {
			id: Math.max(...bookmarks.map(b => b.id), 0) + 1,
			...newBookmark,
			target: '_blank'
		};
		bookmarks = [...bookmarks, bookmark];
		showBookmarkModal = false;
		newBookmark = {
			name: '',
			url: '',
			description: '',
			icon: 'fa-link',
			roles: []
		};
	};

	const deleteBookmark = (id: number) => {
		bookmarks = bookmarks.filter(b => b.id !== id);
	};

	const toggleRole = (role: string) => {
		if (newBookmark.roles.includes(role)) {
			newBookmark.roles = newBookmark.roles.filter(r => r !== role);
		} else {
			newBookmark.roles = [...newBookmark.roles, role];
		}
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

	const openBookmark = (url: string, target: string) => {
		if (target === '_blank') {
			window.open(url, '_blank');
		} else {
			window.location.hash = url;
		}
	};
</script>

<div class="p-6 space-y-6">
	<!-- Header -->
	<div>
		<a href={setupOverviewRoute} class="flex items-center gap-2 text-[#0b3a7a] hover:text-[#082654] text-sm font-medium mb-4">
			<i class="fas fa-arrow-left"></i>Back to Setup
		</a>
		<h1 class="text-3xl font-bold text-gray-800 mb-2">Project Bookmarks</h1>
		<p class="text-gray-600">Create quick links to external resources and internal project pages</p>
	</div>

	<!-- Add Bookmark Button -->
	<button
		on:click={() => (showBookmarkModal = true)}
		class="px-4 py-2 bg-[#0b3a7a] text-white rounded-lg hover:bg-[#082654] font-medium transition-colors flex items-center gap-2"
	>
		<i class="fas fa-plus"></i>
		Add Bookmark
	</button>

	<!-- Bookmarks Grid -->
	{#if bookmarks.length === 0}
		<div class="bg-white rounded-lg shadow p-12 text-center">
			<i class="fas fa-bookmark text-4xl text-gray-300 mb-4 block"></i>
			<p class="text-gray-500">No bookmarks yet. Create one to get started.</p>
		</div>
	{:else}
		<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
			{#each bookmarks as bookmark (bookmark.id)}
			<div class="bg-white rounded-lg shadow hover:shadow-lg transition-shadow p-6 group">
				<div class="flex items-start justify-between mb-3">
					<i class="fas {bookmark.icon} text-2xl text-[#0b3a7a]"></i>
					<button
							on:click={() => deleteBookmark(bookmark.id)}
							class="px-2 py-1 bg-red-50 text-red-600 rounded opacity-0 group-hover:opacity-100 transition-opacity hover:bg-red-100 text-xs"
						>
							<i class="fas fa-trash"></i>
						</button>
					</div>

					<h3 class="font-bold text-gray-800 mb-2">{bookmark.name}</h3>
					<p class="text-sm text-gray-600 mb-4">{bookmark.description}</p>

					<div class="flex flex-wrap gap-1 mb-4">
						{#each bookmark.roles as role}
							<span class="px-2 py-1 rounded text-xs font-medium {getRoleColor(role)}">
								{role}
							</span>
						{/each}
					</div>

					<button
						on:click={() => openBookmark(bookmark.url, bookmark.target)}
						class="w-full px-3 py-2 bg-[#0b3a7a] text-white rounded hover:bg-[#082654] text-sm font-medium transition-colors flex items-center justify-center gap-2"
					>
						<i class="fas fa-arrow-up-right-from-square"></i>
						Open Link
					</button>

					<p class="text-xs text-gray-500 mt-3 truncate">{bookmark.url}</p>
				</div>
			{/each}
		</div>
	{/if}

	<!-- Bookmark Tips -->
	<div class="bg-[#0b3a7a]/5 rounded-lg shadow p-6 border border-[#0b3a7a]/10">
		<h3 class="text-lg font-bold text-gray-800 mb-3 flex items-center gap-2">
			<i class="fas fa-lightbulb text-[#0b3a7a]"></i>
			Bookmark Tips
		</h3>
		<ul class="space-y-2 text-sm text-gray-700">
			<li class="flex items-start gap-2">
				<span class="text-[#0b3a7a] font-bold">•</span>
				<span><strong>External links:</strong> Use full URLs (e.g., https://example.com) and they will open in new tabs</span>
			</li>
			<li class="flex items-start gap-2">
				<span class="text-[#0b3a7a] font-bold">•</span>
				<span><strong>Internal links:</strong> Use hash URLs (e.g., #/docs/dictionary) for internal pages</span>
			</li>
			<li class="flex items-start gap-2">
				<span class="text-[#0b3a7a] font-bold">•</span>
				<span><strong>Role-based access:</strong> Select which user roles can see each bookmark</span>
			</li>
			<li class="flex items-start gap-2">
				<span class="text-[#0b3a7a] font-bold">•</span>
				<span><strong>Documentation:</strong> Link to study protocols, SOPs, and training materials</span>
			</li>
		</ul>
	</div>

	<!-- Suggested Bookmarks -->
	<div class="bg-gray-50 rounded-lg shadow p-6 border border-gray-200">
		<h3 class="text-lg font-bold text-gray-800 mb-4 flex items-center gap-2">
			<i class="fas fa-star text-yellow-500"></i>
			Suggested Bookmarks
		</h3>
		<div class="space-y-3">
			<div class="bg-white rounded p-4 border border-gray-200 hover:border-[#0b3a7a] transition-colors cursor-pointer">
				<h4 class="font-semibold text-gray-800 mb-1">Study Protocol</h4>
				<p class="text-sm text-gray-600">Link to the main research protocol document</p>
			</div>
			<div class="bg-white rounded p-4 border border-gray-200 hover:border-[#0b3a7a] transition-colors cursor-pointer">
				<h4 class="font-semibold text-gray-800 mb-1">Standard Operating Procedures</h4>
				<p class="text-sm text-gray-600">SOPs for data collection and validation</p>
			</div>
			<div class="bg-white rounded p-4 border border-gray-200 hover:border-[#0b3a7a] transition-colors cursor-pointer">
				<h4 class="font-semibold text-gray-800 mb-1">Training Materials</h4>
				<p class="text-sm text-gray-600">User training and onboarding resources</p>
			</div>
			<div class="bg-white rounded p-4 border border-gray-200 hover:border-[#0b3a7a] transition-colors cursor-pointer">
				<h4 class="font-semibold text-gray-800 mb-1">Data Management Plan</h4>
				<p class="text-sm text-gray-600">Data governance and quality standards</p>
			</div>
		</div>
	</div>

	<!-- Add Bookmark Modal -->
	{#if showBookmarkModal}
		<div class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
			<div class="bg-white rounded-lg shadow-xl p-6 max-w-md w-full mx-4 max-h-[90vh] overflow-y-auto">
				<h2 class="text-xl font-bold text-gray-800 mb-4">Add New Bookmark</h2>

			<div class="space-y-4">
				<div>
					<label class="block text-sm font-medium text-gray-700 mb-1">Bookmark Name</label>
					<input
						type="text"
						bind:value={newBookmark.name}
						class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-[#0b3a7a] outline-none"
						placeholder="e.g., Study Protocol"
					/>
				</div>

				<div>
					<label class="block text-sm font-medium text-gray-700 mb-1">URL</label>
					<input
						type="url"
						bind:value={newBookmark.url}
						class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-[#0b3a7a] outline-none"
						placeholder="https://example.com or #/page"
					/>
				</div>

				<div>
					<label class="block text-sm font-medium text-gray-700 mb-1">Description</label>
					<textarea
						bind:value={newBookmark.description}
						class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-[#0b3a7a] outline-none"
						placeholder="Brief description of the bookmark"
						rows="3"
					></textarea>
				</div>

				<div>
					<label class="block text-sm font-medium text-gray-700 mb-2">Visible to Roles</label>
					<div class="space-y-2">
						{#each availableRoles as role}
							<label class="flex items-center gap-2 cursor-pointer">
								<input
									type="checkbox"
									checked={newBookmark.roles.includes(role)}
									on:change={() => toggleRole(role)}
									class="w-4 h-4 text-[#0b3a7a] rounded"
								/>
								<span class="text-sm text-gray-700">{role}</span>
							</label>
						{/each}
					</div>
				</div>
			</div>				<div class="flex gap-2 justify-end mt-6 border-t pt-4">
					<button
						on:click={() => (showBookmarkModal = false)}
						class="px-4 py-2 border border-gray-300 text-gray-700 rounded-lg hover:bg-gray-50 font-medium transition-colors"
					>
						Cancel
					</button>
					<button
						on:click={addBookmark}
						disabled={!newBookmark.name.trim() || !newBookmark.url.trim()}
						class="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 font-medium transition-colors disabled:opacity-50"
					>
						Add Bookmark
					</button>
				</div>
			</div>
		</div>
	{/if}
</div>
