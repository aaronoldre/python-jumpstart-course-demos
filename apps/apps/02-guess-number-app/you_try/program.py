import random

print('----------------------------')
print('   GUESS THE NUMBER APP')
print('-----------------------------')
print()


the_number = random.randint(0,100)
guess_text = raw_input('Guess a number between 0 and 100: ')

while int(guess_text) != the_number:

	if int(guess_text) > the_number:
		print('Sorry but {} is HIGHER than the number'.format(guess_text))
		guess_text = raw_input('Guess a number between 0 and 100: ')

	if int(guess_text) < the_number:
		print('Sorry but {} is LOWER than the number'.format(guess_text))
		guess_text = raw_input('Guess a number between 0 and 100: ')
print("YES! You've got it. The number was {}".format(the_number))
