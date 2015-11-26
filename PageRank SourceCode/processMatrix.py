# ARGUMENTS : The filename of the inlinks graph
# RETURNS : An inlink dictionary with the list of inlinks mapped against each page

def processMatrix(fileName):
	
	inDict = {}
	f = open(fileName,'r')

	for line in f:

		pages = line.split(" ")
		page = pages.pop(0)

		page = page.split('\n').pop(0)

		if len(pages) != 0:
			if pages[0] != '':	
				pages[-1] = pages[-1].split('\n').pop(0)

				if '' in pages:
					pages.remove('')	
								
				inDict[page] = list(set(pages))
			else:
				inDict[page] = [] 

		else:
			inDict[page] = list(set(pages))

	return inDict



