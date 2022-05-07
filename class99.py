import os
import shutil

source=input("enterSourceFolderName")
destination=input("enterDestinationFolderName")
source=source+'/'
destination=destination+'/'
listOfFiles=os.listdir(source)
for file in listOfFiles:
    shutil.copy((source+file),destination)

    