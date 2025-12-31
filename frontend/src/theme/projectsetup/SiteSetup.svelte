<script lang="ts">
	interface Site {
		id: number;
		name: string;
		code: string;
		address: string;
		contact: string;
		participantCount?: number;
		users?: Array<{
			name: string;
			avatar: string;
		}>;
	}

	let sites: Site[] = [
		{
			id: 1,
			name: 'SITE 21 S2ert',
			code: 'SITE-001',
			address: '123 Medical Center Drive, New York, NY 10001',
			contact: 'dr.smith@hospital.com',
			participantCount: 12,
			users: [
				{ name: 'John Smith', avatar: 'https://api.dicebear.com/7.x/avataaars/svg?seed=John' },
				{ name: 'Sarah Johnson', avatar: 'https://api.dicebear.com/7.x/avataaars/svg?seed=Sarah' },
				{ name: 'Mike Davis', avatar: 'https://api.dicebear.com/7.x/avataaars/svg?seed=Mike' }
			]
		},
		{
			id: 2,
			name: 'Research Center Boston',
			code: 'SITE-002',
			address: '456 Research Blvd, Boston, MA 02115',
			contact: 'dr.johnson@research.com',
			participantCount: 8,
			users: [
				{ name: 'Emily Brown', avatar: 'https://api.dicebear.com/7.x/avataaars/svg?seed=Emily' },
				{ name: 'David Wilson', avatar: 'https://api.dicebear.com/7.x/avataaars/svg?seed=David' },
				{ name: 'Lisa Anderson', avatar: 'https://api.dicebear.com/7.x/avataaars/svg?seed=Lisa' }
			]
		},
		{
			id: 3,
			name: 'Clinical Hub Toronto',
			code: 'SITE-003',
			address: '789 Clinical Avenue, Toronto, ON M5H 2N2',
			contact: 'dr.williams@clinical.com',
			participantCount: 5,
			users: [
				{ name: 'Robert Taylor', avatar: 'https://api.dicebear.com/7.x/avataaars/svg?seed=Robert' },
				{ name: 'Jennifer White', avatar: 'https://api.dicebear.com/7.x/avataaars/svg?seed=Jennifer' },
				{ name: 'Christopher Lee', avatar: 'https://api.dicebear.com/7.x/avataaars/svg?seed=Christopher' }
			]
		}
	];

	let showModal = false;
	let isEditing = false;
	let editingId: number | null = null;
	let successMessage = '';

	let formData = {
		name: '',
		code: '',
		address: '',
		contact: ''
	};

	const openAddModal = () => {
		isEditing = false;
		editingId = null;
		formData = {
			name: '',
			code: '',
			address: '',
			contact: ''
		};
		showModal = true;
	};

	const openEditModal = (site: Site) => {
		isEditing = true;
		editingId = site.id;
		formData = {
			name: site.name,
			code: site.code,
			address: site.address,
			contact: site.contact
		};
		showModal = true;
	};

	const closeModal = () => {
		showModal = false;
		formData = {
			name: '',
			code: '',
			address: '',
			contact: ''
		};
	};

	const saveSite = () => {
		if (!formData.name || !formData.code || !formData.address || !formData.contact) {
			alert('Please fill in all required fields');
			return;
		}

		if (isEditing && editingId !== null) {
			// Update existing site
			const index = sites.findIndex(s => s.id === editingId);
			if (index !== -1) {
				sites[index] = {
					...sites[index],
					name: formData.name,
					code: formData.code,
					address: formData.address,
					contact: formData.contact
				};
			}
			successMessage = 'Site updated successfully!';
		} else {
			// Add new site
			const newSite: Site = {
				id: Math.max(...sites.map(s => s.id), 0) + 1,
				name: formData.name,
				code: formData.code,
				address: formData.address,
				contact: formData.contact,
				participantCount: 0
			};
			sites = [...sites, newSite];
			successMessage = 'Site added successfully!';
		}

		closeModal();
		setTimeout(() => {
			successMessage = '';
		}, 3000);
	};

	const deleteSite = (id: number) => {
		if (confirm('Are you sure you want to delete this site?')) {
			sites = sites.filter(s => s.id !== id);
			successMessage = 'Site deleted successfully!';
			setTimeout(() => {
				successMessage = '';
			}, 3000);
		}
	};

	const getTotalParticipants = () => {
		return sites.reduce((sum, site) => sum + (site.participantCount || 0), 0);
	};
</script>

