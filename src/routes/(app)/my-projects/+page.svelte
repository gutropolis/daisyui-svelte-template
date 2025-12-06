<script lang="ts">
	interface Milestone {
		label: string;
		done: boolean;
	}

	interface Project {
		id: string;
		code: string;
		title: string;
		status: 'Production' | 'Staging' | 'Draft';
		subtitle: string;
		phase: string;
		area: string;
		sponsor: string;
		started: string;
		enrolled: number;
		target: number;
		milestones: Milestone[];
	}

	let searchQuery = '';
	let selectedStatus: 'all' | 'Production' | 'Staging' | 'Draft' = 'all';

	const stats = [
		{ label: 'Total Projects', value: 12, accent: 'blue-500', icon: '📁' },
		{ label: 'Active', value: 0, accent: 'green-500', icon: '✅' },
		{ label: 'In Staging', value: 0, accent: 'orange-400', icon: '⏳' },
		{ label: 'Drafts', value: 0, accent: 'purple-500', icon: '📝' }
	];

	const projects: Project[] = [
		{
			id: '1',
			code: 'CT-2024-001',
			title: 'Novel Immunotherapy for Advanced Melanoma',
			status: 'Production',
			subtitle: 'Novel Immunotherapy for Advanced Melanoma',
			phase: 'Phase II',
			area: 'Oncology',
			sponsor: 'BioPharma Inc.',
			started: '15/1/2024',
			enrolled: 87,
			target: 150,
			milestones: [
				{ label: 'Protocol Finalization', done: true },
				{ label: 'IRS Approval', done: true },
				{ label: 'First Patient in', done: true }
			]
		},
		{
			id: '2',
			code: 'CT-2024-002',
			title: 'Cardiovascular Outcomes Trial for SGLT2 Inhibitors',
			status: 'Staging',
			subtitle: 'Cardiovascular Outcomes Trial for SGLT2 Inhibitors',
			phase: 'Phase III',
			area: 'Cardiology',
			sponsor: 'MedTech Solutions',
			started: '1/3/2024',
			enrolled: 45,
			target: 300,
			milestones: [
				{ label: 'Site Selection', done: true },
				{ label: 'Regulatory Submission', done: true },
				{ label: 'Site Initiation', done: false }
			]
		}
	];

	const statusStyles = {
		Production: 'bg-green-50 text-green-700',
		Staging: 'bg-amber-50 text-amber-700',
		Draft: 'bg-purple-50 text-purple-700'
	};

	$: filteredProjects = projects.filter((project) => {
		const query = searchQuery.trim().toLowerCase();
		const matchesSearch =
			project.title.toLowerCase().includes(query) || project.code.toLowerCase().includes(query);
		const matchesStatus = selectedStatus === 'all' || project.status === selectedStatus;
		return matchesSearch && matchesStatus;
	});
</script>

