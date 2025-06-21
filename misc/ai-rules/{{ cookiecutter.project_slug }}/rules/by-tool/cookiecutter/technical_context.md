---
description: Rule for adding technical context for AI to Cookiecutter templates
alwaysApply: false
---

## Description

This rule ensures that each Cookiecutter template includes a technical context document for AI, providing essential information about the project's technologies, setup, dependencies, and tool usage.

## Rule

When creating a Cookiecutter template:

1.  Create a file named `TECHNICAL_CONTEXT_FOR_AI_DELETE_AFTER_USE.md` in the root directory of the *generated project* (i.e., within the `{{cookiecutter.project_slug}}` directory).
2.  This file should contain a detailed description of the project's technical context, including:
    *   Technologies Used
    *   Development Setup
    *   Technical Constraints
    *   Dependencies
    *   Tool Usage Patterns
    *   Components/Code Organization

## Caution

**This documentation is for the generated project, not the Cookiecutter template.**

When writing the content for `TECHNICAL_CONTEXT_FOR_AI_DELETE_AFTER_USE.md`, do not include instructions on how to use the Cookiecutter template itself. This file is intended to live inside the generated project and should only contain technical context relevant to that project.

Instructions for using the Cookiecutter template should be in the template's `README.md` or other dedicated documentation outside of the `{{cookiecutter.project_slug}}` directory. The creation and maintenance of the template's own documentation is handled separately and is outside the scope of this rule.

## User Message

When a user generates a project using this Cookiecutter template, the `TECHNICAL_CONTEXT_FOR_AI_DELETE_AFTER_USE.md` file will be present in their new project. The file should contain the following message at the top:

```
# IMPORTANT: TECHNICAL CONTEXT FOR AI - DELETE AFTER USE

This file provides technical context about your project for AI co-editors.
If your AI co-editor uses file-based memory, instruct it to read the content of this file to populate its memory.
You can safely delete this file after your AI has gained sufficient context and populated its memory, or keep it if you plan to continue using AI assistance.
```

## Implementation

*   The AI will enforce this rule by:
    *   Checking for the existence of the `TECHNICAL_CONTEXT_FOR_AI_DELETE_AFTER_USE.md` file in new Cookiecutter templates.
    *   Validating the content of the file against the required sections.
    *   Providing guidance and suggestions for completing the file.

## Benefits

*   Improved understanding of Cookiecutter templates for AI.
*   Facilitates AI-driven development and automation.
*   Ensures consistent documentation across projects.
