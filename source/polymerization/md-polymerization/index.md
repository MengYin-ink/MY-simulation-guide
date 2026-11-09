# MD Polymerization & Crosslinking

This module describes a reproducible procedure for simulating reaction-driven
polymer growth and network formation with molecular dynamics. The exact
reaction model and implementation are system-specific and must be documented
separately.

## Generic process

```text
Molecular models and force field
    → initial-system generation
    → minimization and equilibration
    → reactive-site identification
    → candidate-pair selection
    → reaction criterion or probability
    → bond and topology update
    → post-reaction relaxation
    → repeat until a stated stopping criterion
    → validate and analyze the final network
```

## Required method specification

Document the candidate reactive sites, geometric or kinetic criteria,
temperature and timestep, probability interpretation, bond/topology update,
charge and force-field handling, relaxation procedure, stopping criteria, and
random seeds. State whether the simulation models chain propagation,
crosslinking, or both; these processes are not interchangeable.

## Validation

Check that reactions preserve atom identity and valid topology, energy and
structure remain numerically stable after updates, the intended reaction
counts are reached, and results are reproducible across suitable independent
seeds. Assess sensitivity to timestep, reaction parameters, and initial
configuration.

Use the generic [MD workflow](../../workflows/molecular-dynamics/index) for
simulation stages and the [reactive-polymerization method guide](../../methods/reactive-polymerization/index)
for modeling considerations.

Internal reaction scripts, proprietary force-field parameters, and
unpublished system details should not be placed in this public guide without
authorization.
