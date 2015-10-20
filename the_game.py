from random import randint, sample
import random

ITEMS_TO_SHOW_QTY = 10
TRIES = 3

#TYPES = ['int', 'float', 'str', 'bool', 'list', 'tuple', 'set', 'dict', 'complex']
TYPES = [random, int, float, str, bool, list, tuple, set, dict, complex]

TYPE_HINT = {'count':'Return number of occurrences of value',
			 'index':'Return first index of value',
			 'append':'Append object to end',
			 'extend':'Extend by appending elements from the iterable',
			 'insert':'Insert object before index',
			 'pop':'Remove and return item at index(key)',
			 'remove':'Remove first occurrence of value',
			 'reverse':'Reverse *IN PLACE*',
			 'sort':'Stable sort *IN PLACE*',
			 'clear':'Remove all items',
			 'copy':'A shallow copy',
			 'get':'Get item by index, else return substitute value',
			 'items':'list of D\'s (key, value) pairs, as 2-tuples',
			 'imag':'The imaginary part of a complex number',
			 'real':'The real part of a complex number',
			 'denominator':'The denominator of a rational number in lowest terms',
			 'numerator':'The numerator of a rational number in lowest terms',
			 'format':'Return a formatted version of item, using substitutions from args and kwargs',
			 'isalnum':'Return True if all characters are alphanumeric',
			 'isalpha':'Return True if all characters are alphabetic',
			 'isdigit':'Return True if all characters are digits',
			 'join':'Return concatenaterd item',
			 'partition':'Search for the separator and return the part before it and, the separator itself, and the part after it',
			 'rfind':'Return the highest index where subitem sub is found',
			 'find':'Return the lowest index where subitem sub is found',
			 'split':'Return a list of the words in the string',
			 'strip':'Strips leading and trailing whitespace'
			 }


#Generates a list 
def generateDescription(item_type):
	result = list()
	dir_list = dir(item_type)		#Get the list 'dir()'
	for item in dir_list:
		if (item.find('_') < 0):    #Exclude overloaded functions (with '__')
			result.append(item)
	return result

def printDescription(description):
	
	#Limit descriptions
	if len(description) > ITEMS_TO_SHOW_QTY: 
		show_items = ITEMS_TO_SHOW_QTY
	else:
		show_items = len(description)

	#Randomize limited qty of descriptions
	items_to_show = [description[i] for i in sample(range(len(description)), show_items)]	

	#Add descriptions to corresponding attribute

	print('\nCheck the hints below and type your answer (or press Enter to get new hints)\n')
	for item in items_to_show:
		print('{} - {}'.format(item, TYPE_HINT.get(item,'')))

def Play(secret, description, TRIES):
	counter = 0
	answer = ''

	while (answer != secret) and (counter < TRIES):
		printDescription(description)
		#print(secret)		
		answer = raw_input('\nANSWER: >> ')
		counter += 1
	return counter

print(chr(27) + "[2J")
print('### THE REAL Pythonista GAME ###\n')
print('Guess the Python basic varaible type by its methods listed below:')

restart = 'y'
while restart != 'n':
	if restart == 'y':
		type_idx = randint(0,len(TYPES)-1)				#Idx of the secret type to guess
		secret_type = TYPES[type_idx]					#Secrets type	
		secret = str(TYPES[type_idx]).split('\'')[1]	#Converts "<type 'tuple'>" to "tuple")
		description = generateDescription(secret_type)
		if Play(secret, description, TRIES) < TRIES:
			print('\n'+''.join(['#' for i in range(60)]))
			print('Right answer. Congratulations!')
			print(''.join(['#' for i in range(60)])+'\n')
		else:
			print('Sorry. You loose.')	
	restart = str(raw_input('Do you want to try again? (y/n)'))
else: 
	print('Thanks for playing. Bye!')
	print(''.join(['#' for i in range(60)]))