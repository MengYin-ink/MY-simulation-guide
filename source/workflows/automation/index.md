# Automation

Automation should be developed in stages:

1. **Knowledge and standards:** document scientific assumptions, workflow
   steps, interfaces, and validation criteria.
2. **Workflow automation:** implement versioned scripts with standardized
   inputs and outputs, error reporting, and validation.
3. **Agent-driven execution:** allow a planner or agent to select and execute
   approved tools, inspect results, and request or perform follow-up steps
   under explicit controls.

Do not skip workflow validation before adding autonomous decision-making.
Document each workflow's prerequisites, input schema, output schema, failure
states, and acceptance checks. Keep executables and secrets in separately
maintained, access-controlled code and compute environments; this public site
describes their contracts and use.
