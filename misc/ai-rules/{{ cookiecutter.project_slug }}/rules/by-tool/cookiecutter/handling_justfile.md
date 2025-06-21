---
description: Handling Jinja2 and Justfile Template Conflicts
globs: ["**/{{cookiecutter.project_slug}}/justfile"]
alwaysApply: false
---
## Description
When converting an existing project into a Cookiecutter template, a common challenge arises if the project contains a `justfile`. Both Cookiecutter's Jinja2 engine and the `just` command runner use the `{{ variable }}` syntax for templating. This rule ensures that these conflicting syntaxes are handled correctly, preventing errors during project generation.

## Rule
When a `justfile` exists within a Cookiecutter template (`{{cookiecutter.project_slug}}/justfile`):

1.  All syntax intended for the **`just` command runner** (e.g., `just` variables, recipe arguments) that uses `{{ }}` notation MUST be wrapped in a `{% raw %}` ... `{% endraw %}` block.
2.  This tells the Cookiecutter (Jinja2) engine to treat the enclosed block as raw, literal text and to pass it through to the generated file without modification.
3.  Any syntax intended for **Cookiecutter** (i.e., variables defined in `cookiecutter.json`) MUST remain outside of `{% raw %}` blocks to ensure they are correctly rendered during project generation.

## Implementation
- The AI will enforce this rule by:
  - Scanning any `justfile` within the Cookiecutter template directory.
  - Identifying all occurrences of `{{ }}` syntax.
  - If the variable within the braces is not defined in `cookiecutter.json`, the AI will automatically enclose the statement in a `{% raw %}` ... `{% endraw %}` block.
  - The AI will verify that variables defined in `cookiecutter.json` are not wrapped in `{% raw %}` blocks.

## Benefits
- Prevents `UndefinedValueError` errors during the `cookiecutter` generation process.
- Guarantees that the final, generated `justfile` is valid and functions as expected.
- Creates a clean, maintainable, and idiomatic separation between the two templating layers.
- It is the standard, prescribed solution for this common nested-templating problem.

## Examples
✅ Correct:
```makefile
# In: {{cookiecutter.project_slug}}/justfile

# Cookiecutter variable - NOT wrapped
project_author := "{{ cookiecutter.author_name }}"

# Just recipe with a Just argument - WRAPPED in {% raw %}
run command:
    @echo "Running command: {% raw %}{{command}}{% endraw %}"
    @echo "Author is: {{ project_author }}"

```

❌ Incorrect:
```makefile
# In: {{cookiecutter.project_slug}}/justfile

# This will cause a Cookiecutter error because 'command' is not
# a variable in cookiecutter.json.
run command:
    @echo "Running command: {{command}}"
```
