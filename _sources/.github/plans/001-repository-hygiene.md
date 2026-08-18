Repository hygiene audit for databasebook
========================================

Problem
-------

Audit the repository before modernization work so source content can be preserved while generated output, local artifacts, and stale files are identified safely.

Approach
--------

- Inspected the current worktree, tracked-file inventory, branch layout, and Git status.
- Inspected Jupyter Book configuration in `_config.yml` and `_toc.yml`.
- Inspected branch evidence for publishing, especially the `gh-pages` branch and the absence of GitHub Actions workflows.
- Distinguished current source files from generated output and local-only artifacts based on file roles, references, and Git metadata.

Todos
-----

- inventory-repository-state
- assess-publishing-workflow
- draft-cleanup-recommendations

Notes
-----

- The current worktree is not clean. It contains tracked deletions from older course material plus untracked new source files and untracked new build output.
- Findings below separate "currently in the worktree" from "currently tracked in Git" where that distinction matters.

## A. Repository Structure Summary

Major directories and likely purpose:

- Repository root: Jupyter Book source root. Current top-level source files include `_config.yml`, `_toc.yml`, chapter markdown files, `pyMongoOverview.ipynb`, datasets (`dept.csv`, `emp.csv`), bibliography, logo, and requirements.
- `_static/`: source static assets for the book (images and one PDF). This should generally stay version-controlled, but it currently also contains checkpoint noise.
- `_build/`: generated Jupyter Book / Sphinx output. Contains `.doctrees`, rendered HTML, copied assets, search index, reports, and executed notebook output.
- `.ipynb_checkpoints/`: Jupyter autosave checkpoints; local-only, not source.
- `.github/`: maintainer/copilot metadata in the current worktree; not part of the book build or publishing flow.
- `.git/`: repository metadata.

Branch-level publishing structure:

- `main` / `course-redesign-2026`: source branch history.
- `gh-pages`: root-level rendered site with `.nojekyll`, HTML pages, `_static/`, `_images/`, `_sources/`, and `searchindex.js`.
- No `.github/workflows/` directory was found, so there is no repository-local automated Pages deployment workflow in the worktree.

High-signal current-state observations:

- `git ls-files` reports 425 tracked paths on `main`; 349 of them are under `_build/`.
- The current worktree contains untracked source-like files that are referenced by the current TOC and/or chapters: `module2.md`, `module3.md`, `normalization.md`, `practice.md`, `_static/diff.png`, `_static/customers.png`, `_static/project_schema.png`.
- The current worktree also contains tracked deletions of older material such as `week1.md`, `week1_sqlite.ipynb`, `week2.md`, `week3.md`, `week5.md`, `week8.md`, `sqlite-intro.md`, `sqlite_r.md`, `cassandra.md`, `database_selection.md`, `markdown.md`, and scratch notebooks `Untitled.ipynb` / `Untitled1.ipynb`.

## B. Source vs Generated Files

### Source

Current source files/directories that should remain under version control:

- Book config: `_config.yml`, `_toc.yml`
- Current chapter/source content:
  - `welcome.md`
  - `module1.md`
  - `intro.md`
  - `sqlite_intro.md`
  - `algebra.md`
  - `ra_queries.md`
  - `join.md`
  - `week6.md`
  - `postgres.md`
  - `week7.md`
  - `mongodb.md`
  - `pyMongoOverview.ipynb`
- Current worktree source additions that also appear to be real book content and should likely be tracked if retained:
  - `module2.md`
  - `module3.md`
  - `normalization.md`
  - `practice.md`
  - `_static/diff.png`
  - `_static/customers.png`
  - `_static/project_schema.png`
- Source assets/data:
  - `_static/` images/PDF (excluding nested checkpoint files and `.DS_Store`)
  - `logo.png`
  - `dept.csv`
  - `emp.csv`
  - `references.bib`
  - `requirements.txt`

### Generated

Generated build artifacts:

- Entire `_build/` tree, including:
  - `_build/.doctrees/`
  - `_build/html/`
  - `_build/jupyter_execute/`
  - `_build/html/_sources/`
  - `_build/html/_images/`
  - `_build/html/_static/`
  - `_build/html/reports/`
  - `_build/html/searchindex.js`
  - `_build/html/objects.inv`
  - `_build/html/.buildinfo`
