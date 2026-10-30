Usage
=====

Every problem solved with SPAIDER lives in its own folder. You write the
model and the optimization problem as text, choose the solution options in a
script, and call ``spaider_main``. SPAIDER generates the MATLAB functions it
needs from your model, solves the problem and stores the results.

.. _problem-folder:

The problem folder
------------------

A new problem needs three files written by you:

``startup.m``
   Adds the SPAIDER folders to the MATLAB path (see :doc:`installation`).
   Copy it from an existing problem; it works unchanged as long as the folder
   sits at the same depth.

``input_model.m``
   The model: states, controls, parameters, objective function and
   constraints, written as strings.

``problem_<name>.m``
   The script you run. It sets the solver options and calls
   ``spaider_main``.

When the problem runs, SPAIDER writes the following files into the same
folder. Do not edit them, since they are overwritten on every run.

========================  ==================================================
File                      Contents
========================  ==================================================
``modelo_eq.m``           Right-hand side of the differential equations
``modelo_eq_sens.m``      Model augmented with the sensitivity equations
``alg_eq.m``              Algebraic equations
``obf1.m``, ``obf2.m``    Objective function and its gradient
``cr1.m``, ``cr2.m``      Constraints and their Jacobians
========================  ==================================================

Writing the model: ``input_model.m``
------------------------------------

``input_model`` returns the model as cell arrays of strings. Start from the
defaults returned by ``dae_default`` and fill in what your problem needs:

.. code-block:: matlab

   function [dx y par e_var a_var c_var J cr_eq cr_deq input] = input_model

   [dx y par e_var a_var c_var J cr_eq cr_deq] = dae_default;

   % Horizon, initial conditions and bounds
   input.t0   = 0;               % initial time
   input.tf   = 250;             % final time
   input.x0   = [0.72 0.05 1];   % initial condition of the states
   input.nU   = 1;               % number of control variables
   input.u_lb = [0];             % lower bound of each control
   input.u_ub = [0.001];         % upper bound of each control
   input.u0   = [0.0005];        % initial guess of each control
   input.is0  = 2;               % first iteration (2^is0 stages)
   input.isF  = 10;              % last iteration

   % Parameters
   par(1) = {'k1 = 0.053'};
   par(2) = {'k2 = 0.128'};
   par(3) = {'cb_in = 5'};

   % Differential equations: dx(i) = d x(i) / dt
   dx(1) = {'-k1*x(1)*x(2) - (u(1)/x(3))*x(1)'};
   dx(2) = {'-k1*x(1)*x(2) - 2*k2*x(2)^2 + (u(1)/x(3))*(cb_in - x(2))'};
   dx(3) = {'u(1)'};

   % Objective function (minimized)
   J = {'-cao*Vo + x(end,1)*x(end,3)'};

   % Constraints
   cr_eq(1)  = {'[]'};                      % equality, = 0
   cr_deq(1) = {'x(end,2) - cb_mais'};      % inequality, <= 0
   end

The notation inside the strings is:

- ``x(i)`` is the *i*-th state and ``u(j)`` the *j*-th control.
- ``x(end,i)`` is the value of state *i* at the final time; use it for
  terminal objectives and terminal constraints.
- ``x(:,i)`` is the whole trajectory of state *i*; use it for path
  constraints.
- Parameters declared in ``par`` can be used by name.
- The objective ``J`` is **minimized**. To maximize a quantity, write its
  negative.
- Inequality constraints are written in the form ``g <= 0``.

SPAIDER differentiates these expressions symbolically to build the
sensitivity equations and the gradients passed to the optimizer.

Running the problem: ``problem_<name>.m``
-----------------------------------------

The script runs ``startup``, sets the ``fmincon`` and ODE options, fills the
``in_SPAIDER`` structure and calls ``spaider_main``:

.. code-block:: matlab

   startup

   optNLP = optimset('Algorithm', 'interior-point', 'GradObj', 'on', ...
                     'GradConstr', 'on', 'Display', 'iter', ...
                     'TolX', 1e-10, 'TolFun', 1e-10, 'TolCon', 1e-3);
   optODE = odeset('RelTol', 1e-9, 'AbsTol', 1e-9);

   in_SPAIDER.problem.method       = 'single shooting';
   in_SPAIDER.problem.type         = 'optimal control';
   in_SPAIDER.problem.analitic_derivarive = 'sensitivy analisys';
   in_SPAIDER.problem.algorithm    = 'serial';
   in_SPAIDER.problem.tfree        = 0;
   in_SPAIDER.problem.interpolation = 'stage';

   in_SPAIDER.conv.f_tol  = 1e-5;
   % ... remaining options, see the Configuration page

   out_SPAIDER = spaider_main(in_SPAIDER, optNLP, optODE);

Every field of ``in_SPAIDER`` is described in :doc:`configuration`. Turning
``GradObj`` and ``GradConstr`` on makes ``fmincon`` use the gradients
computed by SPAIDER from the sensitivity equations, which is usually much
faster and more accurate than finite differences.

Results
-------

``spaider_main`` returns a structure with the solution of every iteration:
the optimal control profile and its stage times, the objective function,
the state trajectories, the wavelet detail coefficients, the thresholds used
and the convergence measures.

It also creates a results folder inside the problem folder, named after the
interpolation and the wavelet options, for example
``results\_stage\db1_h_sln_heursure\``. The folder holds the log of the run
(``diary``), a ``.mat`` file with all variables and an Excel report with the
results and thresholds of each iteration. When ``plot.control`` is ``'on'``
the control profile is plotted after every iteration.
