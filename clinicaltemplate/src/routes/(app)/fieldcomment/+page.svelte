<script lang="ts">
	interface FieldComment {
		id: number;
		record: string;
		field: string;
		fieldLabel: string;
		comments: string;
		user: string;
		timestamp: string;
		eventName?: string;
	}

	let activeTab = $state('field-comment-log');
	let searchQuery = $state('');
	let filterRecord = $state('all');
	let filterField = $state('all');
	let filterUser = $state('all');
	let filterDataAccessGroup = $state('all');
	let keywordSearch = $state('');

	let fieldComments = $state<FieldComment[]>([
		{
			id: 1,
			record: '1',
			field: 'first_name',
			fieldLabel: 'First Name',
			comments: 'brunettq (03/16/2016 10:32am): "Entered the first name of participant - Participant goes by middle na...',
			user: 'brunettq',
			timestamp: '03/16/2016 10:32am',
			eventName: 'Baseline'
		},
		{
			id: 2,
			record: '2',
			field: 'age',
			fieldLabel: 'Age',
			comments: 'johndoe (01/20/2024 02:15pm): "Age appears to be a data entry error. Need verification...',
			user: 'johndoe',
			timestamp: '01/20/2024 02:15pm',
			eventName: 'Baseline'
		},
		{
			id: 3,
			record: '3',
			field: 'consent_date',
			fieldLabel: 'Consent Date',
			comments: 'sarahm (01/19/2024 11:45am): "Consent obtained and documented...',
			user: 'sarahm',
			timestamp: '01/19/2024 11:45am',
			eventName: 'Day 1'
		},
		{
			id: 4,
			record: '1',
			field: 'vital_signs',
			fieldLabel: 'Vital Signs',
			comments: 'admin (01/18/2024 09:30am): "Blood pressure reading validated...',
			user: 'admin',
			timestamp: '01/18/2024 09:30am',
			eventName: 'Follow-up'
		},
		{
			id: 5,
			record: '4',
			field: 'medication_list',
			fieldLabel: 'Medication List',
			comments: 'nurse_bob (01/17/2024 03:20pm): "Updated medication list based on patient report...',
			user: 'nurse_bob',
			timestamp: '01/17/2024 03:20pm',
			eventName: 'Day 2'
		}
	]);

	let filteredComments = $derived.by(() => {
		let result = fieldComments;

		if (filterRecord !== 'all') {
			result = result.filter(c => c.record === filterRecord);
		}

		if (filterField !== 'all') {
			result = result.filter(c => c.field === filterField);
		}

		if (filterUser !== 'all') {
			result = result.filter(c => c.user === filterUser);
		}

		if (keywordSearch.trim()) {
			const query = keywordSearch.toLowerCase();
			result = result.filter(
				c =>
					c.comments.toLowerCase().includes(query) ||
					c.fieldLabel.toLowerCase().includes(query) ||
					c.record.toLowerCase().includes(query)
			);
		}

		return result;
	});

	const uniqueRecords = $derived(Array.from(new Set(fieldComments.map(c => c.record))));
	const uniqueFields = $derived(Array.from(new Set(fieldComments.map(c => c.field))));
	const uniqueUsers = $derived(Array.from(new Set(fieldComments.map(c => c.user))));

	const exportLog = () => {
		const csv = [
			['Record', 'Field', 'Comments', 'User', 'Timestamp'],
			...filteredComments.map(c => [c.record, c.fieldLabel, c.comments, c.user, c.timestamp])
		]
			.map(row => row.map(cell => `"${cell}"`).join(','))
			.join('\n');

		const blob = new Blob([csv], { type: 'text/csv' });
		const url = URL.createObjectURL(blob);
		const a = document.createElement('a');
		a.href = url;
		a.download = 'field-comment-log.csv';
		a.click();
		URL.revokeObjectURL(url);
	};

	const resetFilters = () => {
		filterRecord = 'all';
		filterField = 'all';
		filterUser = 'all';
		filterDataAccessGroup = 'all';
		keywordSearch = '';
	};

	const viewCommentDetail = (comment: FieldComment) => {
		console.log('View comment:', comment);
	};
</script>

