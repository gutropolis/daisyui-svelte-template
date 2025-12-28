<script lang="ts">
	import { authStore } from '$lib/stores/auth';
	import { goto } from '$app/navigation';

	async function handleLogout() {
		// Clear tokens and auth state
		const { clearTokens } = await import('$lib/auth');
		clearTokens();
		 authStore.logout();
		await goto('/login');
	}
</script>

<div class="space-y-6">
	<!-- Header -->
	<div class="flex justify-between items-center">
		<div>
			<h1 class="text-3xl font-bold text-gray-900">Dashboard</h1>
			<p class="text-gray-600 mt-1">Welcome back to your account</p>
		</div>
		<button onclick={handleLogout} class="btn btn-ghost">Logout</button>
	</div>

	<!-- User Info Card -->
	{#if $authStore.user}
		<div class="card bg-white shadow-lg">
			<div class="card-body">
				<h2 class="card-title text-xl mb-4">Your Profile</h2>

				<div class="grid grid-cols-1 md:grid-cols-2 gap-6">
					<!-- Name -->
					<div>
						<p class="text-sm text-gray-600">Full Name</p>
						<p class="text-lg font-semibold text-gray-900">{$authStore.user.fullName || 'N/A'}</p>
					</div>

					<!-- Email -->
					<div>
						<p class="text-sm text-gray-600">Email Address</p>
						<p class="text-lg font-semibold text-gray-900">{$authStore.user.email}</p>
					</div>

					<!-- Contact Number -->
					{#if $authStore.user.contactNumber}
						<div>
							<p class="text-sm text-gray-600">Contact Number</p>
							<p class="text-lg font-semibold text-gray-900">{$authStore.user.contactNumber}</p>
						</div>
					{/if}

					<!-- Role -->
					<div>
						<p class="text-sm text-gray-600">Role</p>
						<div class="mt-1 inline-block">
							<span
								class="px-3 py-1 rounded-full text-sm font-semibold
								{$authStore.user.role === 'SUPERADMIN'
									? 'bg-red-100 text-red-800'
									: $authStore.user.role === 'ADMIN'
										? 'bg-orange-100 text-orange-800'
										: 'bg-blue-100 text-blue-800'}"
							>
								{$authStore.user.role}
							</span>
						</div>
					</div>

					<!-- Account Status -->
					<div>
						<p class="text-sm text-gray-600">Account Status</p>
						<div class="mt-1">
							<span class="px-3 py-1 rounded-full text-sm font-semibold bg-green-100 text-green-800">
								{$authStore.user.isActive ? 'Active' : 'Inactive'}
							</span>
						</div>
					</div>

					<!-- Member Since -->
					<div>
						<p class="text-sm text-gray-600">Member Since</p>
						<p class="text-lg font-semibold text-gray-900">
							{new Date($authStore.user.createdAt).toLocaleDateString()}
						</p>
					</div>
				</div>
			</div>
		</div>
	{:else}
		<div class="card bg-white shadow-lg">
			<div class="card-body">
				<p class="text-gray-600">Loading user information...</p>
			</div>
		</div>
	{/if}

	<!-- Quick Actions -->
	<div class="grid grid-cols-1 md:grid-cols-3 gap-4">
		<a href="/profile" class="card bg-white shadow-lg hover:shadow-xl transition cursor-pointer">
			<div class="card-body">
				<h3 class="card-title text-lg">Edit Profile</h3>
				<p class="text-gray-600 text-sm">Update your personal information</p>
			</div>
		</a>

		<a href="/settings" class="card bg-white shadow-lg hover:shadow-xl transition cursor-pointer">
			<div class="card-body">
				<h3 class="card-title text-lg">Settings</h3>
				<p class="text-gray-600 text-sm">Manage your account preferences</p>
			</div>
		</a>

		<a href="/help" class="card bg-white shadow-lg hover:shadow-xl transition cursor-pointer">
			<div class="card-body">
				<h3 class="card-title text-lg">Help & Support</h3>
				<p class="text-gray-600 text-sm">Get help with your account</p>
			</div>
		</a>
	</div>
</div>

<style lang="postcss">
	:global(.card) {
		@apply transition-all duration-300;
	}
</style>
