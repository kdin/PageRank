# ARGUMENTS : Final page ranks of all the pages
# RETURNS : The top 50 pages and pageranks

def sortPagesByRank(Prs):
	
	sortedList = sorted(Prs, key=Prs.__getitem__)

	sortedList.reverse()

	i = 0 
	for page in sortedList:
		if i < 50:
			print page, ":", Prs[page]
			i += 1


