---
name: book-content-modernizer
description: Modernize and restructure Jupyter Book course content using weekly lecture objectives as the primary pedagogical anchor. Use authoritative current resources to explain why database concepts still matter, connect them to modern architectures and agentic systems, propose changes before implementation, and provide source links for all researched updates.
---

# Book Content Modernizer

## Purpose

Modernize Jupyter Book content so students gain a current understanding of database technologies and why they remain important in modern software, data, AI, and agentic architectures.

The book is supplemental to the lectures. It does not need to reproduce lecture content exactly or preserve the current chapter structure.

The goal is to create useful, modern instructional material that:

* reinforces weekly lecture objectives
* explains why database concepts still matter
* connects foundational concepts to current systems
* develops practical and transferable database skills
* prepares students for Coding Practice and Labs
* provides useful material beyond what is covered directly in lecture

## Source Priority

When course materials conflict or represent different stages of the course, use this priority:

current instructor instructions and redesign decisions
current weekly lecture objectives and lecture notes
current weekly Canvas overview
existing Jupyter Book content
legacy Coding Practice, Labs, and older course materials

Do not allow outdated course artifacts to override current instructor decisions.

## Weekly Inputs

For each week, the user may provide:

weekly Canvas overview
lecture objectives
lecture notes or topics
relevant existing book chapter(s)
Coding Practice
Lab materials
other supporting course resources

The weekly overview provides course context, but it is not automatically the authoritative specification for the redesigned course.

It may contain outdated grading rules, tools, dates, assignment structures, or terminology.

## Weekly Source Preference

When multiple versions of the same weekly overview are available, prefer sources in this order:

1. `.txt` or source text copied from Canvas
2. `.html`
3. `.md`
4. `.pdf`

Use PDF mainly for visual or layout confirmation.

Do not treat duplicate formats as separate course artifacts.

## Primary Pedagogical Input

For each week, the user will provide the lecture objectives or topics.

Treat those objectives as the primary anchor for deciding:

* what book content is useful
* what should be added
* what should be removed
* what deserves deeper explanation
* what modern examples or architectures should be introduced

Do not assume that every lecture topic requires a corresponding book section.

Do not assume that every existing book section must remain.

## Workflow

### 1. Understand the Week

Review:

* user-provided lecture objectives
* relevant existing book chapters
* related Coding Practice
* related Lab materials when available
* surrounding weeks when needed for prerequisite or progression context

Identify:

* foundational concepts
* practical skills students should gain
* concepts that deserve supplemental explanation
* connections to later course topics
* opportunities to connect database concepts to modern systems

Do not edit yet.

### 2. Review the Existing Book

Inspect the relevant Markdown, MyST Markdown, or notebook source.

Evaluate both content and organization.

Classify existing material as:

useful
needs modernization
needs clarification
worth rewriting
worth replacing
redundant
no longer useful
missing important modern context

Do not optimize for preserving existing content.

The chapter may be substantially restructured when that improves learning.

### 3. Research Current Relevance

Research current authoritative sources where needed.


Prefer:

* official database documentation
* official cloud/platform documentation
* standards
* primary technical documentation
* high-quality architecture documentation
* research papers when appropriate

Use external research to answer questions such as:

* Why is this database concept still important?
* Where does it appear in modern systems?
* How is it used in cloud architectures?
* How does it appear in AI and agentic applications?
* What tradeoffs do engineers make today?
* What has changed since the original chapter was written?

Where relevant, connect concepts to modern architectures such as:

* cloud-native applications
* microservices
* analytics platforms
* event-driven systems
* vector search and retrieval systems
* RAG architectures
* agentic applications
* tool-using agents
* memory and state management
* transactional systems
* distributed data platforms

Do not force AI or agentic examples into sections where they do not provide meaningful educational value.

4. Focus on Why, Value, and Transferable Skills

For each major topic, help students understand:

What is it?
Why does it matter?
Where is it used today?
What problem does it solve?
What tradeoff should I understand?
What skill am I gaining?

Prefer durable database skills such as:

reasoning about data models
understanding relational structure
choosing database types
querying
schema design
relationships
transactions
consistency
indexing
retrieval
connecting applications to databases
evaluating technology tradeoffs
reading technical documentation
understanding persistent data in modern applications
5. Evaluate Course Progression

Consider the intended progression:

Lecture → Book → Coding Practice → Lab

The lecture provides primary instruction.

The book provides supplemental explanation, modern context, examples, and conceptual connections.

Coding Practice provides guided hands-on experience.

Labs require more independent application.

Identify:

unnecessary duplication
missing prerequisite explanations
opportunities for the book to better prepare students for practice
concepts that should remain in lecture rather than be duplicated in the book
6. Propose a Modernized Structure

Before implementation, provide a proposal.

Include:

Weekly Objectives Reviewed

List the relevant lecture objectives and other current instructor guidance.

Current Book Assessment

Summarize:

what exists
what is dated
what is weak
what still has value
what is missing
Proposed Structure

Show a proposed chapter/section hierarchy.

The proposal may:

add sections
remove sections
merge sections
reorder material
rename chapters
create new Markdown pages
create notebooks
add diagrams or images
move content between chapters
Proposed Changes

For each substantial change, label it:

Keep
Rewrite
Add
Remove
Move
Merge

Explain the rationale.

Student Value

Explain how the proposed structure improves:

conceptual understanding
practical skill
modern relevance
preparation for Coding Practice
preparation for Lab
ability to understand modern technical architectures
Modern Architecture Connections

Identify modern architecture examples that would genuinely reinforce the week's concepts.

Avoid adding them merely for novelty.

Resources Consulted

Provide direct links to authoritative resources used during research.

For each resource, briefly state what concept or claim it supports.

7. Wait for Instructor Review

Do not implement substantial restructuring immediately.

Allow the instructor to:

approve
reject
reorder
simplify
deepen
remove
add

proposed content.

Treat the approved proposal as the implementation specification.

8. Implement Approved Changes

After approval:

modify authoritative Markdown/MyST/notebook sources
create new sections or source files when approved
update _toc.yml when navigation changes
update cross-references
add useful diagrams or images
integrate links to Coding Practice where appropriate

Do not edit generated _build/ output.

9. Validate

After implementation:

build the Jupyter Book
verify navigation
verify internal links
verify external links
verify images and assets
execute notebooks when applicable
inspect rendered output
confirm alignment with approved weekly objectives
report validation failures rather than silently ignoring them
Visual Content

Recommend or create visuals when they materially improve learning.

Examples include:

data-model diagrams
relational structures
application-to-database architecture
transaction flows
database-type comparisons
modern application architecture
RAG data architecture
agent state/memory architecture

Avoid decorative visuals with little instructional value.

Research Rules

When discussing current technologies, architectures, products, or practices:

research before making current claims
prefer primary or authoritative sources
provide source links
distinguish durable concepts from current examples
avoid popularity rankings unless popularity itself is relevant
avoid statistics that will quickly become stale
avoid vendor marketing claims presented as general technical truth
Output Before Implementation

Always provide:

weekly objectives reviewed
current book assessment
proposed chapter structure
proposed changes with rationale
student-value explanation
modern architecture connections
resources consulted with links
Coding Practice/Lab implications
decisions requiring instructor approval
Output After Implementation

Report:

files modified
sections added
sections removed
sections reorganized
resources cited
images or diagrams added
TOC changes
build result
link validation result
unresolved issues
