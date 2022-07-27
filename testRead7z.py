
from dataclasses import field
import os
import zipfile
from numpy import extract
import py7zr
""" zipfiles = zipfile.ZipFile("YQA4-FAS8040-0107-B.7z", 'r')
print(zipfiles.namelist()) """


""" archive = py7zr.SevenZipFile('YQA4-FAS8040-0107-B.7z', 'r')
allfiles = archive.getnames()
for file in allfiles: 
    print(file)
    with open(file, 'r') as infile: 
        infile.read()      """


file_names = os.listdir("./source7zfile/")
for file in file_names:
    if file.endswith(".7z"):
        fileName = file.replace(".7z", ".zip")
        print("fileName is " + fileName)
        fileName = os.path.join("./targetzip/",file)
        print("fileName is " + fileName)
        extractDir = file.replace(".7z", "")
        extractDir = os.path.join("./source7zfile/",extractDir)

        print("extractDir is " + extractDir)
        file = os.path.join("./source7zfile/",file)

        ##unzip
        with py7zr.SevenZipFile(file, 'r') as archive:
            archive.extractall(extractDir)
            
file_names2 = os.listdir("./source7zfile/")
for file in file_names2:
    if not file.endswith(".7z"):       
        fileName = os.path.join("./targetzip/",file)
        extractDir = os.path.join("./source7zfile/",file)
        fileName = fileName + '.zip'
        print("fileName is " + fileName)
        print("extractDir is " + extractDir)
        ##zip
        with zipfile.ZipFile(fileName, mode="w") as archive:
            for filename2 in os.listdir(extractDir):
                archive.write(extractDir + "/" + filename2, arcname = filename2)