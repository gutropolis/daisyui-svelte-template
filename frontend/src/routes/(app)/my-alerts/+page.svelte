<script lang="ts">
	import { onMount } from 'svelte';
	import AlertNotificationModal from '$theme/alerts/AlertNotificationModal.svelte';

	interface Alert {
		id: number;
		name: string;
		trigger: string;
		triggerDescription: string;
		sendWhen: string;
		frequency: string;
		emailTo: string;
		subject: string;
		activity: string;
		status: 'active' | 'inactive' | 'draft';
		uniqueId: string;
	}

	interface Notification {
		id: number;
		alertName: string;
		recipient: string;
		subject: string;
		sentDate: string;
		status: 'sent' | 'failed' | 'pending';
		type: 'email' | 'sms' | 'in-app';
	}

	let activeTab = $state('my-alerts');
	let showDeactivated = $state(false);
	let searchQuery = $state('');
	let filterStatus = $state('all');
	let alertModalRef: any;

	let alerts = $state<Alert[]>([
		{
			id: 1,
			name: 'Alert #2: Day 1 - Morning',
			trigger: 'If the following logic is TRUE when the instrument "Send Notification Based on Date Field Value" is saved on any form status: [enrollment_date]>="" and [schedule_notification] = "1"',
			triggerDescription: '(only once, no re-trigger)',
			sendWhen: 'Schedule to send later: 1 days, 8 hours after [enrollment_date]',
			frequency: 'Send one time (only once per record - ie. never re-trigger)',
			emailTo: 'manual@arizona.edu',
			subject: 'Day 1 - Morning',
			activity: 'No alerts sent yet',
			status: 'active',
			uniqueId: 'A-12145'
		},
		{
			id: 2,
			name: 'Alert #2: Day 1 - Afternoon',
			trigger: 'If the following logic is TRUE when the instrument "Send Notification Based on Date Field Value" is saved on any form status: [enrollment_date]>="" and [schedule_notification] = "1"',
			triggerDescription: '(only once, no re-trigger)',
			sendWhen: 'Schedule to send later: 1 days, 14 hours after [enrollment_date]',
			frequency: 'Send one time (only once per record - ie. never re-trigger)',
			emailTo: 'manual@arizona.edu',
			subject: 'Day 1 - Afternoon',
			activity: 'No alerts sent yet',
			status: 'active',
			uniqueId: 'A-12147'
		},
		{
			id: 3,
			name: 'Alert #4: Day 1 - Evening',
			trigger: 'If the following logic is TRUE when the instrument "Send Notification Based on Date Field Value" is saved on any form status: [enrollment_date]>="" and [schedule_notification] = "1"',
			triggerDescription: '(only once, no re-trigger)',
			sendWhen: 'Schedule to send later: 1 days, 20 hours after [enrollment_date]',
			frequency: 'Send one time (only once per record - ie. never re-trigger)',
			emailTo: 'manual@arizona.edu',
			subject: 'Day 1 - Evening',
			activity: 'No alerts sent yet',
			status: 'active',
			uniqueId: 'A-12148'
		},
		{
			id: 4,
			name: 'Alert #5: Day 2 - Morning',
			trigger: 'If the following logic is TRUE when the instrument "Send Notification Based on Date Field Value" is saved on any form status: [enrollment_date]>="" and [schedule_notification] = "1"',
			triggerDescription: '(only once, no re-trigger)',
			sendWhen: 'Schedule to send later: 2 days, 8 hours after [enrollment_date]',
			frequency: 'Send one time (only once per record - ie. never re-trigger)',
			emailTo: 'manual@arizona.edu',
			subject: 'Day 2 - Morning',
			activity: 'No alerts sent yet',
			status: 'active',
			uniqueId: 'A-12149'
		}
	]);

	let notifications = $state<Notification[]>([
		{
			id: 1,
			alertName: 'Form Submission Alert',
			recipient: 'john@example.com',
			subject: 'Form submitted for Patient P001',
			sentDate: '2024-01-28 10:30 AM',
			status: 'sent',
			type: 'email'
		},
		{
			id: 2,
			alertName: 'Missing Data Alert',
			recipient: 'sarah@example.com',
			subject: 'Missing required fields in baseline visit',
			sentDate: '2024-01-28 09:15 AM',
			status: 'sent',
			type: 'email'
		},
		{
			id: 3,
			alertName: 'Status Change Alert',
			recipient: 'admin@example.com',
			subject: 'Record moved to completed',
			sentDate: '2024-01-27 02:00 PM',
			status: 'failed',
			type: 'email'
		},
		{
			id: 4,
			alertName: 'Form Submission Alert',
			recipient: 'john@example.com',
			subject: 'Form submitted for Patient P002',
			sentDate: '2024-01-27 11:45 AM',
			status: 'sent',
			type: 'email'
		},
		{
			id: 5,
			alertName: 'Missing Data Alert',
			recipient: 'sarah@example.com',
			subject: 'Missing required fields in follow-up visit',
			sentDate: '2024-01-26 03:30 PM',
			status: 'pending',
			type: 'email'
		}
	]);

	let filteredAlerts = $derived.by(() => {
		let result = alerts;

		if (!showDeactivated) {
			result = result.filter(a => a.status !== 'inactive');
		}

		if (filterStatus !== 'all') {
			result = result.filter(a => a.status === filterStatus);
		}

		if (searchQuery.trim()) {
			const query = searchQuery.toLowerCase();
			result = result.filter(
				a =>
					a.name.toLowerCase().includes(query) ||
					a.description.toLowerCase().includes(query)
			);
		}

		return result;
	});

	let filteredNotifications = $derived.by(() => {
		let result = notifications;

		if (searchQuery.trim()) {
			const query = searchQuery.toLowerCase();
			result = result.filter(
				n =>
					n.alertName.toLowerCase().includes(query) ||
					n.recipient.toLowerCase().includes(query) ||
					n.subject.toLowerCase().includes(query)
			);
		}

		return result;
	});

	const deleteAlert = (id: number) => {
		alerts = alerts.filter(a => a.id !== id);
	};

	const toggleAlertStatus = (id: number) => {
		const alert = alerts.find(a => a.id === id);
		if (alert) {
			alert.status = alert.status === 'active' ? 'inactive' : 'active';
		}
	};

	const getStatusBadgeColor = (status: string) => {
		switch (status) {
			case 'active':
				return 'bg-green-100 text-green-800';
			case 'inactive':
				return 'bg-gray-100 text-gray-800';
			case 'draft':
				return 'bg-yellow-100 text-yellow-800';
			case 'sent':
				return 'bg-green-100 text-green-800';
			case 'failed':
				return 'bg-red-100 text-red-800';
			case 'pending':
				return 'bg-blue-100 text-blue-800';
			default:
				return 'bg-gray-100 text-gray-800';
		}
	};
