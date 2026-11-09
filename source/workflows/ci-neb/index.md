# CI-NEB Reaction-Path Workflow

This is a reusable procedure outline for a climbing-image nudged elastic band
(CI-NEB) calculation. It is not a substitute for validating that the chosen
method is appropriate for the chemistry or system.

## Inputs

- chemically consistent reactant and product structures with identical atom
  counts and mapping;
- declared composition, charge, spin state, cell, and electronic-structure
  method;
- initial path images and interpolation procedure;
- convergence criteria and any constraints, each justified and recorded.

## Procedure

1. Relax and validate the endpoint structures with compatible settings.
2. Check atom mapping and the proposed bond changes at both endpoints.
3. Generate intermediate images and inspect for unreasonable geometries.
4. Run the path calculation; monitor both force and energy convergence.
5. Inspect image energies and structures, then refine if needed.
6. Validate the candidate saddle point with an appropriate independent
   method, such as a vibrational analysis where feasible.
7. Extract forward and reverse barriers against explicitly stated endpoint
   references, and report reaction energy separately.

## Validation and reporting

Retain the input structures, method and software versions, complete
convergence evidence, image path, energy reference, units, and validation
results. Check that endpoints describe the intended chemistry and that the
path does not change atom identity or encounter unintended states.

A converged path is not by itself proof of a physically correct mechanism.
An electronic energy barrier is also not a rate constant or a free-energy
barrier. See [reaction kinetics](../../theory/reaction-kinetics/index) and
[DFT reaction kinetics](../../polymerization/dft-reaction-kinetics/index).
