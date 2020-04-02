class Node(object):
	def __init__(self, name):
		self.name = name
		self.connected = list()
		self.relation = dict() # relation of self with each key as value of dict

	def addConn (self, other, otherRelation="unknown"):
		# other is a node object
		for i in self.connected:
			if i.name == other.name:
				return False
		self.connected.append(other)
		self.relation[other.name] = otherRelation

	def setRelation(self, other, otherRelation):
		if type(other) == str:
			self.relation[other] = otherRelation
		else:
			self.relation[other.name] = otherRelation

	def __str__(self):
		return self.name

class Network(object):
	def __init__(self):
		self.Nodes = list()
		self.Edge = list()
		self.changed = False


	def loadNetwork(self, filename="network.txt"):
		networkFile = open(filename, 'r')
		for line in networkFile:
			line = line.strip().split("_")
			self.addEdge(line[0], line[1], line[2]) #nodeA nodeB relation
		networkFile.close()
		self.changed = False
		return True	
	
	def saveNetwork(self, filename="network.txt"):
		if not self.changed:
			return False 

		networkFile = open(filename, 'w')
		for i in self.Edge:
			line = i[0].name + "_" + i[1].name + "_" + i[2] + "\n"
			networkFile.write(line)
		networkFile.close()
		self.changed = False
		print("Network Saved Successfully. ")
		return True

	def addEdge(self, nodeA, nodeB, relationBetween):
		# nodeA and nodeB are simply text 
		A = self.nodeInNetwork(nodeA)
		B = self.nodeInNetwork(nodeB)

		if A == False:
			A = Node(nodeA)
			self.Nodes.append(A)
		if B == False:
			B = Node(nodeB)
			self.Nodes.append(B)

		if (A, B, relationBetween) in self.Edge:
			return False

		self.Edge.append((A, B, relationBetween))
		A.addConn(B, relationBetween)
		B.addConn(A, relationBetween)

		self.changed = True

	def removeEdge(self, nodeA, nodeB):
		#nodeA and nodeB are strings
		nodesFound = 0
		for i in self.Nodes:
			if i.name == nodeA:
				A = i
				nodesFound += 1
			if i.name == nodeB:
				B = i
				nodesFound += 1

		if nodesFound < 2:
			return False

		for j in self.Edge:
			if A in j and B in j:
				self.Edge.remove(j)
				A.connected.remove(B)
				B.connected.remove(A)
				del A.relation[B.name]
				del B.relation[A.name]

		self.changed = True
		return True

	def nodeInNetwork(self, nodeA):
		#check if nodeA already exists in the graph 
		for i in self.Nodes:
			if i.name == nodeA:
				return i
		return False

	def showNetwork(self):
		for i in self.Edge:
			print(i[0], i[1], i[2])

	def nodeCount(self):
		return len(self.Nodes)

	def density(self):
		#percentage
		n = self.nodeCount()
		return (len(self.Edge) / ((n**2 - n) / 2)) * 100

net = Network()
net.loadNetwork()
net.showNetwork()

print(net.density())



net.saveNetwork()