# imports for os, regex, and time
import os, re, time

# rename function
# renames files/folders to lowercase
def rename(myFile):
	name = ''
	count = 0

	# regex, converts to lower and removes characters
	# saves what is kept into an array
	q = re.split('[-_&$# ]', myFile.lower())

	# for each part in the array, add to new name
	for z in q:
		if z != '':
			name += z
			if count < len(q) - 1:
				name += '-'

		count += 1

	# returns new name
	return name

# walk function
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
		# for each file or folder in current directory
		for folder in os.listdir('.'):
			if os.path.isdir(folder) or not justFolder:	# if is a folder or checking all files
				name = rename(folder)
				os.rename(folder, name)


# interface
# determines if the user wants to rename files and folders or just folders
looping = True
while looping:
	result = raw_input("Rename only folders? (Yes/No) ")
	result = result.lower()
	if result == 'y' or result == 'yes':
		foldersOnly = True
		looping = False
	elif result == 'n' or result == 'no':
		foldersOnly = False
		looping = False
	else:
		print "Please enter either yes or no"

# determines if the user wants to include subdirectories
looping = True
while looping:
	result = raw_input("Include Subdirectories? (Yes/No) ")
	result = result.lower()
	if result == 'y' or result == 'yes':
		subdirectories = True
		looping = False
	elif result == 'n' or result == 'no':
		subdirectories = False
		looping = False
	else:
		print "Please enter either yes or no"

walk(foldersOnly, subdirectories)

# time.sleep(5)