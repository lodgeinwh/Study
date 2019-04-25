VOWELS = "AEIOUY"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"

def checkio(text):
    import string
    text = text.upper()
    for i in text:
        if i in string.punctuation:
            text = text.replace(i, ' ')
        elif i in VOWELS:
            text = text.replace(i, 'v')
        elif i in CONSONANTS:
            text = text.replace(i, 'c')
	text = text.strip().split(' ')
	
	count = 0
	for string in text:
		if len(string) > 1 and string.isalpha():
			if 'vv' not in string and 'cc' not in string:
				count += 1
	return count

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("My name is ...") == 3, "All words are striped"
    assert checkio("Hello world") == 0, "No one"
    assert checkio("A quantity of striped words.") == 1, "Only of"
    assert checkio("Dog,cat,mouse,bird.Human.") == 3, "Dog, cat and human"