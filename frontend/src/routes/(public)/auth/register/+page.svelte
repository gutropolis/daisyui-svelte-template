<!-- LoginForm.svelte -->
<script lang="ts">
  import { writable } from 'svelte/store';
  import { onMount } from "svelte"; 
  import { getContextClient } from "@urql/svelte";
  import type { User } from "$lib/modal/User";
  import alerts from "$lib/stores/alerts"; 
 	import { PATH } from '$lib/enums/path';
	import { handleGqlErr } from '$lib/utils/gqlfx';
  import { RegisterUser } from "$lib/gql/user";


	let user: User = {
		email: '',
		country: 'US',
		firstName: '',
		lastName: '',
		contact_number: '',
		 
		password: '',
		password2: ''
	};
	let title = '';
	let busy = false;
	let valid = false;
 
	const client = getContextClient();

	let showPassword = $state(false);
	let showConfirmPassword = $state(false);
	let agreedToTerms = $state(false);
	let loading = $state(false);
	let error = $state<string | null>(null);
	let success = $state(false);

	function formatRegisterErrors(errors: Record<string, any> | undefined) {
		if (!errors) return 'Registration failed. Please check your details and try again.';
		return Object.entries(errors)
			.map(([field, messages]) => {
				const parts = Array.isArray(messages)
					? messages.map((m) => (typeof m === 'string' ? m : m?.message || JSON.stringify(m)))
					: [String(messages)];
				return `${field}: ${parts.join(', ')}`;
			})
			.join('; ');
	}

	function togglePasswordVisibility() {
		showPassword = !showPassword;
	}

	function toggleConfirmPasswordVisibility() {
		showConfirmPassword = !showConfirmPassword;
	}

	async function handleRegister(e: SubmitEvent) {
		e.preventDefault();
		error = null;
		success = false;

		// Validation
		if (!user.email || !user.password || !user.password2 || !user.firstName) {
			error = 'Please fill in all required fields';
			return;
		}

		if (user.password !== user.password2) {
			error = 'Passwords do not match';
			return;
		}

		if (user.password.length < 8) {
			error = 'Password must be at least 8 characters';
			return;
		}

		if (!agreedToTerms) {
			error = 'You must agree to the terms & conditions';
			return;
		}

		loading = true;
const regUserInput = {
			email: user.email,
			password: user.password,
			password2: user.password2,
			firstName: user.firstName,
			lastName: user.lastName,
			contact_number: user.contact_number,
			country: user.country, 
		};
		console.log("contact information", { input: regUserInput });
		const res = await client
			.mutation(RegisterUser, {
				email: user.email,
				password1: user.password,
				password2: user.password2,
				firstName: user.firstName,
				lastName: user.lastName,
				contactNumber: user.contact_number 
				 
			})
			.toPromise();
 
    console.log("RES", res);
    loading = false;

    console.log("ERROR", res.error);
    if (res.error) {
      let errMsg = handleGqlErr(res.error);
      alerts.error(title, errMsg);
      return false;
    }

    let result = res.data.register; 
		if (result.success) {
			success = true;
			alerts.success(title || 'Registration', result.message || 'Account created successfully');
			console.log("token",result.token,"refreshToken",result.refreshToken,"message",result.message )
			return;
		}

		const formattedErrors = formatRegisterErrors(result.errors);
		error = formattedErrors;
		alerts.error(title || 'Registration failed', formattedErrors);
	 
	}
</script>