<!-- Success Message -->
{#if successMessage}
	<div class="bg-green-50 border border-green-200 rounded-lg p-4 flex items-center gap-3 mb-6">
		<i class="fas fa-check-circle text-green-600 text-lg"></i>
		<p class="text-green-700 font-medium">{successMessage}</p>
	</div>
{/if}

<div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
	<!-- Main Content Area -->
	<div class="lg:col-span-2 space-y-6">
		<!-- Sites Summary -->
		<div class="grid grid-cols-3 gap-4">
		<div class="bg-white rounded-lg shadow p-4 border-l-4 border-[#0b3a7a]">
			<p class="text-gray-600 text-sm font-medium">Total Sites</p>
			<p class="text-3xl font-bold text-[#0b3a7a] mt-2">{sites.length}</p>
		</div>
		<div class="bg-white rounded-lg shadow p-4 border-l-4 border-green-500">
			<p class="text-gray-600 text-sm font-medium">Total Participants</p>
			<p class="text-3xl font-bold text-green-600 mt-2">{getTotalParticipants()}</p>
		</div>
		<div class="bg-white rounded-lg shadow p-4 border-l-4 border-blue-500">
			<p class="text-gray-600 text-sm font-medium">Avg per Site</p>
			<p class="text-3xl font-bold text-blue-600 mt-2">
				{sites.length > 0 ? Math.round(getTotalParticipants() / sites.length) : 0}
			</p>
		</div>
	</div>

	<!-- Sites Listing Section -->
	<div class="bg-white rounded-lg shadow p-6">
		<div class="flex items-center justify-between mb-6">
			<h2 class="text-xl font-bold text-gray-800 flex items-center gap-2">
				<i class="fas fa-building text-[#0b3a7a]"></i>
				Project Sites
			</h2>
			<button
				on:click={openAddModal}
				class="px-4 py-2 bg-[#0b3a7a] text-white rounded-lg hover:bg-[#082654] font-medium transition-colors flex items-center gap-2"
			>
				<i class="fas fa-plus"></i>
				ADD SITE
			</button>
		</div>

		{#if sites.length === 0}
			<div class="text-center py-12">
				<i class="fas fa-inbox text-4xl text-gray-300 mb-4 block"></i>
				<p class="text-gray-600 font-medium">No sites created yet</p>
				<p class="text-gray-400 text-sm">Click "ADD SITE" to add your first research site</p>
			</div>
		{:else}
			<div class="space-y-3">
				{#each sites as site (site.id)}
					<div class="flex items-center justify-between p-4 bg-gray-50 rounded-lg border border-gray-200 hover:border-[#0b3a7a]/30 transition-colors">
						<div class="flex-1">
							<div class="flex items-center gap-3">
								<i class="fas fa-map-pin text-[#0b3a7a] text-xl"></i>
								<div>
									<h3 class="font-semibold text-gray-800">{site.name}</h3>
									<p class="text-sm text-gray-600 mt-1">
										<i class="fas fa-barcode text-[#0b3a7a] mr-1"></i>
										{site.code}
									</p>
									<p class="text-xs text-gray-500 mt-1">
										<i class="fas fa-map text-[#0b3a7a] mr-1"></i>
										{site.address}
									</p>
									<p class="text-xs text-gray-500 mt-1">
										<i class="fas fa-envelope text-[#0b3a7a] mr-1"></i>
										{site.contact}
									</p>
									{#if site.participantCount}
										<p class="text-xs text-gray-500 mt-1">
											<i class="fas fa-users text-[#0b3a7a] mr-1"></i>
											{site.participantCount} participants
										</p>
									{/if}
								</div>
							</div>
						</div>
						<div class="flex items-center gap-4">
							<!-- User Avatars with overlap -->
							<div class="flex items-center">
								{#if site.users}
									<div class="flex -space-x-4">
										{#each site.users.slice(0, 4) as user, index (user.name)}
											<div class="relative group">
												<img
													src={user.avatar}
													alt={user.name}
													class="w-12 h-12 rounded-full border-3 border-white hover:shadow-lg transition-all hover:z-20 hover:scale-110 cursor-pointer"
													title={user.name}
												/>
											</div>
										{/each}
										{#if site.users.length > 4}
											<div class="w-12 h-12 rounded-full bg-blue-500 text-white flex items-center justify-center text-sm font-bold border-3 border-white hover:shadow-lg transition-all hover:z-20 hover:scale-110 cursor-pointer flex-shrink-0" title={`+${site.users.length - 4} more members`}>
												+{site.users.length - 4}
											</div>
										{/if}
									</div>
								{/if}
							</div>

							<!-- Action Buttons -->
							<div class="flex gap-2">
								<button
									on:click={() => openEditModal(site)}
									class="p-2 rounded-lg hover:bg-gray-200 text-[#0b3a7a] transition-colors"
									title="Edit Site"
								>
									<i class="fas fa-pen-square text-lg"></i>
								</button>
								<button
									on:click={() => deleteSite(site.id)}
									class="p-2 rounded-lg hover:bg-red-100 text-red-500 transition-colors"
									title="Delete Site"
								>
									<i class="fas fa-trash text-lg"></i>
								</button>
							</div>
						</div>
					</div>
				{/each}
			</div>
		{/if}
	</div>
	</div>

	<!-- Sidebar with Information -->
	<div class="lg:col-span-1">
		<div class="bg-blue-50 rounded-lg p-5 border border-blue-200 sticky top-4 space-y-6">
			<!-- What are Sites -->
			<div>
				<h3 class="text-sm font-bold text-gray-800 mb-2 flex items-center gap-2">
					<i class="fas fa-info-circle text-blue-600"></i>
					What are Sites?
				</h3>
				<p class="text-xs text-gray-700 leading-relaxed">
					Sites are individual research locations or hospitals where your clinical study is being conducted. Each site enrolls and manages participants, collects data, and reports results back to the coordinating center.
				</p>
			</div>

			<!-- Why Sites Matter -->
			<div>
				<h3 class="text-sm font-bold text-gray-800 mb-2 flex items-center gap-2">
					<i class="fas fa-question-circle text-blue-600"></i>
					Why Sites Matter
				</h3>
				<ul class="text-xs text-gray-700 space-y-1.5 leading-relaxed">
					<li class="flex gap-2">
						<span class="text-blue-600 font-semibold">•</span>
						<span><strong>Participant Recruitment:</strong> Sites enroll eligible participants</span>
					</li>
					<li class="flex gap-2">
						<span class="text-blue-600 font-semibold">•</span>
						<span><strong>Data Collection:</strong> Conduct visits per protocol</span>
					</li>
					<li class="flex gap-2">
						<span class="text-blue-600 font-semibold">•</span>
						<span><strong>Geographic Coverage:</strong> Expand study reach</span>
					</li>
					<li class="flex gap-2">
						<span class="text-blue-600 font-semibold">•</span>
						<span><strong>Compliance:</strong> Track regulatory compliance</span>
					</li>
					<li class="flex gap-2">
						<span class="text-blue-600 font-semibold">•</span>
						<span><strong>Quality Control:</strong> Monitor data quality</span>
					</li>
				</ul>
			</div>

			<!-- Site Code Information -->
			<div>
				<h3 class="text-sm font-bold text-gray-800 mb-2 flex items-center gap-2">
					<i class="fas fa-barcode text-blue-600"></i>
					Site Code (Must be Unique)
				</h3>
				<p class="text-xs text-gray-700 leading-relaxed mb-2">
					A unique identifier for each site used in data management and reporting. Each site must have a distinct code.
				</p>
				<div class="bg-white border border-gray-300 rounded p-2.5 text-xs">
					<p class="text-gray-600 mb-1"><strong>Example:</strong></p>
					<p class="font-mono text-gray-700 text-xs">SITE-001</p>
					<p class="text-gray-600 text-xs mt-2 leading-relaxed">
						✓ Use uppercase with hyphens<br/>
						✓ Sequential numbering<br/>
						✓ Must be unique across all sites
					</p>
				</div>
			</div>

			<!-- Site Information Fields -->
			<div>
				<h3 class="text-sm font-bold text-gray-800 mb-2 flex items-center gap-2">
					<i class="fas fa-file-alt text-blue-600"></i>
					Site Information Fields
				</h3>
				<ul class="text-xs text-gray-700 space-y-2">
					<li class="flex gap-2">
						<span class="text-blue-600 font-semibold">→</span>
						<span><strong>Name:</strong> Official site name or facility name</span>
					</li>
					<li class="flex gap-2">
						<span class="text-blue-600 font-semibold">→</span>
						<span><strong>Code:</strong> Unique site identifier (required)</span>
					</li>
					<li class="flex gap-2">
						<span class="text-blue-600 font-semibold">→</span>
						<span><strong>Address:</strong> Complete site location</span>
					</li>
					<li class="flex gap-2">
						<span class="text-blue-600 font-semibold">→</span>
						<span><strong>Primary Contact:</strong> Site coordinator email</span>
					</li>
				</ul>
			</div>

			<!-- Site Staff and Users -->
			<div>
				<h3 class="text-sm font-bold text-gray-800 mb-2 flex items-center gap-2">
					<i class="fas fa-users text-blue-600"></i>
					Site Staff & Users
				</h3>
				<p class="text-xs text-gray-700 leading-relaxed">
					Each site has a team of staff members who conduct study activities. User avatars are displayed with overlapping layout showing up to 4 members. Click "+X" to see additional team members.
				</p>
			</div>

			<!-- Participant Tracking -->
			<div>
				<h3 class="text-sm font-bold text-gray-800 mb-2 flex items-center gap-2">
					<i class="fas fa-chart-bar text-blue-600"></i>
					Participant Tracking
				</h3>
				<p class="text-xs text-gray-700 leading-relaxed mb-2">
					Track participant enrollment across all sites with summary statistics:
				</p>
				<ul class="text-xs text-gray-700 space-y-1">
					<li class="flex gap-2">
						<span class="text-blue-600">•</span>
						<span><strong>Total Sites:</strong> Number of active research sites</span>
					</li>
					<li class="flex gap-2">
						<span class="text-blue-600">•</span>
						<span><strong>Total Participants:</strong> Aggregate enrollment across all sites</span>
					</li>
					<li class="flex gap-2">
						<span class="text-blue-600">•</span>
						<span><strong>Average per Site:</strong> Mean participants per site</span>
					</li>
				</ul>
			</div>

			<!-- Quick Tips -->
			<div class="bg-white rounded p-3 border border-gray-200">
				<h4 class="text-xs font-semibold text-gray-800 mb-2 flex items-center gap-2">
					<i class="fas fa-lightbulb text-yellow-500"></i>
					Quick Tips
				</h4>
				<ul class="text-xs text-gray-700 space-y-1">
					<li class="flex gap-2">
						<span class="text-blue-600">→</span>
						<span>Keep site codes consistent and meaningful</span>
					</li>
					<li class="flex gap-2">
						<span class="text-blue-600">→</span>
						<span>Update contact information promptly</span>
					</li>
					<li class="flex gap-2">
						<span class="text-blue-600">→</span>
						<span>Document all site staff changes</span>
					</li>
					<li class="flex gap-2">
						<span class="text-blue-600">→</span>
						<span>Monitor participant enrollment trends</span>
					</li>
				</ul>
			</div>
		</div>
	</div>
</div>

<!-- Modal Overlay -->
{#if showModal}
	<div class="fixed inset-0 bg-black/50 flex items-center justify-center z-50">
		<div class="bg-white rounded-lg shadow-lg p-8 max-w-md w-full mx-4">
			<h2 class="text-xl font-bold text-gray-800 mb-6">
				{isEditing ? 'Edit Site' : 'Add New Site'}
			</h2>

			<form on:submit|preventDefault={saveSite} class="space-y-4">
				<!-- Name -->
				<div>
					<label class="block text-sm font-medium text-gray-700 mb-2">
						Name
						<span class="text-red-500">*</span>
					</label>
					<input
						type="text"
						bind:value={formData.name}
						class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-[#0b3a7a] focus:border-transparent outline-none"
						placeholder="Enter site name"
					/>
				</div>

				<!-- Code -->
				<div>
					<label class="block text-sm font-medium text-gray-700 mb-2">
						Code
						<span class="text-red-500">*</span>
					</label>
					<input
						type="text"
						bind:value={formData.code}
						class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-[#0b3a7a] focus:border-transparent outline-none"
						placeholder="Enter site code (e.g., SITE-001)"
					/>
				</div>

				<!-- Address -->
				<div>
					<label class="block text-sm font-medium text-gray-700 mb-2">
						Address
						<span class="text-red-500">*</span>
					</label>
					<input
						type="text"
						bind:value={formData.address}
						class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-[#0b3a7a] focus:border-transparent outline-none"
						placeholder="Enter site address"
					/>
				</div>

				<!-- Primary Contact -->
				<div>
					<label class="block text-sm font-medium text-gray-700 mb-2">
						Primary Contact
						<span class="text-red-500">*</span>
					</label>
					<input
						type="email"
						bind:value={formData.contact}
						class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-[#0b3a7a] focus:border-transparent outline-none"
						placeholder="Enter contact email"
					/>
				</div>

				<!-- Buttons -->
				<div class="flex gap-3 justify-end mt-6 pt-4 border-t">
					<button
						type="button"
						on:click={closeModal}
						class="px-6 py-2 border border-gray-300 text-gray-700 rounded-lg hover:bg-gray-50 font-medium transition-colors"
					>
						CANCEL
					</button>
					<button
						type="submit"
						class="px-6 py-2 bg-[#0b3a7a] text-white rounded-lg hover:bg-[#082654] font-medium transition-colors"
					>
						SAVE
					</button>
				</div>
			</form>
		</div>
	</div>
{/if}

<style>
	:global(body.modal-open) {
		overflow: hidden;
	}
</style>

