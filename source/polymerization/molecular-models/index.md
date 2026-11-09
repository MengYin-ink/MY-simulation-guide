# Molecular Models

This module describes how to prepare and document molecular models for
reaction and polymer-network simulations. The model definition should be
consistent across electronic-structure calculations, kinetic models, and MD.

## Model record

For each publicly shareable model, record:

- a stable model identifier and provenance;
- molecular structure, charge, spin state, and relevant stereochemistry;
- functional groups and candidate reactive sites;
- atom mapping used to relate reactant, product, and trajectory structures;
- geometry-preparation and optimization procedure;
- force-field or electronic-structure model used, with version information;
- known limitations and any assumptions used to simplify the structure.

## Reactive species and initial configurations

Radical or other reactive-state models need an explicit electron-count and
spin-state rationale. Initial configurations should document relative
orientation, separation, constraints (if any), and how alternative
configurations were sampled.

## Validation and release checks

Check connectivity, atom mapping, charge and spin, geometry quality, and
consistency between input and output structures. Do not publish proprietary
molecular structures, internal atom labels, or unpublished configurations
without authorization.

Use the [DFT reaction-kinetics module](../dft-reaction-kinetics/index) for
reactant/product pathway setup and the
[MD polymerization module](../md-polymerization/index) for system construction.
