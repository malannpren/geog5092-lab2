#!/usr/bin/env python
# coding: utf-8

# In[83]:


#part 1

import pandas as pd
import geopandas as gpd
import glob
from shapely.geometry import Polygon
import numpy as np

# open text files

polylist = []
polydict = {'num_coords': [], 'district': [], 'geometry': []}
crs={'init': 'epsg:4326'}

file_names = glob.glob('*.txt')

for item in file_names:
    district = item[-6:-4]
    df = pd.read_csv(item, sep='\t')
    df['X'] = df['X'].astype(float)
    df['Y'] = df['Y'].astype(float)
    
    # create a polygon from each file
    
    coordinates = list(zip(df['X'],df['Y']))
    num_coords = len(coordinates)
    poly = Polygon(coordinates)
    polydict['num_coords'].append(num_coords)
    polydict['district'].append(district)
    polydict['geometry'].append(poly)
    
polydict_gdf = gpd.GeoDataFrame(polydict, crs = crs)

#converting the districts to shp
polydict_shp = proj_polydict.to_file('shp')


# In[88]:


# part 2

import rasterstats
from rasterstats import zonal_stats

workspace = r'C:\Users\catan\Desktop\GEOG5092\lab2\lab2_data\data\agriculture'
img_list = glob.glob(workspace+r'.\\*.tif')

x_df = pd.DataFrame()
for img in img_list:
    output = img[-13:-9]
    x = zonal_stats(polydict_gdf, img,
            stats="count sum")
    output = pd.DataFrame(x)
    output['district'] = polydict_gdf['district']
    output['year'] = img[-13:-9]
    output['percent_cover'] = (output['sum']/output['count'] * 100)
    x_df = x_df.append(output)
    
for index, row in x_df.iterrows():
    print("In", row['year'], ", district", row['district'], "was", row['percent_cover'],"% agricultural land")





