from striprtf.striprtf import rtf_to_text
import string

def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts



with open("input/TestGreekLetter.txt") as infile:
    text = infile.read()
    #strip integers
    text = text.translate({ord(i): None for i in '1234567890'})

print(text)
print("------- word count ---------")
print( word_count(text))

print("------- word count ---------")