</script>

<div class="p-6 space-y-6 min-h-screen bg-gray-50">
	<!-- Header -->
	<div class="flex items-center justify-between">
		<div>
			<h1 class="text-3xl font-bold text-gray-800 mb-2">Alerts & Notifications</h1>
			<p class="text-gray-600 text-sm max-w-4xl leading-relaxed">
				The Alerts & Notifications feature allows you to construct alerts and send customized email notifications. These notifications may be sent to one or more recipients and can be triggered or scheduled when a form/survey is saved and/or based on conditional logic whenever data is saved or imported. When adding/editing an alert, you will need to 1) set how the alert gets triggered, 2) define when the notification should be sent (including how many times), and 3) specify the recipient, sender, message text, and other settings for the notification. For the message, you may utilize customized options such as rich text, the piping of field variables (including Smart Variables), and uploading multiple file attachments.
			</p>
			<a href="#" class="text-[#0b3a7a] hover:underline text-sm mt-2 inline-block">Learn more</a>
		</div>
	</div>

	<!-- Tabs -->
	<div class="flex gap-1 border-b border-gray-200">
		<button
			onclick={() => (activeTab = 'my-alerts')}
			class="px-4 py-3 font-medium text-sm border-b-2 transition-all {activeTab === 'my-alerts'
				? 'border-[#0b3a7a] text-[#0b3a7a]'
				: 'border-transparent text-gray-600 hover:text-[#0b3a7a]'}"
		>
			<i class="fas fa-bell mr-2"></i>My Alerts
		</button>
		<button
			onclick={() => (activeTab = 'notification-log')}
			class="px-4 py-3 font-medium text-sm border-b-2 transition-all {activeTab === 'notification-log'
				? 'border-[#0b3a7a] text-[#0b3a7a]'
				: 'border-transparent text-gray-600 hover:text-[#0b3a7a]'}"
		>
			<i class="fas fa-history mr-2"></i>Notification Log
		</button>
	</div>

	<!-- My Alerts Tab -->
	{#if activeTab === 'my-alerts'}
		<div class="space-y-6">
			<!-- Controls -->
			<div class="flex justify-between items-center">
				<button
					onclick={() => alertModalRef.open()}
					class="bg-[#0b3a7a] hover:bg-[#082654] text-white font-medium py-2 px-4 rounded-lg flex items-center gap-2 transition-colors shadow"
				>
					<i class="fas fa-plus"></i>Add New Alert
				</button>
				<div class="flex items-center gap-4">
					<label class="flex items-center gap-2 cursor-pointer">
						<input
							type="checkbox"
							bind:checked={showDeactivated}
							class="w-4 h-4 rounded border-gray-300"
						/>
						<span class="text-sm text-gray-700">Show deactivated</span>
					</label>
					<input
						type="text"
						placeholder="Search alerts..."
						bind:value={searchQuery}
						class="px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-[#0b3a7a] w-48"
					/>
				</div>
			</div>

			<!-- Alerts List -->
			{#if filteredAlerts.length > 0}
				<div class="space-y-4">
					{#each filteredAlerts as alert (alert.id)}
						<div class="bg-white rounded-lg shadow-sm border border-gray-200 overflow-hidden hover:shadow-md transition-shadow">
							<!-- Alert Header -->
							<div class="bg-gradient-to-r from-[#0b3a7a] to-[#0d5fa0] text-white px-6 py-4 flex items-center justify-between">
								<div class="flex items-center gap-3">
									<div class="flex-1">
										<h3 class="font-semibold text-lg">{alert.name}</h3>
										<p class="text-xs text-white/70">ID: {alert.uniqueId}</p>
									</div>
								</div>
								<div class="flex items-center gap-1">
									<button
										title="Edit alert"
										class="p-2 rounded hover:bg-white/20 transition-colors"
									>
										<i class="fas fa-edit"></i>
									</button>
									<button
										title="Options"
										class="p-2 rounded hover:bg-white/20 transition-colors"
									>
										<i class="fas fa-ellipsis-v"></i>
									</button>
								</div>
							</div>

							<!-- Alert Details -->
							<div class="px-6 py-4 space-y-4">
								<!-- Trigger -->
								<div>
									<p class="text-xs font-semibold text-gray-500 uppercase tracking-wide mb-2">Trigger</p>
									<p class="text-sm text-gray-700 leading-relaxed">{alert.trigger}</p>
									<p class="text-xs text-gray-500 mt-1">{alert.triggerDescription}</p>
								</div>

								<!-- Schedule and Email in two columns -->
								<div class="grid grid-cols-2 gap-6">
									<div>
										<p class="text-xs font-semibold text-gray-500 uppercase tracking-wide mb-2">Schedule</p>
										<p class="text-sm text-gray-700">{alert.sendWhen}</p>
										<p class="text-xs text-gray-500 mt-2">{alert.frequency}</p>
									</div>

									<div>
										<p class="text-xs font-semibold text-gray-500 uppercase tracking-wide mb-2">Email Configuration</p>
										<div class="text-sm space-y-1 text-gray-700">
											<p><span class="font-medium">To:</span> {alert.emailTo}</p>
											<p><span class="font-medium">Subject:</span> {alert.subject}</p>
										</div>
									</div>
								</div>

								<!-- Activity -->
								<div class="pt-2 border-t border-gray-200">
									<p class="text-xs text-gray-500"><i class="fas fa-history mr-1"></i>{alert.activity}</p>
								</div>
							</div>

							<!-- Alert Status and Actions -->
							<div class="bg-gray-50 px-6 py-3 flex items-center justify-between border-t border-gray-200">
								<div>
									<span class="inline-block px-3 py-1 rounded-full text-xs font-semibold {getStatusBadgeColor(alert.status)}">
										{alert.status.charAt(0).toUpperCase() + alert.status.slice(1)}
									</span>
								</div>
								<div class="flex items-center gap-2">
									<button
										onclick={() => toggleAlertStatus(alert.id)}
										title={alert.status === 'active' ? 'Deactivate' : 'Activate'}
										class="px-3 py-1 rounded text-xs font-medium transition-colors {alert.status === 'active'
											? 'bg-yellow-100 text-yellow-800 hover:bg-yellow-200'
											: 'bg-blue-100 text-blue-800 hover:bg-blue-200'}"
									>
										<i class="fas fa-power-off mr-1"></i>{alert.status === 'active' ? 'Deactivate' : 'Activate'}
									</button>
									<button
										title="Copy alert"
										class="px-3 py-1 rounded text-xs font-medium bg-gray-200 text-gray-800 hover:bg-gray-300 transition-colors"
									>
										<i class="fas fa-copy mr-1"></i>Copy
									</button>
									<button
										onclick={() => deleteAlert(alert.id)}
										title="Delete alert"
										class="px-3 py-1 rounded text-xs font-medium bg-red-100 text-red-800 hover:bg-red-200 transition-colors"
									>
										<i class="fas fa-trash mr-1"></i>Delete
									</button>
								</div>
							</div>
						</div>
					{/each}
				</div>
			{:else}
				<div class="bg-white rounded-lg shadow p-12 text-center">
					<i class="fas fa-inbox text-4xl text-gray-300 mb-4 block"></i>
					<p class="text-gray-500 text-lg">No alerts found</p>
				</div>
			{/if}
		</div>
	{/if}

	<!-- Notification Log Tab -->
	{#if activeTab === 'notification-log'}
		<div class="space-y-6">
			<!-- Controls -->
			<div class="flex justify-between items-center">
				<div class="text-sm text-gray-600">
					Showing <span class="font-semibold text-gray-800">{filteredNotifications.length}</span> notification
					{filteredNotifications.length === 1 ? 'record' : 'records'}
				</div>
				<div class="flex items-center gap-4">
					<select
						bind:value={filterStatus}
						class="px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-[#0b3a7a] text-sm"
					>
						<option value="all">All Status</option>
						<option value="sent">Sent</option>
						<option value="pending">Pending</option>
						<option value="failed">Failed</option>
					</select>
					<input
						type="text"
						placeholder="Search notifications..."
						bind:value={searchQuery}
						class="px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-[#0b3a7a] w-48"
					/>
				</div>
			</div>

			<!-- Notifications Table -->
			{#if filteredNotifications.length > 0}
				<div class="bg-white rounded-lg shadow-sm border border-gray-200 overflow-hidden">
					<table class="w-full">
						<thead class="bg-gray-50 border-b border-gray-200">
							<tr>
								<th class="px-6 py-3 text-left text-xs font-semibold text-gray-700 uppercase tracking-wide">Alert Name</th>
								<th class="px-6 py-3 text-left text-xs font-semibold text-gray-700 uppercase tracking-wide">Recipient</th>
								<th class="px-6 py-3 text-left text-xs font-semibold text-gray-700 uppercase tracking-wide">Subject</th>
								<th class="px-6 py-3 text-left text-xs font-semibold text-gray-700 uppercase tracking-wide">Sent Date/Time</th>
								<th class="px-6 py-3 text-left text-xs font-semibold text-gray-700 uppercase tracking-wide">Status</th>
								<th class="px-6 py-3 text-right text-xs font-semibold text-gray-700 uppercase tracking-wide">Actions</th>
							</tr>
						</thead>
						<tbody>
							{#each filteredNotifications as notification (notification.id)}
								<tr class="border-b border-gray-200 hover:bg-gray-50 transition-colors">
									<td class="px-6 py-4 font-medium text-gray-900">{notification.alertName}</td>
									<td class="px-6 py-4 text-sm text-gray-600">{notification.recipient}</td>
									<td class="px-6 py-4 text-sm text-gray-600">{notification.subject}</td>
									<td class="px-6 py-4 text-sm text-gray-600">{notification.sentDate}</td>
									<td class="px-6 py-4">
										<span class="inline-block px-3 py-1 rounded-full text-xs font-semibold {getStatusBadgeColor(notification.status)}">
											{notification.status.charAt(0).toUpperCase() + notification.status.slice(1)}
										</span>
									</td>
									<td class="px-6 py-4 text-right">
										<div class="flex justify-end gap-2">
											<button
												title="View notification"
												class="p-2 rounded hover:bg-[#0b3a7a]/10 text-[#0b3a7a] transition-colors"
											>
												<i class="fas fa-eye"></i>
											</button>
											<button
												title="Retry sending"
												class="p-2 rounded hover:bg-yellow-50 text-yellow-600 transition-colors"
											>
												<i class="fas fa-redo"></i>
											</button>
										</div>
									</td>
								</tr>
							{/each}
						</tbody>
					</table>
				</div>
			{:else}
				<div class="bg-white rounded-lg shadow p-12 text-center">
					<i class="fas fa-inbox text-4xl text-gray-300 mb-4 block"></i>
					<p class="text-gray-500 text-lg">No notifications found</p>
				</div>
			{/if}
		</div>
	{/if}
</div>

<!-- Alert Notification Modal -->
<AlertNotificationModal bind:this={alertModalRef} />

<style>
	:global(body) {
		font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen', 'Ubuntu',
			'Cantarell', 'Fira Sans', 'Droid Sans', 'Helvetica Neue', sans-serif;
	}
</style>
