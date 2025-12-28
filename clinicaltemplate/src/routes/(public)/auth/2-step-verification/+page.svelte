<script lang="ts">
	import { enhance } from '$app/forms';

	let { form } = $props();

	let code = $state(['', '', '', '', '', '']);
	let loading = $state(false);

	function handleCodeInput(index: number, event: Event) {
		const input = event.target as HTMLInputElement;
		const value = input.value;

		if (value.length > 1) {
			// Handle paste
			const digits = value.replace(/\D/g, '').split('');
			code = code.map((_, i) => digits[i] || '');
		} else if (/^\d*$/.test(value)) {
			code[index] = value;
			// Auto-focus to next input
			if (value && index < 5) {
				const nextInput = document.getElementById(`digit-${index + 1}`) as HTMLInputElement;
				nextInput?.focus();
			}
		} else {
			input.value = code[index];
		}
	}

	function handleKeyDown(index: number, event: KeyboardEvent) {
		if (event.key === 'Backspace' && !code[index] && index > 0) {
			const prevInput = document.getElementById(`digit-${index - 1}`) as HTMLInputElement;
			prevInput?.focus();
		}
	}

	function handleSubmit() {
		loading = true;
	}

	const fullCode = code.join('');
</script>

<div class="card bg-white shadow-lg">
	<div class="card-body space-y-6">
		<!-- Logo and Title -->
		<div class="text-center space-y-3">
			<div class="flex justify-center mb-2">
				<div class="text-4xl text-primary">💜</div>
			</div>
			<h1 class="text-2xl font-bold text-gray-900">Two Step Verification 📱</h1>
			<p class="text-sm text-gray-600">
				We sent a verification code to your mobile. Enter the code from the mobile in the field
				below.
			</p>
			<p class="text-xs text-gray-500">
				<span class="font-semibold">•••••</span>1234
			</p>
		</div>

		<!-- Error Messages -->
		{#if form?.invalid}
			<div class="alert alert-error alert-sm">
				<span>Invalid verification code. Please try again.</span>
			</div>
		{/if}
		{#if form?.expired}
			<div class="alert alert-error alert-sm">
				<span>Verification code has expired. Please request a new one.</span>
			</div>
		{/if}

		<!-- Verification Form -->
		<form method="POST" action="?/verify" use:enhance class="space-y-6" onsubmit={handleSubmit}>
			<!-- Code Label -->
			<div class="space-y-4">
				<label class="label" for="code">
					<span class="label-text text-gray-700 font-medium">Type your 6 digit security code</span>
				</label>

				<!-- OTP Input Fields -->
				<div class="grid grid-cols-6 justify-center">
					{#each code as digit, index (index)}
						<input
							id="digit-{index}"
							type="text"
							inputmode="numeric"
							maxlength="1"
							value={digit}
							onchange={(e) => handleCodeInput(index, e)}
							oninput={(e) => handleCodeInput(index, e)}
							onkeydown={(e) => handleKeyDown(index, e)}
							class="otp-input w-12 h-12 sm:w-14 sm:h-14 border border-gray-300 rounded-md text-center text-xl font-normal text-gray-700 focus:border-primary focus:outline-none transition"
							required
						/>
					{/each}
				</div>

				<!-- Hidden input for form submission -->
				<input type="hidden" name="code" value={fullCode} />
			</div>

			<!-- Verify Button -->
			<button
				type="submit"
				class="btn btn-primary w-full text-white font-semibold mt-4"
				disabled={loading}
			>
				{#if loading}
					<span class="loading loading-spinner loading-sm"></span>
					Verifying...
				{:else}
					Verify my account
				{/if}
			</button>
		</form>

		<!-- Resend Code -->
		<div class="text-center">
			<p class="text-sm text-gray-600">
				Didn't get the code?
				<a href="#" class="link link-primary font-medium">Resend</a>
			</p>
		</div>

		<!-- Edit Number Link -->
		<div class="text-center">
			<a href="/auth/login" class="link link-sm text-gray-500 hover:text-gray-700">
				Edit registered mobile number
			</a>
		</div>
	</div>
</div>

<style lang="postcss">
	.card {
		border-radius: 0.5rem;
		border: 1px solid #e5e7eb;
		margin: 0 auto;
		width: 100%;
		max-width: 100%;
	}

	.card-body {
		padding: 2rem;
	}

	.space-y-6 > * + * {
		margin-top: 1.5rem;
	}

	.space-y-4 > * + * {
		margin-top: 1rem;
	}

	.otp-input {
		font-family: monospace;
		caret-color: #6366f1;
		flex-shrink: 0;
	}

	.otp-input::-webkit-outer-spin-button,
	.otp-input::-webkit-inner-spin-button {
		-webkit-appearance: none;
		margin: 0;
	}

	.otp-input[type='number'] {
		-moz-appearance: textfield;
	}

	.otp-input:focus {
		border-color: #6366f1 !important;
		box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.1);
	}

	.btn-primary {
		background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%);
		border: none;
	}

	.btn-primary:hover:not(:disabled) {
		opacity: 0.9;
	}

	.btn-primary:disabled {
		opacity: 0.6;
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
		border-radius: 0.375rem;
	}

	:global(.loading) {
		margin-right: 0.5rem;
	}
</style>
