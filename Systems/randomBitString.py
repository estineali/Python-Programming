import random

def genString(size, pref=False, startEndBit=0):
	retString = ""
	if pref:
		retString += str(startEndBit)
	
	for i in range(size - 2):
		retString += str(random.randint(0, 1))

	if pref:
		retString += str(startEndBit)
	
	return retString

def differentialBitString(partitions):
	# Returns a string of bits 
	# for example for RISC V R-Type Instructions 
	# each shift in meaning would shift the bits 

	# print(differentialBitString([7, 5, 5, 3, 5, 7]))
	# Run this to understand 
	# 7 bits of Funct7 and opcode, 5 for each register rs1 rs2 rd, 3 for funct3
	
	retString = ""
	
	adding = True

	for i in range(len(partitions)):
		retString += int(partitions[i]) * str(int(adding))
		adding = not adding 

	return retString 

def convertToUnsig(binString):
	binString = binString[::-1]
	decVal = 0 
	for i in range(len(binString)):
		decVal += int(binString[i]) * (2 ** i)

	return decVal

def convertToSigned(binString):
	#2s Compliment 
	negative = False

	if binString[0] == "1":
		negative == True
	binString = binString[::-1]
	decVal = 0 
	for i in range(len(binString) - 1):
		decVal += int(binString[i]) * (2 ** i)

def GenerateInstR_arg(operation, rd=None, rs1=None, rs2=None):
	# work if ind
	retBinString = ""
	return retBinString
