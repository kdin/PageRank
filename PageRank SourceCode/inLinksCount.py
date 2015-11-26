from processMatrix import processMatrix

# ARGUMENTS : An inlinks dictionary
# RETURNS : The count of inlinks of all pages

def inLinksCount(inLinks):
	
	inLinkCount = {}
	for page in inLinks:
		inLinkCount[page] = len(inLinks[page])

	sortedList = sorted(inLinkCount, key=inLinkCount.__getitem__)

	for page in sortedList:

		print "PAGE:",page,"--->",inLinkCount[page]
