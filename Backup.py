
import numpy
import random
import time
import json

#totally not stolen code  <-- dont you lie to me
eData = json.load(open('enemies.json'))
def json_extract(obj, key):
	arr = []
	def extract(obj, arr, key):
		if isinstance(obj, dict):
			for k, v in obj.items():
				if isinstance(v, (dict, list)):
					extract(v, arr, key)
				elif k == key:
					arr.append(v)
				elif isinstance(obj, list):
					for item in obj:
						extract(item, arr, key)
		return arr
	values = extract(obj, arr, key)
	return values

eHealthInst = json_extract('enemies.json', "health")
eNameInst = json_extract('enemies.json', "name")
eAttInst = json_extract('enemies.json', "attack")

"""
PLAYER STATS
"""

pData = json.load(open('playerStats.json'))

exp = pData["exp"]
level = pData["level"]
health = pData["health"]
gold = pData["gold"]
inventory = pData["inventory"]

strength = pData["strength"]
magik = pData["magik"]
speed = pData["speed"]
damage = pData["damage"]
attacks = pData["attacks"]

"""
ENEMY EMPTY STATS
"""



"""
STUFF FOR CHOICES
"""

"""
ACTUAL GAME STUFF
"""

#Selects the enemy for when you eter the arena randomly
def enemy_random():
	global enemyName
	global enemyHealth
	global enemyDamage
	global enemyAttacks
	enemy = random.randint(1,2)
	if enemy == 1:
		enemyName = "Guy With Knife"
		enemyHealth = 25
		enemyDamage = 5 + random.randint(1,8)
		enemyAttacks = 2
		begin_battle()

	elif enemy == 2:
		enemyName = "Black Dragon"
		enemyHealth =150
		enemyDamage = 15 + random.randint(1, 10)
		enemyAttacks = 1
		begin_battle()

def enemy_attack(enemyDamage, enemyAttacks):
	global health
	for t in range(enemyAttacks):
		health = health - enemyDamage
		print("Your opponent deals " + str(enemyDamage) + " damage to you")
	print("Your health = " + str(health))

#Runs the initial battle sequence and checks opponent's health as the battle continues
def battle():
	global gold
	print("1. Attack")
	battle_choice = 0
	try:
		battle_choice = int(input("What would you like to do? "))
	except:
		battle()
	
	if health <= 0:
		print("You have been defeated you lose all but 15 of your gold, Now go heal and come back later!!!")
		gold = 15
	if battle_choice == 1:
		attack(strength, speed)
	if enemyHealth > 0:
		enemy_attack(enemyDamage, enemyAttacks)
	if enemyHealth <= 0:
		time.sleep(1)
		print("Your opponent the " + str(enemyName) + " has been defeated!")
		
#Loops the battle sequence and tells what enemy you get
def begin_battle():
	global gold
	global enemyHealth
	time.sleep(1)
	print("The Gate of the Arena opens, Crowd Cheers can be heard as you exit the waiting area, You see your opponent " + str(enemyName) + " Prepare for combat!")
	while True:
		if enemyHealth < 0:
			break
		elif health <= 0:
			print("You have been defeated you lose all but 15 of your gold, Now go heal and come back later!!!")
			gold = 15
			time.sleep(1)
			break
		else:
			battle()
		

#List main choices for the Arena and Weapon
def list_main_choice():
	if 'sword' not in inventory:
		print("1. Go get a weapon")
		print("2. Go Into The Arena")
		print("3. Go to the church (Heal)")
	elif 'sword' in inventory:
		print("1. Go Into The Arena")
		print("2. Go to the church (Heal)")

#Defines the equations for the player attacking opponents
def attack(strength, speed):
	global damage
	global enemyHealth
	if 'sword' in inventory:
		damage *= 2
	elif strength > 0:
		damage += (strength * 0.5)
	for d in range(attacks):
		damage +=random.randint(1,10)
		enemyHealth = enemyHealth - damage
		print("You deal " + str(damage) + " damage to your opponent")
	damage = 5
	time.sleep(1)
	print("Enemy Health = " + str(enemyHealth))

while True:
	if 'sword' not in inventory:
		print("You are a level " + str(level) + " adventurer a new arena has opened up recently and you have been exited to try it out, You have been recommended to go grab a weapon from the storehouse but its your choice. (Type the number of what you would like to pick)")
	elif 'sword' in inventory:
		print("You are a level " + str(level) + " adventurer. Since you have a weapon and are ready to fight its reccomened to enter the Arena, Or you can check on the shop or do whatever, no one's gonna check.")
	list_main_choice()
	try:
		choice = int(input("What would you like to do? "))
	except:
		break

	if 'sword' not in inventory:
		if choice == 1:
			inventory.append("sword") #trying to fix this with json magic
			print("You have picked up a sword, You are now ready to fight in the Arena!")
			list_main_choice()
			try:
				choice = int(input("What would you like to do? "))
			except:
				break 
		elif choice == 2:
			print("You have entered the Arena, Prepared for combat you wait as your opponent is randomly generated for you, How convienient for you!")
			enemy_random()
			begin_battle()
		elif choice == 3:
			print("Ah, Adventurerer would you like to heal for only 15 gold pieces? (Type Y or N)")
			heal_choice = input("Do you want to heal for 15 Gold?")

			if heal_choice.upper() == "Y":
				if gold >= 15:
					gold = gold - 15
					health = 100
				if heal_choice == "N" or "n":
					print("Wow! You're poor get out of my church you filthy Hobo!")
		else:
			print("u stupid why u put in wron g numbEr")

	if 'sword' in inventory:
		if choice == 1 and health >= 1:
			print("You have entered the Arena, Prepared for combat you wait as your opponent is randomly generated for you, How convienient for you!")
			enemy_random()
			begin_battle()
		elif choice == 1:
			print("you are too weak, you loser haha go to bed")
            
		elif choice == 2:
			print("Ah, Adventurerer would you like to heal for only 15 gold pieces? (Type Y or N)")
			heal_choice = input("Do you want to heal for 15 Gold?")

			if heal_choice.upper() == "Y":
				if gold >= 15:
					gold = gold - 15
					health = 100
					print("You have been fully healed, Praise be our lord and savior the Giant Flying Spaghetti Monster")
			if heal_choice.upper() == "N" :
			  print("Wow! You're poor get out of my church you filthy Hobo!")
		else:
			print("u stupid why u put in wron g numbEr")
