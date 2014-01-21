# imports for os, regex, and time
import os, re, time

# rename function
# renames files/folders to lowercase
def rename(myFile):
	name = ''
	count = 0

	# regex, converts to lower and removes characters
	# saves what is kept into an array
	# can make additional changes here as necessary
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

# introduction message
print "Welcome to Zander's 'Naming Convention Converter' setup."
print "This program will automatically convert Files and Folders (as desired)"
print "into the proper naming convention for your CMS or other system."
print "The base function of this program converts file names to lower case and"
print "changes unwanted symbols (ie &, _) to dashes (-)."
print "This program can be modified to make other symbol changes as required."
print ""
print "======================================================================="
print "======================================================================="
print ""

# interface
# determines if the user wants to rename files and folders or just folders
looping = True
while looping:
	result = raw_input("Would you like to only rename folders? (Yes/No) ")
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
	result = raw_input("Would you like to include Subdirectories? (Yes/No) ")
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