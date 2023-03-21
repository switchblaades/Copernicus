from glob import glob
import rasterio
import os
import numpy as np
import numpy.ma as ma

fileB04 = glob('*B04*'+'*.jp2')
fileB08 = glob('*B08*'+'*.jp2')

with rasterio.open(os.path.join(os.getcwd(), fileB04[0]), 'r') as raster04:
    #print(raster04.profile)
    raster_data04 = raster04.read(1)
	
with rasterio.open(os.path.join(os.getcwd(), fileB08[0]), 'r') as raster08:
    #print(raster04.profile)
    raster_data08 = raster08.read(1)
	
NDVI = (raster_data08a-raster_data04)/(raster_data08+raster_data04)

mask = np.logical_and(NDVI > 0.35, NDVI < 0.5)
profile.update({"driver": "GTiff",
             "compress": 'lzw'})
			
with rasterio.open('mask02.tif', 'w', **profile) as out:
    out.write(mask,1)
    