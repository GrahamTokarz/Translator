#List of inputs that are irregular plurals
irregularplurals = [
	'sixty',
	'six',
	'celery',
	'ninety',
	'miss',
	'child',
	'pass',
	'mulch',
	'goose',
	'chemistry',
	'mongoose', #Both Mongeese and mongooses are acceptable
	'eighty',
	'cyclops',
	'person',
	'elf',
	'sphynx',
	'seventy',
	'fifty',
	'twenty',
	'fourty',
	'thirty',
	'sky',
	'woman',
	'mass',
	'electricity'
]

#List of corresponding translations
trans = {
	'sixty': 'antina',
	'six': 'antinat',
	'celery': 'badboychoopyuk',
	'ninety': 'bontna',
	'miss': 'cadc',
	'child': 'chainy',
	'pass': 'colin',
	'mulch': 'cowee',
	'goose': 'dudugalata',
	'chemistry': 'fsshtshhkerbloomy',
	'mongoose': 'kewaht',
	'eighty': 'kikna',
	'cyclops': 'lampanichaon',
	'person': 'lihus',
	'elf': 'nav',
	'sphynx': 'myaxxa',
	'seventy': 'patna',
	'fifty': 'pinna',
	'twenty': 'ruana',
	'fourty': 'snalna',
	'thirty': 'twina',
	'sky': 'whishi',
	'woman': 'woh',
	'mass': 'womusieh',
	'electricity': 'xatolero'
}

#Checks if the input is an irregular plural
def check(word):
	if (irregularplurals.count(word) == 1):
		return "true"
	else:
		return "false"

#Returns the Spangley translation of the input
def translate(word):
	return trans[word]

#Returns the number of irregular plural translation rules present
def wordcount():
	return len(irregularplurals)