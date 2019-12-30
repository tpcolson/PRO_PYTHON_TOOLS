#STAND ALONE SCRIPT
#ARCHIVES A SDE FEATURE CLASS
import sys, string, os, arcpy, calendar, datetime, traceback,smtplib,zipfile,shutil
import arcpy
from arcpy import env
from arcgis.gis import GIS
from subprocess import call

# Set the name of the feature service. This will control many variable in this script
NAME = "GRSM_EXOTICS"
# Define log setting
try:
    d = datetime.datetime.now()
    log = open("C:\\PYTHON_LOGS\LOG."+NAME+".txt","a")
    log.write("----------------------------" + "\n")
    log.write("----------------------------" + "\n")
    log.write("Log: " + str(d) + "\n")
    log.write("\n")
# Start process...
    starttime = datetime.datetime.now()
    log.write("Begin process:\n")
    log.write("     Process started at " + str(starttime) + "\n")
    log.write("\n")
      
    ### Start setting variables
    # Mail Server Settings
    SERVER = "1.2.3.4"
    PORT = "25"
    FROM = "BINKY_THE_CLOWN@ME.COM"
    MAILDOMAIN = '@ME.COM'
    # Data Steward getting the email. Needs to be their email address...without @nps.gov at the end
    userList=["ME"]
    # Define a seperate email list if fail, data steward won't know what error message means
    userListFail = ["YOU"]
    # get a list of usernames from the list of named tuples returned from ListUsers
    userNames = [u for u in userList]
    userNamesFail = [u for u in userListFail]
    # take the userNames list and make email addresses by appending the appropriate suffix.
    emailList = [name +  MAILDOMAIN for name in userNames]
    emailListFail = [name +  MAILDOMAIN for name in userNamesFail]
    TO = emailList
    TOFail = emailListFail
    # Grab date for the email
    DATE = d
   
    # Use X Drive for testing, once script is working, change to full UNC path IAW File and Folder naming protocol
    # e.g. \\\\inpgrsms05vm\COMMON\RMS\Fisheries_Management\Angler_Creel\Data\Tabular\Archive\\
    OutFolder = "\\\\inpgrsms06vm\SQL_BACKUPS\SDE_ARCHIVE\EXOTICS\\"
    # First letters need to indicate protocol needs to be same name as SDE Feature Class
    # Don't forget underscore at end of feature class name!
    OutName = NAME+"_"+time.strftime("%Y%m%d%H%M%S")+"_ARCHIVE.gdb"
    GDB = OutFolder+"\\"+OutName
    arcpy.env.configKeyword = "DEFAULTS"
    arcpy.CreateFileGDB_management(OutFolder, OutName)
    #This needs to be the full path to the SDE connection file, which must be in the same folder
    # AFter testing and moving to final folder, needs to be UNC path
    # e.g \\\\inpgrsms05vm\COMMON\RMS\Fisheries_Management\Angler_Creel\Data\Tabular\Archive\\RESTON BATS.sde
    arcpy.env.workspace = "C:\PRODUCTION\GRSM_GEODB\RESTON_EXOTICS.sde"
    # Converts the SDE data, which will always start with [DBNAME].[SCHEMA]
    arcpy.FeatureClassToFeatureClass_conversion("EXOTICS.DBO.GRSM_EXOTICS_SITE_POINT",GDB, "GRSM_EXOTICS_SITE_POINT", "", "", "DEFAULTS")
    arcpy.FeatureClassToFeatureClass_conversion("EXOTICS.DBO.GRSM_EXOTICS_SITE_POLY",GDB, "GRSM_EXOTICS_SITE_POLY", "", "", "DEFAULTS")
    arcpy.FeatureClassToFeatureClass_conversion("EXOTICS.DBO.GRSM_VEG_EXOTICS_SCOUTING_POINTS",GDB, "GRSM_VEG_EXOTICS_SCOUTING_POINTS", "", "", "DEFAULTS")
    arcpy.FeatureClassToFeatureClass_conversion("EXOTICS.DBO.GRSM_VEG_EXOTICS_SCOUTING_DATA",GDB, "GRSM_VEG_EXOTICS_SCOUTING_DATA", "", "", "DEFAULTS")    
    arcpy.Compact_management(GDB)
    #https://enterprise.arcgis.com/en/server/latest/publish-services/windows/h-zip-python-script.htm
    def zipws(path, zip, keep):
        for (dirpath, dirnames, filenames) in os.walk(path):
            for file in filenames:
                if not file.endswith('.lock'):
                    arcpy.AddMessage("Adding %s..." % os.path.join(path, dirpath, file))
                    try:
                        if keep:
                            zip.write(os.path.join(dirpath, file),
                            os.path.join(os.path.basename(path), os.path.join(dirpath, file)[len(path)+len(os.sep):]))
                        else:
                            zip.write(os.path.join(dirpath, file),            
                            os.path.join(dirpath[len(path):], file)) 
                            
                    except Exception as e:
                        arcpy.AddWarning("    Error adding %s: %s" % (file, e))

        return None

    if __name__ == '__main__':
        try:
            infolder = GDB
            outfile = OutFolder+OutName+'.zip'      
            try:
                    zip = zipfile.ZipFile(outfile, 'w', zipfile.ZIP_DEFLATED)
                    zipws(infolder, zip, True)
                    zip.close()
            except RuntimeError:
                    if os.path.exists(outfile):
                            os.unlink(outfile)
                    zip = zipfile.ZipFile(outfile, 'w', zipfile.ZIP_STORED)
                    zipws(infolder, zip, True)
                    zip.close()
                    arcpy.AddWarning("    Unable to compress zip file contents.")
                       
            arcpy.AddMessage("Zip file created successfully")
            shutil.rmtree(GDB)
        except:
            tb = sys.exc_info()[2]
            tbinfo = traceback.format_tb(tb)[0]
            pymsg = "PYTHON ERRORS:\nTraceback Info:\n" + tbinfo + "\nError Info:\n    " + \
                    str(sys.exc_type)+ ": " + str(sys.exc_value) + "\n"
            arcpy.AddError(pymsg)

            msgs = "GP ERRORS:\n" + arcpy.GetMessages(2) + "\n"
            arcpy.AddError(msgs)
        
            
    

	
    # Write nothing to log if success.
    endtime = datetime.datetime.now()
    log.write("     Completed successfully in " 
           + str(endtime - starttime) + "\n")
    log.write("\n")
    log.close()
    #Define email message if success
    SUBJECT = "Notification of Successful Archive of "+NAME
    MSG = NAME + " was archived at  "+ GDB +" at "+ str(DATE)
    print (MSG)
    print (emailList)
 
    # Send an email notifying steward of successful archive
    #MESSAGE = "\ From: %s To: %s Subject: %s %s" % (FROM, ", ".join(TO), SUBJECT, MSG)
    MESSAGE = "Subject: %s\n\n%s" % (SUBJECT, MSG)
    try:
            try:
                print("Connecting to Server...")
                server = smtplib.SMTP(SERVER,PORT)
                try:
                    print("Login...")
                    try:
                        print("Sending mail...")
                        server.sendmail(FROM, TO, MESSAGE)
                    except Exception as e:
                        print("Send Error Mail\n" + e.message)
                except Exception as e:
                    print("Error Authentication Server: check the credentials \n" + e.message)
            except Exception as e:
                print("Error Connecting to Server : check the URL of the server and communications port ( 25 and ' the default ) \n" + e.message)
     
            print("Quit.")
            server.quit()
     
    except Exception as e:
            print (e.message)
