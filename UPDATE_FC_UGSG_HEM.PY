#UPDATES A FC USING THE USGS HEM SCHEMA 
import sys, os, arcpy
import errno
import traceback  
from arcpy import env 
#Get user input
gdb_name = arcpy.GetParameterAsText(0)
fc_name = arcpy.GetParameterAsText(1)



#Create required PERMANENT Field
try:
        in_Field = "PERMANENT_IDENTIFIER"
        if len(arcpy.ListFields(fc_name,in_Field))>0:
                arcpy.AddWarning (in_Field+" exits already")
        else:
                arcpy.AddField_management(fc_name, in_Field, "TEXT", "", "", 40, in_Field, "NULLABLE", "NON_REQUIRED")
                arcpy.AddMessage ("Sasquatch created the "+in_Field+" field")
except arcpy.ExecuteError:
        msgs = arcpy.GetMessages(2)
        arcpy.AddError(msgs)
except:
        tb = sys.exc_info()[2]
        tbinfo = traceback.format_tb(tb)[0]
        pymsg = "PYTHON ERRORS:\nTraceback info:\n" + tbinfo + "\nError Info:\n" + str(sys.exc_info()[1])
        msgs = "ArcPy ERRORS:\n" + arcpy.GetMessages(2) + "\n"
        arcpy.AddError(pymsg)
        arcpy.AddError(msgs)

#Create required EVENTDATE Field
try:
        in_Field = "EVENTDATE"
        if len(arcpy.ListFields(fc_name,in_Field))>0:
                arcpy.AddWarning (in_Field+" exits already")
        else:
                arcpy.AddField_management(fc_name, in_Field, "DATE", "", "", "", in_Field, "NULLABLE", "NON_REQUIRED")
                arcpy.AddMessage ("Sasquatch created the "+in_Field+" field")
except arcpy.ExecuteError:
        msgs = arcpy.GetMessages(2)
        arcpy.AddError(msgs)
except:
        tb = sys.exc_info()[2]
        tbinfo = traceback.format_tb(tb)[0]
        pymsg = "PYTHON ERRORS:\nTraceback info:\n" + tbinfo + "\nError Info:\n" + str(sys.exc_info()[1])
        msgs = "ArcPy ERRORS:\n" + arcpy.GetMessages(2) + "\n"
        arcpy.AddError(pymsg)
        arcpy.AddError(msgs)
		
#Create required REACHCODE Field
try:
        in_Field = "REACHCODE"
        if len(arcpy.ListFields(fc_name,in_Field))>0:
                arcpy.AddWarning (in_Field+" exits already")
        else:
                arcpy.AddField_management(fc_name, in_Field, "TEXT", "", "", 14, in_Field, "NULLABLE", "NON_REQUIRED")
                arcpy.AddMessage ("Sasquatch created the "+in_Field+" field")
except arcpy.ExecuteError:
        msgs = arcpy.GetMessages(2)
        arcpy.AddError(msgs)
except:
        tb = sys.exc_info()[2]
        tbinfo = traceback.format_tb(tb)[0]
        pymsg = "PYTHON ERRORS:\nTraceback info:\n" + tbinfo + "\nError Info:\n" + str(sys.exc_info()[1])
        msgs = "ArcPy ERRORS:\n" + arcpy.GetMessages(2) + "\n"
        arcpy.AddError(pymsg)
        arcpy.AddError(msgs)
		
#Create required REACHSMDATE Field
try:
        in_Field = "REACHSMDATE"
        if len(arcpy.ListFields(fc_name,in_Field))>0:
                arcpy.AddWarning (in_Field+" exits already")
        else:
                arcpy.AddField_management(fc_name, in_Field, "DATE", "", "", "", in_Field, "NULLABLE", "NON_REQUIRED")
                arcpy.AddMessage ("Sasquatch created the "+in_Field+" field")
except arcpy.ExecuteError:
        msgs = arcpy.GetMessages(2)
        arcpy.AddError(msgs)
