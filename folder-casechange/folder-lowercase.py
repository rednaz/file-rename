#Folder Renamed to LowerCase
#Eric 'Zander' Nelson

import os, re, time

folders = os.listdir('./')

for folder in folders:
	if os.path.isdir(folder):
		name = ''
		count = 0

		q = re.split('[_&-/$/#]', folder.lower())

		for z in q:
			if z != '':
				name += z
				if count < len(q) - 1:
					name += '-'

			count += 1

		os.rename(folder, name)

#time.sleep(5)