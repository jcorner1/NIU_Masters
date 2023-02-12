import xarray as xr
import pandas as pd
import numpy as np
import os
import sys
import datetime as dt
import glob

#interate through the files in system files inputted through the command line.
for path in sys.argv:
    name = str(path)
    print(f'Trying file: {name}')
    
    #Allow only the netCDF file to be opened.
    if name[-4:] == '.nc4':
        print('Correct file found')
        
        #open the file and save off reflectivity data. Data must be flipped for the purpose of MET
        ds = xr.open_dataset(name)
        ref = ds.mrms_lcref.values
        met_data = np.flip(ref, axis = 0)

#Create init time from pathfile name. obs data needs no valid time, but MET does!        
init = dt.datetime.strptime(f'{name[-16:-4]}00', '%Y%m%d%H%M%S')
valid =  init


#Add attributes needed to reference data for MET        
attrs = {
        'valid': valid.strftime("%Y%m%d_%H%M%S"),
        'init':  init.strftime("%Y%m%d_%H%M%S"),
        'lead':  '00',
        'accum': '00',
        'name' : 'reflectivity',
        'long_name': 'Reflectivity',
        'level' : 'surface',
        'units' : 'dBZ',
        
        'grid': {
            'long_name': 'Reflectivity',
            'name' : 'reflectivity',
            'type' : 'LatLon',
            #'hemisphere' : 'N',
            'Nlon' : 7000.0,
            'Nlat' : 3500.0,
            'lat_ll' : 20.0,
            'lon_ll' : -130.0,
            'delta_lat' : 0.01,
            'delta_lon' : 0.01,
            }
        }