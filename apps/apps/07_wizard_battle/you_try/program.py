from actors import Wizard, Creature, SmallAnimal, Dragon
import random
import time


def main():
	print_header()
	game_loop()

def print_header():
	print('----------------------------')
	print('     WIZARD GAME APP')
	print('-----------------------------')
	print(' ')


def game_loop():
	
	creatures = [
			SmallAnimal('Toad', 1),
			Creature('Tiger', 12),
			SmallAnimal('Bat', 3),
			Dragon('Dragon', 50, 75, True),
			Wizard('Evil Wizard', 1000)
	]

	hero = Wizard('Gandolf', 27)

	while True:

		active_creature = random.choice(creatures)
		print("A {} of level {} has appeared from the dark and foggy forest ...".format(active_creature.name, active_creature.level))
		print("")

		cmd = raw_input("Do you want to [a]ttack, [r]un away, or [l]ook around? ")
		if cmd == 'a':

			if hero.attack(active_creature):
				creatures.remove(active_creature)
			else:
				print("The wizard runs and hides to take time to recover...")
				time.sleep(5)
				print("The wizard returns revitalized!")


		elif cmd == 'r':
			print("The wizard has been unsure of his powers and runs away")

		elif cmd == 'l':
			print("Wizard {} takes in the surroundings and sees: ".format(hero.name))
			for i in creatures:
				print("* A {} of level {}".format(i.name, i.level))
		else:
			print("OK. Exiting game....bye")
			break


		if not creatures:
			print("You've defeated all the creatures")
			break


if __name__ == '__main__':
    main()