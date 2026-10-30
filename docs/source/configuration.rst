Configuration
=============

All options of a run are fields of the ``in_SPAIDER`` structure, set in the
problem script before calling ``spaider_main``. The values shown are the
ones used in the bundled example (Problem 1A).

Problem (``in_SPAIDER.problem``)
--------------------------------

.. list-table::
   :header-rows: 1
   :widths: 25 20 55

   * - Field
     - Example
     - Description
   * - ``method``
     - ``'single shooting'``
     - Solution method. Alternatives: ``'multiple shooting'``,
       ``'simultaneous'``, ``'indirect'``.
   * - ``type``
     - ``'optimal control'``
     - Problem type. Alternatives: ``'dynamic parameter estimation'``,
       ``'static optimization'``.
   * - ``analitic_derivarive``
     - ``'sensitivy analisys'``
     - How gradients are computed. Alternatives:
       ``'automatic diferentiation'``, ``'numeric'``. Only used when
       ``GradObj``/``GradConstr`` are ``'on'`` in ``optNLP``. (The field
       name and values are spelled exactly as shown.)
   * - ``algorithm``
     - ``'serial'``
     - ``'parallel'`` is recommended only for multiple shooting and
       external simulators (EMSO, HYSYS).
   * - ``tfree``
     - ``0``
     - ``1`` if the final time is free (optimized), ``0`` if fixed.
   * - ``interpolation``
     - ``'stage'``
     - Representation of the control profile between mesh points:
       ``'stage'`` (piecewise constant), ``'linear'``, ``'spline'``,
       ``'nearest'``, ``'reg_const'``.

Convergence (``in_SPAIDER.conv``)
---------------------------------

.. list-table::
   :header-rows: 1
   :widths: 25 20 55

   * - Field
     - Example
     - Description
   * - ``f_tol``
     - ``1e-5``
     - Tolerance on the relative change of the objective function between
       two iterations of the adaptive algorithm.
   * - ``f_tol2``
     - ``10``
     - Second-order tolerance of the adaptive algorithm.
   * - ``t_ref``
     - ``3072.37``
     - Reference CPU time, used to compare runs.
   * - ``fref``
     - ``0.431721``
     - Reference value of the objective function (e.g. from the
       literature). Used in the convergence measure.
   * - ``utarg``
     - ``0``
     - ``1`` to use a reference control profile as target.

Solver (``in_SPAIDER.solver``)
------------------------------

.. list-table::
   :header-rows: 1
   :widths: 25 20 55

   * - Field
     - Example
     - Description
   * - ``type``
     - ``'external'``
     - ``'internal'`` or ``'external'``. EMSO must be ``'external'``.
   * - ``name``
     - ``'ode45'``
     - Integrator or simulator: any MATLAB ODE solver (``ode45``,
       ``ode15s``, ``ode23s``...), ``dasslc``, ``emso``, ``hysys``,
       ``aspen``.
   * - ``reg``
     - ``0``
     - Regularization function option (only when the interpolation is not
       ``'stage'``).
   * - ``sampling``
     - ``50``
     - Number of sampling points in each stage.
   * - ``speed_factor``
     - ``0``
     - Tries to speed up the solution; may reduce its quality.

Case study (``in_SPAIDER.casestudy``)
-------------------------------------

.. list-table::
   :header-rows: 1
   :widths: 25 20 55

   * - Field
     - Example
     - Description
   * - ``status``
     - ``'off'``
     - ``'on'`` repeats the run several times, e.g. to compare thresholds.
   * - ``iter``
     - ``'16'``
     - Number of repetitions (as a string).

Plots (``in_SPAIDER.plot``)
---------------------------

.. list-table::
   :header-rows: 1
   :widths: 25 20 55

   * - Field
     - Example
     - Description
   * - ``control``
     - ``'on'``
     - Plot the control profile after each iteration.
   * - ``state``
     - ``0``
     - ``1`` to plot the state trajectories.
   * - ``plot_after``
     - ``'off'``
     - ``'on'`` only plots results already stored in a ``.mat`` file,
       without solving.
   * - ``tf_p``
     - ``250``
     - Final time used for the plots.
   * - ``record``
     - ``'off'``
     - Save the generated figures.
   * - ``video``
     - ``'off'``
     - Record a video of the refinement of the control profile.

Adaptive wavelets (``in_SPAIDER.wavelets``)
-------------------------------------------

.. list-table::
   :header-rows: 1
   :widths: 25 20 55

   * - Field
     - Example
     - Description
   * - ``procedure``
     - ``'on'``
     - ``'on'`` for wavelet-based adaptive refinement, ``'off'`` for
       uniform refinement from ``is0`` to ``isF``.
   * - ``wname``
     - ``'db1'``
     - Wavelet family: ``db1``, ``db2``... ``db4``, ``'mayer'``.
   * - ``thresholding``
     - ``'automatic'``
     - How the threshold is chosen: ``'automatic'``, ``'norm-based'`` or
       ``'fixed'``.
   * - ``tptr``
     - ``'heursure'``
     - Threshold rule for ``'automatic'``: ``'rigrsure'``,
       ``'heursure'``, ``'sqtwolog'``, ``'gcv'``, ``'bayes'``,
       ``'cvpshrink'``.
   * - ``sorh``
     - ``'h'``
     - ``'h'`` hard or ``'s'`` soft thresholding.
   * - ``scal``
     - ``'sln'``
     - Threshold rescaling: ``'sln'``, ``'mln'`` or ``'one'``.
   * - ``norm_threshold``
     - ``0.8``
     - Threshold for ``'norm-based'``.
   * - ``fix_threshold``
     - ``1e-5``
     - Threshold for ``'fixed'``.
   * - ``max_refinement``
     - ``128``
     - Maximum number of stages.
   * - ``refinement_position``
     - ``0.44``
     - Position of the new mesh point inside a refined stage, between
       0.1 and 0.9.
   * - ``delt``
     - ``1e-56``
     - Small numerical tolerance used in the refinement.
   * - ``rel``
     - ``'on'``
     - Write the thresholds of each iteration to the Excel report.

Horizon and initial guess (``input_model.m``)
---------------------------------------------

These options are returned by ``input_model`` in the ``input`` structure:
``t0``, ``tf``, ``x0``, ``nU``, ``u_lb``, ``u_ub``, ``u0``, ``is0``,
``isF``, ``x0_lb``, ``x0_ub``. See :doc:`usage` for their meaning.
``is0`` sets the first mesh (``2^is0`` stages) and ``isF`` the last
iteration of the adaptive algorithm.