- Rendered HTML on `gh-pages` is also generated, even if it is currently required for publishing.

### Local-only

Files/directories that should normally stay out of version control:

- `.DS_Store`
- `_static/.DS_Store`
- `.ipynb_checkpoints/`
- `_static/.ipynb_checkpoints/`
- Scratch notebooks like `Untitled.ipynb` and `Untitled1.ipynb`
- Build/execution logs such as `_build/html/reports/*.log` and `*.err.log`
- Local database artifact `week1.db`

### Unclear / requires verification

- `pyMongoOverview.py`: present in the current worktree but untracked. It looks like a notebook-exported or parallel script version of `pyMongoOverview.ipynb`, and it contains an absolute local path. Likely local/derived unless intentionally maintained as a separate source artifact.
- `databasebook` tracked entry on `main`: Git reports it as a gitlink/submodule entry (`160000`) but there is no `.gitmodules` mapping. This is stale and should be treated as suspicious metadata until intentionally resolved.
- Older lesson files deleted in the worktree but still tracked in `main` history (for example `week1.md`, `week1_sqlite*.ipynb`, `week2.md`, `week3.md`, `week5.md`, `week8.md`, `cassandra.md`, `database_selection.md`, `markdown.md`, `sqlite_r.md`). These may be intentionally retired source rather than accidental clutter; keep them only if still pedagogically needed.

## C. Proposed .gitignore

Proposed entries:

- `.DS_Store`
  - Ignore macOS Finder metadata files.
- `**/.ipynb_checkpoints/`
  - Ignore Jupyter autosave checkpoint directories everywhere in the repo, including root and nested under `_static/`.
- `_build/`
  - Ignore Jupyter Book / Sphinx build output, rendered HTML, copied static assets, search indexes, reports, doctrees, and executed notebooks.
- `.jupyter_cache/`
  - Ignore Jupyter execution cache if it is introduced later.
- `__pycache__/`
  - Ignore Python bytecode cache directories.
- `*.py[cod]`
  - Ignore Python bytecode files.
- `.venv/`
  - Ignore project-local virtual environments.
- `venv/`
  - Ignore virtual environments created with the conventional name `venv`.
- `.env`
  - Ignore a local environment file if one is added later.
- `.env.*`
  - Ignore environment-specific variants such as `.env.local`.
- `*.log`
  - Ignore local and build-generated log files such as notebook execution reports.
- `Untitled*.ipynb`
  - Ignore scratch notebooks created during ad hoc exploration.
- `*.db`
  - Likely appropriate for local SQLite exercise outputs such as `week1.db`; if the course intentionally ships seed databases later, narrow this rule to specific filenames instead.

## D. Currently Tracked Cleanup Candidates

Tracked or historically tracked items that would normally be excluded or reviewed for removal from the source branch:

- `_build/**`
  - 349 tracked paths on `main`; all are generated build artifacts.
- `.ipynb_checkpoints/**`
  - Tracked checkpoint files exist at the repository root.
- `_static/.ipynb_checkpoints/**`
  - Tracked nested checkpoint notebooks/images exist under source assets.
- `.DS_Store`
  - Tracked at repository root.
- `_static/.DS_Store`
  - Tracked under source assets.
- `_build/html/reports/*.log` and `*.err.log`
  - Generated execution logs; one currently contains local filesystem paths from `/Users/olgascrivner/...`.
- `week1.db`
  - Tracked SQLite database file; typically a local exercise artifact.
- `databasebook`
  - Tracked gitlink/submodule entry with no `.gitmodules` mapping.
- `Untitled.ipynb`, `Untitled1.ipynb`
  - Scratch-looking notebooks.
- Likely stale or duplicate content currently tracked in `main` history and deleted in the worktree:
  - `sqlite-intro.md` (duplicate naming variant of `sqlite_intro.md`)
  - `week1.md`
  - `week1_sqlite.ipynb`
  - `week1_sqlite_problems.ipynb`
  - `week1_sqlite_solutions.ipynb`
  - `week2.md`
  - `week3.md`
  - `week5.md`
  - `week8.md`
  - `sqlite_r.md`
  - `cassandra.md`
  - `database_selection.md`
  - `markdown.md`
