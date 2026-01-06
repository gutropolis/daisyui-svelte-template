<script lang="ts">
	import { PROJECT_ANALYSIS_ROUTE, PROJECT_DETAIL_DASHBOARD_ROUTE } from "$lib/enums/routes";
	import { getStatusColor } from "$lib/utils/projecthelper";

	interface Project {
		id: string;
		code: string;
		title: string;
		phase: string;
		therapeuticArea: string;
		sponsor: string;
		status: 'development' | 'staging' | 'production';
		startDate: string;
		enrollmentProgress: {
			current: number;
			target: number;
		};
		milestones: Array<{
			name: string;
			completed: boolean;
		}>;
	}

	let projects: Project[] = [
		{
			id: '1',
			code: 'CT-2024-001',
			title: 'Novel Immunotherapy for Advanced Melanoma',
			phase: 'Phase II',
			therapeuticArea: 'Oncology',
			sponsor: 'BioPharma Inc.',
			status: 'production',
			startDate: '15/1/2024',
			enrollmentProgress: {
				current: 87,
				target: 150
			},
			milestones: [
				{ name: 'Protocol Finalization', completed: true },
				{ name: 'IRS Approval', completed: true },
				{ name: 'First Patient in', completed: true }
			]
		},
		{
			id: '2',
			code: 'CT-2024-002',
			title: 'Cardiovascular Outcomes Trial for SGLT2 Inhibitors',
			phase: 'Phase III',
			therapeuticArea: 'Cardiology',
			sponsor: 'MedTech Solutions',
			status: 'staging',
			startDate: '1/3/2024',
			enrollmentProgress: {
				current: 45,
				target: 300
			},
			milestones: [
				{ name: 'Site Selection', completed: true },
				{ name: 'Regulatory Submission', completed: true },
				{ name: 'Site Initiation', completed: false }
			]
		},
		{
			id: '3',
			code: 'CT-2024-003',
			title: 'Diabetes Management with Novel GLP-1 Agonist',
			phase: 'Phase II',
			therapeuticArea: 'Endocrinology',
			sponsor: 'Pharma Global LLC',
			status: 'production',
			startDate: '10/2/2024',
			enrollmentProgress: {
				current: 156,
				target: 200
			},
			milestones: [
				{ name: 'Protocol Finalization', completed: true },
				{ name: 'IRS Approval', completed: true },
				{ name: 'First Patient in', completed: true }
			]
		},
		{
			id: '4',
			code: 'CT-2024-004',
			title: 'Respiratory Disease Treatment Study',
			phase: 'Phase III',
			therapeuticArea: 'Pulmonology',
			sponsor: 'RespiraCare Inc.',
			status: 'staging',
			startDate: '5/1/2024',
			enrollmentProgress: {
				current: 203,
				target: 500
			},
			milestones: [
				{ name: 'Site Selection', completed: true },
				{ name: 'Regulatory Submission', completed: true },
				{ name: 'Site Initiation', completed: true }
			]
		},
		{
			id: '5',
			code: 'CT-2024-005',
			title: 'Alzheimer\'s Disease Cognitive Function Trial',
			phase: 'Phase II/III',
			therapeuticArea: 'Neurology',
			sponsor: 'NeuroTech Pharmaceuticals',
			status: 'production',
			startDate: '20/1/2024',
			enrollmentProgress: {
				current: 78,
				target: 120
			},
			milestones: [
				{ name: 'Protocol Finalization', completed: true },
				{ name: 'IRS Approval', completed: true },
				{ name: 'First Patient in', completed: true }
			]
		},
		{
			id: '6',
			code: 'CT-2024-006',
			title: 'Rheumatoid Arthritis Inflammation Study',
			phase: 'Phase III',
			therapeuticArea: 'Rheumatology',
			sponsor: 'ImmunoGen Solutions',
			status: 'production',
			startDate: '15/6/2023',
			enrollmentProgress: {
				current: 450,
				target: 450
			},
			milestones: [
				{ name: 'Protocol Finalization', completed: true },
				{ name: 'IRS Approval', completed: true },
				{ name: 'First Patient in', completed: true }
			]
		},
		{
			id: '7',
			code: 'CT-2024-007',
			title: 'Depression Treatment with New Antidepressant',
			phase: 'Phase II',
			therapeuticArea: 'Psychiatry',
			sponsor: 'MindCare Therapeutics',
			status: 'staging',
			startDate: '1/4/2024',
			enrollmentProgress: {
				current: 92,
				target: 250
			},
			milestones: [
				{ name: 'Site Selection', completed: true },
				{ name: 'Regulatory Submission', completed: false },
				{ name: 'Site Initiation', completed: false }
			]
		},
		{
			id: '8',
			code: 'CT-2024-008',
			title: 'Hepatitis C Viral Cure Study',
			phase: 'Phase III',
			therapeuticArea: 'Gastroenterology',
			sponsor: 'ViralCure Inc.',
			status: 'production',
			startDate: '8/3/2024',
			enrollmentProgress: {
				current: 134,
				target: 350
			},
			milestones: [
				{ name: 'Protocol Finalization', completed: true },
				{ name: 'IRS Approval', completed: true },
				{ name: 'First Patient in', completed: true }
			]
		},
		{
			id: '9',
			code: 'CT-2024-009',
			title: 'Cancer Immunotherapy Combination Trial',
			phase: 'Phase III',
			therapeuticArea: 'Oncology',
			sponsor: 'OncoBiotech Corp',
			status: 'development',
			startDate: '12/2/2024',
			enrollmentProgress: {
				current: 45,
				target: 300
			},
			milestones: [
				{ name: 'Protocol Finalization', completed: true },
				{ name: 'IRS Approval', completed: true },
				{ name: 'First Patient in', completed: false }
			]
		},
		{
			id: '10',
			code: 'CT-2024-010',
			title: 'Osteoporosis Prevention in Postmenopausal Women',
			phase: 'Phase II',
			therapeuticArea: 'Orthopedics',
			sponsor: 'BoneHealth Pharma',
			status: 'production',
			startDate: '5/2/2024',
			enrollmentProgress: {
				current: 178,
				target: 225
			},
			milestones: [
				{ name: 'Protocol Finalization', completed: true },
				{ name: 'IRS Approval', completed: true },
				{ name: 'First Patient in', completed: true }
			]
		},
		{
			id: '11',
			code: 'CT-2024-011',
			title: 'Migraine Prevention with Novel Monoclonal Antibody',
			phase: 'Phase III',
			therapeuticArea: 'Neurology',
			sponsor: 'NeuroShield Inc.',
			status: 'staging',
			startDate: '10/1/2024',
			enrollmentProgress: {
				current: 267,
				target: 400
			},
			milestones: [
				{ name: 'Site Selection', completed: true },
				{ name: 'Regulatory Submission', completed: true },
				{ name: 'Site Initiation', completed: true }
			]
		},
		{
			id: '12',
			code: 'CT-2024-012',
			title: 'Chronic Kidney Disease Management Protocol',
			phase: 'Phase II',
			therapeuticArea: 'Nephrology',
			sponsor: 'RenalCare Therapeutics',
			status: 'production',
			startDate: '18/3/2024',
			enrollmentProgress: {
				current: 123,
				target: 180
			},
			milestones: [
				{ name: 'Protocol Finalization', completed: true },
				{ name: 'IRS Approval', completed: true },
				{ name: 'First Patient in', completed: true }
			]
		}
	];

 

	const formatStatus = (s: string) => s.charAt(0).toUpperCase() + s.slice(1);

	const getEnrollmentPercentage = (current: number, target: number) => {
		return Math.round((current / target) * 100);
	};

	const getMilestoneProgress = (milestones: Array<{ name: string; completed: boolean }>) => {
		const completed = milestones.filter(m => m.completed).length;
		return `${completed}/${milestones.length}`;
	};

	// Summary counts for dashboard cards
	const totalProjects = projects.length;
	const productionCount = projects.filter(p => p.status === 'production').length;
	const stagingCount = projects.filter(p => p.status === 'staging').length;
	const developmentCount = projects.filter(p => p.status === 'development').length;
