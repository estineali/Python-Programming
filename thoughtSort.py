#Sorting algorithm i thought of during Algorithms class

'''
	Todo:
	 - Optimize: improve space complexity
	 - reduce number of built in functions used 
'''
def ThoughtSort(lst):
	m = lst.copy()
	x = []
	while len(m) > 1:
		mx = max(m)
		m.remove(mx)
		mn = min(m)
		m.remove(mn)
		x.insert(len(x)//2, mx)
		x.insert(len(x)//2, mn)
	if len(m) == 1:
		x.insert(len(x)//2, m[0])
	return x 


l = [13, 44, 73, -5, -41, 0, 17]
print(ThoughtSort(l))