<div class="min-h-screen bg-slate-50 py-10">
	<div class="space-y-6 w-full">
		<section class="w-full rounded-3xl bg-white p-6 shadow-xl">
			<header class="mb-6 flex flex-col gap-2 md:flex-row md:items-center md:justify-between">
				<div>
					<h1 class="text-3xl font-semibold text-slate-900">My Projects</h1>
					<p class="text-sm text-slate-500">View and manage your clinical research projects</p>
				</div>
				<a
					href="/project/new"
					class="btn btn-primary rounded-full px-5 py-2.5 text-sm font-semibold"
				>
					Create New Project
				</a>
			</header>

			<!-- Filters -->
			<div class="mb-6 grid gap-4 md:grid-cols-2">
				<input
					type="text"
					placeholder="Search projects or codes"
					class="input input-bordered w-full rounded-2xl border-slate-200 bg-white px-4 py-3 shadow-sm focus:ring-2 focus:ring-slate-200"
					bind:value={searchQuery}
				/>
				<select
					class="select select-bordered w-full rounded-2xl border-slate-200 bg-white px-4 py-3 shadow-sm focus:ring-2 focus:ring-slate-200"
					bind:value={selectedStatus}
				>
					<option value="all">All Status</option>
					<option value="Production">Production</option>
					<option value="Staging">Staging</option>
					<option value="Draft">Draft</option>
				</select>
			</div>

			<!-- Stats cards -->
			<div class="grid grid-cols-1 gap-4 md:grid-cols-2 lg:grid-cols-4">
				{#each stats as stat}
					<div
						class="relative overflow-hidden rounded-2xl border border-slate-100 bg-white p-5 shadow-sm"
					>
						<span class={`absolute inset-y-0 left-0 w-1 bg-${stat.accent}`}></span>
						<div class="flex items-center justify-between gap-4">
							<div>
								<p class="text-xs uppercase tracking-[0.2em] text-slate-500">{stat.label}</p>
								<p class="text-3xl font-bold text-slate-900">{stat.value}</p>
							</div>
							<div class="text-3xl opacity-70">{stat.icon}</div>
						</div>
					</div>
				{/each}
			</div>
		</section>

		<section class="w-full space-y-6 rounded-3xl bg-white p-6 shadow-xl">
			<div class="grid grid-cols-1 gap-6 lg:grid-cols-2">
				{#each filteredProjects as project}
					<article class="rounded-2xl border border-slate-100 bg-slate-50 shadow-sm">
						<div class="flex items-start justify-between gap-4 border-b border-slate-100 p-5">
							<div>
								<p class="text-xs uppercase tracking-[0.3em] text-slate-400">{project.code}</p>
								<h2 class="text-lg font-semibold text-slate-900">{project.title}</h2>
								<p class="text-sm text-slate-500">{project.subtitle}</p>
							</div>
							<div class="flex items-center gap-3 text-slate-500">
								<button
									class="rounded-full border border-slate-200 bg-white p-2 text-sm text-slate-500 shadow-sm transition hover:border-slate-300"
								>
									<span class="sr-only">Edit project</span>
									<svg
										xmlns="http://www.w3.org/2000/svg"
										class="h-4 w-4"
										fill="none"
										viewBox="0 0 24 24"
										stroke="currentColor"
									>
										<path
											stroke-linecap="round"
											stroke-linejoin="round"
											stroke-width="1.5"
											d="M11 5h6m-6 4h6m-6 4h4"
										/>
									</svg>
								</button>
								<button
									class="rounded-full border border-slate-200 bg-white p-2 text-sm text-slate-500 shadow-sm transition hover:border-slate-300"
								>
									<span class="sr-only">View project</span>
									<svg
										xmlns="http://www.w3.org/2000/svg"
										class="h-4 w-4"
										fill="none"
										viewBox="0 0 24 24"
										stroke="currentColor"
									>
										<circle cx="12" cy="12" r="3" />
										<path
											stroke-linecap="round"
											stroke-linejoin="round"
											stroke-width="1.5"
											d="M21 12c0-4.8-4.6-8-9-8s-9 3.2-9 8c0 4.8 4.6 8 9 8s9-3.2 9-8z"
										/>
									</svg>
								</button>
								<button
									class="rounded-full border border-slate-200 bg-white p-2 text-sm text-slate-500 shadow-sm transition hover:border-slate-300"
								>
									<span class="sr-only">Copy link</span>
									<svg
										xmlns="http://www.w3.org/2000/svg"
										class="h-4 w-4"
										fill="none"
										viewBox="0 0 24 24"
										stroke="currentColor"
									>
										<rect x="9" y="9" width="6" height="6" rx="1" />
										<path
											stroke-linecap="round"
											stroke-linejoin="round"
											stroke-width="1.5"
											d="M4 4h4v4m6 6h4v4"
										/>
									</svg>
								</button>
								<span
									class={`rounded-full px-3 py-1 text-xs font-semibold ${statusStyles[project.status]}`}
								>
									{project.status}
								</span>
							</div>
						</div>

						<div class="grid gap-4 px-5 pb-5 text-sm text-slate-500 md:grid-cols-3">
							<div>
								<p class="text-xs uppercase tracking-[0.3em] text-slate-400">Phase</p>
								<p class="text-base font-semibold text-slate-900">{project.phase}</p>
							</div>
							<div>
								<p class="text-xs uppercase tracking-[0.3em] text-slate-400">Therapeutic Area</p>
								<p class="text-base font-semibold text-slate-900">{project.area}</p>
							</div>
							<div>
								<p class="text-xs uppercase tracking-[0.3em] text-slate-400">Sponsor</p>
								<p class="text-base font-semibold text-slate-900">{project.sponsor}</p>
							</div>
						</div>

						<div class="space-y-4 border-t border-slate-100 px-5 pb-5">
							<div
								class="flex items-center justify-between text-xs uppercase tracking-[0.3em] text-slate-400"
							>
								<span>Date Started</span>
								<span>{project.started}</span>
							</div>
							<div class="space-y-2">
								<div class="flex items-center justify-between text-sm font-semibold text-slate-900">
									<span>Enrollment Progress</span>
									<span>{project.enrolled}/{project.target}</span>
								</div>
								<div class="h-2 overflow-hidden rounded-full bg-slate-200">
									<div
										class="h-full rounded-full bg-gradient-to-r from-slate-900 to-indigo-600"
										style={`width: ${(project.enrolled / project.target) * 100}%`}
									></div>
								</div>
							</div>

							<div>
								<p class="text-xs uppercase tracking-[0.3em] text-slate-400">Milestone Progress</p>
								<ul class="mt-2 space-y-2 text-sm text-slate-600">
									{#each project.milestones as milestone}
										<li class="flex items-start gap-2">
											<span
												class={`mt-1 h-3 w-3 rounded-full ${milestone.done ? 'bg-green-400' : 'bg-slate-300'}`}
											></span>
											<span class={`${milestone.done ? 'text-slate-900' : 'text-slate-500'}`}>
												{milestone.label}
											</span>
										</li>
									{/each}
								</ul>
							</div>
						</div>

						<div class="flex gap-3 border-t border-slate-100 p-5">
							<button
								class="flex-1 rounded-2xl border border-slate-200 bg-white py-2 text-sm font-semibold text-slate-700 shadow-sm transition hover:border-slate-300"
							>
								View Details
							</button>
							<button
								class="flex-1 rounded-2xl border border-slate-200 bg-white py-2 text-sm font-semibold text-slate-700 shadow-sm transition hover:border-slate-300"
							>
								Analytics
							</button>
						</div>
					</article>
				{/each}
			</div>

			{#if filteredProjects.length === 0}
				<div
					class="rounded-2xl border border-dashed border-slate-200 bg-white/60 p-6 text-center text-sm text-slate-500"
				>
					No projects match that query yet.
				</div>
			{/if}
		</section>
	</div>
</div>
