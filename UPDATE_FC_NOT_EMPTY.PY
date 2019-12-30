#CREATES AN EXISTING, NON-EMPTY FC USING AN ORGANIZATION STANDARD SCHEMA
import os
import errno
import arcpy
import sys  
import traceback
#Get user input

gdb_name = arcpy.GetParameterAsText(0)
fc_name = arcpy.GetParameterAsText(1)
unit_code = arcpy.GetParameterAsText(2)
unit_name = arcpy.GetParameterAsText(3)
reg_code = arcpy.GetParameterAsText(4)
time_format = arcpy.GetParameterAsText(5)



#Create the GDB
#gdb_name = os.path.join(gdb_name, gdb_name)


#arcpy.SetParameterAsText(6, gdb_name+"\\"+gdb_name)       
#Create the NPS Standard Domains
#Create DOM_PUBLICDISPLAY_NPS2016 domain
try:
        PUBLICDISPLAYDict = {"No Public Map Display":"No Public Map Display", "Public Map Display": "Public Map Display"}
        domains = arcpy.da.ListDomains(gdb_name)
        domain_names = [domain.name for domain in domains]
        if 'DOM_PUBLICDISPLAY_NPS2016' in domain_names :
                arcpy.AddWarning("DOM_PUBLICDISPLAY_NPS2016 already exists")
                for domain in domains:
                        if domain.name == 'DOM_PUBLICDISPLAY_NPS2016':
                                values = [cv for cv in domain.codedValues]
                                if not set(set(["No Public Map Display", "Public Map Display"])).issubset(values):
                                        arcpy.AddWarning("DOM_PUBLICDISPLAY_NPS2016 is missing a coded value pair.")
                                        for code in DATAACCESSDict:
                                                arcpy.AddCodedValueToDomain_management(gdb_name, "DOM_PUBLICDISPLAY_NPS2016", code, DATAACCESSDict[code])
                                        arcpy.AddWarning("But Sasquatch took care of it.")
        else:
                arcpy.CreateDomain_management(gdb_name, "DOM_PUBLICDISPLAY_NPS2016", "Public Map Display Yes/No", "TEXT", "CODED")
                arcpy.AddMessage ("Sasquatch created the DOM_PUBLICDISPLAY_NPS2016 domain")
                for code in PUBLICDISPLAYDict:        
                        arcpy.AddCodedValueToDomain_management(gdb_name, "DOM_PUBLICDISPLAY_NPS2016", code, PUBLICDISPLAYDict[code])
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
        domains = arcpy.da.ListDomains(gdb_name)
        domain_names = [domain.name for domain in domains]
        if 'DOM_DATAACCESS_NPS2016' in domain_names :
                arcpy.AddWarning("DOM_DATAACCESS_NPS2016 already exists")
                for domain in domains:
                        if domain.name == 'DOM_DATAACCESS_NPS2016':
                                values = [cv for cv in domain.codedValues]
                                if not set(set(["Internal NPS Only", "Secure Access Only", "Unrestricted"])).issubset(values):
                                        arcpy.AddWarning("DOM_DATAACCESS_NPS2016 is missing a coded value pair.")
                                        for code in DATAACCESSDict:
                                                arcpy.AddCodedValueToDomain_management(gdb_name, "DOM_DATAACCESS_NPS2016", code, DATAACCESSDict[code])
                                        arcpy.AddWarning("But Sasquatch took care of it.")
        else:
                arcpy.CreateDomain_management(gdb_name, "DOM_DATAACCESS_NPS2016", "Restriction Level", "TEXT", "CODED")
                arcpy.AddMessage ("Sasquatch created the DOM_DATAACCESS_NPS2016 domain")
                for code in DATAACCESSDict:        
                        arcpy.AddCodedValueToDomain_management(gdb_name, "DOM_DATAACCESS_NPS2016", code, DATAACCESSDict[code])
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
        domains = arcpy.da.ListDomains(gdb_name)
        domain_names = [domain.name for domain in domains]
        if 'DOM_XYACCURACY_NPS2016' in domain_names :
                arcpy.AddWarning("DOM_XYACCURACY_NPS2016 already exists")
                for domain in domains:
                        if domain.name == 'DOM_XYACCURACY_NPS2016':
                                values = [cv for cv in domain.codedValues]
                                if not set(set(["Unknown", "<5cm", ">=5cm and <50cm", ">=50cm and < 1m", ">=1m and <5m", ">=5m and <14m", ">=14m","Scaled"])).issubset(values):
                                        arcpy.AddWarning("DOM_XYACCURACY_NPS2016 is missing a coded value pair.")
                                        for code in XYACCURACYDict:
                                                arcpy.AddCodedValueToDomain_management(gdb_name, "DOM_XYACCURACY_NPS2016", code, XYACCURACYDict[code])
                                        arcpy.AddWarning("But Sasquatch took care of it.")
        else:
                arcpy.CreateDomain_management(gdb_name, "DOM_XYACCURACY_NPS2016", "Data of unknown origin, spatial accuracy,unknown scale or resolution where a minimum mapping unit or scale of reference cannot be statistically determined (Qualitative accuracy assessment).", "TEXT", "CODED")       
                arcpy.AddMessage ("Sasquatch created the DOM_XYACCURACY_NPS2016 domain")
                for code in XYACCURACYDict:        
                        arcpy.AddCodedValueToDomain_management(gdb_name, "DOM_XYACCURACY_NPS2016", code, XYACCURACYDict[code])
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
        domains = arcpy.da.ListDomains(gdb_name)
        domain_names = [domain.name for domain in domains]
        if 'DOM_REGIONCODE_NPS2016' in domain_names:
                arcpy.AddWarning("DOM_REGIONCODE_NPS2016 already exists")
                for domain in domains:
                        if domain.name == 'DOM_REGIONCODE_NPS2016':
                                values = [cv for cv in domain.codedValues]
                                if not set(set(["AKR", "IMR", "MWR", "NCR", "NER", "PWR", "SER","WASO"])).issubset(values):
                                        arcpy.AddWarning("DOM_REGIONCODE_NPS2016 is missing a coded value pair.")
                                        for code in REGIONCODEDict:
                                                arcpy.AddCodedValueToDomain_management(gdb_name, "DOM_REGIONCODE_NPS2016", code, REGIONCODEDict[code])
                                        arcpy.AddWarning("But Sasquatch took care of it.")
        else:
                arcpy.CreateDomain_management(gdb_name, "DOM_REGIONCODE_NPS2016", "Region Code", "TEXT", "CODED")       
                arcpy.AddMessage ("Sasquatch created the DOM_REGIONCODE_NPS2016 domain")
                for code in REGIONCODEDict:        
                        arcpy.AddCodedValueToDomain_management(gdb_name, "DOM_REGIONCODE_NPS2016", code, REGIONCODEDict[code]) 
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
#Grab the Feature Class
#fc_name = gdb_name+"\\"+fc_name

