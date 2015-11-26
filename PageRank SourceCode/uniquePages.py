# ARGUMENTS : The filename of the inlinks graph
# RETURNS : A List of unique pages in the inlinks graph
# Reads the file line by line to check duplicates and adds
# unique pages to the list

def uniquePages(fileName):

	uniquePagesList = []

	f = open(fileName,'r')
		
	for line in f:
		pages = line.split(' ')

		pages[-1] = pages[-1].split('\n').pop(0)

		if '' in pages:
			pages.remove('')

		for page in pages:

			if page not in uniquePagesList:
				uniquePagesList.append(page)

	return uniquePagesList


