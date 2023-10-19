import os
import rasterio
import numpy as np

input_folder = r"path"
output_folder = r"path"

def process_classification_map(input_folder, output_folder):
    files = os.listdir(input_folder)

    for file in files:
        if file.endswith('.tif'):
            input_path = os.path.join(input_folder, file)
            output_path = os.path.join(output_folder, file)

            with rasterio.open(input_path) as src:
                profile = src.profile.copy()
                profile.update(compress='lzw', nodata=0)

                classification_map = src.read(1)

                
                modified_map = np.zeros_like(classification_map, dtype=np.uint8)
                modified_map[classification_map == 4] = 1
                modified_map[np.logical_and(classification_map >= 5, classification_map <= 7)] = 2
                modified_map[np.logical_and(classification_map >= 8, classification_map <= 10)] = 3

                with rasterio.open(output_path, 'w', **profile) as dst:
                    dst.write(modified_map, 1)


process_classification_map(input_folder, output_folder)
