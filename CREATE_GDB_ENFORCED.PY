#CREATES A FGDB IN A ORGANIZATION STANDARD LOCATION USING AN ORGANIZATION STANDARD SCHEMA
import os
import errno
import arcpy
import sys  
import traceback 
#Get user input
gdb_name = arcpy.GetParameterAsText(0)
fc_name = arcpy.GetParameterAsText(1)
fc_type = arcpy.GetParameterAsText(2)
has_m = arcpy.GetParameterAsText(3)
has_z = arcpy.GetParameterAsText(4)
spat_ref = arcpy.GetParameterAsText(5)
unit_code = arcpy.GetParameterAsText(6)
unit_name = arcpy.GetParameterAsText(7)
reg_code = arcpy.GetParameterAsText(8)
time_format = arcpy.GetParameterAsText(9)

#Get the current project directory
curr = arcpy.mp.ArcGISProject("CURRENT").filePath
folder = "/".join(curr.split("\\")[:-1])
#Get the current working data directory within the project
#This is where GRSM policy requires the GDB to be
#Edit this to meet your needs, but the "Create Folders in Pro Project" MUST create this directory first!
#So that means if this needs to be different, the python for "Create Folders in Pro Project" must also be edited!
############
#EDIT ME AFTER EDITING NEW_FC.py!!!!!!!!!!!
os.chdir(folder+"/data/working")
############
path = os.getcwd()

#Create the GDB
#path +"\\"+ gdb_name+".gdb = path +"\\"+ gdb_name+".gdb"

if arcpy.Exists(path +"\\"+ gdb_name+".gdb"):
        arcpy.AddWarning (path +"\\"+ gdb_name+".gdb already exists!")
else:
        arcpy.CreateFileGDB_management(path, gdb_name)
        arcpy.AddMessage ("Sasquatch created the file geodatabae in "+path+"\\"+gdb_name)
arcpy.SetParameterAsText(10, gdb_name)       
#Create the NPS Standard Domains
#Create DOM_PUBLICDISPLAY_NPS2016 domain
try:
        PUBLICDISPLAYDict = {"No Public Map Display":"No Public Map Display", "Public Map Display": "Public Map Display"}
        domains = arcpy.da.ListDomains(path +"\\"+ gdb_name+".gdb")
        domain_names = [domain.name for domain in domains]
        if 'DOM_PUBLICDISPLAY_NPS2016' in domain_names :
                arcpy.AddWarning("DOM_PUBLICDISPLAY_NPS2016 already exists")
                for domain in domains:
                        if domain.name == 'DOM_PUBLICDISPLAY_NPS2016':
                                values = [cv for cv in domain.codedValues]
                                if not set(set(["No Public Map Display", "Public Map Display"])).issubset(values):
                                        arcpy.AddWarning("DOM_PUBLICDISPLAY_NPS2016 is missing a coded value pair.")
                                        for code in DATAACCESSDict:
                                                arcpy.AddCodedValueToDomain_management(path+"\\"+gdb_name+".gdb", "DOM_PUBLICDISPLAY_NPS2016", code, DATAACCESSDict[code])
                                        arcpy.AddWarning("But Sasquatch took care of it.")
        else:
                #arcpy.SetParameterAsText(10, gdb_name)  
                arcpy.CreateDomain_management(path+"\\"+gdb_name+".gdb", "DOM_PUBLICDISPLAY_NPS2016", "Public Map Display Yes/No", "TEXT", "CODED")
                arcpy.AddMessage ("Sasquatch created the DOM_PUBLICDISPLAY_NPS2016 domain")
                for code in PUBLICDISPLAYDict:        
                        arcpy.AddCodedValueToDomain_management(path+"\\"+gdb_name+".gdb", "DOM_PUBLICDISPLAY_NPS2016", code, PUBLICDISPLAYDict[code])
                arcpy.AddMessage ("Sasquatch added coded domain values to the DOM_PUBLICDISPLAY_NPS2016 domain")
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