except:
        tb = sys.exc_info()[2]
        tbinfo = traceback.format_tb(tb)[0]
        pymsg = "PYTHON ERRORS:\nTraceback info:\n" + tbinfo + "\nError Info:\n" + str(sys.exc_info()[1])
        msgs = "ArcPy ERRORS:\n" + arcpy.GetMessages(2) + "\n"
        arcpy.AddError(pymsg)
        arcpy.AddError(msgs)
		
#Create required REACHRESOLUTION Field
try:
        in_Field = "REACHRESOLUTION"
        if len(arcpy.ListFields(fc_name,in_Field))>0:
                arcpy.AddWarning (in_Field+" exits already")
        else:
                arcpy.AddField_management(fc_name, in_Field, "LONG", "10", "", "", in_Field, "NULLABLE", "NON_REQUIRED")
                arcpy.AddMessage ("Sasquatch created the "+in_Field+" field")
except arcpy.ExecuteError:
        msgs = arcpy.GetMessages(2)
        arcpy.AddError(msgs)
except:
        tb = sys.exc_info()[2]
        tbinfo = traceback.format_tb(tb)[0]
        pymsg = "PYTHON ERRORS:\nTraceback info:\n" + tbinfo + "\nError Info:\n" + str(sys.exc_info()[1])
        msgs = "ArcPy ERRORS:\n" + arcpy.GetMessages(2) + "\n"
        arcpy.AddError(pymsg)
        arcpy.AddError(msgs)
		
#Create required FEATURE_PERMANENT_IDENTIFIER Field
try:
        in_Field = "FEATURE_PERMANENT_IDENTIFIER"
        if len(arcpy.ListFields(fc_name,in_Field))>0:
                arcpy.AddWarning (in_Field+" exits already")
        else:
                arcpy.AddField_management(fc_name, in_Field, "TEXT", "", "", 40, in_Field, "NULLABLE", "NON_REQUIRED")
                arcpy.AddMessage ("Sasquatch created the "+in_Field+" field")
except arcpy.ExecuteError:
        msgs = arcpy.GetMessages(2)
        arcpy.AddError(msgs)
except:
        tb = sys.exc_info()[2]
        tbinfo = traceback.format_tb(tb)[0]
        pymsg = "PYTHON ERRORS:\nTraceback info:\n" + tbinfo + "\nError Info:\n" + str(sys.exc_info()[1])
        msgs = "ArcPy ERRORS:\n" + arcpy.GetMessages(2) + "\n"
        arcpy.AddError(pymsg)
        arcpy.AddError(msgs)

#Create required FEATURECLASSREF Field
try:
        in_Field = "FEATURECLASSREF"
        if len(arcpy.ListFields(fc_name,in_Field))>0:
                arcpy.AddWarning (in_Field+" exits already")
        else:
                arcpy.AddField_management(fc_name, in_Field, "LONG", "10", "", "", in_Field, "NULLABLE", "NON_REQUIRED")
                arcpy.AddMessage ("Sasquatch created the "+in_Field+" field")
except arcpy.ExecuteError:
        msgs = arcpy.GetMessages(2)
        arcpy.AddError(msgs)
except:
        tb = sys.exc_info()[2]
        tbinfo = traceback.format_tb(tb)[0]
        pymsg = "PYTHON ERRORS:\nTraceback info:\n" + tbinfo + "\nError Info:\n" + str(sys.exc_info()[1])
        msgs = "ArcPy ERRORS:\n" + arcpy.GetMessages(2) + "\n"
        arcpy.AddError(pymsg)
        arcpy.AddError(msgs)
		
#Create required SOURCE_ORIGINATOR Field
try:
        in_Field = "SOURCE_ORIGINATOR"
        if len(arcpy.ListFields(fc_name,in_Field))>0:
                arcpy.AddWarning (in_Field+" exits already")
        else:
                arcpy.AddField_management(fc_name, in_Field, "TEXT", "", "", 130, in_Field, "NULLABLE", "NON_REQUIRED")
                arcpy.AddMessage ("Sasquatch created the "+in_Field+" field")
