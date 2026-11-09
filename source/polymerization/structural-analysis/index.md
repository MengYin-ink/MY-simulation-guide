# Structural Analysis

Structural analysis converts simulation trajectories and final configurations
into well-defined observables. Each reported quantity should include its
definition, units, sampling window, uncertainty, and analysis implementation.

| Observable | Example question | Interpretation check |
|---|---|---|
| Conversion | What fraction of defined reactive sites reacted? | Define the denominator and treatment of inaccessible sites. |
| Composition and sequence | Which units are incorporated, and in what order? | State how chain membership and sequence are identified. |
| Crosslink density | How many network connections form per chosen reference? | Define what counts as a crosslink and the normalization. |
| Connectivity | Is the system one connected network or several components? | Report finite-size and periodic-boundary conventions. |
| Radial distribution function | How are selected components spatially correlated? | State species, normalization, and sampling. |
| Domain structure | What spatial heterogeneity appears in the model? | Define the descriptor and length-scale limitations. |
| Diffusion | How do selected species move over sampled times? | Check time regime, finite-size effects, and statistical error. |

Structural descriptors do not by themselves establish macroscopic properties.
For example, a radial distribution function is not a direct prediction of gas
permeability. Property claims need an appropriate physical model, sufficient
sampling, and validation against independent evidence.

Only publish approved trajectory examples and results. See the
[public/private boundary](../../resources/public-private-boundary).
