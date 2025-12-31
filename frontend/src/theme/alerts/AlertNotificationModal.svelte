<script lang="ts">
	interface AlertForm {
		title: string;
		triggerType: 'specific-form' | 'conditional-form' | 'import-logic';
		formName: string;
		formStatus: string;
		conditionalLogic: string;
		ensureLogicBeforeSending: boolean;
		sendWhen: 'immediately' | 'on-next' | 'after-lapse' | 'exact-date';
		nextEventValue: number;
		nextEventUnit: string;
		lapseDays: number;
		lapseHours: number;
		lapseMinutes: number;
		exactDateTime: string;
		frequency: 'once' | 'every-time' | 'multiple';
		multipleDays: number;
		emailFrom: string;
		emailTo: string;
		manualEmails: string;
		subject: string;
		message: string;
		preventPiping: boolean;
		attachments: File[];
		expirationDateTime: string;
	}

	let isOpen = $state(false);
	let activeStep = $state(0);
	let showMoreOptions = $state(false);

	let formData = $state<AlertForm>({
		title: '',
		triggerType: 'specific-form',
		formName: '',
		formStatus: 'any',
		conditionalLogic: '',
		ensureLogicBeforeSending: false,
		sendWhen: 'immediately',
		nextEventValue: 1,
		nextEventUnit: 'day',
		lapseDays: 0,
		lapseHours: 0,
		lapseMinutes: 0,
		exactDateTime: '',
		frequency: 'every-time',
		multipleDays: 0,
		emailFrom: 'j.johnston@ufl.edu',
		emailTo: '',
		manualEmails: '',
		subject: '',
		message: '',
		preventPiping: true,
		attachments: [],
		expirationDateTime: ''
	});

	const forms = [
		'Baseline',
		'Intervention',
		'Checkpoint 30 Day',
		'Checkpoint 6 Month',
		'Checkpoint 1 Year'
	];

	const formStatuses = ['any form status', 'complete', 'incomplete', 'unverified'];

	export const open = () => {
		isOpen = true;
		activeStep = 0;
	};

	export const close = () => {
		isOpen = false;
		resetForm();
	};

	const resetForm = () => {
		formData = {
			title: '',
			triggerType: 'specific-form',
			formName: '',
			formStatus: 'any',
			conditionalLogic: '',
			ensureLogicBeforeSending: false,
			sendWhen: 'immediately',
			nextEventValue: 1,
			nextEventUnit: 'day',
			lapseDays: 0,
			lapseHours: 0,
			lapseMinutes: 0,
			exactDateTime: '',
			frequency: 'every-time',
			multipleDays: 0,
			emailFrom: 'j.johnston@ufl.edu',
			emailTo: '',
			manualEmails: '',
			subject: '',
			message: '',
			preventPiping: true,
			attachments: [],
			expirationDateTime: ''
		};
		activeStep = 0;
	};

	const saveAlert = () => {
		console.log('Saving alert:', formData);
		close();
	};

	const handleFileUpload = (event: Event) => {
		const input = event.target as HTMLInputElement;
		if (input.files) {
			formData.attachments = Array.from(input.files);
		}
	};
</script>

