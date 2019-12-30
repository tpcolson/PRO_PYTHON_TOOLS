
#TOOL TO CALCULATE COORDINATES WITH  USER INPUT CHOICE OF UTM ZONE
import sys, os, arcpy
import errno
import traceback  
from arcpy import env 
#Get user input
fc_name = arcpy.GetParameterAsText(0)
want_utm = arcpy.GetParameterAsText(1)
utm_zone = arcpy.GetParameterAsText(2)
x_field = arcpy.GetParameterAsText(3)
y_field = arcpy.GetParameterAsText(4)
want_ll = arcpy.GetParameterAsText(5)
spa_ref = arcpy.GetParameterAsText(6)
lat = arcpy.GetParameterAsText(7)
lon = arcpy.GetParameterAsText(8)

if utm_zone == "1":
    epsg = "26901"
if utm_zone == "2":
    epsg = "26902"
if utm_zone == "3":
    epsg = "26903"
if utm_zone == "4":
    epsg = "26904"
if utm_zone == "5":
    epsg = "26905"
if utm_zone == "6":
    epsg = "26906"
if utm_zone == "7":
    epsg = "26907"
if utm_zone == "8":
    epsg = "26908"
if utm_zone == "9":
    epsg = "26909"
if utm_zone == "10":
    epsg = "26910"
if utm_zone == "11":
    epsg = "26911"
if utm_zone == "12":
    epsg = "26912"
if utm_zone == "13":
    epsg = "26913"
if utm_zone == "14":
    epsg = "26914"
if utm_zone == "15":
    epsg = "26915"
if utm_zone == "16":
    epsg = "26916"
if utm_zone == "17":
    epsg = "26917"
if utm_zone == "18":
    epsg = "26918"
if utm_zone == "19":
    epsg = "26919"
if utm_zone == "20":
    epsg = "26920"
if utm_zone == "21":
    epsg = "26921"
if spa_ref == "WGS 84":
    llepsg = "4326"
if spa_ref == "GCS NAD83":
    llepsg = "4269"
    




if str(want_utm) == 'true':
    arcpy.CalculateField_management(fc_name, x_field, "arcpy.PointGeometry(!Shape.centroid!,!Shape.spatialReference!).projectAs(arcpy.SpatialReference("+epsg+")).firstPoint.X","PYTHON_9.3","#")
    arcpy.CalculateField_management(fc_name, y_field, "arcpy.PointGeometry(!Shape.centroid!,!Shape.spatialReference!).projectAs(arcpy.SpatialReference("+epsg+")).firstPoint.Y","PYTHON_9.3","#")

if str(want_ll) == 'true':
    arcpy.CalculateField_management(fc_name, "LON", "arcpy.PointGeometry(!Shape.centroid!,!Shape.spatialReference!).projectAs(arcpy.SpatialReference("+llepsg+")).firstPoint.X","PYTHON_9.3","#")
    arcpy.CalculateField_management(fc_name, "LAT", "arcpy.PointGeometry(!Shape.centroid!,!Shape.spatialReference!).projectAs(arcpy.SpatialReference("+llepsg+")).firstPoint.Y","PYTHON_9.3","#")





    














