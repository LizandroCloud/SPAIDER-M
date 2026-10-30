Installation
============

SPAIDER is a collection of MATLAB scripts. There is no installer: you
download the source code and let each problem's ``startup.m`` add the SPAIDER
folders to the MATLAB path.

Requirements
------------

- **MATLAB.** SPAIDER was developed and tested on MATLAB for Windows.
- **Optimization Toolbox**, for ``fmincon``, which solves the NLP problem.
- **Symbolic Math Toolbox**, used to derive the sensitivity equations and
  the gradients of the objective function and constraints from the model
  written in ``input_model.m``.
- **Wavelet Toolbox**, used by the adaptive mesh refinement (wavelet
  decomposition and thresholding).
- **Parallel Computing Toolbox** (optional), only for
  ``problem.algorithm = 'parallel'``.
- **Microsoft Excel** (optional). Result reports are written with
  ``xlswrite``.

.. note::

   Some paths are built with Windows separators (``\``) and the DASSLC solver
   ships with precompiled Windows binaries (``.mexw32``/``.mexw64``). On Linux
   or macOS use a MATLAB solver such as ``ode45`` or ``ode15s``, and expect to
   adapt the result folder paths.

Getting the source code
-----------------------

Clone the repository with Git:

.. code-block:: console

   $ git clone https://github.com/LizandroCloud/SpAIDER.git

or download it as a ZIP file from
`GitHub <https://github.com/LizandroCloud/SpAIDER>`_ and extract it.

Setting the MATLAB path
-----------------------

You do not need to edit the MATLAB path by hand. Every problem folder
contains a ``startup.m`` that goes three levels up from the problem folder to
the SPAIDER root and adds the following folders to the path:

.. code-block:: matlab

   path(path, path0);                     % SPAIDER root
   path(path, [path0 '/dasslc/']);
   path(path, [path0 '/plot_tools/']);
   path(path, [path0 '/test_routines']);
   path(path, [path0 '/utilities']);
   path(path, [path0 '/wavelets']);
   path(path, [path0 '/functions']);

Because the root is found by relative position, a problem folder must sit
exactly two levels below a folder inside the SPAIDER root, for example
``problems_sequential/matlab/<your problem>/``.

Checking the installation
-------------------------

Open MATLAB, change to the folder of the bundled example and run it:

.. code-block:: matlab

   cd 'problems_sequential/matlab/Problem.1A - SemiBacth Ishothermal CSTR Reactor (Srinavasan et al. 2003) (fixT-endC-sU) (+)'
   problem_1A

The welcome banner and the ``fmincon`` iteration log should appear in the
Command Window, followed by the plot of the control profile. See
:doc:`examples` for what this problem solves.