# Something went wrong
except:
    
     # Get the traceback object
    tb = sys.exc_info()[2]
    tbinfo = traceback.format_tb(tb)[0]
     # Concatenate information together concerning 
     # the error into a message string
    pymsg = "PYTHON ERRORS:\nTraceback info:\n" + tbinfo + "\nError Info:\n" + str(sys.exc_info()[1])
    msgs = "ArcPy ERRORS:\n" + arcpy.GetMessages(2) + "\n"
    # Return python error messages for use in 
    # script tool or Python Window
    arcpy.AddError(pymsg)
    arcpy.AddError(msgs)
    # Print Python error messages for use in 
    # Python / Python Window
    log.write("" + pymsg + "\n")
    log.write("" + msgs + "")
    log.close()
    # Define email message if something went wrong
    SUBJECT = "Notification of Un-Successful Archive of "+NAME 
    MSG = "Did Not archive "+NAME +" at "+ str(DATE)+ "; " +pymsg + "; " + msgs
    print (MSG)
    print (emailListFail)
 
    # Send an email notifying steward of unsuccessful archive
    #MESSAGE = "\ From: %s To: %s Subject: %s %s" % (FROM, ", ".join(TO), SUBJECT, MSG)
    MESSAGE = "Subject: %s\n\n%s" % (SUBJECT, MSG)
    try:
            try:
                print("Connecting to Server...")
                server = smtplib.SMTP(SERVER,PORT)
                try:
                    print("Login...")
                    try:
                        print("Sending mail...")
                        server.sendmail(FROM, TOFail, MESSAGE)
                    except Exception as e:
                        print("Send Error Mail\n" + e.message)
                except Exception as e:
                    print("Error Authentication Server: check the credentials \n" + e.message)
            except Exception as e:
                print("Error Connecting to Server : check the URL of the server and communications port ( 25 and ' the default ) \n" + e.message)
     
            print("Quit.")
            server.quit()
     
    except Exception as e:
            print (e.message)