#Create DOM_DATAACCESS_NPS2016 domain
try:
        DATAACCESSDict = {"Internal NPS Only":"Internal NPS Only", "Secure Access Only": "Secure Access Only", "Unrestricted": "Unrestricted"}
        domains = arcpy.da.ListDomains(path +"\\"+ gdb_name+".gdb")
        domain_names = [domain.name for domain in domains]
        if 'DOM_DATAACCESS_NPS2016' in domain_names :
                arcpy.AddWarning("DOM_DATAACCESS_NPS2016 already exists")
                for domain in domains:
                        if domain.name == 'DOM_DATAACCESS_NPS2016':
                                values = [cv for cv in domain.codedValues]
                                if not set(set(["Internal NPS Only", "Secure Access Only", "Unrestricted"])).issubset(values):
                                        arcpy.AddWarning("DOM_DATAACCESS_NPS2016 is missing a coded value pair.")
                                        for code in DATAACCESSDict:
                                                arcpy.AddCodedValueToDomain_management(path+"\\"+gdb_name+".gdb", "DOM_DATAACCESS_NPS2016", code, DATAACCESSDict[code])
                                        arcpy.AddWarning("But Sasquatch took care of it.")
        else:
                arcpy.CreateDomain_management(path+"\\"+gdb_name+".gdb", "DOM_DATAACCESS_NPS2016", "Restriction Level", "TEXT", "CODED")
                arcpy.AddMessage ("Sasquatch created the DOM_DATAACCESS_NPS2016 domain")
                for code in DATAACCESSDict:        
                        arcpy.AddCodedValueToDomain_management(path+"\\"+gdb_name+".gdb", "DOM_DATAACCESS_NPS2016", code, DATAACCESSDict[code])
                arcpy.AddMessage ("Sasquatch added coded domain values to the DOM_DATAACCESS_NPS2016 domain")
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
#Create DOM_XYACCURACY_NPS2016 domain
try:
        XYACCURACYDict = {"Unknown":"Unknown", "<5cm": "<5cm", ">=5cm and <50cm": ">=5cm and <50cm" , ">=50cm and < 1m": ">=50cm and < 1m", ">=1m and <5m": ">=1m and <5m" , ">=5m and <14m": ">=5m and <14m" , ">=14m": ">=14m" , "Scaled": "Scaled"}
        domains = arcpy.da.ListDomains(path +"\\"+ gdb_name+".gdb")
        domain_names = [domain.name for domain in domains]
        if 'DOM_XYACCURACY_NPS2016' in domain_names :
                arcpy.AddWarning("DOM_XYACCURACY_NPS2016 already exists")
                for domain in domains:
                        if domain.name == 'DOM_XYACCURACY_NPS2016':
                                values = [cv for cv in domain.codedValues]
                                if not set(set(["Unknown", "<5cm", ">=5cm and <50cm", ">=50cm and < 1m", ">=1m and <5m", ">=5m and <14m", ">=14m","Scaled"])).issubset(values):
                                        arcpy.AddWarning("DOM_XYACCURACY_NPS2016 is missing a coded value pair.")
                                        for code in XYACCURACYDict:
                                                arcpy.AddCodedValueToDomain_management(path+"\\"+gdb_name+".gdb", "DOM_XYACCURACY_NPS2016", code, XYACCURACYDict[code])
                                        arcpy.AddWarning("But Sasquatch took care of it.")
        else:
                arcpy.CreateDomain_management(path+"\\"+gdb_name+".gdb", "DOM_XYACCURACY_NPS2016", "Data of unknown origin, spatial accuracy,unknown scale or resolution where a minimum mapping unit or scale of reference cannot be statistically determined (Qualitative accuracy assessment).", "TEXT", "CODED")       
                arcpy.AddMessage ("Sasquatch created the DOM_XYACCURACY_NPS2016 domain")
                for code in XYACCURACYDict:        
                        arcpy.AddCodedValueToDomain_management(path+"\\"+gdb_name+".gdb", "DOM_XYACCURACY_NPS2016", code, XYACCURACYDict[code])
                arcpy.AddMessage ("Sasquatch added coded domain values to the DOM_XYACCURACY_NPS2016 domain")
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

