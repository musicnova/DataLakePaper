#!/bin/sh
rm -f /home/user/anaconda3/conda-bld/linux-64/datalakeplan-0.0.*-py35_0.tar.bz2
# READ https://conda.io/docs/user-guide/tutorials/build-pkgs-skeleton.html
conda skeleton pypi datalakeplan
conda-build --python 3.5 datalakeplan && conda install --use-local datalakeplan && anaconda upload /home/user/anaconda3/conda-bld/linux-64/datalakeplan-0.0.*-py35_0.tar.bz2
