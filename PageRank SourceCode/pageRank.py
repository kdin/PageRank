# __author__ = Dinesh Kannan

# An implementation of PageRank algorithm to find page ranks of all pages in a given inlink graph

# Import external modules
from __future__ import division
import sys
import math

# User defined modules
from processMatrix import processMatrix
from pageOutlinks import pageOutlinks
from pageOutlinks import sinkNodes
from uniquePages import uniquePages
from rankResults import sortPagesByRank
from inLinksCount import inLinksCount

# Program global variables
d = 0.85
roundCount = 0
perplexityDifferenceList = [10,10,10,10]
perplexityPrevious = 1000

# Program constant containing unique pages
uniquePagesList = []


# ARGUMENTS : The file name of the inlink graph
# RETURNS  : The top 50 pages with according to page ranks as well as inlink counts
# Starts with equal probabilities for all pages and calculates page rank with the formula
# until the probabilities converge.
def pageRank(fileName):


	global uniquePagesList

	inLinks = processMatrix(fileName)
	print "THE SORTED PAGES BASED ON INLINKS:", inLinksCount(inLinks)

	outLinksCount = pageOutlinks(inLinks)

	sinkNodesList = sinkNodes(outLinksCount)

	uniquePagesList = uniquePages(fileName)
	uniquePagesList = list(set(uniquePagesList))

	totalPages = len(uniquePagesList)

	equalProbability = 1/totalPages
	sinkProportion = len(sinkNodesList)/totalPages

	print "++++++++++++++++++++++++++++++++++++++++++++++++_____________________PROPORTION OF SINKS",sinkProportion

	pagesWithoutInLinks = 0

	for page in uniquePagesList:
		if len(inLinks[page]) == 0:
			pagesWithoutInLinks += 1
		elif inLinks[page][0] == '' or inLinks[page][0] == ' ':
			pagesWithoutInLinks += 1

	print "PROPORTION OF PAGES WITHOUT INLINKS------->",(pagesWithoutInLinks/totalPages)


	Prs = {}
	newPrs ={}	
	uniformProportionNumber = 0
	rankProportion = 0
	rankList = []
	pRank = 0
	reverseDict = {}
	for page in uniquePagesList:
 		Prs[page] = equalProbability 
 		newPrs[page] = 0

	while pageRankNotConverged(Prs):

		sinkPr = 0
		for sinkNode in sinkNodesList:
			sinkPr += Prs[sinkNode]

		for page in uniquePagesList:
			newPrs[page] = (1-d)/totalPages
			newPrs[page] += d*(sinkPr/totalPages)

			if page in inLinks:			
				if len(inLinks[page]) == 0 or inLinks[page][0] == '' or inLinks[page][0] == ' ':
					newPrs[page] = newPrs[page]

				else:
					for inLink in inLinks[page]:
						if inLink != ' ' and inLink != '':
							if outLinksCount[inLink] != 0: 
								newPrs[page] += d*(Prs[inLink]/(outLinksCount[inLink]))
			
			else:
				newPrs[page] = newPrs[page]

		for page in uniquePagesList:
			Prs[page] = newPrs[page]
			
	sortPagesByRank(Prs)

	for page in uniquePagesList:
		if Prs[page] < equalProbability:
			uniformProportionNumber += 1

	rankProportion = uniformProportionNumber/totalPages	

	print "++++++++++++++++++++++++++++++++++++++++++++++++_____________________PROPORTION LESS THAN UNIFORM",rankProportion




# ARGUMENTS : the intermediate page ranks of all pages
# RETURNS : False, iff the page rank hasn't converged.
# Convergence is obtained when the difference in perplexities is lesser than 1 for atleast 4 iterations

def pageRankNotConverged(Prs):

	global perplexityDifferenceList
	global perplexityPrevious
	global roundCount

	entropy = 0
	for page in uniquePagesList:
		entropy += (Prs[page] * math.log(Prs[page],2))

	entropy = -entropy
	
	perplexity = pow(2,entropy)

	perplexityDifferenceList.pop(0)
	perplexityDifferenceList.append(perplexity-perplexityPrevious)

	perplexityPrevious = perplexity
	roundCount += 1
	print "PERPLEXITY VALUE FOR ROUND:",roundCount,"-------------------------------->",perplexity

	if perplexityDifferenceList[0] < 1 and perplexityDifferenceList[1] < 1 and perplexityDifferenceList[2] < 1 and perplexityDifferenceList[3] < 1:
		return False

	else:
		return True





if __name__ == "__main__" :

	fileName = sys.argv[1]

	pageRank(fileName)