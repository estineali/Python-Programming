import math as m 

coordinates = [(-2, 2), (1, 1), (0, 0)]

def dist(A, B):
	sq_val = (B[0] - A[0])**2 + (B[1] - A[1])**2 
	return (sq_val, m.sqrt(sq_val))

def midpoint(A, B):
	return ((A[0] + B[0]) / 2, (A[1] + B[1])/2)

def gradient(A, B):
	return (B[1] - A[1])/(B[0] - A[0])

print("AB = ", dist(coordinates[0], coordinates[1]))
print("midpoint AB = ", midpoint(coordinates[0], coordinates[1]))
print("gradient AB = ", gradient(coordinates[0], coordinates[1]))
print("AC = ", dist(coordinates[0], coordinates[2]))
print("midpoint AC = ", midpoint(coordinates[0], coordinates[2]))
print("gradient AC = ", gradient(coordinates[0], coordinates[2]))
print("BC = ", dist(coordinates[1], coordinates[2]))
print("midpoint BC = ", midpoint(coordinates[1], coordinates[2]))
print("gradient BC = ", gradient(coordinates[1], coordinates[2]))