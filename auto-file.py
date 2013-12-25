#Auto File Rename
#Eric 'Zander' Nelson

import os
import re

folders = os.listdir("../../../Python27/files-to-test")

def seasonRegX(folder):
	pattern = '([A-Za-z]+|[0-9])'
	q = re.search(pattern, folder)
	filename = ''

	for match in q.group:
		if match.lower() == 'season':
			filename += ' - s'
		else:
			filename += match

	return filename

for filename in folders:
	print seasonRegX(filename)