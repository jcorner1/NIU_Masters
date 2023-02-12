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
  
    #Allow the netCDF file to work
    if name[-4:] == '.nc4':
        print('Correct file found')
        
        #open the file and save off reflectivity data. Data must be flipped for the purpose of MET
        ds = xr.open_dataset(name)
        ref = ds.refc.values
        met_data = np.flip(ref, axis = 0)
        
        #create forecast hour from pathfile name.
        fhour = path[-6:-4]
        
#create the initial time from path and calculate valid time with forecast hour.        
init = dt.datetime.strptime(str(ds.time.values)[0:19], '%Y-%m-%dT%H:%M:%S' )
valid = init + dt.timedelta(hours = int(fhour))


#Add attributes needed to reference data for MET
attrs = {
        'valid': valid.strftime("%Y%m%d_%H%M%S"),
        'init':  init.strftime("%Y%m%d_%H%M%S"),
        'lead':  fhour,
        'accum': '00',
        'name': 'Reflectivity',
    
        'GRIB_name' : 'Maximum/Composite radar reflectivity',
        'GRIB_shortName' : 'refc',
        'GRIB_units' : 'dB',
        'long_name' : 'Maximum/Composite radar reflectivity',
        'units' : 'dB',
        'type' : 'Lambert Conformal',
        'level' : 'surface',
        
        'grid': {
            'GRIB_paramId' : 260390,
            'GRIB_dataType' : 'fc',
            'GRIB_numberOfPoints' : 1905141,
            'GRIB_typeOfLevel' : 'atmosphere',
            'GRIB_stepUnits' : 1,
            'GRIB_stepType' : 'instant',
            'GRIB_gridType' : 'lambert',
            'GRIB_DxInMetres' : 3000.0,
            'GRIB_DyInMetres' : 3000.0,
            'GRIB_LaDInDegrees' : 38.5,
            'GRIB_Latin1InDegrees' : 38.5,
            'GRIB_Latin2InDegrees' : 38.5,
            'GRIB_LoVInDegrees' : 262.5,
            'GRIB_NV' : 0,
            'GRIB_Nx' : 1799,
            'GRIB_Ny' : 1059,
            'GRIB_cfName' : 'unknown',
            'GRIB_cfVarName' : 'unknown',
            'GRIB_gridDefinitionDescription' : 'Lambert Conformal can be secant or tangent, conical or bipolar',
            'GRIB_iScansNegatively' : 0,
            'GRIB_jPointsAreConsecutive' : 0,
            'GRIB_jScansPositively' : 1,
            'GRIB_latitudeOfFirstGridPointInDegrees' : 21.138123,
            'GRIB_latitudeOfSouthernPoleInDegrees' : 0.0,
            'GRIB_longitudeOfFirstGridPointInDegrees' : 237.280472,
            'GRIB_longitudeOfSouthernPoleInDegrees' : 0.0,
            'GRIB_missingValue' : 9999,
            'name': 'Reflectivity',
            'type' : 'Lambert Conformal',
            'hemisphere' : 'N',
            'nx' : 1799,
            'ny' : 1059,
            'scale_lat_1' : 38.5,
            'scale_lat_2' : 38.5,
            'd_km' : 3.0, 
            'r_km' : 6367.47,
            'lon_orient' : 262.5,
            'lat_pin' : 21.13812300000003,
            'x_pin' : 0.0,
            'y_pin' : 0.0
            }
        }        
        
