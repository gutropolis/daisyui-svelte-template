<script lang="ts">
	import { authUser } from '$lib/stores/app';
	import IconEdit from '$theme/icons/IconEdit.svelte';
	import IconSave from '$theme/icons/IconSave.svelte';
	import { page } from '$app/stores';
	import { getStatusColor } from '$lib/utils/projecthelper';
	import Breadcrumb from '$theme/common/Breadcrumb.svelte';

	
  let { data } = $props();

	// Assuming user data is in data.user or from store
	let user = $derived($authUser || data?.user);

	let isEditing = $state(false);

	function toggleEdit() {
		isEditing = !isEditing;
	}


	 
</script>

<div class="p-6 space-y-6">
	<Breadcrumb />

	<div>
		<h2 class="text-3xl font-bold text-gray-800 mb-2">My Profile</h2>
		<p class="text-gray-600">Welcome back! Here's an overview of your projects.</p>
	</div>

	<!-- Profile Details -->
	<div class="bg-white rounded-lg shadow-md p-6 mb-6">
		<div class="flex items-center space-x-4 mb-6">
			<div class="avatar">
				<div class="w-20 h-20 rounded-full ring ring-primary ring-offset-base-100 ring-offset-2">
					<img src={user?.avatar || 'https://picsum.photos/seed/user/80/80'} alt="Profile" />
				</div>
			</div>
			<div class="flex-1">
				<h3 class="text-2xl font-bold text-gray-900">{user?.fullName || 'User Name'}</h3>
				<p class="text-gray-600">{user?.email || 'user@example.com'}</p>
				<p class="text-sm text-gray-500 mt-1">Member since {user?.createdAt ? new Date(user.createdAt).toLocaleDateString() : 'N/A'}</p>
			</div>
			<div class="flex space-x-2">
				<button class="btn btn-outline btn-sm" onclick={toggleEdit}>
					<IconEdit />
					{isEditing ? 'Cancel' : 'Edit Profile'}
				</button>
			</div>
		</div>

		<div class="grid grid-cols-1 md:grid-cols-2 gap-6">
			<!-- Account Information -->
			<div>
				<h4 class="text-lg font-semibold text-gray-900 mb-4">Account Information</h4>
				<div class="space-y-3">
					<div>
						<label class="block text-sm font-medium text-gray-700">Username</label>
						<p class="text-gray-900 mt-1">{user?.username || 'N/A'}</p>
					</div>
					<div>
						<label class="block text-sm font-medium text-gray-700">Email</label>
						<p class="text-gray-900 mt-1">{user?.email || 'N/A'}</p>
					</div>
					<div>
						<label class="block text-sm font-medium text-gray-700">Role</label>
						<p class="text-gray-900 mt-1">{user?.role || 'User'}</p>
					</div>
				</div>
			</div>

			<!-- Profile Information -->
			<div>
				<h4 class="text-lg font-semibold text-gray-900 mb-4">Profile Information</h4>
				<div class="space-y-3">
					<div>
						<label class="block text-sm font-medium text-gray-700">First Name</label>
						<p class="text-gray-900 mt-1">{user?.firstName || 'N/A'}</p>
					</div>
					<div>
						<label class="block text-sm font-medium text-gray-700">Last Name</label>
						<p class="text-gray-900 mt-1">{user?.lastName || 'N/A'}</p>
					</div>
					<div>
						<label class="block text-sm font-medium text-gray-700">Phone</label>
						<p class="text-gray-900 mt-1">{user?.phone || 'N/A'}</p>
					</div>
				</div>
			</div>
		</div>
	</div>

	<!-- Stats Grid -->
	<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
		<div class="bg-white rounded-lg shadow p-6 border-l-4 border-blue-500">
			<div class="flex items-center justify-between">
				<div>
					<p class="text-gray-600 text-sm">Total Projects</p>
					<p class="text-3xl font-bold text-gray-800">5</p>
				</div>
				<i class="fas fa-folder-open text-blue-500 text-4xl opacity-20"></i>
			</div>
		</div>

		<div class="bg-white rounded-lg shadow p-6 border-l-4 border-green-500">
			<div class="flex items-center justify-between">
				<div>
					<p class="text-gray-600 text-sm">Active</p>
					<p class="text-3xl font-bold text-gray-800">55</p>
				</div>
				<i class="fas fa-check-circle text-green-500 text-4xl opacity-20"></i>
			</div>
		</div>

		<div class="bg-white rounded-lg shadow p-6 border-l-4 border-amber-500">
			<div class="flex items-center justify-between">
				<div>
					<p class="text-gray-600 text-sm">In Staging</p>
					<p class="text-3xl font-bold text-gray-800">6</p>
				</div>
				<i class="fas fa-hourglass-half text-amber-500 text-4xl opacity-20"></i>
			</div>
		</div>

		<div class="bg-white rounded-lg shadow p-6 border-l-4 border-purple-500">
			<div class="flex items-center justify-between">
				<div>
					<p class="text-gray-600 text-sm">Drafts</p>
					<p class="text-3xl font-bold text-gray-800">4</p>
				</div>
				<i class="fas fa-file text-purple-500 text-4xl opacity-20"></i>
			</div>
		</div>
	</div>

	<!-- Projects Table -->
	<div class="bg-white rounded-lg shadow overflow-hidden">
		<div class="p-6 border-b border-gray-200">
			<h3 class="text-xl font-bold text-gray-800">Your Projects</h3>
		</div>
		<div class="overflow-x-auto">
			 
		</div>
	</div>

	<!-- Create New Project Button -->
	<div class="flex justify-end">
		<a href=" " class="px-6 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition-colors font-medium">
			<i class="fas fa-plus mr-2"></i>Create New Project
		</a>
	</div>
</div>

<style>
	:global(.badge) {
		display: inline-block;
		padding: 4px 12px;
		border-radius: 9999px;
		font-size: 12px;
		font-weight: 500;
	}

	:global(.badge-warning) {
		background-color: #fef3c7;
		color: #92400e;
	}

	:global(.badge-info) {
		background-color: #bfdbfe;
		color: #1e40af;
	}

	:global(.badge-success) {
		background-color: #bbf7d0;
		color: #065f46;
	}
</style>
