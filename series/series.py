import os, re, time

def seriesName(folder):
	pattern = '([A-Za-z]+|[0-9])'
	q = re.split(pattern, folder)
	filename = ''

	i = 1

	filename += q[1];

	while q[i].lower() != 'season':
		i += 1;

	series = filename

	i += 2
	filename += ' - s'

	if (int(q[i]) < 10):
		filename += '0'
		filename += q[i]
	else:
		filename += q[i]

	return filename, series, q[i]

def episodeName(series, folder, title, epNumber, seasonNum):

	dest = series + '/' + 'Season ' + str(seasonNum) + '/'

	if seasonNum == 1 and epNumber == 1:
		os.makedirs(series)
		
	if not os.path.exists(dest):
		os.makedirs(dest)

	for episode in os.listdir(folder):
		temp = title + 'e'

		if epNumber < 10:
			temp += '0'
		temp += str(epNumber)
		epNumber += 1

		os.rename(folder + '/' + episode, dest + temp)

	return epNumber

series = ''
season = 1
epNum = 1

for folder in os.listdir('.'):
	if os.path.isdir(folder):
		epTitle, newSeries, newSeason = seriesName(folder)

		if newSeries != series:
			series = newSeries
			season = 1
			epNum = 1

		if newSeason != season:
			season = newSeason
			epNum = 1

		
		epNum = episodeName(series, folder, epTitle, epNum, season)

#time.sleep(5)
