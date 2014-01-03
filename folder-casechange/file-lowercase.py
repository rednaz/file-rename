#files Renamed to LowerCase
#Eric 'Zander' Nelson

import os, re, time

files = os.listdir('./')

for myFile in files:
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

	os.rename(myFile, name)

#time.sleep(5)