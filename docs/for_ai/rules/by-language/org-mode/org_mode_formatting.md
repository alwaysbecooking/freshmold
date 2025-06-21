---
description: Org Mode Formatting Rule
globs: ["*.org"]
alwaysApply: false
---
## Description
This rule ensures that Org mode files use the correct syntax for inline code.

## Rule
When writing in Org mode files (`.org`):
- For inline code, you MUST use tildes (`~...~`).
- You MUST NOT use backticks (`` `...` ``), which is a Markdown convention.

## Rationale
Using the correct syntax ensures that the document renders correctly in Org mode environments like Emacs. Mixing syntaxes leads to formatting errors and reduces readability.

## Examples
✅ Correct:
```org
Use the ~cruft~ command to update your project.
```

❌ Incorrect:
```org
Use the `cruft` command to update your project.
```
