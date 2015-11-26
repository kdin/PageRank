# ARGUMENTS : An inLinks Dictionary
# RETURNS : The count of outlinks against each page as a dictionary
# Counts the outlinks from each page and is zero when there is none.

def pageOutlinks(inDict):

	outDict = {}
	
	for link in inDict:
		if link not in outDict:
			outDict[link] = 0
		for page in inDict[link]:
			if page != '':
				if page in outDict:
					outDict[page] += 1

				else:
					outDict[page] = 1

	return outDict

# ARGUMENTS : The outlinks count dictionary
# RETURNS : The List of sinknodes , pages that has no outlinks

def sinkNodes(outLinks):
	
	sinkNodesList = []
	for page in outLinks:

		if outLinks[page] == 0:
			sinkNodesList.append(page)

	return sinkNodesList
