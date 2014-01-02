#Folder Renamed to LowerCase
#Eric 'Zander' Nelson

import os
import re
import time

folders = os.listdir('./')

for folder in folders:
	if os.path.isdir(folder):
		os.rename(folder, folder.lower())

#time.sleep(5)