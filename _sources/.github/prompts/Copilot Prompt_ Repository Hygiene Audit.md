You are preparing this repository for a larger course modernization project.

Your task is a repository hygiene audit only.

Do not modify, delete, rename, move, untrack, or create files yet.

Inspect the entire `databasebook` repository and determine:

1. Which files and directories are source files that should remain under version control.
2. Which files and directories appear to be generated build artifacts.
3. Which files are local development artifacts, caches, temporary files, environment files, or operating-system-specific files.
4. Which files may currently be required for the existing Jupyter Book / GitHub Pages deployment workflow.
5. Whether generated files such as `_build/`, rendered HTML, notebook checkpoints, or other outputs are currently tracked.
6. Whether the repository contains hard-coded local paths, environment-specific configuration, or stale files.
7. Whether a `.gitignore` is currently missing or incomplete.

Then provide:

## A. Repository Structure Summary
Explain the current repository structure and identify the likely purpose of each major directory.

## B. Source vs Generated Files
Classify important files/directories as:
- Source
- Generated
- Local-only
- Unclear / requires verification

## C. Proposed `.gitignore`
Propose a `.gitignore` appropriate for this repository.

Do not create it yet.

For every proposed entry, briefly explain why it should be ignored.

## D. Currently Tracked Cleanup Candidates
Identify files that appear to be tracked by Git but would normally be excluded.

Do not untrack them yet.

## E. Publishing Risk
Inspect the Jupyter Book and GitHub Pages configuration and explain whether removing generated files from version control could affect the current publishing workflow.

## F. Recommended Cleanup Plan
Provide a safe sequence for cleaning the repository without breaking the published book.

Important constraints:

- Preserve all instructional source content.
- Do not assume `_build/` or rendered HTML can be removed until the current publishing workflow is understood.
- Do not make any changes.
- Prefer evidence from repository files and Git configuration over assumptions.
- Flag uncertainty explicitly.