except arcpy.ExecuteError:
        msgs = arcpy.GetMessages(2)
        arcpy.AddError(msgs)
except:
        tb = sys.exc_info()[2]
        tbinfo = traceback.format_tb(tb)[0]
        pymsg = "PYTHON ERRORS:\nTraceback info:\n" + tbinfo + "\nError Info:\n" + str(sys.exc_info()[1])
        msgs = "ArcPy ERRORS:\n" + arcpy.GetMessages(2) + "\n"
        arcpy.AddError(pymsg)
        arcpy.AddError(msgs)
		
#Create required SOURCE_DATADESC Field
try:
        in_Field = "SOURCE_DATADESC"
        if len(arcpy.ListFields(fc_name,in_Field))>0:
                arcpy.AddWarning (in_Field+" exits already")
        else:
                arcpy.AddField_management(fc_name, in_Field, "TEXT", "", "", 100, in_Field, "NULLABLE", "NON_REQUIRED")
                arcpy.AddMessage ("Sasquatch created the "+in_Field+" field")
except arcpy.ExecuteError:
        msgs = arcpy.GetMessages(2)
        arcpy.AddError(msgs)
except:
        tb = sys.exc_info()[2]
        tbinfo = traceback.format_tb(tb)[0]
        pymsg = "PYTHON ERRORS:\nTraceback info:\n" + tbinfo + "\nError Info:\n" + str(sys.exc_info()[1])
        msgs = "ArcPy ERRORS:\n" + arcpy.GetMessages(2) + "\n"
        arcpy.AddError(pymsg)
        arcpy.AddError(msgs)
		
#Create required SOURCE_FEATUREID Field
try:
        in_Field = "SOURCE_FEATUREID"
        if len(arcpy.ListFields(fc_name,in_Field))>0:
                arcpy.AddWarning (in_Field+" exits already")
        else:
                arcpy.AddField_management(fc_name, in_Field, "TEXT", "", "", 100, in_Field, "NULLABLE", "NON_REQUIRED")
                arcpy.AddMessage ("Sasquatch created the "+in_Field+" field")
except arcpy.ExecuteError:
        msgs = arcpy.GetMessages(2)
        arcpy.AddError(msgs)
except:
        tb = sys.exc_info()[2]
        tbinfo = traceback.format_tb(tb)[0]
        pymsg = "PYTHON ERRORS:\nTraceback info:\n" + tbinfo + "\nError Info:\n" + str(sys.exc_info()[1])
        msgs = "ArcPy ERRORS:\n" + arcpy.GetMessages(2) + "\n"
        arcpy.AddError(pymsg)
        arcpy.AddError(msgs)
		
#Create required FEATUREDETAILURL Field
try:
        in_Field = "FEATUREDETAILURL"
        if len(arcpy.ListFields(fc_name,in_Field))>0:
                arcpy.AddWarning (in_Field+" exits already")
        else:
                arcpy.AddField_management(fc_name, in_Field, "TEXT", "", "", 255, in_Field, "NULLABLE", "NON_REQUIRED")
                arcpy.AddMessage ("Sasquatch created the "+in_Field+" field")
except arcpy.ExecuteError:
        msgs = arcpy.GetMessages(2)
        arcpy.AddError(msgs)
except:
        tb = sys.exc_info()[2]
        tbinfo = traceback.format_tb(tb)[0]
        pymsg = "PYTHON ERRORS:\nTraceback info:\n" + tbinfo + "\nError Info:\n" + str(sys.exc_info()[1])
        msgs = "ArcPy ERRORS:\n" + arcpy.GetMessages(2) + "\n"
        arcpy.AddError(pymsg)
        arcpy.AddError(msgs)


