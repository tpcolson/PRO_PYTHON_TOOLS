#TOOL TO CALCULATE ATTRIBUTE VALUE OF A POINT BASED ON ITS SPATIAL RELATIONSHIP TO NEAREST LINE AND USE A USER-CHOICE ATTRIBUTE OF THE LINE
#TO UPDAT A USER-CHOICE ATTRIBUTE IN THE POINT
from time import strftime  
print("Script Start: " + strftime("%Y-%m-%d %H:%M:%S"))
import arcpy
currgdb = arcpy.mp.ArcGISProject("CURRENT").defaultGeodatabase
update_feature_class = arcpy.GetParameterAsText(0)
polyline_feature_class = arcpy.GetParameterAsText(1)
update_name = arcpy.GetParameterAsText(2)
polyline_name = arcpy.GetParameterAsText(3)
#Feature class to be updated
#Feature class containing the attribute we want is nearest

arcpy.MakeFeatureLayer_management(update_feature_class,"update_lyr")
arcpy.MakeFeatureLayer_management(polyline_feature_class,"near_lyr")

print("Created Layers: " + strftime("%Y-%m-%d %H:%M:%S"))
#create a temporary table of near results
out_table = currgdb+'\\LOCATIONS_CLOSE'
if arcpy.Exists(out_table):
  arcpy.Delete_management(out_table)
  print("Deleted Near Table: " + strftime("%Y-%m-%d %H:%M:%S"))

arcpy.GenerateNearTable_analysis("update_lyr", "near_lyr", out_table)
  
print("Generated Near Table:" + strftime("%Y-%m-%d %H:%M:%S"))
#create a list of attributes from the near feature class where
#the second field is the attribute we want to know is the nearest
nearFieldsList = ["OBJECTID",polyline_name]
nearDict = {r[0]:r[1] for r in arcpy.da.SearchCursor("near_lyr", nearFieldsList)}

matchFieldsList = ["IN_FID", "NEAR_FID"]
matchDict = {r[0]:nearDict[r[1]] for r in arcpy.da.SearchCursor(out_table, matchFieldsList)}
#write the nearest attribute to the update feature class
#where the second field is the attribute that is being updated with
#the name of the nearest feature
updateFieldsList = ["OBJECTID", update_name]
with arcpy.da.UpdateCursor("update_lyr", updateFieldsList) as updateRows:  
    for updateRow in updateRows:  
        keyValue = updateRow[0]  
        # verify that the keyValue is in the Dictionary  
        if keyValue in matchDict:  
             updateRow[1] = matchDict[keyValue]  
             updateRows.updateRow(updateRow)
  
print("Updated Features: " + strftime("%Y-%m-%d %H:%M:%S"))

del nearDict
del matchDict  
print("Script Finish: " + strftime("%Y-%m-%d %H:%M:%S"))



