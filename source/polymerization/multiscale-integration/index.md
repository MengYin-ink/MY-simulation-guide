# Multiscale Integration

This module defines how information can be transferred from reaction
energetics to kinetic models, then to polymerization simulations and
structural analysis. Each transfer must state its assumptions, units, and
validation target.

## Energetics are not probabilities

An Arrhenius model may be written as

```text
k(T) = A exp(-Ea / (R T))
```

where `Ea` is an activation energy per mole and `R` is the molar gas
constant. Transition state theory is commonly written as

```text
k(T) = (kB T / h) exp(-Delta G‡ / (kB T))
```

where `Delta G‡` is the activation Gibbs free energy per molecule. A static
electronic-structure path calculation commonly provides an electronic energy
difference, not the complete activation free energy. Entropic, thermal,
standard-state, and dynamical effects may require additional calculations or
approximations.

A rate constant also does not by itself specify a discrete reaction
probability in an MD algorithm. That mapping depends on the simulated
time-step, event model, local encounter or concentration assumptions, and
whether the MD time represents physical kinetics. State and validate this
mapping rather than applying a barrier directly as a probability.

## Integration record

For each transfer, record:

1. the source quantity, its reference state, and units;
2. the equation or model used and its assumptions;
3. parameters not supplied by the source calculation;
4. the target simulation input and how it is interpreted;
5. sensitivity tests and independent validation.

## Long-term automation

Automation should follow validated and standardized workflows. A future
system that accepts molecular structures and returns a reaction barrier would
need to validate structure and reactive-site identification, generate and
check pathways, monitor convergence, validate transition states, extract
results, and retain full provenance. Documentation defines this contract;
execution scripts belong in a separately maintained code repository.
