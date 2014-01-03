#Folder and all SubFolders Renamed to LowerCase
#Eric 'Zander' Nelson

import os, re, time

def rename(myFile, path):
	name = ''
	count = 0

	q = re.split('[-_&$#]', myFile.lower())

	for z in q:
		if z != '':
			name += z
			if count < len(q) - 1:
				name += '-'

		count += 1

	#print q

	os.rename(os.path.join(path, myFile), os.path.join(path, name))

for path, folders, files in os.walk('.'):
	for folder in folders:
		rename(folder, path)

	for aFile in files:
		rename(aFile, path)

#time.sleep(5)