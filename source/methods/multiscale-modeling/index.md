# Multiscale Modeling

Multiscale modeling transfers information between methods that describe
different length, time, or physical scales. For reaction-driven polymer
formation, a possible chain is:

```text
Electronic reaction energetics
    → kinetic model and assumptions
    → reaction-selection model
    → polymerization simulation
    → structural observables
```

Each transfer requires a defined quantity, units, assumptions, and validation
target. In particular, a DFT electronic barrier is not automatically an MD
reaction probability. The project-specific integration plan is documented in
[Multiscale Integration](../../polymerization/multiscale-integration/index).
