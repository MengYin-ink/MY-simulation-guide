# Molecular-Dynamics Workflow

## Inputs and preparation

Define the target question, molecular composition, boundary conditions,
force field, initial configuration, and any chemical or reaction model.
Validate topology, atom types, charges, and force-field coverage before
production runs.

## Procedure

1. Generate and inspect the initial system.
2. Minimize to remove severe overlaps or unfavorable contacts.
3. Equilibrate under a stated ensemble and monitor stability.
4. Run production sampling with recorded settings and independent repeats
   where appropriate.
5. Assess equilibration, sampling adequacy, and convergence for each reported
   observable.
6. Analyze trajectory data with documented scripts and definitions.

## Validation and reporting

Report software and force-field versions, system size, boundary conditions,
ensemble, timestep, temperature/pressure control, equilibration and
production lengths, output frequency, random seeds, and analysis window.
Check energy and structural stability and quantify uncertainty or
run-to-run variation.

For simulations that create bonds, also document the reaction criterion,
topology updates, and how the reaction timescale is interpreted. See
[MD Polymerization & Crosslinking](../../polymerization/md-polymerization/index).