#Create DOM_REGIONCODE_NPS2016 domain
try:
        REGIONCODEDict = {"AKR":"AKR", "IMR": "IMR", "MWR": "MWR" , "NCR": "NCR", "NER": "NER" , "PWR": "PWR" , "SER": "SER" , "WASO": "WASO"}
        domains = arcpy.da.ListDomains(path +"\\"+ gdb_name+".gdb")
        domain_names = [domain.name for domain in domains]
        if 'DOM_REGIONCODE_NPS2016' in domain_names:
                arcpy.AddWarning("DOM_REGIONCODE_NPS2016 already exists")
                for domain in domains:
                        if domain.name == 'DOM_REGIONCODE_NPS2016':
                                values = [cv for cv in domain.codedValues]
                                if not set(set(["AKR", "IMR", "MWR", "NCR", "NER", "PWR", "SER","WASO"])).issubset(values):
                                        arcpy.AddWarning("DOM_REGIONCODE_NPS2016 is missing a coded value pair.")
                                        for code in REGIONCODEDict:
                                                arcpy.AddCodedValueToDomain_management(path+"\\"+gdb_name+".gdb", "DOM_REGIONCODE_NPS2016", code, REGIONCODEDict[code])
                                        arcpy.AddWarning("But Sasquatch took care of it.")
        else:
                arcpy.CreateDomain_management(path+"\\"+gdb_name+".gdb", "DOM_REGIONCODE_NPS2016", "Region Code", "TEXT", "CODED")       
                arcpy.AddMessage ("Sasquatch created the DOM_REGIONCODE_NPS2016 domain")
                for code in REGIONCODEDict:        
                        arcpy.AddCodedValueToDomain_management(path+"\\"+gdb_name+".gdb", "DOM_REGIONCODE_NPS2016", code, REGIONCODEDict[code]) 
                arcpy.AddMessage ("Sasquatch added coded domain values to the DOM_REGIONCODE_NPS2016 domain")
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

#Create the Feature Class
in_Table = path+"\\"+gdb_name+".gdb\\"+fc_name
if arcpy.Exists(in_Table):
        arcpy.AddWarning  (in_Table+" Exists already")

else:
        arcpy.CreateFeatureclass_management(path+"\\"+gdb_name+".gdb", fc_name, fc_type, "", has_m, has_z, spat_ref)
        arcpy.AddMessage  ("Sasquatch created"+in_Table)

#Create required PUBLICDISPLAY Field
try:
        in_Field = "PUBLICDISPLAY"
        default = "No Public Map Display"
        if len(arcpy.ListFields(in_Table,in_Field))>0:
                arcpy.AddWarning (in_Field+" exits already")
        else:
                arcpy.AddField_management(path+"\\"+gdb_name+".gdb\\"+fc_name, in_Field, "TEXT", "", "", 50, in_Field, "NON_NULLABLE", "REQUIRED", "DOM_PUBLICDISPLAY_NPS2016")
                arcpy.AddMessage ("Sasquatch created the "+in_Field+" field and the attribute domain is DOM_PUBLICDISPLAY_NPS2016")
                arcpy.AssignDefaultToField_management(path+"\\"+gdb_name+".gdb\\"+fc_name, in_Field, default)
                arcpy.AddMessage ("Saquatch assigned "+default+" as the default value for "+ in_Field)
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
     
        
#Create required DATAACCESS Field
try:
        in_Field = "DATAACCESS"
        default = "Internal NPS Only"
        if len(arcpy.ListFields(in_Table,in_Field))>0:
                arcpy.AddWarning(in_Field+" exits already")
        else:
                arcpy.AddField_management(path+"\\"+gdb_name+".gdb\\"+fc_name, in_Field, "TEXT", "", "", 50, in_Field, "NON_NULLABLE", "REQUIRED", "DOM_DATAACCESS_NPS2016")
                arcpy.AddMessage ("Sasquatch created the "+in_Field+" field and the attribute domain is DOM_DATAACCESS_NPS2016")
                arcpy.AssignDefaultToField_management(path+"\\"+gdb_name+".gdb\\"+fc_name, in_Field, default)
                arcpy.AddMessage ("Saquatch assigned "+default+" as the default value for "+ in_Field)
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
        