- `_static/diff.ppng.png`
  - Tracked typo/duplicate-looking asset; replaced in the current worktree by `_static/diff.png`.

Important nuance:

- Several cleanup candidates are already deleted from the current worktree but not yet committed. Do not treat those deletions as complete cleanup until the source-of-truth branch strategy is decided.

## E. Publishing Risk

Evidence inspected:

- No `.github/workflows/` directory exists in the current worktree.
- `gh-pages` exists as a separate branch and contains root-level rendered site files plus `.nojekyll`.
- `gh-pages` latest commit is an "Update documentation" commit that changes rendered HTML/output files.
- The source branch still tracks `_build/`, but the published branch stores rendered HTML at the branch root, not under `_build/`.

Likely interpretation:

- GitHub Pages is most likely serving the `gh-pages` branch, not `_build/html` directly from `main`.
- That means removing generated `_build/` files from the source branch would probably not take the currently published site offline.
- However, the current publish process appears manual or external to the repository, because no in-repo automation was found.

Why caution is still required:

- If the maintainer currently builds from the source branch and then manually copies or imports `_build/html` to `gh-pages`, `_build/` remains a necessary local intermediate even if it should not be tracked.
- Repository metadata in `_config.yml` is stale:
  - `repository.url` points to `https://github.com/executablebooks/jupyter-book`
  - `repository.path_to_book` is `docs`, but the book root is the repository root
  - `repository.branch` is `master`, but the active source branch is `main` / `course-redesign-2026`
- Those stale settings affect repository/issue links in the rendered book and are evidence that the deployment configuration has drifted.

Additional stale/environment-specific findings relevant to publishing:

- `pyMongoOverview.py` contains a hard-coded absolute local path: `/Users/olgascrivner/Documents/IU-DataScience/Database/Summer2022/Week7/2020-03-13/noncomm_use_subset/*.json`
- `_build/html/reports/pyMongoOverview.err.log` contains local virtualenv paths and a notebook timeout trace.
- `pyMongoOverview.ipynb` references `mongosetup.md`, which is missing from the current worktree.
- The current tracked `_toc.yml` in the worktree references source files that are still untracked, so the worktree is not yet in a clean publishable source-controlled state.

Risk conclusion:

- Removing generated files from version control on the source branch is probably safe for the live site only after GitHub Pages branch settings and the human publishing procedure are verified.
- Removing or rewriting generated files on `gh-pages` without a tested replacement publish step would be risky.

## F. Recommended Cleanup Plan

Safe sequence:

1. Confirm GitHub Pages settings on GitHub:
   - verify which branch/folder is published
   - verify whether Pages serves `gh-pages` root
2. Preserve source before cleanup:
   - decide which current untracked source files are intentional and should be committed as source (`module2.md`, `module3.md`, `normalization.md`, `practice.md`, and referenced `_static/` assets)
   - decide whether `pyMongoOverview.py` is a maintained source artifact or local derivative
3. Add a repository `.gitignore` first:
   - ignore checkpoints, `_build/`, `.DS_Store`, logs, virtualenvs, env files, and likely local SQLite outputs
4. Clean only the source branch first:
   - stop tracking `_build/**`
   - stop tracking checkpoint directories
   - stop tracking `.DS_Store` and execution logs
   - remove the stale `databasebook` gitlink if it is no longer a real submodule
5. Verify the source branch builds successfully from source alone:
   - ensure all TOC-referenced files are actually tracked
   - fix stale config metadata and broken internal references
   - run a clean Jupyter Book build locally
6. Keep publishing isolated:
   - do not delete `gh-pages` output until a fresh publish from the cleaned source branch succeeds
   - after a successful test publish, treat `gh-pages` as generated deploy output, not authoring source
7. Only then review pedagogical/stale source cleanup:
   - archive or remove retired lessons and duplicate files once it is clear they are not needed for the course redesign

Suggested order of operations for follow-up work:

- Phase 1: source-control hygiene (`.gitignore`, untrack generated/local files)
- Phase 2: source consistency (track intended chapters/assets, fix stale config and broken references)
- Phase 3: publishing validation (clean build, publish to `gh-pages`, verify live site)
- Phase 4: historical source pruning (retired lessons, duplicate filenames, stale submodule entry)