<div class="p-6 space-y-6 min-h-screen bg-gray-50">
	<!-- Header -->
	<div class="flex items-start justify-between">
		<div>
			<h1 class="text-3xl font-bold text-gray-800 mb-2">Field Comment Log</h1>
			<p class="text-gray-600 text-sm max-w-4xl leading-relaxed">
				This page displays the Field Comment Log for all records/events/fields in this project. You may use the controls below to perform keyword searches in the comments as well as filter the comments by record, event, field, or data access group. Keep in mind that if you do not have user privileges to view some data collection instruments, then comments for any fields on those instruments will not be displayed in the table. Also, if you belong to a data access group, then you will only see results for records that belong to your group. The entire Field Comment Log is downloadable as a file in Excel/CSV format.
			</p>
		</div>
	</div>

	<!-- Filters Section -->
	<div class="bg-white rounded-lg shadow-sm border border-gray-200 p-6">
		<h2 class="text-lg font-semibold text-gray-800 mb-4">Filters</h2>

		<div class="grid grid-cols-2 md:grid-cols-4 gap-4 mb-4">
			<!-- Records Filter -->
			<div>
				<label class="block text-sm font-medium text-gray-700 mb-2">All records</label>
				<select
					bind:value={filterRecord}
					class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-[#0b3a7a] text-sm"
				>
					<option value="all">All records</option>
					{#each uniqueRecords as record}
						<option value={record}>Record {record}</option>
					{/each}
				</select>
			</div>

			<!-- Fields Filter -->
			<div>
				<label class="block text-sm font-medium text-gray-700 mb-2">All fields</label>
				<select
					bind:value={filterField}
					class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-[#0b3a7a] text-sm"
				>
					<option value="all">All fields</option>
					{#each uniqueFields as field}
						<option value={field}>{field}</option>
					{/each}
				</select>
			</div>

			<!-- Users Filter -->
			<div>
				<label class="block text-sm font-medium text-gray-700 mb-2">All users</label>
				<select
					bind:value={filterUser}
					class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-[#0b3a7a] text-sm"
				>
					<option value="all">All users</option>
					{#each uniqueUsers as user}
						<option value={user}>{user}</option>
					{/each}
				</select>
			</div>

			<!-- Data Access Group Filter -->
			<div>
				<label class="block text-sm font-medium text-gray-700 mb-2">Data access groups</label>
				<select
					bind:value={filterDataAccessGroup}
					class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-[#0b3a7a] text-sm"
				>
					<option value="all">All data access groups</option>
					<option value="group1">Group 1</option>
					<option value="group2">Group 2</option>
				</select>
			</div>
		</div>

		<!-- Keyword Search -->
		<div class="mb-4">
			<label class="block text-sm font-medium text-gray-700 mb-2">Keyword search</label>
			<input
				type="text"
				placeholder="Search in comments..."
				bind:value={keywordSearch}
				class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-[#0b3a7a] text-sm"
			/>
		</div>

		<!-- Action Buttons -->
		<div class="flex gap-2">
			<button
				onclick={resetFilters}
				class="px-4 py-2 border border-gray-300 text-gray-700 rounded-lg hover:bg-gray-50 transition-colors font-medium text-sm"
			>
				Reset
			</button>
			<a href="#" class="text-[#0b3a7a] hover:underline text-sm py-2">Search tips</a>
		</div>
	</div>

	<!-- Results Section -->
	<div class="bg-white rounded-lg shadow-sm border border-gray-200 overflow-hidden">
		<!-- Results Header -->
		<div class="bg-gray-50 px-6 py-4 border-b border-gray-200 flex items-center justify-between">
			<div>
				<p class="text-sm font-semibold text-gray-800">
					Results returned: <span class="text-[#0b3a7a]">{filteredComments.length}</span>
				</p>
			</div>
			<button
				onclick={exportLog}
				class="px-4 py-2 bg-green-100 text-green-800 rounded-lg hover:bg-green-200 transition-colors font-medium text-sm flex items-center gap-2"
			>
				<i class="fas fa-download"></i>Export entire log
			</button>
		</div>

		<!-- Comments Table -->
		{#if filteredComments.length > 0}
			<div class="overflow-x-auto">
				<table class="w-full">
					<thead class="bg-gray-50 border-b border-gray-200">
						<tr>
							<th class="px-6 py-3 text-left text-xs font-semibold text-gray-700 uppercase tracking-wide">Record</th>
							<th class="px-6 py-3 text-left text-xs font-semibold text-gray-700 uppercase tracking-wide">Field</th>
							<th class="px-6 py-3 text-left text-xs font-semibold text-gray-700 uppercase tracking-wide">Comments</th>
							<th class="px-6 py-3 text-right text-xs font-semibold text-gray-700 uppercase tracking-wide">Actions</th>
						</tr>
					</thead>
					<tbody>
						{#each filteredComments as comment (comment.id)}
							<tr class="border-b border-gray-200 hover:bg-gray-50 transition-colors">
								<td class="px-6 py-4 text-sm font-medium text-gray-900">{comment.record}</td>
								<td class="px-6 py-4 text-sm text-gray-600">
									<div class="font-medium">{comment.field}</div>
									<div class="text-xs text-gray-500">({comment.fieldLabel})</div>
								</td>
								<td class="px-6 py-4 text-sm text-gray-700">
									<p class="line-clamp-2">{comment.comments}</p>
									<p class="text-xs text-gray-500 mt-1">{comment.user} - {comment.timestamp}</p>
								</td>
								<td class="px-6 py-4 text-right">
									<button
										onclick={() => viewCommentDetail(comment)}
										class="inline-flex items-center gap-2 px-3 py-1 rounded text-sm font-medium text-[#0b3a7a] bg-blue-50 hover:bg-blue-100 transition-colors"
									>
										<i class="fas fa-comment"></i>
										<span>{comment.comments.split('\n').length} comment</span>
									</button>
								</td>
							</tr>
						{/each}
					</tbody>
				</table>
			</div>
		{:else}
			<div class="p-12 text-center">
				<i class="fas fa-inbox text-4xl text-gray-300 mb-4 block"></i>
				<p class="text-gray-500 text-lg">No field comments found</p>
			</div>
		{/if}
	</div>
</div>

<style>
	:global(body) {
		font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen', 'Ubuntu',
			'Cantarell', 'Fira Sans', 'Droid Sans', 'Helvetica Neue', sans-serif;
	}
</style>
