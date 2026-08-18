Use the `academic-calendar-schedule-updater` skill.

Target:

* Institution: Indiana University Bloomington
* Semester: Fall 2026
* Schedule file: locate the saved course schedule HTML file matching `Schedule*.html` in the workspace

Task:

1. Inspect the existing schedule HTML.
2. Identify the current weekly date strings in the schedule table.
3. Verify the official Indiana University Bloomington Fall 2026 academic calendar using the authoritative Registrar calendar.
4. Confirm:

   * full-term start date
   * full-term end date
   * Thanksgiving break
   * any other instructional breaks that affect the weekly schedule
5. Determine the existing weekly convention used by the schedule.
6. Calculate the Fall 2026 weekly date ranges using the same convention and the same compact format, such as `Aug24-Aug30`.
7. Preserve the existing number of week cells.
8. Do not modify:

   * assignment names
   * quizzes
   * coding practice labels
   * labs
   * DataCamp entries
   * images
   * image paths
   * links
   * CSS
   * table structure
   * cell dimensions
   * DesignPlus or Canvas styling
9. Before editing anything, show:

   * the official calendar dates found
   * the proposed old-date → new-date mapping
   * any weeks overlapping an official break
   * any ambiguity or mismatch
10. Stop and wait for approval before modifying the HTML.

This is a skill-validation run. Do not make unrelated repository changes.