#Create required MEASURE Field
try:
        in_Field = "MEASURE"
        if len(arcpy.ListFields(fc_name,in_Field))>0:
                arcpy.AddWarning (in_Field+" exits already")
        else:
                arcpy.AddField_management(fc_name, in_Field, "DOUBLE", "38", "8", "", in_Field, "NULLABLE", "NON_REQUIRED")
                arcpy.AddMessage ("Sasquatch created the "+in_Field+" field")
except arcpy.ExecuteError:
        msgs = arcpy.GetMessages(2)
        arcpy.AddError(msgs)
except:
        tb = sys.exc_info()[2]
        tbinfo = traceback.format_tb(tb)[0]
        pymsg = "PYTHON ERRORS:\nTraceback info:\n" + tbinfo + "\nError Info:\n" + str(sys.exc_info()[1])
        msgs = "ArcPy ERRORS:\n" + arcpy.GetMessages(2) + "\n"
        arcpy.AddError(pymsg)
        arcpy.AddError(msgs)
        
#Create required EVENTOFFSET Field
try:
        in_Field = "EVENTOFFSET"
        if len(arcpy.ListFields(fc_name,in_Field))>0:
                arcpy.AddWarning (in_Field+" exits already")
        else:
                arcpy.AddField_management(fc_name, in_Field, "DOUBLE", "38", "8", "", in_Field, "NULLABLE", "NON_REQUIRED")
                arcpy.AddMessage ("Sasquatch created the "+in_Field+" field")
except arcpy.ExecuteError:
        msgs = arcpy.GetMessages(2)
        arcpy.AddError(msgs)
except:
        tb = sys.exc_info()[2]
        tbinfo = traceback.format_tb(tb)[0]
        pymsg = "PYTHON ERRORS:\nTraceback info:\n" + tbinfo + "\nError Info:\n" + str(sys.exc_info()[1])
        msgs = "ArcPy ERRORS:\n" + arcpy.GetMessages(2) + "\n"
        arcpy.AddError(pymsg)
        arcpy.AddError(msgs)
		
#Create required RIVERORDER Field
try:
        in_Field = "RIVERORDER"
        if len(arcpy.ListFields(fc_name,in_Field))>0:
                arcpy.AddWarning (in_Field+" exits already")
        else:
                arcpy.AddField_management(fc_name, in_Field, "LONG", "10", "", "", in_Field, "NULLABLE", "NON_REQUIRED")
                arcpy.AddMessage ("Sasquatch created the "+in_Field+" field")
except arcpy.ExecuteError:
        msgs = arcpy.GetMessages(2)
        arcpy.AddError(msgs)
except:
        tb = sys.exc_info()[2]
        tbinfo = traceback.format_tb(tb)[0]
        pymsg = "PYTHON ERRORS:\nTraceback info:\n" + tbinfo + "\nError Info:\n" + str(sys.exc_info()[1])
        msgs = "ArcPy ERRORS:\n" + arcpy.GetMessages(2) + "\n"
        arcpy.AddError(pymsg)
        arcpy.AddError(msgs)
		
		
#Create required STATION_NAME Field
try:
        in_Field = "STATION_NAME"
        if len(arcpy.ListFields(fc_name,in_Field))>0:
                arcpy.AddWarning (in_Field+" exits already")
        else:
                arcpy.AddField_management(fc_name, in_Field, "TEXT", "", "", 50, in_Field, "NULLABLE", "NON_REQUIRED")
                arcpy.AddMessage ("Sasquatch created the "+in_Field+" field")
except arcpy.ExecuteError:
        msgs = arcpy.GetMessages(2)
        arcpy.AddError(msgs)
except:
        tb = sys.exc_info()[2]
        tbinfo = traceback.format_tb(tb)[0]
        pymsg = "PYTHON ERRORS:\nTraceback info:\n" + tbinfo + "\nError Info:\n" + str(sys.exc_info()[1])
        msgs = "ArcPy ERRORS:\n" + arcpy.GetMessages(2) + "\n"
        arcpy.AddError(pymsg)
        arcpy.AddError(msgs)



        



  
















