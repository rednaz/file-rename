#Folder and all SubFolders Renamed to LowerCase
#Eric 'Zander' Nelson

# imports for os, regex, and time
import os, re, time

# rename function
# path is for subdirectories
def rename(myFile, path):
	name = ''
	count = 0

	# regex, converts to lower and removes characters
	# saves what is kept into an array
	q = re.split('[-_&$#]', myFile.lower())

	# for each part in the array, add to new name
	for z in q:
		if z != '':
			name += z
			if count < len(q) - 1:
				name += '-'

		count += 1

	os.rename(os.path.join(path, myFile), os.path.join(path, name))

for path, folders, files in os.walk('.'):
	for folder in folders:
		rename(folder, path)

#time.sleep(5)