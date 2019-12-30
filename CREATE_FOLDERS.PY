
#CREATES FOLDERS IN THE ROOT OF A PRO PROJECT BASED ON AN ORGANIZATION-ENFORCED PROJECT FOLDER STRUCTURE
import os
import errno
import arcpy
folders = arcpy.GetParameterAsText(0)
curr = arcpy.mp.ArcGISProject("CURRENT").filePath
folder = "/".join(curr.split("\\")[:-1])+"/"

#This is the GIS project folder structure GRSM policy requires
#Edit this to meet your needs
#'Data\\Working' is where Create Standard GDB in Enforced Location in Pro Project will write the output FGDB
############
#EDIT ME
directories = ['Data','Data\\GPS','Data\\Working','Data\\Tabular','Products','Documents', 'Documents\\Pics_Graphics']
###########
basedirectory = folder +'\\'
for i in range (len (directories)):
    newDir = basedirectory + directories[i]
    try:
        os.makedirs(newDir)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
           raise
        else:
           print ("\nBE CAREFUL! Directory %s already exists." % newDir)


















