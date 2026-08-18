---
name: academic-calendar-schedule-updater
description: Update weekly date ranges in an existing course schedule HTML file using the institution's official academic calendar while preserving assignments, images, links, styling, and table structure.
---

# Academic Calendar Schedule Updater

## Purpose

Use this skill to update semester-specific weekly date ranges in an existing course schedule HTML file.

The skill is intended to be reusable across courses and institutions.

## Inputs

- Target institution and campus
- Target semester and year
- Existing course schedule HTML file, typically `Schedule*.html`

## Workflow


1. Locate the supplied course schedule HTML file, typically matching
   Schedule*.html.

2. Inspect the existing HTML structure before editing.

3. Identify the institution/campus and target semester/year.

4. Retrieve the official academic calendar from the institution's
   authoritative Registrar or academic-calendar website.

5. Verify:
   - full-term start date
   - full-term end date
   - instructional breaks
   - major no-class periods that affect weekly schedule ranges

6. Calculate consecutive Sunday-Saturday or Monday-Sunday week ranges
   according to the format already used in the supplied schedule.

7. Preserve the existing compact date style exactly:
   MonDD-MonDD
   Example:
   Aug24-Aug30
   Aug31-Sep06

8. Inspect the schedule table cells and identify existing weekly date
   strings.

9. Replace only the weekly date text.

10. Preserve:
    - images
    - links
    - assignment names
    - quizzes
    - labs
    - DataCamp references
    - CSS
    - HTML structure
    - table dimensions
    - DesignPlus/Canvas styling

11. Do not rewrite or reformat the HTML unnecessarily.

12. Produce a change summary listing:
    - calendar source used
    - semester start/end
    - breaks identified
    - old date → new date mappings

13. Validate that the resulting HTML remains structurally valid.

## Calendar Source Rules

Prefer the institution's official Registrar or academic calendar.

Do not rely on:
- previous semester dates
- search-result snippets
- unofficial calendars
- third-party websites

If an authoritative calendar cannot be verified, stop and report the issue rather than guessing.

## Break Handling

Do not automatically remove or redesign a week because it overlaps a break.

Instead:

1. preserve the existing course content
2. identify the affected week
3. report the overlap
4. request approval before changing assignments or course structure

## Validation

After editing:

- verify all expected weekly date strings were updated
- verify the number of week cells did not change
- verify images and links remain unchanged
- verify the HTML structure remains valid
- report any dates or cells that could not be mapped confidently

## Output Summary

Report:

- authoritative calendar source
- semester start date
- semester end date
- identified breaks
- old → new weekly date mappings
- affected break weeks
- files modified
- any unresolved issues

## Update the Canvas source

Use HTML copied directly from the Canvas HTML editor as the authoritative source for the actual update.

Modify only the requested weekly date text.

Preserve all other content and markup, including:

assignment names
quizzes
labs
Coding Practice
DataCamp entries
images
image URLs
links
href
src
data-api-* attributes
Canvas file and module IDs
CSS
inline styles
table structure
cell dimensions
DesignPlus markup
Canvas-specific attributes

Do not unnecessarily reformat, normalize, or restructure the HTML.

## Create a new output file

Never overwrite the authoritative Canvas source file.

Treat the supplied Canvas HTML source as immutable input.

Create a new updated HTML file using the user-specified name and location.

If no output name is specified, use:

<original-name>.updated-<term>.html

Example:

Schedule.canvas-source.html

→

Schedule.canvas-updated-2026FA.html

## Validate

Compare the original Canvas source with the updated output.

Verify:

all intended weekly date strings were updated
no unrelated text changed
the number of week cells remains unchanged
assignments and other course content remain unchanged
Canvas links and resource attributes remain unchanged
HTML structure remains valid
the original source file was not modified

Report any mapping or cell that could not be updated confidently.
