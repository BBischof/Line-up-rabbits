import sys
verbose = False
if len(sys.argv) >= 2:
	args = sys.argv
	totalNumber = int(args[1])
	leftShowingNum = int(args[2])
	rightShowingNum = int(args[3])
	if len(args) >= 5:
		if args[4] == "-v":
			verbose = True

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

def powerset(elements):
    if len(elements) > 0:
        head = elements[0]
        for tail in powerset(elements[1:]):
            yield [head] + tail
            yield tail
    else:
        yield []

def computeMultiplicity(behinds):
	mult = 1
	for b in behinds:
		if len(b) > 0:
			mult = mult * factorial(len(b))
	return mult

def genSubsetsWithComplements(listToSeparate):
	if len(listToSeparate) > 0:
		p = powerset(listToSeparate)
		pairs = []
		for s in p:
			pairs.append((s, [x for x in listToSeparate if x not in s]))
		return pairs
	else:
		return "err"

def split(inputList, tallsList, behindList):
	#multiplicity = m
	if len(inputList) == 0:
		if verbose:
			print str(tallsList) + ", " + str(behindList) + ", "  + str(len(tallsList)) + ", " + str(computeMultiplicity(behindList))
		#outputList[i].append([tallsList, behindList, len(tallsList), computeMultiplicity(behindList)])
		outputDict[currentDiv][currentSide].append([len(tallsList), computeMultiplicity(behindList)])
		#multiplicity += computeMultiplicity(behindList)
	elif len(inputList) == 1:
		if verbose:
			print str(tallsList + inputList) + ", " + str(behindList) + ", " + str(len(tallsList + inputList)) + ", " + str(computeMultiplicity(behindList))
		#outputList[i].append([tallsList + inputList, behindList, len(tallsList + inputList), computeMultiplicity(behindList)])
		outputDict[currentDiv][currentSide].append([len(tallsList + inputList), computeMultiplicity(behindList)])
		#multiplicity += computeMultiplicity(behindList)
	elif len(inputList) > 1:
		for p in genSubsetsWithComplements(inputList[:-1]):
			if (len(tallsList) >= 1):
				split(p[0], tallsList + [inputList[-1]], behindList + [p[1]])
			elif (len(tallsList) == 0):
				split(p[0], [inputList[-1]], behindList + [p[1]])
			#return multiplicity

def countPatterns(l,r,pats):
	total = 0
	for key in pats.keys():
		lmult = 0
		rmult = 0
		for order in pats[key]["L"]:
			if order[0]==l-1:
				lmult += order[1]
		for order in pats[key]["R"]:
			if order[0]==r-1:
				rmult += order[1]
		total += lmult*rmult
	print "showing left: " + str(l) + " showing right: " + str(r) + " number of patters: " + str(total)

if ((totalNumber + 1 >= leftShowingNum + rightShowingNum) & (leftShowingNum >= 1) & (rightShowingNum >= 1)):
	lst = range(1,totalNumber+1)
	if verbose:
		print lst
	outputList = []
	i = 0
	outputDict = {}
	currentDiv = ""
	currentSide = ""
	for division in genSubsetsWithComplements(lst[:-1]):
		currentDiv = str(division)
		# outputList.append([division, "||"])
		outputDict[currentDiv]={"L": [], "R": []}
		# print "#############################################"
		if verbose:
			print "division: " + str(division)
		# print "#############################################"
		# print "left side"
		currentSide = "L"
		#multiplicity = 0
		split(division[0], [], [])
	#	print "right side"
		currentSide = "R"
		# outputList[i].append("|")
		split(division[1], [], [])
		i +=1

	for key in outputDict.keys():
		if verbose:
			print key,outputDict[key]

	if verbose:
			print "###############"

	countPatterns(leftShowingNum,rightShowingNum,outputDict)
else:
	print "There are zero patterns, check your conditions!"

#print genSubsetsWithComplements(lst)







