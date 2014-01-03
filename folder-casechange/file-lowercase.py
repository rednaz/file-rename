# Files Renamed to LowerCase
# Eric 'Zander' Nelson

# imports for os, regex, and time
import os, re, time

files = os.listdir('.')

# for each file and folder in current directory
for myFile in files:
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

	# renames file
	os.rename(myFile, name)

#time.sleep(5)