<div class="card bg-white shadow-lg">
	<div class="card-body space-y-6">
		<!-- Logo and Title -->
		<div class="text-center space-y-2">
			<div class="flex justify-center mb-4">
				<div class="text-4xl text-primary">💜</div>
			</div>
			<h1 class="text-2xl font-bold text-gray-900">Create Account 🚀</h1>
			<p class="text-sm text-gray-600">Start your healthcare journey today</p>
		</div>

		<!-- Success Message -->
		{#if success}
			<div class="alert alert-success alert-sm">
				<span>✓ Account created successfully! Redirecting...</span>
			</div>
		{/if}

		<!-- Error Messages -->
		{#if error}
			<div class="alert alert-error alert-sm">
				<span>{error}</span>
			</div>
		{/if}

		<!-- Registration Form -->
		<form onsubmit={handleRegister} class="space-y-4">
			<!-- Full Name Input -->
			<div class="form-control">
				<label class="label" for="firstname">
					<span class="label-text text-gray-700">First Name <span class="text-red-500">*</span></span>
				</label>
				<input
					id="firstname"
					type="text"
					placeholder="Enter your first name"
					class="input input-bordered w-full focus:outline-none focus:border-primary"
					bind:value={user.firstName}
					required
					disabled={loading}
				/>
			</div>

			<div class="form-control">
				<label class="label" for="lastname">
					<span class="label-text text-gray-700">Last Name</span>
				</label>
				<input
					id="lastname"
					type="text"
					placeholder="Enter your last name"
					class="input input-bordered w-full focus:outline-none focus:border-primary"
					bind:value={user.lastName}
					disabled={loading}
				/>
			</div>

			<!-- Email Input -->
			<div class="form-control">
				<label class="label" for="email">
					<span class="label-text text-gray-700">Email <span class="text-red-500">*</span></span>
				</label>
				<input
					id="email"
					type="email"
					placeholder="Enter your email"
					class="input input-bordered w-full focus:outline-none focus:border-primary"
					bind:value={user.email}
					required
					disabled={loading}
				/>
			</div>

			<!-- Contact Number Input -->
			<div class="form-control">
				<label class="label" for="contactNumber">
					<span class="label-text text-gray-700">Contact Number</span>
				</label>
				<input
					id="contactNumber"
					type="tel"
					placeholder="Enter your contact number (optional)"
					class="input input-bordered w-full focus:outline-none focus:border-primary"
					bind:value={user.contact_number}
					disabled={loading}
				/>
			</div>

			<!-- Password Input -->
			<div class="form-control">
				<label class="label" for="password">
					<span class="label-text text-gray-700">Password <span class="text-red-500">*</span></span>
				</label>
				<div class="relative">
					<input
						id="password"
						type={showPassword ? 'text' : 'password'}
						placeholder="••••••••"
						class="input input-bordered w-full focus:outline-none focus:border-primary"
						bind:value={user.password}
						required
						disabled={loading}
					/>
					<button
						type="button"
						onclick={togglePasswordVisibility}
						class="absolute right-3 top-1/2 transform -translate-y-1/2 text-gray-500 hover:text-gray-700"
						tabindex="-1"
						disabled={loading}
					>
						{#if showPassword}
							<svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
								<path
									stroke-linecap="round"
									stroke-linejoin="round"
									stroke-width="2"
									d="M13.875 18.825A10.05 10.05 0 0112 19c-4.478 0-8.268-2.943-9.543-7a9.97 9.97 0 011.563-4.803m5.596-3.856a3.375 3.375 0 11-6.75 0 3.375 3.375 0 016.75 0M15 12a3 3 0 11-6 0 3 3 0 016 0z"
								></path>
							</svg>
						{:else}
							<svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
								<path
									stroke-linecap="round"
									stroke-linejoin="round"
									stroke-width="2"
									d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"
								></path>
								<path
									stroke-linecap="round"
									stroke-linejoin="round"
									stroke-width="2"
									d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"
								></path>
							</svg>
						{/if}
					</button>
				</div>
			</div>

			<!-- Confirm Password Input -->
			<div class="form-control">
				<label class="label" for="confirmPassword">
					<span class="label-text text-gray-700">Confirm Password <span class="text-red-500">*</span></span>
				</label>
				<div class="relative">
					<input
						id="confirmPassword"
						type={showConfirmPassword ? 'text' : 'password'}
						placeholder="••••••••"
						class="input input-bordered w-full focus:outline-none focus:border-primary"
						bind:value={user.password2}
						required
						disabled={loading}
					/>
					<button
						type="button"
						onclick={toggleConfirmPasswordVisibility}
						class="absolute right-3 top-1/2 transform -translate-y-1/2 text-gray-500 hover:text-gray-700"
						tabindex="-1"
						disabled={loading}
					>
						{#if showConfirmPassword}
							<svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
								<path
									stroke-linecap="round"
									stroke-linejoin="round"
									stroke-width="2"
									d="M13.875 18.825A10.05 10.05 0 0112 19c-4.478 0-8.268-2.943-9.543-7a9.97 9.97 0 011.563-4.803m5.596-3.856a3.375 3.375 0 11-6.75 0 3.375 3.375 0 016.75 0M15 12a3 3 0 11-6 0 3 3 0 016 0z"
								></path>
							</svg>
						{:else}
							<svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
								<path
									stroke-linecap="round"
									stroke-linejoin="round"
									stroke-width="2"
									d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"
								></path>
								<path
									stroke-linecap="round"
									stroke-linejoin="round"
									stroke-width="2"
									d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"
								></path>
							</svg>
						{/if}
					</button>
				</div>
			</div>

			<!-- Terms & Conditions -->
			<label class="label cursor-pointer" for="terms">
				<input
					id="terms"
					type="checkbox"
					bind:checked={agreedToTerms}
					class="checkbox checkbox-sm checkbox-primary"
					required
					disabled={loading}
				/>
				<span class="label-text ml-2 text-sm text-gray-700">
					I agree to the <a href="#" class="link link-primary">Terms & Conditions</a>
				</span>
			</label>

			<!-- Register Button -->
			<button type="submit" class="btn btn-primary w-full text-white font-semibold" disabled={loading}>
				{#if loading}
					<span class="loading loading-spinner loading-sm"></span>
					Creating Account...
				{:else}
					Create Account
				{/if}
			</button>
		</form>

		<!-- Divider -->
		<div class="flex items-center gap-3">
			<div class="flex-1 border-t border-gray-300"></div>
			<span class="text-sm text-gray-500">or</span>
			<div class="flex-1 border-t border-gray-300"></div>
		</div>

		<!-- Sign In Link -->
		<div class="text-center">
			<p class="text-sm text-gray-600">
				Already have an account?
				<a href="{PATH.LOGIN}" class="link link-primary font-medium">Sign in</a>
			</p>
		</div>

		<!-- Social Signup -->
		<div class="flex gap-4 justify-center">
			<button
				type="button"
				class="btn btn-ghost btn-sm rounded-full w-10 h-10 p-0 flex items-center justify-center"
				aria-label="Sign up with Facebook"
			>
				<svg class="w-5 h-5 text-blue-600" fill="currentColor" viewBox="0 0 24 24">
					<path
						d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"
					/>
				</svg>
			</button>
			<button
				type="button"
				class="btn btn-ghost btn-sm rounded-full w-10 h-10 p-0 flex items-center justify-center"
				aria-label="Sign up with Twitter"
			>
				<svg class="w-5 h-5 text-blue-400" fill="currentColor" viewBox="0 0 24 24">
					<path
						d="M23 3a10.9 10.9 0 01-3.14 1.53 4.48 4.48 0 00-7.86 3v1A10.66 10.66 0 013 4s-4 9 5 13a11.64 11.64 0 01-7 2s9 5 20 5a9.5 9.5 0 00-9-5.5c4.75 2.25 7-7 7-7s1.1 5-5 8.5c-3.5 2-7 1-7 1"
					/>
				</svg>
			</button>
			<button
				type="button"
				class="btn btn-ghost btn-sm rounded-full w-10 h-10 p-0 flex items-center justify-center"
				aria-label="Sign up with GitHub"
			>
				<svg class="w-5 h-5 text-gray-800" fill="currentColor" viewBox="0 0 24 24">
					<path
						d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v 3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"
					/>
				</svg>
			</button>
			<button
				type="button"
				class="btn btn-ghost btn-sm rounded-full w-10 h-10 p-0 flex items-center justify-center"
				aria-label="Sign up with Google"
			>
				<svg class="w-5 h-5" viewBox="0 0 24 24">
					<path
						fill="#4285F4"
						d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z"
					/>
					<path
						fill="#34A853"
						d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z"
					/>
					<path
						fill="#FBBC05"
						d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.07H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.93l2.85-2.22.81-.62z"
					/>
					<path
						fill="#EA4335"
						d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.07l3.66 2.84c.87-2.6 3.3-4.53 6.16-4.53z"
					/>
				</svg>
			</button>
		</div>
	</div>
</div>

<style lang="postcss">
	.card {
		border-radius: 0.5rem;
		border: 1px solid #e5e7eb;
		margin: 0 auto;
		width: 100%;
	}

	.card-body {
		padding: 2rem;
	}

	.space-y-4 > * + * {
		margin-top: 1rem;
	}

	.space-y-6 > * + * {
		margin-top: 1.5rem;
	}

	.input,
	.btn {
		border-radius: 0.375rem;
	}

	.input {
		height: 2.5rem;
		padding: 0.625rem 0.75rem;
		border: 1px solid #d1d5db;
		background-color: #fff;
	}

	.input:focus {
		border-color: #6366f1;
		box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.1);
	}

	.input:disabled {
		opacity: 0.6;
		cursor: not-allowed;
	}

	.btn-primary {
		background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%);
		border: none;
	}

	.btn-primary:hover:not(:disabled) {
		opacity: 0.9;
	}

	.btn-primary:disabled {
		opacity: 0.7;
		cursor: not-allowed;
	}

	.link-primary {
		color: #6366f1;
	}

	.link-primary:hover {
		text-decoration: underline;
	}

	.label-text {
		font-size: 0.875rem;
		font-weight: 500;
	}

	.alert-error {
		background-color: #fee2e2;
		color: #dc2626;
		border: 1px solid #fecaca;
	}

	.alert-success {
		background-color: #dcfce7;
		color: #166534;
		border: 1px solid #bbf7d0;
	}
</style>
