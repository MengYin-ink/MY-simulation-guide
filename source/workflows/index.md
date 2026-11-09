# Reusable Simulation Workflows

This section contains procedures that can be reused across research projects.
Project-specific applications belong under
[Polymerization Project](../polymerization/index), which should link to these
shared procedures instead of duplicating them.

Every workflow should specify:

- prerequisites and supported model scope;
- inputs, units, and expected outputs;
- software and tested versions;
- ordered execution steps and resource requirements;
- validation and convergence criteria;
- known limitations, failure modes, and provenance to record.

```{toctree}
:maxdepth: 1

ci-neb/index
molecular-dynamics/index
dft/index
md/index
multiscale/index
automation/index
```

The procedures here are documentation, not an execution service. Keep
automation code and credentials out of the public documentation repository.
