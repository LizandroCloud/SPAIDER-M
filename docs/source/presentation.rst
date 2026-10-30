What is SPAIDER?
================

Sequential and Parallel Algorithms Integrated to Differential Equation
Routines (SPAIDER) is a collection of Matlab/Python scripts tailored to
solve dynamic optimization and optimal control problems.

It provides single shooting (control vector parameterization) and
multiple shooting algorithms. The main features of SPAIDER include:

- Adaptive strategies for control-vector parameterization.
- Symbolic environment for modelling of differential and algebraic equations (DAEs).
- Interfaces with external solvers such as Aspen Hysys, Aspen Plus and EMSO.
- Integration with Machine Learning Models.
- Python and Matlab Interfaces.

How it works
------------

In the single-shooting approach the control profile :math:`u(t)` is
discretized into piecewise stages, and the dynamic optimization problem
becomes a nonlinear programming (NLP) problem in the stage values. SPAIDER
solves this NLP with ``fmincon``, integrating the DAE model at every
evaluation and computing gradients through sensitivity equations.

Instead of refining the mesh uniformly, SPAIDER analyses the optimal control
profile of each iteration with a wavelet transform. Detail coefficients that
survive a thresholding step mark the regions where the profile changes
sharply, and only those regions are refined in the next iteration. The
result is a control profile with few stages where it is smooth and many
where it switches, at a fraction of the cost of a uniformly fine mesh.

Iterations stop when the objective function stops improving (see
``conv.f_tol`` in :doc:`configuration`) or when the maximum number of
iterations or stages is reached.

Source Code
-----------

The SPAIDER source code is available on GitHub:
`LizandroCloud/SpAIDER <https://github.com/LizandroCloud/SpAIDER>`_.

