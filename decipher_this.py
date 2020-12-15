'''
You are given a secret message you need to decipher. Here are the things you need to know to decipher it:

For each word:

    the second and the last letter is switched (e.g. Hello becomes Holle)
    the first letter is replaced by its character code (e.g. H becomes 72)

Note: there are no special characters used, only letters and spaces

Examples

decipherThis('72olle 103doo 100ya'); // 'Hello good day'
decipherThis('82yade 115te 103o'); // 'Ready set go'

Source: Codewars.
'''

def decipher_this(string):
    #Decipher a string of words. 
    return " ".join([decipher_word(i) for i in string.split()])

def decipher_word(word):
   #Decipher a single word.  
    
    numeric_segment = ""
    if word[0:3].isnumeric():
        numeric_segment = chr(int(word[0:3]))
        word = word[3:]
    elif word[0:2].isnumeric():
        numeric_segment = chr(int(word[0:2]))
        word = word[2:]
    
    if len(word) <= 1:
        return numeric_segment + word

    return numeric_segment + word[-1] + word[1:-1] + word[0]

# Test.assert_equals(decipher_this("65 119esi 111dl 111lw 108dvei 105n 97n 111ka"), "A wise old owl lived in an oak")
# Test.assert_equals(decipher_this("84eh 109ero 104e 115wa 116eh 108sse 104e 115eokp"), "The more he saw the less he spoke")
# Test.assert_equals(decipher_this("84eh 108sse 104e 115eokp 116eh 109ero 104e 104dare"), "The less he spoke the more he heard")
# Test.assert_equals(decipher_this("87yh 99na 119e 110to 97ll 98e 108eki 116tah 119esi 111dl 98dri"), "Why can we not all be like that wise old bird")
# Test.assert_equals(decipher_this("84kanh 121uo 80roti 102ro 97ll 121ruo 104ple"), "Thank you Piotr for all your help")