{#if isOpen}
	<div class="fixed inset-0 bg-black/50 flex items-center justify-center z-50">
		<div class="bg-white rounded-lg shadow-lg max-w-2xl w-full max-h-[90vh] overflow-auto">
			<!-- Header -->
			<div class="bg-white border-b border-gray-200 sticky top-0 z-10 px-6 py-4 flex justify-between items-center">
				<h2 class="text-xl font-bold text-gray-900">Create new alert</h2>
				<button
					onclick={close}
					class="text-gray-400 hover:text-gray-600 transition-colors"
					title="Close"
				>
					<i class="fas fa-times text-xl"></i>
				</button>
			</div>

			<!-- Content -->
			<div class="px-6 py-4">
				<!-- Alert Title -->
				<div class="mb-8">
					<div class="bg-blue-50 border border-blue-200 rounded p-3 mb-4">
						<p class="text-sm text-gray-700">
							You may define the settings for your alert in Steps 1-3 below. After clicking the Save button at the bottom,
							your alert will immediately become active and may be triggered at any time thereafter. If you would like to
							remove or stop using an alert, it may be deactivated at any time. You may modify an existing alert at any time,
							even after some notifications have already been sent or scheduled.
						</p>
					</div>

					<label class="block mb-2">
						<span class="text-sm font-semibold text-gray-900 mb-1 block">Title of this alert:</span>
						<span class="text-xs text-red-500">* must provide value</span>
						<input
							type="text"
							bind:value={formData.title}
							placeholder="Enter alert title (e.g., 'New Subject Consented on XYZ Study')"
							class="w-full mt-2 px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-[#0b3a7a]"
						/>
					</label>
				</div>

				<!-- Step 1: Triggering the Alert -->
				<div class="mb-8 border border-gray-200 rounded-lg overflow-hidden">
					<div class="bg-blue-600 text-white px-4 py-3 flex items-center gap-2">
						<i class="fas fa-bell"></i>
						<h3 class="font-bold text-sm">STEP 1: Triggering the Alert</h3>
					</div>
					<div class="p-4 bg-gray-50">
						<div class="mb-4">
							<p class="text-sm font-semibold text-gray-900 mb-3">How will this alert be triggered?</p>
							<div class="space-y-2">
								<label class="flex items-center gap-2">
									<input
										type="radio"
										bind:group={formData.triggerType}
										value="specific-form"
										class="w-4 h-4"
									/>
									<span class="text-sm text-gray-700">When a record is saved on a specific form/survey</span>
								</label>
								<label class="flex items-center gap-2">
									<input
										type="radio"
										bind:group={formData.triggerType}
										value="conditional-form"
										class="w-4 h-4"
									/>
									<span class="text-sm text-gray-700">When a record is saved on a specific form/survey with conditional logic</span>
									<span class="text-xs text-red-500">*</span>
								</label>
								<label class="flex items-center gap-2">
									<input
										type="radio"
										bind:group={formData.triggerType}
										value="import-logic"
										class="w-4 h-4"
									/>
									<span class="text-sm text-gray-700">Using conditional logic during a data import or data entry</span>
								</label>
							</div>
						</div>

						<div class="border-t border-gray-200 pt-4">
							<p class="text-sm font-semibold text-gray-900 mb-3">Trigger the alert...</p>
							<div class="flex gap-2 mb-4">
								<select
									bind:value={formData.formName}
									class="flex-1 px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-[#0b3a7a] text-sm"
								>
									<option value="">Select form...</option>
									{#each forms as form}
										<option value={form}>{form}</option>
									{/each}
								</select>
								<select
									bind:value={formData.formStatus}
									class="flex-1 px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-[#0b3a7a] text-sm"
								>
									{#each formStatuses as status}
										<option value={status}>{status}</option>
									{/each}
								</select>
								<span class="text-xs text-gray-500 py-2">(excludes data imports)</span>
							</div>

							{#if formData.triggerType !== 'specific-form'}
								<div class="mb-4">
									<label class="block mb-2">
										<span class="text-sm font-semibold text-gray-900">while the following logic is true:</span>
										<textarea
											bind:value={formData.conditionalLogic}
											placeholder="e.g., [age] > 30 and [sex] = '1'"
											class="w-full mt-1 px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-[#0b3a7a] text-sm"
											rows="3"
										></textarea>
									</label>
									<p class="text-xs text-gray-500 mt-1 flex items-center gap-1">
										<i class="fas fa-check text-green-600"></i>
										Valid
									</p>
									<a href="#" class="text-xs text-[#0b3a7a] hover:underline block mt-2">
										How to use 'stop logic' to disable a scheduled alert
									</a>
								</div>

								<label class="flex items-center gap-2">
									<input
										type="checkbox"
										bind:checked={formData.ensureLogicBeforeSending}
										class="w-4 h-4"
									/>
									<span class="text-sm text-gray-700">Ensure logic is still true before sending notification?</span>
									<button class="text-gray-400 hover:text-gray-600" title="Help">
										<i class="fas fa-question-circle text-xs"></i>
									</button>
								</label>
							{/if}

							<p class="text-xs text-red-600 mt-3 font-semibold">
								* The alert will not be re-triggered if the form/survey is saved again, unless it is set to send
								"Every time" in Step 2 below.
							</p>
						</div>
					</div>
				</div>

				<!-- Step 2: Alert Schedule -->
				<div class="mb-8 border border-gray-200 rounded-lg overflow-hidden">
					<div class="bg-blue-600 text-white px-4 py-3 flex items-center gap-2">
						<i class="fas fa-clock"></i>
						<h3 class="font-bold text-sm">STEP 2: Set the Alert Schedule</h3>
					</div>
					<div class="p-4 bg-gray-50">
						<div class="mb-6">
							<p class="text-sm font-semibold text-gray-900 mb-3">When to send the alert?</p>
							<div class="space-y-2">
								<label class="flex items-center gap-2">
									<input
										type="radio"
										bind:group={formData.sendWhen}
										value="immediately"
										class="w-4 h-4"
									/>
									<span class="text-sm text-gray-700">Send immediately</span>
								</label>
								<label class="flex items-center gap-2">
									<input
										type="radio"
										bind:group={formData.sendWhen}
										value="on-next"
										class="w-4 h-4"
									/>
									<div class="flex items-center gap-2">
										<span class="text-sm text-gray-700">Send on next</span>
										<select
											bind:value={formData.nextEventUnit}
											class="px-2 py-1 border border-gray-300 rounded text-sm"
										>
											<option value="day">day</option>
											<option value="hour">hour</option>
											<option value="month">month</option>
										</select>
										<span class="text-sm text-gray-700">at time</span>
										<input
											type="time"
											class="px-2 py-1 border border-gray-300 rounded text-sm"
											placeholder="HH:MM"
										/>
									</div>
								</label>
								<label class="flex items-center gap-2">
									<input
										type="radio"
										bind:group={formData.sendWhen}
										value="after-lapse"
										class="w-4 h-4"
									/>
									<span class="text-sm text-gray-700">Send after lapse of time:</span>
									<input
										type="number"
										bind:value={formData.lapseDays}
										min="0"
										class="w-12 px-2 py-1 border border-gray-300 rounded text-sm"
									/>
									<span class="text-sm text-gray-700">days</span>
									<input
										type="number"
										bind:value={formData.lapseHours}
										min="0"
										max="23"
										class="w-12 px-2 py-1 border border-gray-300 rounded text-sm"
									/>
									<span class="text-sm text-gray-700">hours</span>
									<input
										type="number"
										bind:value={formData.lapseMinutes}
										min="0"
										max="59"
										class="w-12 px-2 py-1 border border-gray-300 rounded text-sm"
									/>
									<span class="text-sm text-gray-700">minutes</span>
								</label>
								<label class="flex items-center gap-2">
									<input
										type="radio"
										bind:group={formData.sendWhen}
										value="exact-date"
										class="w-4 h-4"
									/>
									<span class="text-sm text-gray-700">Send at exact date/time:</span>
									<input
										type="datetime-local"
										bind:value={formData.exactDateTime}
										class="px-2 py-1 border border-gray-300 rounded text-sm"
										placeholder="MM/DD/YYYY HH:MM"
									/>
								</label>
							</div>
						</div>

						<div class="border-t border-gray-200 pt-4">
							<p class="text-sm font-semibold text-gray-900 mb-3">Send it how many times?</p>
							<div class="space-y-2">
								<label class="flex items-center gap-2">
									<input
										type="radio"
										bind:group={formData.frequency}
										value="once"
										class="w-4 h-4"
									/>
									<span class="text-sm text-gray-700">Just once</span>
								</label>
								<label class="flex items-center gap-2">
									<input
										type="radio"
										bind:group={formData.frequency}
										value="every-time"
										class="w-4 h-4"
									/>
									<span class="text-sm text-gray-700">
										Every time the form/survey in Step 1 is saved (excludes data imports)
									</span>
								</label>
								<label class="flex items-center gap-2">
									<input
										type="radio"
										bind:group={formData.frequency}
										value="multiple"
										class="w-4 h-4"
									/>
									<span class="text-sm text-gray-700">Multiple times: Send every</span>
									<input
										type="number"
										bind:value={formData.multipleDays}
										min="0"
										class="w-12 px-2 py-1 border border-gray-300 rounded text-sm"
									/>
									<select class="px-2 py-1 border border-gray-300 rounded text-sm">
										<option>days</option>
										<option>hours</option>
										<option>weeks</option>
									</select>
									<span class="text-sm text-gray-700">after initially being sent</span>
								</label>
							</div>
						</div>
					</div>
				</div>

				<!-- Step 3: Message Settings -->
				<div class="mb-8 border border-gray-200 rounded-lg overflow-hidden">
					<div class="bg-blue-600 text-white px-4 py-3 flex items-center gap-2">
						<i class="fas fa-envelope"></i>
						<h3 class="font-bold text-sm">STEP 3: Message Settings</h3>
					</div>
					<div class="p-4 bg-gray-50">
						<div class="mb-4">
							<label class="block mb-2">
								<span class="text-sm font-semibold text-gray-900">Email From:</span>
								<span class="text-xs text-red-500">* must provide value</span>
								<select
									bind:value={formData.emailFrom}
									class="w-full mt-1 px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-[#0b3a7a]"
								>
									<option value="j.johnston@ufl.edu">j.johnston@ufl.edu</option>
									<option value="admin@example.com">admin@example.com</option>
								</select>
							</label>
						</div>

						<div class="mb-4">
							<label class="block mb-2">
								<span class="text-sm font-semibold text-gray-900">Email To:</span>
								<span class="text-xs text-red-500">* must provide value</span>
								<div class="flex gap-2 mt-1">
									<select
										bind:value={formData.emailTo}
										class="flex-1 px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-[#0b3a7a]"
									>
										<option value="">Select recipient...</option>
										<option value="j.johnston@ufl.edu">j.johnston@ufl.edu</option>
										<option value="admin@example.com">admin@example.com</option>
									</select>
									<button
										onclick={() => (showMoreOptions = !showMoreOptions)}
										class="text-[#0b3a7a] hover:underline text-sm font-medium px-2"
									>
										+ Show more options
									</button>
								</div>
							</label>

							{#if showMoreOptions}
								<div class="mt-2 p-3 bg-white border border-gray-200 rounded-lg">
									<label class="block mb-2">
										<span class="text-sm text-gray-700">Or manually enter emails:</span>
										<input
											type="text"
											bind:value={formData.manualEmails}
											placeholder="jane@example.com; john@mysite.org"
											class="w-full mt-1 px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-[#0b3a7a] text-sm"
										/>
									</label>
								</div>
							{/if}
						</div>

						<div class="mb-4">
							<label class="block mb-2">
								<span class="text-sm font-semibold text-gray-900">Subject:</span>
								<span class="text-xs text-red-500">* must provide value</span>
								<input
									type="text"
									bind:value={formData.subject}
									placeholder="Study XYZ New Subject Consented"
									class="w-full mt-1 px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-[#0b3a7a]"
								/>
							</label>
						</div>

						<div class="mb-4">
							<label class="block mb-2">
								<span class="text-sm font-semibold text-gray-900">Message:</span>
								<span class="text-xs text-red-500">* must provide value</span>
								<textarea
									bind:value={formData.message}
									placeholder="Record [participant_id] has consented to study. Review consent here: [survey-url:prescreening_survey]"
									class="w-full mt-1 px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-[#0b3a7a] text-sm"
									rows="4"
								></textarea>
							</label>
							<p class="text-xs text-gray-500 mt-1">
								In the subject or message, you may use
								<span class="bg-blue-100 text-blue-800 px-2 py-1 rounded text-xs font-medium">Piping</span>
								and
								<span class="bg-green-100 text-green-800 px-2 py-1 rounded text-xs font-medium">Smart Variables</span>
							</p>
							<p class="text-xs text-gray-500 mt-2">
								Example: Hi [first_name]! Please complete this survey: [survey-link:followup_survey]
							</p>
						</div>

						<div class="mb-4">
							<label class="flex items-center gap-2">
								<input
									type="checkbox"
									bind:checked={formData.preventPiping}
									class="w-4 h-4"
								/>
								<span class="text-sm text-gray-700">Prevent piping of data for Identifier fields</span>
								<button class="text-gray-400 hover:text-gray-600" title="Help">
									<i class="fas fa-question-circle text-xs"></i>
								</button>
							</label>
						</div>

						<button
							class="bg-green-600 hover:bg-green-700 text-white font-medium py-2 px-4 rounded-lg flex items-center gap-2 transition-colors"
						>
							<i class="fas fa-paperclip"></i>
							Add attachments
						</button>

						{#if formData.attachments.length > 0}
							<div class="mt-3 p-3 bg-white border border-gray-200 rounded-lg">
								<p class="text-sm font-medium text-gray-900 mb-2">Attachments:</p>
								<ul class="space-y-1">
									{#each formData.attachments as file}
										<li class="text-sm text-gray-600 flex items-center justify-between">
											<span>{file.name}</span>
											<button class="text-red-600 hover:text-red-700">
												<i class="fas fa-trash text-xs"></i>
											</button>
										</li>
									{/each}
								</ul>
							</div>
						{/if}
					</div>
				</div>

				<!-- Optional: Alert Expiration -->
				<div class="mb-8 border border-gray-200 rounded-lg overflow-hidden">
					<div class="bg-gray-600 text-white px-4 py-3">
						<h3 class="font-bold text-sm">Optional: Automatic Alert Expiration</h3>
					</div>
					<div class="p-4 bg-gray-50">
						<label class="block mb-2">
							<span class="text-sm font-semibold text-gray-900">Alert expiration:</span>
							<input
								type="datetime-local"
								bind:value={formData.expirationDateTime}
								class="w-full mt-1 px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-[#0b3a7a]"
								placeholder="MM/DD/YYYY HH:MM"
							/>
						</label>
						<p class="text-xs text-gray-600 mt-2">
							This alert will be auto-deactivated at the specified date/time above. Note: This will cause any
							already-scheduled notifications not to be sent after the expiration time.
						</p>
					</div>
				</div>
			</div>

			<!-- Footer with Save/Cancel -->
			<div class="border-t border-gray-200 px-6 py-4 flex justify-end gap-3 bg-gray-50">
				<button
					onclick={close}
					class="px-4 py-2 border border-gray-300 text-gray-700 rounded-lg hover:bg-gray-50 font-medium transition-colors"
				>
					Cancel
				</button>
				<button
					onclick={saveAlert}
					class="px-4 py-2 bg-green-600 hover:bg-green-700 text-white rounded-lg font-medium transition-colors"
				>
					Save
				</button>
			</div>
		</div>
	</div>
{/if}

<style>
	:global(.modal-open) {
		overflow: hidden;
	}
</style>