#Create required PUBLICDISPLAY Field
try:
        in_Field = "PUBLICDISPLAY"
        default = "No Public Map Display"
        if len(arcpy.ListFields(fc_name,in_Field))>0:
                arcpy.AddWarning (in_Field+" exits already")
        else:
                arcpy.AddWarning (in_Field+" doesn't exist")
                arcpy.AddField_management(fc_name, in_Field, "TEXT", "", "", 50, in_Field, "NULLABLE", "REQUIRED", "DOM_PUBLICDISPLAY_NPS2016")
                arcpy.AddMessage ("Sasquatch created the "+in_Field+" field and the attribute domain is DOM_PUBLICDISPLAY_NPS2016")
                arcpy.AssignDefaultToField_management(fc_name, in_Field, default)
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
        if len(arcpy.ListFields(fc_name,in_Field))>0:
                arcpy.AddWarning(in_Field+" exits already")
        else:
                arcpy.AddField_management(fc_name, in_Field, "TEXT", "", "", 50, in_Field, "NULLABLE", "REQUIRED", "DOM_DATAACCESS_NPS2016")
                arcpy.AddMessage ("Sasquatch created the "+in_Field+" field and the attribute domain is DOM_DATAACCESS_NPS2016")
                arcpy.AssignDefaultToField_management(fc_name, in_Field, default)
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
        if len(arcpy.ListFields(fc_name,in_Field))>0:
                arcpy.AddWarning (in_Field+" exits already")
        else:
                arcpy.AddField_management(fc_name, in_Field, "TEXT", "", "", 10, in_Field, "NULLABLE", "REQUIRED")
                arcpy.AddMessage ("Sasquatch created the "+in_Field+" field")
                arcpy.AssignDefaultToField_management(fc_name, in_Field, unit_code)
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
        if len(arcpy.ListFields(fc_name,in_Field))>0:
                arcpy.AddWarning (in_Field+" exits already")
        else:
                arcpy.AddField_management(fc_name, in_Field, "TEXT", "", "", 254, in_Field, "NULLABLE", "REQUIRED")
                arcpy.AddMessage ("Sasquatch created the "+in_Field+" field")
                arcpy.AssignDefaultToField_management(fc_name, in_Field, unit_name)
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
        if len(arcpy.ListFields(fc_name,in_Field))>0:
                arcpy.AddWarning (in_Field+" exits already")
        else:
                arcpy.AddField_management(fc_name, in_Field, "TEXT", "", "", 10, in_Field, "NULLABLE", "NON_REQUIRED")
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
        if len(arcpy.ListFields(fc_name,in_Field))>0:
                arcpy.AddWarning (in_Field+" exits already")
        else:
                arcpy.AddField_management(fc_name, in_Field, "TEXT", "", "", 254, in_Field, "NULLABLE", "NON_REQUIRED")
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
        if len(arcpy.ListFields(fc_name,in_Field))>0:
                arcpy.AddWarning (in_Field+" exits already")
        else:
                arcpy.AddField_management(fc_name, in_Field, "TEXT", "", "", 4, in_Field, "NULLABLE", "REQUIRED", "DOM_REGIONCODE_NPS2016")
                arcpy.AddMessage ("Sasquatch created the "+in_Field+" field and the attribute domain is DOM_REGIONCODE_NPS2016")
                arcpy.AssignDefaultToField_management(fc_name, in_Field, reg_code)
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
        if len(arcpy.ListFields(fc_name,in_Field))>0:
                arcpy.AddWarning (in_Field+" exits already")
        else:
                arcpy.AddField_management(fc_name, in_Field, "DATE", "", "", "", in_Field, "NULLABLE", "REQUIRED")
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
        if len(arcpy.ListFields(fc_name,in_Field))>0:
                arcpy.AddWarning (in_Field+" exits already")
        else:
                arcpy.AddField_management(fc_name, in_Field, "TEXT", "", "", 50, in_Field, "NULLABLE", "REQUIRED")
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
        if len(arcpy.ListFields(fc_name,in_Field))>0:
                arcpy.AddWarning (in_Field+" exits already")
        else:
                arcpy.AddField_management(fc_name, in_Field, "DATE", "", "", "", in_Field, "NULLABLE", "REQUIRED")
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
        if len(arcpy.ListFields(fc_name,in_Field))>0:
                arcpy.AddWarning (in_Field+" exits already")
        else:
                arcpy.AddField_management(fc_name, in_Field, "TEXT", "", "", 50, in_Field, "NULLABLE", "REQUIRED")
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
        if len(arcpy.ListFields(fc_name,in_Field))>0:
                arcpy.AddWarning (in_Field+" exits already")
                arcpy.AlterField_management(fc_name,in_Field,"","","",254,"","")
                arcpy.AddWarning (in_Field+" length was increased to 254 characters")
        else:
                arcpy.AddField_management(fc_name, in_Field, "TEXT", "", "", 254, in_Field, "NULLABLE", "REQUIRED")
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
        if len(arcpy.ListFields(fc_name,in_Field))>0:
                arcpy.AddWarning (in_Field+" exits already")
        else:
                arcpy.AddField_management(fc_name, in_Field, "TEXT", "", "", 254, in_Field, "NULLABLE", "REQUIRED")
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
#Create required XYACCURACY Field
try:
        in_Field = "XYACCURACY"
        if len(arcpy.ListFields(fc_name,in_Field))>0:
                arcpy.AddWarning (in_Field+" exits already")
        else:
                arcpy.AddField_management(fc_name, in_Field, "TEXT", "", "", 50, in_Field, "NULLABLE", "REQUIRED", "DOM_XYACCURACY_NPS2016")
                arcpy.AddMessage ("Sasquatch created the "+in_Field+" field and the attribute domain is DOM_XYACCURACY_NPS2016")
                arcpy.AssignDefaultToField_management(fc_name, in_Field, "Unknown")
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
        if len(arcpy.ListFields(fc_name,in_Field))>0:
                arcpy.AddWarning (in_Field+" exits already")
        else:
                arcpy.AddField_management(fc_name, in_Field, "GUID", "", "", "", in_Field, "NULLABLE", "NON_REQUIRED")
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
        if len(arcpy.ListFields(fc_name,in_Field))>0:
                arcpy.AddWarning (in_Field+" exits already")
        else:
                arcpy.AddField_management(fc_name, in_Field, "TEXT", "", "", 254, in_Field, "NULLABLE", "NON_REQUIRED")
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
        if len(arcpy.ListFields(fc_name,"GlobalID"))>0:
                arcpy.AddWarning ("GlobalID exits already")
        else:
                arcpy.AddGlobalIDs_management(fc_name)
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
        arcpy.EnableEditorTracking_management(fc_name, "CREATEUSER","CREATEDATE", "EDITUSER", "EDITDATE", "NO_ADD_FIELDS", time_format)
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

arcpy.SetParameterAsText(6, gdb_name)













