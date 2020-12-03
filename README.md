# geog5092-lab2
Lab 2 for GEOG 5092, Fall 2020

Completed by Mallory Prentiss

Goal: Learn to encode vector geometry. Gain familiarity with Shapely,and Geopandas properties.

Task: You will encode the text files into polygon features. Then you will calculate percentage of agricultural land in each polygon in 2004 and in 2009 using the GlobCover rasters.

Part I:
1) Read the text files and extract the x, y coordinates for each district.
2) Create a polygon fromeach file and create a geodataframe with the following two fields: ‘num_coords’ and ‘district’. populatethe correspondingvalue for the twofieldsyou added. ‘num_coords’ should contain the number of vertices, or coordinate pairs, used to encode each polygon. ‘districts’ should be the suffix of each text file (i.e., ‘01’, ‘05’ or ‘06’). 
Hint: steps 1 and 2 should be done concurrently as you encode the polygons.
TIP: What are the methods to create a geodataframe? Which data structure allows for data schema (pre-defined data structure such as column names)

Part II:
1) Calculate the number of agricultural pixels in each district (i.e., each polygon) in 2004 and in 2009.
2) In a final print statement, reportthe amountof agricultural landas a percentage of the total number of pixels ineach districtin 2004 and in 2009 (i.e., print these six values). Go through the single steps very carefully and make use of the Geopandas and Shapely documentationto find out more about usage and the required.Make efficient use of help forums and blogs as well.

Hint: Which GIS process would you use to calculate the number of pixels within each district? Is there a python packagethat provide this functionality? If so, howdo you install it?
