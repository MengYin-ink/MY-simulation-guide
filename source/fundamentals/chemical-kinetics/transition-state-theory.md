# Transition State Theory

Transition state theory (TST) estimates a reaction rate from the free-energy
barrier between reactants and a transition state. In its common
Eyring-equation form,

```text
k(T) = (k_B T / h) exp(-Delta G^‡ / (R T))
```

where `k_B` is Boltzmann's constant, `h` is Planck's constant, `R` is the gas
constant, `T` is temperature, and `Delta G^‡` is the activation Gibbs free
energy.

The estimate assumes that configurations near the transition state are in
quasi-equilibrium with the reactants and that crossing the dividing surface
leads to products. Recrossing and dynamical effects can make the actual rate
differ from this estimate. The method and its assumptions should be considered
when interpreting calculated barriers or rates.

For a complete calculation procedure, see the relevant
[reaction-pathway method](../../methods/reaction-pathways/index) and
[simulation workflow](../../workflows/index).
