import arcpy
import numpy as np
update_feature_class = arcpy.GetParameterAsText(0)
source_dem= arcpy.GetParameterAsText(1)
elev_attrib= arcpy.GetParameterAsText(2)

#SET MULTIPLE SOURCES FOR RASTER DEMS
#HERE WE GIVE THE USER 4 CHOICES FROM 2 PHYSICAL NETWORK LOCATIONS
if str(source_dem) == 'Twin Creeks: Elevation in Feet':
    dem = '\\\\inpgrsms06vm\\GISDATA\\GIS_Final\\data\\basedata\\elevation\\GRSM_10MDEM_2180604\\grsm10dem'
if str(source_dem) == 'Twin Creeks: Elevation in Meters':
    dem = '\\\\inpgrsms06vm\\GISDATA\\GIS_Final\\data\\basedata\\elevation\\GRSM_10DEM_Meters_2180603\\mgrsm10dem'
if str(source_dem) == 'HQ: Elevation in Feet':
    dem = '\\\\inpgrsms05vm\\GISDATA\\GIS_Final\\data\\basedata\\elevation\\GRSM_10MDEM_2180604\\grsm10dem'
if str(source_dem) == 'HQ: Elevation in Meters':
    dem = '\\\\inpgrsms05vm\\GISDATA\\GIS_Final\\data\\basedata\\elevation\\GRSM_10DEM_Meters_2180603\\mgrsm10dem' 


rast = arcpy.Raster(dem)
desc = arcpy.Describe(rast)

ulx = desc.Extent.XMin
uly = desc.Extent.YMax
lly = desc.Extent.YMin
#Spatialrefernce
sr = desc.spatialReference


rstArray  = arcpy.RasterToNumPyArray(rast)

with arcpy.da.UpdateCursor(update_feature_class,["SHAPE@",elev_attrib]) as uc:
    for row in uc:
        pnt = row[0].projectAs(sr)
        #assuming every point falls to the left and below uperleft corner
        deltaX = pnt.centroid.X - ulx
        deltaY = lly- pnt.centroid.Y
        arow = int(deltaY/rast.meanCellHeight)
        acol = int(deltaX/rast.meanCellWidth)
        row[1] = rstArray[arow,acol]
        uc.updateRow(row)









        



        



  


















