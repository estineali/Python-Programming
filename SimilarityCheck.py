def similar(stringA, stringB):
	
	stringA = stringA.strip().lower()
	stringB = stringB.strip().lower()

	if len(stringB) > len(stringA):
		stringA, stringB = stringB, stringA 

	#if they are identical, then they are similar
	if stringA == stringB:
		return True

	#if one is in another, then they are similar
	if stringA in stringB or stringB in stringA: 
		return True

	if len(stringB) > 1:
		return similar(stringA, stringB[:-1])
	else:
	 	return False


def percentageSimilarity(stringA, stringB):
	#How much stringA is similar to stringB
	#returns float
	return 0.0







A = "Medicine"

B = "Medicinal"


print(similar(A, B))