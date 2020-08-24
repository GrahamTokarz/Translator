#List of possible inputs
strangewords = [
	'demon',
	'vampire',
	'language',
	'nathan',
	'mean',
	'spangley'
]

#List of first possible meanings
Aform = [
	'an evil spirit',
	'one that sucks blood',
	'spoken',
	'a name',
	'not nice',
	'formal usage'
]

#List of second possible meanings
Bform = [
	'an evil person',
	'reanimated dead',
	'written',
	'a derogatory name',
	'as a definition',
	'informal usage'
]

#List of translations for the first meanings
Atrans = {
	'demon': 'luccarta',
	'vampire': 'vevevlee',
	'language': 'lsebva',
	'nathan': 'Pokecha',
	'mean': 'shyiwu',
	'spangley': 'Spughleh'
}

#List of translations for the second meanings
Btrans = {
	'demon': 'isonscarya',
	'vampire': 'akeylom',
	'language': 'mockihaki',
	'nathan': 'Weepacha',
	'mean': 'sholint',
	'spangley': 'Spugleh'
}

#Checks if the input word is a word with multiple possible meanings
def check(word):
	if (strangewords.count(word) == 1):
		return "true"
	else:
		return "false"

#Queries the user about which meaning they would like to use for the input word, then returns the corresponsing Spangley word
def translate(word):
	context = ''
	while (context.lower() != Aform[strangewords.index(word)] and context.lower() != Bform[strangewords.index(word)]):
		 context = raw_input("What context is the best fit for " + word + ' in this situation? \n' + Aform[strangewords.index(word)] + ' or ' + Bform[strangewords.index(word)] + '? \n')
	if (context.lower() == Aform[strangewords.index(word)]):
		return Atrans[word]
	else:
		return Btrans[word]

#Returns the number of translation rules present for words with multiple meanings
def wordcount():
	return len(strangewords) * 2