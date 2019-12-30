
#TOOL TO CALCULATE ATTRIBUTE VALUE OF A POINT BASED ON ITS SPATIAL RELATIONSHIP WITHIN A POLYGON AND USE A USER-CHOICE ATTRIBUTE OF THE POLYGON
#TO UPDAT A USER-CHOICE ATTRIBUTE IN THE POINT
import arcpy
update_feature_class = arcpy.GetParameterAsText(0)
poly_feature_class = arcpy.GetParameterAsText(1)
update_name = arcpy.GetParameterAsText(2)
poly_name = arcpy.GetParameterAsText(3)

poly_count = 0
relateDict = {}
# Set up search cursor for poly fc
with arcpy.da.SearchCursor(poly_feature_class,[poly_name,'SHAPE@']) as search_cursor:

    # Iterate through polygons
    for polygon in search_cursor:
        if not polygon[0] in relateDict:
            relateDict[polygon[0]] = polygon[1]
        else:
            relateDict[polygon[0]] = relateDict[polygon[0]].union(polygon[1])

poly_names = []
for name in sorted(relateDict):
    poly_names.append(name)
    poly_count += 1

point_count = 0
comparison_count = 0
# Set up update cursor for point fc
with arcpy.da.UpdateCursor(update_feature_class, ['SHAPE@', update_name]) as update_cursor:

    # Iterate through points
    for point in update_cursor:
        point_count += 1
        name_list = []
        for name in poly_names:
            comparison_count += 1
            poly = relateDict[name]
            # Check if the current point is within the current polygon
            if point[0].within(poly):  # Returns True or False
                # Add the polygon name to the list
                name_list.append(name)
        point[1] = ",".join(name_list)
        # Update the cursor with the new value
        update_cursor.updateRow(point)
arcpy.AddMessage("Processed {0} Polygon/Point comparisons for {1} Polygons and {2} Points".format(comparison_count, poly_count, point_count))




