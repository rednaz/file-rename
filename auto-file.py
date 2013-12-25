#Auto File Rename
#Eric 'Zander' Nelson

import os
import re

folders = os.listdir("../../../../../../Python27/files-to-test")

def seasonRegX(folder):
	pattern = '([A-Za-z]+|[0-9])'
	q = re.split(pattern, folder)
	filename = ''

	i = 1

	filename += q[1];

	while q[i].lower() != 'season':
		i += 1;

	i += 2
	filename += ' - s'

	if (int(q[i]) < 10):
		filename += '0'
		filename += q[i]
	else:
		filename += q[i]

	return filename

for filename in folders:
	print seasonRegX(filename)