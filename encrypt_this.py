
'''
Encrypt this!

You want to create secret messages which can be deciphered by the Decipher this! kata. Here are the conditions:

    Your message is a string containing space separated words.
    You need to encrypt each word in the message using the following rules:
        The first letter needs to be converted to its ASCII code.
        The second letter needs to be switched with the last letter
    Keepin' it simple: There are no special characters in input.

Examples:

encrypt_this("Hello") == "72olle"
encrypt_this("good") == "103doo"
encrypt_this("hello world") == "104olle 119drlo"
'''

def encrypt_this(text):
    return " ".join([encrypt_word(i) for i in text.split()])

def encrypt_word(word):
    numerical_segment = str(ord(word[0]))
    word = word[1:]
    if len(word) <= 1:
        return numerical_segment + word
    else:
        return numerical_segment + word[-1] + word[1:-1] + word[0]