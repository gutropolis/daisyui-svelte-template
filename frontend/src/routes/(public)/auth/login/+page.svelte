<!-- LoginForm.svelte -->
<script lang="ts"> 
  import { goto } from "$app/navigation";
  import { createEventDispatcher } from "svelte";
  import { getContextClient } from "@urql/svelte";
  import {  setTokens, clearTokens } from '$lib/stores/authStore'; 
	import Input from '$theme/components/form/Input.svelte';
  import { writable } from 'svelte/store';
	import { handleGqlErr } from "$lib/utils/gqlfx";
	import alerts from "$lib/stores/alerts";
  import { LoginUser, RegisterUser } from "$lib/gql/user";
  import { PATH } from '$lib/enums/path';
  import { authUser } from '$lib/stores/app';
  import graph   from "$theme/images/graph.png";

  let loading = false;
  let error = "";
  let valid = false;
  let showPassword = writable(false); 
  const client = getContextClient();
  let email="";
  let password="";
  
  function togglePasswordVisibility() {
    showPassword.update(v => !v);
  }
  
  async function handleSubmit() {
    //Add Code for graphql

    let title = "Login Member";
    if (loading) return;
    loading = true;
   
    const res = await client
      .mutation(LoginUser, {  
        email: email,
        password: password,  
      })
      .toPromise();
 
    console.log("RES", res);
    loading = false;

    console.log("ERROR", res.error);
    if (res.error) {
      let errMsg = handleGqlErr(res.error);
	  error=errMsg;
      alerts.error(title, errMsg);
      return false;
    }

    let result = res.data.tokenAuth;
 
    if (result) {
      alerts.success(title,"Login Successfully!!"); 
      setTokens(result.token, result.refreshToken);
      authUser.set(result?.user);
      goto(PATH.MY_PROFILE);
      
      console.log("token",result.token,"refreshToken", result.refreshToken,   )
      return;
    }
    //End Graphql
  } 
</script>
<div class="card bg-white shadow-lg">
	<div class="card-body space-y-6">
		<!-- Logo and Title -->
		<div class="text-center space-y-2">
			<div class="flex justify-center mb-4">
				<div class="text-4xl text-primary">💜</div>
			</div>
			<h1 class="text-2xl font-bold text-gray-900">Welcome Back! 👋</h1>
			<p class="text-sm text-gray-600">Sign in to your account to continue</p>
		</div>

		<!-- Error Message -->
		{#if error}
			<div class="alert alert-error alert-sm">
				<span>{error}</span>
			</div>
		{/if}

		<!-- Login Form -->
		<form onsubmit={handleSubmit} class="space-y-4">
			<!-- Email Input -->
			<div class="form-control">
				<label class="label" for="email">
					<span class="label-text text-gray-700">Email Address</span>
				</label>
				<input
					id="email"
					type="email"
					bind:value={email}
					placeholder="Enter your email"
					class="input input-bordered w-full focus:outline-none focus:border-primary"
					disabled={loading}
					required
				/>
			</div>

			<!-- Password Input -->
			<div class="form-control">
				<label class="label" for="password">
					<span class="label-text text-gray-700">Password</span>
				</label>
				<div class="relative">
					<input
						id="password"
						type={$showPassword ? 'text' : 'password'}
						bind:value={password}
						placeholder="••••••••"
						class="input input-bordered w-full focus:outline-none focus:border-primary"
						disabled={loading}
						required
					/>
					<button
						type="button"
						onclick={togglePasswordVisibility}
						class="absolute right-3 top-1/2 transform -translate-y-1/2 text-gray-500 hover:text-gray-700"
						tabindex="-1"
					>
						{#if $showPassword}
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

			<!-- Forgot Password Link -->
			<div class="flex justify-end">
				<a href="/auth/forgot-password" class="link link-primary text-sm">Forgot Password?</a>
			</div>

			<!-- Login Button -->
			<button type="submit" disabled={loading} class="btn btn-primary w-full text-white font-semibold">
				{#if loading}
					<span class="loading loading-spinner loading-sm"></span>
					Signing in...
				{:else}
					Login
				{/if}
			</button>
		</form>

		<!-- Sign Up Link -->
		<div class="text-center">
			<p class="text-sm text-gray-600">
				New on our platform?
				<a href="/auth/register" class="link link-primary font-medium">Create an account</a>
			</p>
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

	.btn-primary {
		background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%);
		border: none;
	}

	.btn-primary:hover {
		opacity: 0.9;
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
</style>
