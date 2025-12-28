<script lang="ts">
	import { onMount } from 'svelte';
	import { goto } from '$app/navigation';
	import { graphqlClient } from '$lib/graphql/client';
	import { LIST_PROJECTS_QUERY, DELETE_PROJECT_MUTATION } from '$lib/graphql/operations';
	import { authStore } from '$lib/stores/auth';

	type Project = {
		id: number;
		ownerId: number;
		creatorId: number;
		name: string;
		code?: string | null;
		description?: string | null;
		sponsor?: string | null;
		createdAt: string;
		updatedAt: string;
	};

	let projects: Project[] = [];
	let page = 1;
	const limit = 10;
	let total = 0;
	let totalPages = 0;
	let hasNext = false;
	let hasPrev = false;
	let loading = false;
	let error: string | null = null;
	let ownerPrefilled = false;

	let filters = {
		name: '',
		code: '',
		sponsor: '',
		ownerId: ''
	};

	const resetFilters = () => {
		filters = {
			name: '',
			code: '',
			sponsor: '',
			ownerId: filters.ownerId ? filters.ownerId : ''
		};
		page = 1;
		loadProjects();
	};

	async function loadProjects() {
		loading = true;
		error = null;
		const filterPayload: Record<string, unknown> = {};

		if (filters.name.trim()) {
			filterPayload.name = filters.name.trim();
		}
		if (filters.code.trim()) {
			filterPayload.code = filters.code.trim();
		}
		if (filters.sponsor.trim()) {
			filterPayload.sponsor = filters.sponsor.trim();
		}
		if (filters.ownerId.trim()) {
			const ownerValue = Number(filters.ownerId);
			if (!Number.isNaN(ownerValue)) {
				filterPayload.ownerId = ownerValue;
			}
		}

		try {
			const response = await graphqlClient.request(LIST_PROJECTS_QUERY, {
				page,
				limit,
				filters: Object.keys(filterPayload).length ? filterPayload : null
			});
			const payload = response.projects;
			projects = payload.items ?? [];
			total = payload.total;
			totalPages = payload.totalPages;
			hasNext = payload.hasNext;
			hasPrev = payload.hasPrev;
		} catch (err) {
			error = err instanceof Error ? err.message : 'Unable to load projects';
		} finally {
			loading = false;
		}
	}

	async function deleteProject(id: number) {
		if (!confirm('Delete this project permanently?')) return;
		try {
			loading = true;
			await graphqlClient.request(DELETE_PROJECT_MUTATION, { id });
			await loadProjects();
		} catch (err) {
			error = err instanceof Error ? err.message : 'Failed to delete project';
		} finally {
			loading = false;
		}
	}

	function goToAdd() {
		goto('/admin/project/add');
	}

	function goToEdit(id: number) {
		goto(`/admin/project/edit?id=${id}`);
	}

	function prevPage() {
		if (!hasPrev) return;
		page = Math.max(1, page - 1);
		loadProjects();
	}

	function nextPage() {
		if (!hasNext) return;
		page += 1;
		loadProjects();
	}

	onMount(async () => {
		if ($authStore.user && !ownerPrefilled) {
			filters.ownerId = `${Number($authStore.user.id)}`;
			ownerPrefilled = true;
		}
		await loadProjects();
	});
</script>

<div class="space-y-6">
  <header class="flex items-center justify-between">
    <div>
      <p class="text-sm uppercase tracking-[0.2em] text-gray-500">Admin / Projects</p>
      <h1 class="text-3xl font-semibold leading-tight">Project Directory</h1>
    </div>
    <button class="btn btn-primary" on:click={goToAdd} disabled={loading}>
      Add New Project
    </button>
  </header>

  <section class="card bg-base-100 shadow">
    <div class="card-body">
      <form
        class="grid gap-4 md:grid-cols-4"
        on:submit|preventDefault={() => {
          page = 1;
          loadProjects();
        }}
      >
        <label class="input-group">
          <span>Name</span>
          <input
            class="input input-bordered w-full"
            type="text"
            placeholder="Search by name"
            bind:value={filters.name}
          />
        </label>
        <label class="input-group">
          <span>Code</span>
          <input
            class="input input-bordered w-full"
            type="text"
            placeholder="Code"
            bind:value={filters.code}
          />
        </label>
        <label class="input-group">
          <span>Sponsor</span>
          <input
            class="input input-bordered w-full"
            type="text"
            placeholder="Sponsor"
            bind:value={filters.sponsor}
          />
        </label>
        <label class="input-group">
          <span>Owner</span>
          <input
            class="input input-bordered w-full"
            type="number"
            placeholder="Owner ID"
            bind:value={filters.ownerId}
          />
        </label>
      </form>
      <div class="flex items-center gap-2 mt-2">
        <button class="btn btn-sm" type="button" on:click={loadProjects} disabled={loading}>
          Apply
        </button>
        <button class="btn btn-sm btn-ghost" type="button" on:click={resetFilters}>
          Reset
        </button>
      </div>
    </div>
  </section>

  <section class="card bg-base-100 shadow">
    <div class="card-body">
      {#if loading}
        <div class="flex items-center justify-center">
          <span class="loading loading-dots loading-lg text-primary"></span>
          <span class="ml-3">Loading projects...</span>
        </div>
      {:else}
        {#if error}
          <p class="text-sm text-error">{error}</p>
        {/if}
        {#if projects.length === 0}
          <p class="text-sm text-gray-600">No projects found for the current filter.</p>
        {:else}
          <div class="overflow-auto">
            <table class="table w-full">
              <thead>
                <tr>
                  <th>ID</th>
                  <th>Name</th>
                  <th>Code</th>
                  <th>Sponsor</th>
                  <th>Owner</th>
                  <th>Creator</th>
                  <th>Created</th>
                  <th>Actions</th>
                </tr>
              </thead>
              <tbody>
                {#each projects as project}
                  <tr>
                    <td>{project.id}</td>
                    <td class="font-semibold">{project.name}</td>
                    <td>{project.code ?? '-'}</td>
                    <td>{project.sponsor ?? '-'}</td>
                    <td>{project.ownerId}</td>
                    <td>{project.creatorId}</td>
                    <td>{new Date(project.createdAt).toLocaleDateString()}</td>
                    <td>
                      <div class="flex gap-2">
                        <button
                          class="btn btn-xs btn-outline"
                          on:click={() => goToEdit(project.id)}
                          disabled={loading}
                        >
                          Edit
                        </button>
                        <button
                          class="btn btn-xs btn-error btn-outline"
                          on:click={() => deleteProject(project.id)}
                          disabled={loading}
                        >
                          Delete
                        </button>
                      </div>
                    </td>
                  </tr>
                {/each}
              </tbody>
            </table>
          </div>
        {/if}
      {/if}
      <div class="flex items-center justify-between mt-4">
        <p class="text-sm text-gray-500">
          Page {page} of {totalPages} · {total} projects total
        </p>
        <div class="btn-group">
          <button class="btn btn-sm" on:click={prevPage} disabled={!hasPrev || loading}>
            Prev
          </button>
          <button class="btn btn-sm" on:click={nextPage} disabled={!hasNext || loading}>
            Next
          </button>
        </div>
      </div>
    </div>
  </section>
</div>