</script>

<div class="p-8 space-y-8">
	<!-- Header -->
	<div>
		<h1 class="text-4xl font-bold text-gray-800 mb-2">My Projects</h1>
		<p class="text-gray-600">View and manage your clinical research projects</p>
	</div>

	<!-- Summary Cards -->
		<!-- Stats Grid -->
	<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
		<div class="bg-white rounded-lg shadow p-6 border-l-4 border-blue-500">
			<div class="flex items-center justify-between">
				<div>
					<p class="text-gray-600 text-sm">Total Projects</p>
					<p class="text-3xl font-bold text-gray-800">{projects.length}</p>
				</div>
				<i class="fas fa-folder-open text-blue-500 text-4xl opacity-20"></i>
			</div>
		</div>

		<div class="bg-white rounded-lg shadow p-6 border-l-4 border-green-500">
			<div class="flex items-center justify-between">
				<div>
					<p class="text-gray-600 text-sm">Active</p>
					<p class="text-3xl font-bold text-gray-800">{projects.filter(p => p.status === 'Production').length}</p>
				</div>
				<i class="fas fa-check-circle text-green-500 text-4xl opacity-20"></i>
			</div>
		</div>

		<div class="bg-white rounded-lg shadow p-6 border-l-4 border-amber-500">
			<div class="flex items-center justify-between">
				<div>
					<p class="text-gray-600 text-sm">In Staging</p>
					<p class="text-3xl font-bold text-gray-800">{projects.filter(p => p.status === 'Staging').length}</p>
				</div>
				<i class="fas fa-hourglass-half text-amber-500 text-4xl opacity-20"></i>
			</div>
		</div>

		<div class="bg-white rounded-lg shadow p-6 border-l-4 border-purple-500">
			<div class="flex items-center justify-between">
				<div>
					<p class="text-gray-600 text-sm">Drafts</p>
					<p class="text-3xl font-bold text-gray-800">{projects.filter(p => p.status === 'Draft').length}</p>
				</div>
				<i class="fas fa-file text-purple-500 text-4xl opacity-20"></i>
			</div>
		</div>
	</div>

	<!-- Projects Grid -->
	<div class="grid grid-cols-2 gap-6">
		{#each projects as project (project.id)}
			<div class="bg-white rounded-lg shadow-md hover:shadow-lg transition-shadow border border-gray-200">
			<!-- Header with Status Badge and Action Icons -->
			<div class="p-6 border-b border-gray-200 flex items-start justify-between">
				<div class="flex-1">
					<h2 class="text-lg font-bold text-[#0b3a7a]">{project.code}</h2>
					<p class="text-sm text-gray-600 mt-1">{project.title}</p>
				</div>
				<div class="flex items-center gap-3">
					<div class="flex gap-1">
						<div class="relative group">
							<button class="p-2 rounded-lg hover:bg-gray-100 text-[#0b3a7a] transition-colors">
								<i class="fas fa-pen-square text-lg"></i>
							</button>
							<div class="absolute bottom-full left-1/2 transform -translate-x-1/2 mb-2 hidden group-hover:block bg-gray-800 text-white text-xs px-2 py-1 rounded whitespace-nowrap z-10">
								Edit Project
							</div>
						</div>
						<div class="relative group">
							<button class="p-2 rounded-lg hover:bg-gray-100 text-[#0b3a7a] transition-colors">
								<i class="fas fa-eye text-lg"></i>
							</button>
							<div class="absolute bottom-full left-1/2 transform -translate-x-1/2 mb-2 hidden group-hover:block bg-gray-800 text-white text-xs px-2 py-1 rounded whitespace-nowrap z-10">
								View Details
							</div>
						</div>
						<div class="relative group">
							<button class="p-2 rounded-lg hover:bg-gray-100 text-[#0b3a7a] transition-colors">
								<i class="fas fa-copy text-lg"></i>
							</button>
							<div class="absolute bottom-full left-1/2 transform -translate-x-1/2 mb-2 hidden group-hover:block bg-gray-800 text-white text-xs px-2 py-1 rounded whitespace-nowrap z-10">
								Duplicate Project
							</div>
						</div>
						<div class="relative group">
							<button class="p-2 rounded-lg hover:bg-red-50 text-red-500 transition-colors">
								<i class="fas fa-trash text-lg"></i>
							</button>
							<div class="absolute bottom-full left-1/2 transform -translate-x-1/2 mb-2 hidden group-hover:block bg-gray-800 text-white text-xs px-2 py-1 rounded whitespace-nowrap z-10">
								Remove Project
							</div>
						</div>
					</div>
					<span class="px-3 py-1 rounded-full text-xs font-semibold whitespace-nowrap {getStatusColor(project.status)}">
						{formatStatus(project.status)}
					</span>
				</div>
			</div>				<!-- Content -->
				<div class="p-6 space-y-6">
					<!-- Phase, Therapeutic Area, Sponsor & Start Date - 3 Column Layout -->
					<div class="grid grid-cols-3 gap-6">
						<div>
							<p class="text-xs font-semibold text-gray-500 uppercase tracking-wide">Phase</p>
							<p class="text-base font-bold text-[#0b3a7a] mt-1">{project.phase}</p>
						</div>
						<div>
							<p class="text-xs font-semibold text-gray-500 uppercase tracking-wide">Therapeutic Area</p>
							<p class="text-base font-bold text-[#0b3a7a] mt-1">{project.therapeuticArea}</p>
						</div>
						<div>
							<p class="text-xs font-semibold text-gray-500 uppercase tracking-wide">Sponsor</p>
							<p class="text-base font-bold text-[#0b3a7a] mt-1">{project.sponsor}</p>
						</div>
					</div>

					<!-- Started Date -->
					<div>
						<p class="text-xs font-semibold text-gray-500 uppercase tracking-wide">Started</p>
						<p class="text-base font-bold text-[#0b3a7a] mt-1">{project.startDate}</p>
					</div>

					<!-- Enrollment Progress -->
					<div>
						<div class="flex items-center justify-between mb-2">
							<p class="text-sm font-semibold text-gray-700">Enrollment Progress</p>
							<p class="text-sm font-bold text-gray-900">{project.enrollmentProgress.current}/{project.enrollmentProgress.target}</p>
						</div>
						<div class="w-full bg-gray-200 rounded-full h-2 overflow-hidden">
							<div
								class="bg-[#0b3a7a] h-full rounded-full transition-all duration-300"
								style="width: {getEnrollmentPercentage(project.enrollmentProgress.current, project.enrollmentProgress.target)}%"
							></div>
						</div>
					</div>

					<!-- Milestone Progress -->
					<div>
						<div class="flex items-center justify-between mb-3">
							<p class="text-sm font-semibold text-gray-700">Milestone Progress</p>
							<p class="text-sm font-bold text-gray-900">{getMilestoneProgress(project.milestones)}</p>
						</div>
						<div class="space-y-2">
							{#each project.milestones as milestone (milestone.name)}
								<div class="flex items-center gap-2">
									{#if milestone.completed}
										<div class="w-5 h-5 rounded-full bg-green-100 flex items-center justify-center flex-shrink-0">
											<i class="fas fa-check text-green-600 text-xs"></i>
										</div>
									{:else}
										<div class="w-5 h-5 rounded-full bg-gray-200 flex items-center justify-center flex-shrink-0">
											<i class="fas fa-circle text-gray-400 text-xs"></i>
										</div>
									{/if}
									<p class="text-sm text-gray-700">{milestone.name}</p>
								</div>
							{/each}
						</div>
					</div>
				</div>

			<!-- Action Buttons -->
			<div class="px-6 pb-6 pt-4 border-t border-gray-200 grid grid-cols-2 gap-3">
				<a href="{PROJECT_DETAIL_DASHBOARD_ROUTE}" class="px-4 py-2 border border-gray-300 text-gray-700 rounded-lg hover:bg-gray-50 font-medium transition-colors flex items-center justify-center gap-2 text-sm">
					<i class="fas fa-file-alt"></i>
					View Details
				</a>
				<a href="{PROJECT_ANALYSIS_ROUTE}" class="px-4 py-2 border border-gray-300 text-gray-700 rounded-lg hover:bg-gray-50 font-medium transition-colors flex items-center justify-center gap-2 text-sm">
					<i class="fas fa-chart-bar"></i>
					Analytics
				</a>
			</div>
			</div>
		{/each}
	</div>

	<!-- Empty State (optional) -->
	{#if projects.length === 0}
		<div class="text-center py-12">
			<i class="fas fa-inbox text-4xl text-gray-300 mb-4 block"></i>
			<p class="text-gray-600 font-medium">No projects found</p>
			<p class="text-gray-400 text-sm">You don't have any projects yet</p>
		</div>
	{/if}
</div>
