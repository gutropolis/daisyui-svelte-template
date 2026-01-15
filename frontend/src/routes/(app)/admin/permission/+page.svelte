<script lang="ts">
	import { onMount } from 'svelte';
	 
	import type { PermissionType } from '$lib/modal/Plan';
	import PermissionForm from './PermissionForm.svelte';
	import PermissionList from './PermissionList.svelte';
	import PaginationModal from './PaginationModal.svelte';
	import FilterModal from './FilterModal.svelte';
	import { CREATE_PERMISSION_MUTATION, DELETE_PERMISSION_MUTATION, PERMISSIONS_QUERY, PLAN_FEATURES_QUERY, UPDATE_PERMISSION_MUTATION } from '$lib/gql/plan';
	import alerts from '$lib/stores/alerts';
	import { getContextClient } from '@urql/svelte';
	import { handleGqlErr } from '$lib/utils/gqlfx';

	const client = getContextClient();
	// State
	let permissions: PermissionType[] = [];
	let features: Array<{ id: number; name: string }> = [];
	let loading = false;
	let error = '';
	let success = '';
	let isEditing = false;
	let editingId: number | null = null;
	let paginationModalOpen = false;
	let filterModalOpen = false;

	// Pagination state
	let currentPage = 1;
	let totalPages = 1;
	let total = 0;
	let hasNext = false;
	let hasPrev = false;

	// Filter state
	let searchTerm = '';
	let selectedFeature = '';

	// Form state
	let formData = {
		keyName: '',
		name: '',
		description: '',
		icon: '',
		featureId: ''
	};

	

	// Load permissions and features on mount
	onMount(async () => {
		await loadFeatures();
		await loadPermissions();
	});

	// Load features
	async function loadFeatures() {
		loading = true;
	 		let title = "Features";
			const res = await client.query(PLAN_FEATURES_QUERY, {}).toPromise();
			 
          
			if (res.error) {
				alerts.error(title, res.error.message);
				return;
			}
			let planFeature = res?.data?.planFeatures;
            console.log("Plan ",planFeature);
			 
			if (planFeature.success) {
				features = planFeature.data;
			}
		loading = false;
		 
	}

	// Load permissions
	async function loadPermissions() {
		let title = "Permissions";
		loading = true;
		error = '';
		try {
			const filterInput: any = {};
			if (selectedFeature) {
				filterInput.featureId = parseInt(selectedFeature);
			}
			if (searchTerm) {
				filterInput.search = searchTerm;
			}

			const response = await client.query(PERMISSIONS_QUERY, {
				page: currentPage,
				limit: 10,
				filterInput: Object.keys(filterInput).length > 0 ? filterInput : null
			}).toPromise();
			 
          
			if (response.error) {
				alerts.error(title, response.error.message);
				return;
			}

		 

			let permission =response.data.permissions;

			if (permission.success) {
				permissions = permission.data;
				const pagination = permission.pagination;
				totalPages = pagination.totalPages;
				total = pagination.total;
				hasNext = pagination.hasNext;
				hasPrev = pagination.hasPrev;
			} else {
				error = permission.message;
			}
		} catch (err: any) {
			error = `Failed to load permissions: ${err.message}`;
			console.error(err);
		} finally {
			loading = false;
		}
	}

	// Create permission
	async function handleCreate() {
		if (!formData.keyName || !formData.name || !formData.featureId) {
			error = 'Key name, name, and feature are required';
			return;
		}

		loading = true;
		error = '';
		success = '';
	    const title="Add Permission";
		

        

		try {
		
        // Save the Connector
        const response = await client
            .mutation(CREATE_PERMISSION_MUTATION, {
				input: {
					keyName: formData.keyName,
					name: formData.name,
					featureId: parseInt(formData.featureId),
					description: formData.description || null,
					icon: formData.icon || null
				}
			})
            .toPromise();

        
        if (response.error) {
            const errMsg = handleGqlErr(response.error);
            alerts.error(title, errMsg);
            return "";
        }
        let permisson =response.data?.createPermission;
			if (permisson.success) {
				 
                alerts.success(title,"Permission created successfully!");  
				success = 'Permission created successfully!';
				await loadPermissions();
				resetForm();
				setTimeout(() => (success = ''), 3000);
			} else {
				error = permisson.message;
			}
		} catch (err: any) {
			error = `Failed to create permission: ${err.message}`;
			console.error(err);
			 alerts.error(title, err);
		} finally {
			loading = false;
		}
	}

	// Update permission
	async function handleUpdate() {
		if (!editingId || !formData.name) {
			error = 'Name is required';
			return;
		}

		loading = true;
		error = '';
		success = '';
        const title="Update Permission";
		try {
 
			const response = await client.mutation(UPDATE_PERMISSION_MUTATION, {
				id: editingId,
				input: {
					name: formData.name,
					description: formData.description || null,
					icon: formData.icon || null
				}
			}).toPromise();

			if (response.data.updatePermission.success) {
				success = 'Permission updated successfully!';
				await loadPermissions();
				resetForm();
				setTimeout(() => (success = ''), 3000);
				alerts.success(title,success);  
			} else {
				error = response.data.updatePermission.message;
			}
		} catch (err: any) {
			error = `Failed to update permission: ${err.message}`;
			console.error(err);
			alerts.error(title, err);
			
		} finally {
			loading = false;
		}
	}

	// Delete permission
	async function handleDelete(id: number) {
		loading = true;
		error = '';
		success = '';
         const title="Delete Permission";
		try {
			const response = await client.mutation(DELETE_PERMISSION_MUTATION, {
				id
			});

			if (response.data.deletePermission.success) {
				success = 'Permission deleted successfully!';
				await loadPermissions();
				setTimeout(() => (success = ''), 3000);
				alerts.success(title,success);  
			} else {
				error = response.data.deletePermission.message;
			}
		} catch (err: any) {
			error = `Failed to delete permission: ${err.message}`;
			console.error(err);
			alerts.error(title, err);
		} finally {
			loading = false;
		}
	}

	// Edit permission
	function startEdit(permission: PermissionType) {
		isEditing = true;
		editingId = permission.id;
		formData = {
			keyName: permission.keyName,
			name: permission.name,
			description: permission.description || '',
			icon: permission.icon || '',
			featureId: permission.featureId.toString()
		};
	}

	// Reset form
	function resetForm() {
		isEditing = false;
		editingId = null;
		formData = {
			keyName: '',
			name: '',
			description: '',
			icon: '',
			featureId: ''
		};
		error = '';
	}

	// Handle form submit
	async function handleFormSubmit(isEditMode: boolean) {
		if (isEditMode) {
			await handleUpdate();
		} else {
			await handleCreate();
		}
	}

	// Handle page change
	function handlePageChange(newPage: number) {
		currentPage = newPage;
		loadPermissions();
		paginationModalOpen = false;
	}

	// Handle search
	function handleSearch(term: string) {
		searchTerm = term;
		currentPage = 1;
		loadPermissions();
	}

	// Handle feature filter
	function handleFilterByFeature(featureId: string) {
		selectedFeature = featureId;
		currentPage = 1;
		loadPermissions();
	}

	// Clear filters
	function clearFilters() {
		searchTerm = '';
		selectedFeature = '';
		currentPage = 1;
		loadPermissions();
		filterModalOpen = false;
	}
