from random import randint, sample

import os
import random
import pydoc
import sys

TRIES = 3

class NewGame(object):

	TYPES_AS_STRING = ['int', 'float', 'str', 'bool', 'list', 'tuple', 'set', 'dict', 'complex']

	def __init__(self, items_to_show_qty, secret=''):
		self.ITEMS_TO_SHOW_QTY = items_to_show_qty
		
		if secret == '':
			type_idx = randint(0,len(self.TYPES_AS_STRING)-1)			# Idx of the secret type to guess
			self.__secret = self.TYPES_AS_STRING[type_idx]					# Secret type	
			self.description = self.__get_hint_of_object()	# Dict of methods, attrs + descriptions
			self.property_list = self.description.keys()					# List of methods and attributes of SECRET		
		else:
			if secret in seld.TYPES_AS_STRING:
				self.__secret = secret
				self.description = self.__get_hint_of_object()	# Dict of methods, attrs + descriptions
				self.property_list = self.description.keys()			# List of methods and attributes of SECRET		
		
	def __get_hint_of_object(self):
		"""
		privat method
		Generates a dict of 'property' : 'Description'

		input: 'object_type' name as string
		output: dictionari with hints by object's methods
		"""

		variable_s = 'variable = '
		exec(variable_s + self.__secret) in globals(), locals()
		variable_type = variable

		method_description = lambda x: pydoc.getdoc(getattr(variable_type, x))

		methods_list = [x for x in dir(variable) if x[0] != '_' ]
		hints_dict = {x:method_description(x) for x in methods_list}

		return hints_dict

	def print_description(self, limiter_shuffle=1):
		'''
		Prints descriptions nice and tidy.

		limiter_shuffle - Limit count of descriptions to be generated.
		'''
		if limiter_shuffle:
			if len(self.property_list) > self.ITEMS_TO_SHOW_QTY: 
				items_to_show = sample(self.property_list, self.ITEMS_TO_SHOW_QTY)
			else:
				items_to_show = sample(self.property_list, len(self.property_list))

			print(	'#'*60+
					'\n\nCheck the hints below and type your answer (or press Enter to get new hints)\n'
					)
		else:
			items_to_show = self.property_list 
		
		# Add descriptions to corresponding attribute
		# Prints in nice and tidy format and Cuts out everything after '>>>' in descrption
		for item in items_to_show:
			print('-' * 60)
			descr_str = self.description.get(item,'')
			descr_str = descr_str.replace(self.__secret, '___')

			if '>>>' in descr_str:
				cursor_idx = descr_str.find('>>>')
			else:
				cursor_idx = len(descr_str)

			print(	' '*20+	
					'*** {} ***\n\n {}'
					''.format( item, descr_str[ 0: cursor_idx] ))	# Cuts the string after '>>>'

		print('-' * 60)

	def check_answer(self, answer):
		if (answer.lower() == self.__secret):
			return 1
		else:
			return 0

	def get_secret(self):
		return self.__secret

def footer(msg):
	print('\n'+'#' * 60)
	print(msg)
	print('#' * 60 + '\n')

### GAMEPLAY ###
while True:

	os.system('clear')
	print('### THE REAL Pythonista GAME ###\n')
	print('Guess the Python basic varaible type by its methods listed below:\n')

	game = NewGame(3)
	game.counter = 1

	#  Play and wait for right answer or TRIES limit exceeded
	while True:
		game.print_description(1)

		print(	'\nTRY {}/{}:'
				'\n| {} |'.format(game.counter, TRIES,' | '.join(game.TYPES_AS_STRING))) 
		answer = raw_input('Your ANSWER: >> ')


		if game.check_answer(answer):
			footer('Right answer. Congratulations!')
			break
		if (game.counter >= TRIES):
			footer('Sorry. You loose.')
			print('THE RIGHT ANSWER IS: {}'.format(game.get_secret()))
			break

		game.counter += 1

	# Continue?
	while True:
		restart = raw_input('Do you want to try again (y/n): ')
		if restart.lower() == 'n':		
			print('Thanks for playing. Bye!')
			print('#' * 60)
			sys.exit()
		elif restart.lower() == 'y':
			break
		else:
			continue