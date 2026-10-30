Examples
========

The repository includes example problems that also serve as templates for
new problems.

Problem 1A: semi-batch isothermal CSTR
--------------------------------------

Folder: ``problems_sequential/matlab/Problem.1A - SemiBacth Ishothermal CSTR Reactor (Srinavasan et al. 2003) (fixT-endC-sU) (+)/``

A semi-batch reactor with the reactions :math:`A + B \rightarrow C` and
:math:`2B \rightarrow D`, taken from Srinivasan et al. (2003) and Schlegel
et al. (2005). The control :math:`u` is the feed rate of B, and the goal is
to maximize the amount of A converted by the final time :math:`t_f = 250`
(objective :math:`J = c_A(t_f)V(t_f) - c_{A,0}V_0`, minimized), subject to
terminal constraints on the concentrations of B and D.

States: :math:`x_1 = c_A`, :math:`x_2 = c_B`, :math:`x_3 = V`.

.. math::

   \frac{dc_A}{dt} &= -k_1 c_A c_B - \frac{u}{V} c_A \\
   \frac{dc_B}{dt} &= -k_1 c_A c_B - 2 k_2 c_B^2 + \frac{u}{V}(c_{B,in} - c_B) \\
   \frac{dV}{dt}   &= u

with :math:`k_1 = 0.053`, :math:`k_2 = 0.128`, :math:`c_{B,in} = 5`,
:math:`0 \le u \le 0.001` and
:math:`x(0) = [0.72,\ 0.05,\ 1]`. The constraints are
:math:`c_B(t_f) \le 0.025` and :math:`c_D(t_f) \le 0.15`.

Run it with:

.. code-block:: matlab

   problem_1A

The problem uses single shooting with piecewise constant controls,
``ode45``, gradients from sensitivity analysis and wavelet refinement with
the ``db1`` wavelet and the ``heursure`` threshold rule.

Wavelet collocation examples
----------------------------

The folder ``problems_wav_colloc/matlab/`` holds problems solved with a
wavelet collocation approach:

- *Problem 2F*: singular control problem (R. Luus, 2002).
- The semi-batch isothermal CSTR above (Srinivasan et al., 2003).
- *P1*: problem of Chen and Hsiao.

Each folder has its own ``startup.m`` and ``main.m``.

References
----------

- Srinivasan, B., Palanki, S., Bonvin, D. (2003). Dynamic optimization of
  batch processes: I. Characterization of the nominal solution.
  *Computers & Chemical Engineering*, 27(1), 1–26.
- Schlegel, M., Stockmann, K., Binder, T., Marquardt, W. (2005). Dynamic
  optimization using adaptive control vector parameterization.
  *Computers & Chemical Engineering*, 29(8), 1731–1751.
