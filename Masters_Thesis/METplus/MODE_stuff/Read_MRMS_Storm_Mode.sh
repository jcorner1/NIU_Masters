#!/bin/bash

#MET needs the location of python set if the libs are ran and built different.

export MET_PYTHON_EXE=/gpfs/fs1/home/ac.jcorner/anaconda3/bin/python3

/gpfs/fs1/home/ac.jcorner/NIU/Masters_Thesis/MET_10.1.2/bin/plot_data_plane PYTHON_NUMPY test_out.ps 'name="Read_MRMS_Storm_Mode.py /lcrc/project/rainfall/jcorner/MODE_data/202006300000/isolated_cell/mrms_lcref202006300000.nc4";'