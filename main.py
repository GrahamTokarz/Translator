import regularplurals
import nonplurals
import irregularplurals
import singplurals
import strangewords

#Initializing variables
lang = 'NA'
query = '';
result = ''
punct = ''
#List of punctuation to remove from the input
punctuation = [
	'!',
	'?',
	'.',
	',',
	':',
	';',
	'-'
]

#List of input phrases
phrases = [
	'cheese doodles',
	'cheese pizza',
	'cheese cubes',
	'cough drop',
	'ferret with extra whiskers',
	'peanut butter',
	'ocean tree',
	"good night sleep good don't be of the having dreams",
	'iron man',
	'captain america',
	'spider man',
	'the flash',
	'greek god of the',
	'roman god of the',
	'alarm clock',
	'roller coaster',
	'language arts',
	'half a day',
	'12 hours',
	'twelve hours',
	"don't do"
]

#List of corresponding translations
phraseTrans = {
	'cheese doodles': 'queiso',
	'cheese pizza': 'wueiso',
	'cheese cubes': 'pueiso',
	'cough drop': 'smogulous',
	'ferret with extra whiskers': 'shmah',
	'peanut butter': 'puntaer',
	'ocean tree': 'puntastche',
	"good night sleep good don't be of the having dreams": 'mufslaep',
	'iron man': 'vooshhuwah',
	'captain america': 'frensha',
	'spider man': 'weiwah',
	'the flash': 'alica',
	'greek god of the': 'mikuntra',
	'roman god of the': 'mokontri',
	'alarm clock': 'aghtiblaghtimytonlesterbont',
	'roller coaster': 'paterromtanpal',
	'language arts': 'akosnoze',
	'half a day': 'leveny',
	'12 hours': 'leveny',
	'twelve hours': 'leveny',
	"don't do": 'shalorm'
}


#Start of output and input
print 'What language are you translating from?'

#Stalls the program until the user inputs S, E, or WordCount
while lang != 'E' and lang != 'S' and lang != 'WordCount':
	lang = raw_input("E for English, S for Spangley. \n")

#Begins the process of translating from Enlgish to Spangley by taking a user input
if (lang == 'E'):
	query = raw_input("Translating from English. Please enter your query. \n")
	print "Processing... Please wait."
	query = query.lower()
	queryIndex = 0
	secIndex = 0

	#Searches for phrases in the query and replaces them with their Spangley equivalent
	newquery = query
	index = 0
	while (index < len(phrases)):
		if (newquery.find(phrases[index]) != -1):
			pPos = newquery.find(phrases[index])
			ePos = pPos + len(phrases[index])
			newquery = newquery[:pPos] + phraseTrans[phrases[index]] + newquery[ePos:]
			print(newquery)
		index = index + 1
			
	#Runs checks for each word except the last to see if it is present in any of the categories of words
	while (' ' in newquery):
		secIndex = newquery.find(' ')
		#Removes punctuation from the word if it is present and runs checks on the word. If the word has a matching translation, it is replaced. At the end of the cycle, the punctuation is replaced.
		if (punctuation.count(newquery[queryIndex:secIndex][len(newquery[queryIndex:secIndex]) - 1]) == 1):
			punct = newquery[queryIndex:secIndex][len(newquery[queryIndex:secIndex]) - 1]
			newquery = newquery[queryIndex:secIndex][:len(newquery[queryIndex:secIndex]) - 1] + newquery[(secIndex):]
			secIndex = secIndex - 1
		if (nonplurals.check(newquery[queryIndex:secIndex]) == "true"):
			result = result + nonplurals.translate(newquery[queryIndex:secIndex]) + ' '
		elif (regularplurals.check(newquery[queryIndex:secIndex]) == "true"):
			result = result + regularplurals.translate(newquery[queryIndex:secIndex]) + ' '
		elif (irregularplurals.check(newquery[queryIndex:secIndex]) == "true"):
			result = result + irregularplurals.translate(newquery[queryIndex:secIndex]) + ' '
		elif (singplurals.check(newquery[queryIndex:secIndex]) == "true"):
			result = result + singplurals.translate(newquery[queryIndex:secIndex]) + ' '
		elif (strangewords.check(newquery[queryIndex:secIndex]) == "true"):
			result = result + strangewords.translate(newquery[queryIndex:secIndex]) + ' '
		elif (regularplurals.pluCheck(newquery[queryIndex:secIndex]) == "true"):
			result = result + regularplurals.pluTrans(newquery[queryIndex:secIndex]) + ' '
		else:
			result = result + newquery[queryIndex:secIndex] + ' '
		newquery = newquery[(secIndex + 1):]
		if (punct != ''):
			result = result[:len(result) -1] + punct + ' '
			punct = ''

	#Removes punctuation from the last word if it is present and runs checks on the word. If the word has a matching translation, it is replaced. At the end of the cycle, the punctuation is replaced.
	if (len(newquery) > 1):
		if (punctuation.count(newquery[len(newquery) - 1]) == 1):
			punct = newquery[len(newquery) - 1]
			newquery = newquery[:len(newquery) - 1]
	if (nonplurals.check(newquery) == "true"):
		result = result + nonplurals.translate(newquery)
	elif (regularplurals.check(newquery) == "true"):
		result = result + regularplurals.translate(newquery)
	elif (irregularplurals.check(newquery) == "true"):
		result = result + irregularplurals.translate(newquery)
	elif (singplurals.check(newquery) == "true"):
		result = result + singplurals.translate(newquery)
	elif (strangewords.check(newquery) == "true"):
		result = result + strangewords.translate(newquery)
	elif (regularplurals.pluCheck(newquery) == "true"):
		result = result + regularplurals.pluTrans(newquery)
	else:
		result = result + newquery
	if (punct != ''):
		result = result + punct

	#Capitalizes the first letter and prints the result of the process
	if (len(result) > 0):
		result = result[0].upper() + result[1:]
		print result

#Begins the process of translating Spangley to English by taking a user input [In Progress]
if (lang == 'S'):
	query = raw_input("Translating from Spangley. Please enter your query. \n")
	print "Processing... Please wait."

	#Checks if the input word is a singular word and if so replaces the word with the corresponding Enlgish word
	quRes = nonplurals.sCheck(query)
	if (quRes == "true"):
		if (query[:1] == query[:1].upper()):
			result = nonplurals.sTrans(query)[:1].upper() + nonplurals.sTrans(query)[1:]
		else:
			result = nonplurals.sTrans(query)
	elif(quRes == "trueLower"):
		result = (nonplurals.sTrans(query.lower()))

	#Capitalizes the first letter
	if (len(result) > 0):
		result = result[0].upper() + result[1:]
		print result
	
	print "Currently incomplete... Come back later."

#Runs checks to gather the number of tranlsation rules present in the translator
if (lang == 'WordCount'):
	rP = regularplurals.wordcount()
	nP = nonplurals.wordcount()
	iP = irregularplurals.wordcount()
	sP = singplurals.wordcount()
	pP = len(phrases)
	sW = strangewords.wordcount()
	print(rP + nP + iP + sP + pP + sW)

