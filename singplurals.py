#List of input words that can be singular or plural
singplurals = [
	'furniture',
	'lightning',
	'pasta',
	'music',
	'popcorn'
]

#List of singular translations
trans = {
	'furniture': 'aimalatno',
	'lightning': 'litchey',
	'pasta': 'mopadirlo',
	'music': 'mytapbid',
	'popcorn': 'nolpina'
}

#List of plural translations
pluTrans = {
	'furniture': 'aimalatnoitt',
	'lightning': 'litcheyitt',
	'pasta': 'mopadirloitt',
	'music': 'mytapbiditt',
	'popcorn': 'nolpinaitt'
}

#Checks if the input word is a word that can be singular or plural in nature
def check(word):
	if (singplurals.count(word) == 1):
		return "true"
	else:
		return "false"

#Queries the user if they would like the singular or plural form of the input word, then returns the equivalent Spangley word
def translate(word):
	singplu = ''
	while (singplu.lower() != "singular" and singplu.lower() != "plural"):
		singplu = raw_input("Singular or Plural form of " + word + "? \n")
	if (singplu.lower() == "singular"):
		return trans[word]
	else:
		return pluTrans[word]

#Returns the number of tranlation rules present for words that can be either singular or plural.
def wordcount():
	return len(singplurals)