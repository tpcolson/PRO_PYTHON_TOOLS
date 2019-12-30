#STAND ALONE SCRIPT
#UPDATES AN AGOL HOSTED FEATURE SERVICE
import arcpy
import sys, string, os, calendar, datetime, traceback,smtplib
from arcpy import env
from subprocess import call

# Mail Server Settings
service = "AGOL_ITEM_NAME"
sd_filename = service + ".sd"
try:
    d = datetime.datetime.now()
    log = open("C:\\PYTHON_LOGS\LOG."+service+".txt","a")
    log.write("----------------------------" + "\n")
    log.write("----------------------------" + "\n")
    log.write("Log: " + str(d) + "\n")
    log.write("\n")
# Start process...
    starttime = datetime.datetime.now()
    log.write("Begin process:\n")
    log.write("     Process started at " + str(starttime) + "\n")
    log.write("\n")
    
    # Mail Server Settings
    SERVER = "1.2.3.4"
    PORT = "25"
    FROM = "ME@YOU.COM"
    MAILDOMAIN = '@ME.COM'
    # Data Steward getting the email. Needs to be their email address...without @nps.gov at the end
    userList=["BIG_FOOT"]
    # get a list of usernames from the list of named tuples returned from ListUsers
    userNames = [u for u in userList]
    # take the userNames list and make email addresses by appending the appropriate suffix.
    emailList = [name +  MAILDOMAIN for name in userNames]
    TO = emailList
    # Grab date for the email
    DATE = d

    # Sign in to portal
    arcpy.SignInToPortal('https://www.arcgis.com', 'USER', 'PASSWORD')

    # Set output file names
    outdir = r"C:\PRODUCTION\GRSM_EXOTICS"
    sd_filename = service + ".sd"
    sd_output_filename = os.path.join(outdir, sd_filename)
    sddraft_filename = service + ".sddraft"
    sddraft_output_filename = os.path.join(outdir, sddraft_filename)
    #Delete any left over SD files from failed previous run
    try:
        os.remove(sd_output_filename)
        print("Successfully deleted ", sd_output_filename)
    except:
        print("Error while deleting file ", sd_output_filename, ", perhaps it doesn't exist")
    try:
        os.remove(sddraft_output_filename)
        print("Successfully deleted ", sddraft_output_filename)
    except:
        print("Error while deleting file ", sddraft_output_filename, ", perhaps it doesn't exist")       

    # Reference map to publish
    aprx = arcpy.mp.ArcGISProject(r"C:\PRODUCTION\GRSM_EXOTICS\GRSM_EXOTICS_PRO.aprx")
    m = aprx.listMaps("GRSM_VEG_EXOTICS_SCOUTING_AGOL")[0]

    # Create FeatureSharingDraft and set service properties
    # https://pro.arcgis.com/en/pro-app/arcpy/sharing/featuresharingdraft-class.htm
    sharing_draft = m.getWebLayerSharingDraft("HOSTING_SERVER", "FEATURE", service)
    sharing_draft.summary = "Great Smoky Mountains National Park Exotics Scouting Locations"
    sharing_draft.tags = "GRSM, EXOTICS, Weeds, Invasive"
    sharing_draft.description = "The National Invasive Species Information Management System (NISIMS) is the NPS standard invasive species data management tool. NISIMS was originally created to be a comprehensive tool by the Bureau of Land Management (BLM) to standardize the collection of invasive species data. NPS adopted the BLM’s data management system for invasive species to standardize the collection and management of exotic plant data collected by the Exotic Plant Management Teams (EPMT). NISIMS was identified as an appropriate replacement for the Alien Plant Control and Monitoring database (APCAM), the previous exotic plant data management system, because it requires the input of data identified as important to collect by NPS, and also includes a spatial component that allows for the mapping and further analysis of infestations. Further, NISIMS was chosen due to its potential for standardizing exotic plant data management across DOI agencies."
    sharing_draft.credits = "Great Smoky Mountains National Park"
    sharing_draft.useLimitations = "The National Park Service shall not be held liable for improper or incorrect use of the data described and/or contained herein. These data and related graphics (i.e. GIF or JPG format files) are not legal documents and are not intended to be used as such. The information contained in these data is dynamic and may change over time. The data are not better than the original sources from which they were derived. It is the responsibility of the data user to use the data appropriately and consistent within the limitations of geospatial data in general and these data in particular. The related graphics are intended to aid the data user in acquiring relevant data; it is not appropriate to use the related graphics as data. The National Park Service gives no warranty, expressed or implied, as to the accuracy, reliability, or completeness of these data. It is strongly recommended that these data are directly acquired from an NPS server and not indirectly through other sources which may have changed the data in some way. Although these data have been processed successfully on computer systems at the National Park Service, no warranty expressed or implied is made regarding the utility of the data on other systems for general or scientific purposes, nor shall the act of distribution constitute any such warranty. This disclaimer applies both to individual use of the data and aggregate use with other data."
    #sharing_draft.portalFolder = "Front Country"
    sharing_draft.overwriteExistingService = "true"
    sharing_draft.allowExporting = True

    # Create Service Definition Draft file
    sharing_draft.exportToSDDraft(sddraft_output_filename)

    # Stage Service
    # https://pro.arcgis.com/en/pro-app/tool-reference/server/stage-service.htm
    sd_output_filename = os.path.join(outdir, sd_filename)
    arcpy.StageService_server(sddraft_output_filename, sd_output_filename)

    # Share to portal
    # https://pro.arcgis.com/en/pro-app/tool-reference/server/upload-service-definition.htm
    print("Uploading Service Definition...")
    arcpy.UploadServiceDefinition_server(sd_output_filename,
                                         "My Hosted Services",
                                         "",
                                         "",
                                         "EXISTING",
                                         "existingFolder",
                                         "",
                                         "OVERRIDE_DEFINITION",
                                         "SHARE_ONLINE",
                                         "PUBLIC",
                                         "SHARE_ORGANIZATION",
                                         ["GRSM","Great Smoky Mountains National Park Open Data"] )
    #Turn on sync and export
    from arcgis.gis import GIS
    gis=GIS('https://www.arcgis.com', 'GRSM_GIS', 'GRSMpassword1!')
    search_result= gis.content.search(service, "Feature Layer")
    update_item = search_result[0]
    from arcgis.features import FeatureLayerCollection
    update_flc = FeatureLayerCollection.fromitem(update_item)
    update_flc.properties
    update_dict = {"capabilities": "Query,Sync,Extract"}
    update_flc.manager.update_definition(update_dict)

    # Clean up SD files
    try:
        os.remove(sd_output_filename)
        print("Successfully deleted ", sd_output_filename)
    except:
        print("Error while deleting file ", sd_output_filename, ", perhaps it doesn't exist")
    try:
        os.remove(sddraft_output_filename)
        print("Successfully deleted ", sddraft_output_filename)
    except:
        print("Error while deleting file ", sddraft_output_filename, ", perhaps it doesn't exist")        
      

    # Write nothing to log if success.
    endtime = datetime.datetime.now()
    log.write("     Completed successfully in " 
           + str(endtime - starttime) + "\n")
    log.write("\n")
    log.close()
    print('done')

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
    SUBJECT = "Notification of Un-Successful AGOL Update of "+service 
    MSG = "Did Not Update: {} - ID: {} at "+ str(DATE)+ "; " +pymsg + "; " + msgs
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
