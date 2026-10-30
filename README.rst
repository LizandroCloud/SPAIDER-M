SPAIDER documentation
=====================

Source of the SPAIDER documentation published on Read the Docs.
SPAIDER (Sequential and Parallel Algorithms Integrated to Differential
Equation Routines) is a MATLAB toolbox for dynamic optimization and optimal
control. Its source code lives at https://github.com/LizandroCloud/SpAIDER.

Building locally
----------------

.. code-block:: console

   $ pip install -r docs/requirements.txt
   $ sphinx-build -b html docs/source docs/build/html

Open ``docs/build/html/index.html`` in a browser. Read the Docs builds the
same configuration from ``.readthedocs.yaml`` on every push.