#Create required UNITCODE Field
try:
        in_Field = "UNITCODE"
        if len(arcpy.ListFields(in_Table,in_Field))>0:
                arcpy.AddWarning (in_Field+" exits already")
        else:
                arcpy.AddField_management(path+"\\"+gdb_name+".gdb\\"+fc_name, in_Field, "TEXT", "", "", 10, in_Field, "NON_NULLABLE", "REQUIRED")
                arcpy.AddMessage ("Sasquatch created the "+in_Field+" field")
                arcpy.AssignDefaultToField_management(path+"\\"+gdb_name+".gdb\\"+fc_name, in_Field, unit_code)
                arcpy.AddMessage ("Saquatch assigned "+unit_code+" as the default value for "+ in_Field)
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
#Create required UNITNAME Field
try:
        in_Field = "UNITNAME"
        if len(arcpy.ListFields(in_Table,in_Field))>0:
                arcpy.AddWarning (in_Field+" exits already")
        else:
                arcpy.AddField_management(path+"\\"+gdb_name+".gdb\\"+fc_name, in_Field, "TEXT", "", "", 254, in_Field, "NON_NULLABLE", "REQUIRED")
                arcpy.AddMessage ("Sasquatch created the "+in_Field+" field")
                arcpy.AssignDefaultToField_management(path+"\\"+gdb_name+".gdb\\"+fc_name, in_Field, unit_name)
                arcpy.AddMessage ("Saquatch assigned "+unit_name+" as the default value for "+ in_Field)
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
#Create required GROUPCODE Field
try:
        in_Field = "GROUPCODE"
        if len(arcpy.ListFields(in_Table,in_Field))>0:
                arcpy.AddWarning (in_Field+" exits already")
        else:
                arcpy.AddField_management(path+"\\"+gdb_name+".gdb\\"+fc_name, in_Field, "TEXT", "", "", 10, in_Field, "NULLABLE", "NON_REQUIRED")
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
#Create required GROUPNAME Field
try:
        in_Field = "GROUPNAME"
        if len(arcpy.ListFields(in_Table,in_Field))>0:
                arcpy.AddWarning (in_Field+" exits already")
        else:
                arcpy.AddField_management(path+"\\"+gdb_name+".gdb\\"+fc_name, in_Field, "TEXT", "", "", 254, in_Field, "NULLABLE", "NON_REQUIRED")
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
#Create required REGIONCODE Field
try:
        in_Field = "REGIONCODE"
        if len(arcpy.ListFields(in_Table,in_Field))>0:
                arcpy.AddWarning (in_Field+" exits already")
        else:
                arcpy.AddField_management(path+"\\"+gdb_name+".gdb\\"+fc_name, in_Field, "TEXT", "", "", 4, in_Field, "NON_NULLABLE", "REQUIRED", "DOM_REGIONCODE_NPS2016")
                arcpy.AddMessage ("Sasquatch created the "+in_Field+" field and the attribute domain is DOM_REGIONCODE_NPS2016")
                arcpy.AssignDefaultToField_management(path+"\\"+gdb_name+".gdb\\"+fc_name, in_Field, reg_code)
                arcpy.AddMessage ("Saquatch assigned "+reg_code+" as the default value for "+ in_Field)
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
#Create required CREATEDATE Field
try:
        in_Field = "CREATEDATE"
        if len(arcpy.ListFields(in_Table,in_Field))>0:
                arcpy.AddWarning (in_Field+" exits already")
        else:
                arcpy.AddField_management(path+"\\"+gdb_name+".gdb\\"+fc_name, in_Field, "DATE", "", "", "", in_Field, "NON_NULLABLE", "REQUIRED")
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
#Create required CREATEUSER Field
try:
        in_Field = "CREATEUSER"
        if len(arcpy.ListFields(in_Table,in_Field))>0:
                arcpy.AddWarning (in_Field+" exits already")
        else:
                arcpy.AddField_management(path+"\\"+gdb_name+".gdb\\"+fc_name, in_Field, "TEXT", "", "", 50, in_Field, "NON_NULLABLE", "REQUIRED")
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
#Create required EDITDATE Field
try:
        in_Field = "EDITDATE"
        if len(arcpy.ListFields(in_Table,in_Field))>0:
                arcpy.AddWarning (in_Field+" exits already")
        else:
                arcpy.AddField_management(path+"\\"+gdb_name+".gdb\\"+fc_name, in_Field, "DATE", "", "", "", in_Field, "NON_NULLABLE", "REQUIRED")
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
#Create required EDITUSER Field
try:
        in_Field = "EDITUSER"
        if len(arcpy.ListFields(in_Table,in_Field))>0:
                arcpy.AddWarning (in_Field+" exits already")
        else:
                arcpy.AddField_management(path+"\\"+gdb_name+".gdb\\"+fc_name, in_Field, "TEXT", "", "", 50, in_Field, "NON_NULLABLE", "REQUIRED")
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
#Create required MAPMETHOD Field
try:
        in_Field = "MAPMETHOD"
        if len(arcpy.ListFields(in_Table,in_Field))>0:
                arcpy.AddWarning (in_Field+" exits already")
        else:
                arcpy.AddField_management(path+"\\"+gdb_name+".gdb\\"+fc_name, in_Field, "TEXT", "", "", 254, in_Field, "NON_NULLABLE", "REQUIRED")
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
#Create required MAPSOURCE Field
try:
        in_Field = "MAPSOURCE"
        if len(arcpy.ListFields(in_Table,in_Field))>0:
                arcpy.AddWarning (in_Field+" exits already")
        else:
                arcpy.AddField_management(path+"\\"+gdb_name+".gdb\\"+fc_name, in_Field, "TEXT", "", "", 254, in_Field, "NON_NULLABLE", "REQUIRED")
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
#Create required SOURCEDATE Field
try:
        in_Field = "SOURCEDATE"
        if len(arcpy.ListFields(in_Table,in_Field))>0:
                arcpy.AddWarning (in_Field+" exits already")
        else:
                arcpy.AddField_management(path+"\\"+gdb_name+".gdb\\"+fc_name, in_Field, "DATE", "", "", "", in_Field, "NULLABLE", "NON_REQUIRED")
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
#Create required XYACCURACY Field
try:
        in_Field = "XYACCURACY"
        if len(arcpy.ListFields(in_Table,in_Field))>0:
                arcpy.AddWarning (in_Field+" exits already")
        else:
                arcpy.AddField_management(path+"\\"+gdb_name+".gdb\\"+fc_name, in_Field, "TEXT", "", "", 50, in_Field, "NON_NULLABLE", "REQUIRED", "DOM_XYACCURACY_NPS2016")
                arcpy.AddMessage ("Sasquatch created the "+in_Field+" field and the attribute domain is DOM_XYACCURACY_NPS2016")
                arcpy.AssignDefaultToField_management(path+"\\"+gdb_name+".gdb\\"+fc_name, in_Field, "Unknown")
                arcpy.AddMessage ("Saquatch assigned Unknown as the default value for "+ in_Field)
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
#Create required GEOMETRYID Field
try:
        in_Field = "GEOMETRYID"
        if len(arcpy.ListFields(in_Table,in_Field))>0:
                arcpy.AddWarning (in_Field+" exits already")
        else:
                arcpy.AddField_management(path+"\\"+gdb_name+".gdb\\"+fc_name, in_Field, "GUID", "", "", "", in_Field, "NULLABLE", "NON_REQUIRED")
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
#Create required NOTES Field
try:
        in_Field = "NOTES"
        if len(arcpy.ListFields(in_Table,in_Field))>0:
                arcpy.AddWarning (in_Field+" exits already")
        else:
                arcpy.AddField_management(path+"\\"+gdb_name+".gdb\\"+fc_name, in_Field, "TEXT", "", "", 254, in_Field, "NULLABLE", "NON_REQUIRED")
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

#Create the required GlobalID Field
try:
        if len(arcpy.ListFields(in_Table,"GlobalID"))>0:
                arcpy.AddWarning ("GlobalID exits already")
        else:
                arcpy.AddGlobalIDs_management(in_Table)
                arcpy.AddMessage ("Sasquatch created the GlobalID field")
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
#Enable editor tracking
try:
        arcpy.EnableEditorTracking_management(path+"\\"+gdb_name+".gdb\\"+fc_name, "CREATEUSER","CREATEDATE", "EDITUSER", "EDITDATE", "NO_ADD_FIELDS", time_format)
        arcpy.AddMessage ("Sasquatch enabled editor tracking on "+fc_name)
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











