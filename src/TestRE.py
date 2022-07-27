import re
""" 
keyLine = '	 product identification=DS2246'
searchModelName = re.search( r'(.*)product identification=(.*?).*', keyLine, re.M|re.I)

print(searchModelName.group(0).replace("	 product identification=", ""))


tempString = " a b c "
print(tempString.strip())

keyLine2 = '      '
searchSpace = re.search( r'( *)', keyLine2, re.M|re.I)

print(keyLine2.isspace()) """

""" keyLine3 = "		Shelf 0: DS224-12  Firmware rev. IOM12 A: 0220  IOM12 B: 0220"
searchDrivePartNumber = re.search( r'(.*)Firmware rev. (.*?) A: (.*?)  (.*?) B: (\d{3,})', keyLine3, re.M|re.I)
print(searchDrivePartNumber)
print(searchDrivePartNumber.group(2))
print(searchDrivePartNumber.group(3))
print(searchDrivePartNumber.group(4))
print(searchDrivePartNumber.group(5))

keyLine4 = "X-Netapp-asup-serial-num: 940000482032"
searchDrivePartNumber2 = re.search( r'X-Netapp-asup-serial-num: (\d{3,})', keyLine4, re.M|re.I)
print(searchDrivePartNumber2)
print(searchDrivePartNumber2.group(0))
print(searchDrivePartNumber2.group(1)) """



keyLine4 = "  product identification=DS224-12"
searchSystemVersion = re.search( r'(.*)product identification=(.*?).*', keyLine4, re.M|re.I)
print(searchSystemVersion)
print(searchSystemVersion.group(0))
print(searchSystemVersion.group(1))
print(searchSystemVersion.group(2))
