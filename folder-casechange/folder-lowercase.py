# Folder Renamed to LowerCase
# Eric 'Zander' Nelson

# imports for os, regex, and time
import os, re, time

# for each folder in current directory
for folder in os.listdir('.'):
	if os.path.isdir(folder):	#only if a folder
		name = ''
		count = 0

		# regex, converts to lower and removes characters
		# saves what is kept into an array
		q = re.split('[-_&$#]', folder.lower())

		# for each part in the array, add to new name
		for z in q:
			if z != '':
				name += z
				if count < len(q) - 1:
					name += '-'

			count += 1

		# renames file
		os.rename(folder, name)

#time.sleep(5)