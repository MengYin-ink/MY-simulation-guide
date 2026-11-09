# Polymerization & Crosslinking Simulation

This section organizes a shareable computational research workflow around
radical polymerization and polymer-network formation. It connects molecular
models, reaction energetics, kinetic assumptions, MD-based network formation,
and structural analysis.

The public pages describe methods and validation standards, not confidential
project records. Specific unpublished structures, reaction barriers,
proprietary parameters, internal code, and experimental comparisons must stay
private unless their release is explicitly authorized.

## Research logic

```text
Molecular models
    → reaction pathways and electronic barriers
    → kinetic model and assumptions
    → polymerization / crosslinking simulation
    → network and morphology analysis
    → carefully qualified structure–property interpretation
```

An electronic barrier is not a rate constant, and a rate constant is not
directly an MD reaction probability. The assumptions and validation at each
transfer are documented in [Multiscale Integration](multiscale-integration/index).

## Project modules

```{toctree}
:maxdepth: 1

project-overview/index
molecular-models/index
dft-reaction-kinetics/index
md-polymerization/index
structural-analysis/index
multiscale-integration/index
```

Generic methods and reusable procedures remain in
[Computational Methods](../methods/index) and [Reusable Workflows](../workflows/index);
this section links those resources to the polymerization research questions.