</script>

<div class="min-h-screen bg-gray-50 p-8">
	<div class="max-w-7xl mx-auto">
		<!-- Header -->
		<div class="mb-8">
			<h1 class="text-4xl font-bold text-gray-900">Permissions Management</h1>
			<p class="text-gray-600 mt-2">Create, edit, and manage permissions for your system</p>
		</div>

		<!-- Alerts -->
		{#if error}
			<div class="mb-6 p-4 bg-red-50 border border-red-200 rounded-lg text-red-800">
				<strong>Error:</strong> {error}
			</div>
		{/if}

		{#if success}
			<div class="mb-6 p-4 bg-green-50 border border-green-200 rounded-lg text-green-800">
				✓ {success}
			</div>
		{/if}

		<div class="grid grid-cols-1 lg:grid-cols-3 gap-8">
			<!-- Form Section -->
			<div class="lg:col-span-1">
				<PermissionForm
					{isEditing}
					{editingId}
					{features}
					{loading}
					{error}
					{formData}
					onSubmit={handleFormSubmit}
					onReset={resetForm}
				/>
			</div>

			<!-- List and Controls Section -->
			<div class="lg:col-span-2 space-y-6">
				<!-- Controls -->
				<div class="bg-white rounded-lg shadow-md p-6">
					<div class="flex gap-3">
						<button
							on:click={() => (filterModalOpen = true)}
							class="flex-1 bg-indigo-600 hover:bg-indigo-700 text-white font-medium py-2 px-4 rounded-md transition"
						>
							🔍 Filter & Search
						</button>
						<button
							on:click={() => (paginationModalOpen = true)}
							class="flex-1 bg-purple-600 hover:bg-purple-700 text-white font-medium py-2 px-4 rounded-md transition"
						>
							📄 Pagination ({currentPage}/{totalPages})
						</button>
						<button
							on:click={loadPermissions}
							disabled={loading}
							class="flex-1 bg-gray-600 hover:bg-gray-700 disabled:bg-gray-400 text-white font-medium py-2 px-4 rounded-md transition"
						>
							🔄 Refresh
						</button>
					</div>
				</div>

				<!-- List Section -->
				<PermissionList
					{permissions}
					{loading}
					onEdit={startEdit}
					onDelete={handleDelete}
					onRefresh={loadPermissions}
				/>
			</div>
		</div>
	</div>
</div>

<!-- Modals -->
<PaginationModal
	isOpen={paginationModalOpen}
	page={currentPage}
	{totalPages}
	{total}
	{hasNext}
	{hasPrev}
	{loading}
	onPageChange={handlePageChange}
	onClose={() => (paginationModalOpen = false)}
/>

<FilterModal
	isOpen={filterModalOpen}
	{features}
	searchTerm={searchTerm}
	selectedFeature={selectedFeature}
	{loading}
	onSearch={handleSearch}
	onFilterByFeature={handleFilterByFeature}
	onClear={clearFilters}
	onClose={() => (filterModalOpen = false)}
/>

<style>
	:global(body) {
		background-color: #f9fafb;
	}
</style>
