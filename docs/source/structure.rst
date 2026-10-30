Code structure
==============

This page describes the layout of the
`SpAIDER repository <https://github.com/LizandroCloud/SpAIDER>`_.

.. code-block:: text

   SpAIDER/
   ├── spaider_main.m          entry point called by the problem scripts
   ├── spaider.m               adaptive single-shooting algorithm
   ├── spaider_conv.m          convergence criteria between iterations
   ├── functions/              objective, constraints and NLP call per solver
   ├── utilities/              model generation, derivatives, mesh, controls
   ├── wavelets/               thresholding and wavelet-based mesh refinement
   ├── dasslc/                 DASSLC DAE solver (C source and MEX files)
   ├── plot_tools/             plots of controls, states and wavelet details
   ├── savefigs/               figure export
   ├── xlsPasteTo/             Excel report helpers
   ├── test_routines/          tests and experiments
   ├── problems_sequential/    example problems (single shooting)
   └── problems_wav_colloc/    example problems (wavelet collocation)

Execution flow
--------------

1. The problem script (``problem_<name>.m``) runs ``startup.m``, sets the
   options and calls ``spaider_main``.
2. ``spaider_main`` reads the model from ``input_model.m``, translates the
   text options, creates the results folder and starts the log.
3. ``spaider`` initializes the variables (``utilities/initialization.m``)
   and writes the model, objective and constraint functions of the problem
   folder (``utilities/write_models.m``, ``write_obj.m``, ``write_cr.m``),
   deriving the sensitivity equations symbolically (``utilities/dyn.m``).
4. At every iteration ``spaider`` calls ``functions/runobjconstr.m``, which
   runs ``fmincon``. The objective and constraints are evaluated by the
   ``objfunc_<solver>.m`` and ``constr_<solver>.m`` functions, which
   integrate the model with the chosen solver.
5. The optimal profile is analysed by the routines in ``wavelets/``, and
   the mesh for the next iteration is refined where the thresholded detail
   coefficients are significant (``utilities/meshref.m``).
6. ``spaider_conv`` checks convergence. When the run ends, ``spaider_main``
   saves the ``.mat`` file and the Excel report.

Main folders
------------

``functions/``
   One set of functions per integrator or simulator: ``objfunc_ode.m``,
   ``objfunc_ode15s.m``, ``objfunc_ode23s.m``, ``objfunc_dasslc.m``,
   ``objfunc_emso.m``, ``objfunc_unisim.m``... with the matching
   ``constr_*.m`` and ``function_*.m``. ``runobjconstr.m`` wraps the call to
   ``fmincon``.

``utilities/``
   Code generation from ``input_model.m`` (``write_models.m``,
   ``write_obj.m``, ``write_cr.m``, ``write_alg.m``), symbolic derivatives
   and Jacobians (``dyn.m``, ``jacmat*.m``), mesh refinement
   (``meshref.m``), control interpolation (``ver_reg*.m``, ``u_reg*.m``)
   and helpers such as ``dae_default.m`` and ``spaider_message.m``.

``wavelets/``
   Threshold selection (``wav_thresh.m``, ``GCVsoft.m``, ``ST.m``),
   denoising (``spaider_wden.m``) and the wavelet mesh (``wav_mesh.m``).

``dasslc/``
   DASSLC (Differential-Algebraic System Solver in C), with its MATLAB
   interface and precompiled Windows MEX files.

``plot_tools/``
   Plots of the control profile (``g_control.m``), states (``g_state.m``),
   constraints and wavelet details (``g_wavedet.m``).
