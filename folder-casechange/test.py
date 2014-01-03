# imports for os, regex, and time
import os, re, time

# rename function
def rename(myFile):
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

	# returns new name
	return name

def walk(justFolder, sub):
	if sub:
		for path, folders, files in os.walk('.'):
			for folder in folders:
				name = rename(folder)
				os.rename(os.path.join(path, folder), os.path.join(path, name))

			if not justFolder:
				for aFile in files:
					name = rename(aFile)
					os.rename(os.path.join(path, aFile), os.path.join(path, name))

	else:
		# for each folder in current directory
		for folder in os.listdir('.'):
			if os.path.isdir(folder) or not justFolder:	# if is a folder or checking all files
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



result = raw_input("Rename only folders?")
result = result.lower()
if result == 'y' or result == 'yes':
	foldersOnly = True
elif result == 'n' or result == 'no':
	foldersOnly = False
else:
	print "nope"

result = raw_input("Include Subdirectories?")
result = result.lower()
if result == 'y' or result == 'yes':
	subdirectories = True
elif result == 'n' or result == 'no':
	subdirectories = False
else:
	print "nope"

walk(foldersOnly, subdirectories)

time.sleep(5)
