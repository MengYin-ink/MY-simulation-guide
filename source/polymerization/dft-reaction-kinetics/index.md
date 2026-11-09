# DFT Reaction Kinetics

This module describes how to define and compare candidate propagation
reactions, calculate reaction pathways, validate results, and connect
energetics to a kinetic model. It is a project-oriented application of the
general [DFT](../../methods/dft/index) and
[reaction-pathway methods](../../methods/reaction-pathways/index).

## Reaction definitions

For two generic monomers, `M1` and `M2`, the four propagation channels are:

| Radical chain end | Incoming monomer | Rate-constant label |
|---|---|---|
| `M1*` | `M1` | `k11` |
| `M1*` | `M2` | `k12` |
| `M2*` | `M1` | `k21` |
| `M2*` | `M2` | `k22` |

The radical chain end and incoming monomer define the direction. Swapping them
is a different modeled reaction and should not be assumed to have the same
barrier or kinetics. For a two-monomer kinetic model, reactivity ratios are
often defined as `r1 = k11/k12` and `r2 = k22/k21`, subject to the model's
kinetic assumptions.

## Calculation stages

1. Define the reaction, atom mapping, charge, spin state, and model boundaries.
2. Prepare and independently check reactant and product structures.
3. Generate and inspect an initial path.
4. Run the chosen path-search method and assess numerical convergence.
5. Validate the candidate transition state and endpoints.
6. Extract both activation and reaction energies with a declared reference.
7. Record uncertainty, assumptions, and the kinetic interpretation separately.

The generic [CI-NEB workflow](../../workflows/ci-neb/index) covers reusable
calculation practice. Do not treat a CI-NEB electronic energy barrier as a
free-energy barrier or rate constant without additional modeling.

## Data to record

For each approved public example, record the method and software versions,
structures or public identifiers, convergence criteria, pathway images,
energy reference, validation evidence, and output units. Keep unpublished
barriers and project-specific structures in private storage unless approved
for release.
