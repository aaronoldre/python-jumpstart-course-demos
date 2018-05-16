import random

class Creature:
	def __init__(self, name, level):
		self.name = name
		self.level = level

	def __repr__(self):
		return "Creature: {} of level {}".format(self.name, self.level)

	def get_defensive_roll(self):
		return random.randint(1,12) * self.level


class Wizard(Creature, object):
	

	def attack(self, creature):
		print("The wizard {} attacks {}!".format(self.name, creature.name))

		my_roll = self.get_defensive_roll()
		creature_roll = creature.get_defensive_roll()

		print("You rolled {}".format(my_roll))
		print("{} rolled {}".format(creature.name, creature_roll))

		if my_roll >= creature_roll:
			print("The wizard has handily defeated the {}".format(creature.name))
			return True
		else:
			print("The wizard has been defeated!!!!!")
			return False	


class SmallAnimal(Creature, object):
	def get_defensive_roll(self):
		base_roll = super(SmallAnimal, self).get_defensive_roll() 
		return base_roll / 2


class Dragon(Creature, object):
	def __init__(self, name, level, scaliness, breathes_fire):
		super(Dragon, self).__init__(name, level)
		self.breathes_fire = breathes_fire
		self.scaliness = scaliness

	def get_defensive_roll(self):
		base_roll = super(Dragon, self).get_defensive_roll()
		fire_modifier = 5 if self.breathes_fire else 1
		scale_modiifer = self.scaliness/10

		return base_roll * fire_modifier * scale_modiifer
