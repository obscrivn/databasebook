# Introduction to Database Technology Course

This repository contains the public instructional materials for an undergraduate Introduction to Database Technology course.

## Course architecture

- Preserve the existing course structure and weekly progression unless explicitly asked to change it.
- The public course book is the canonical source for instructional content, examples, tutorials, and ungraded coding practice.
- Canvas remains the canonical system for graded submissions, quizzes, due dates, grades, and semester-specific logistics.
- Coding Practice activities are formative and should not require graded submission.
- Homework activities are graded assessments and must preserve their intended learning outcomes and appropriate difficulty.
- DataCamp assignments are currently considered stable and should not be modified unless explicitly requested.

## Legacy course materials

Legacy course materials may exist outside this Git repository in the VS Code workspace.

Use them as historical evidence to understand:
- learning objectives
- previous assignment structure
- datasets
- student workflow
- previous tool choices
- sequencing between weeks

Do not modify legacy files.

Do not assume that technologies, links, instructions, or tool choices in legacy materials should be preserved.

Always distinguish between:
1. a technology students are intended to learn
2. a technology that was merely used to deliver an activity

## Modernization principles

Before changing instructional content or an assignment:
1. identify the original learning objective
2. identify dependencies on previous weeks
3. identify obsolete tools, libraries, APIs, links, or workflows
4. distinguish required conceptual knowledge from incidental tooling
5. propose changes before making substantial pedagogical redesigns

Prefer:
- current technologies
- low-friction student setup
- cross-platform workflows
- browser-based environments when pedagogically appropriate
- reproducible examples
- repository-relative file paths
- accessible public documentation

Avoid:
- unnecessary new tools
- semester-specific dates in public course content
- duplicated instructional content between Canvas and the book
- credentials or secrets
- absolute local file paths

## Jupyter Book

Treat source files as authoritative.

Do not edit generated build artifacts when source files exist.

Before making structural changes:
- inspect the current Jupyter Book configuration
- inspect the table of contents
- inspect the current build and publishing workflow

After approved structural or content changes, validate that the book builds successfully.

## Working style

For audit and planning tasks, do not edit files unless explicitly instructed.

Prefer evidence from repository files and legacy course materials over assumptions.

When uncertain about pedagogical intent, report the uncertainty instead of silently redesigning the course.

For substantial implementation work:

1. Create or update a durable implementation plan under `.github/plans/`.
2. Use sequential filenames such as `001-repository-hygiene.md`.
3. Record:
   - problem
   - evidence/current state
   - intended changes
   - risks
   - implementation steps
   - validation steps
   - decisions requiring human approval
4. Do not treat chat-only plans as the project record.
5. Update the plan after implementation with completion status and any deviations.
