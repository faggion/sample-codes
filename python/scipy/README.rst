

.. code-block:: none
  
  sudo port install fortrancl
  ls /opt/local/bin/gfortran-mp-4.7
  sudo ln -s /opt/local/bin/gfortran-mp-4.7 /opt/local/bin/gfortran
  sudo ln -s /opt/local/bin/gfortran-mp-4.7 /opt/local/bin/gfortran-mp
  pip install scipy
  pip install pybrain
  sudo port install glpk
  pip install cvxopt
  pip install openopt
  pip install FuncDesigner


.. code-block:: none
  
  source 2.7.2/bin/activate
  # install http://cran.r-project.org/bin/macosx/tools/gfortran-4.2.3.pkg
  xcode-select --install
  curl -o install_superpack.sh https://raw.github.com/fonnesbeck/ScipySuperpack/master/install_superpack.sh
  sh install_superpack.sh
