def t9_interface(letter):
	#returns corresponding digit
	alpha_map = { 2: 'abc', 3: 'def',
				  4: 'ghi', 5: 'jkl', 6: 'mno', 
				  7: 'pqrs', 8: 'tuv', 9: 'wxyz'}
	for i in alpha_map:
		if letter.lower() in alpha_map[i]:
			return str(i)

def convert_to(letter_string):
	#returns corresponding numstring
	num_string = ''
	for i in letter_string.strip().lower():
		if i == " ":
				num_string += i
		else:
			for j in alpha_map:
				if i in alpha_map[j]:
					num_string += str(j)
			
	return num_string


def reduce_string(letter_string):
	#returns reduced string  
	vowels = "aeiou"
	return "".join([i for i in letter_string.lower() if i not in vowels]).capitalize()


print(reduce_string("hello world"))


