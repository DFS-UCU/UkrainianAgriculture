import os
import shapefile

directory = "../data/czech/"

count = 0

counter = {}

for filename in os.listdir(directory):
    if filename.endswith(".shp"): 
        filepath = os.path.join(directory, filename)
        sf = shapefile.Reader(filepath)
        shapes = sf.shapes()
        records = sf.records()
        for record in sf.records():
            count = count + 1
    else:
        pass

print(count)