import numpy
import random
import time
import json
import sys
import pickle

import arena as battle

####################################################################################################

eData = json.load(open('data/enemies.json'))
eSelection = ""

pData = json.load(open('data/playerStats.json'))

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

def saveGame():
	print("Saving...")
	with open('data/playerStats.json', 'w') as f:
		json.dump(pData, f)
	print("Saved.")
def quitGame():
	print("Bye!")
	sys.exit()

####################################################################################################

#Selects the enemy for when you eter the arena randomly
def enemy_random():
	global enemyName
	global enemyHealth
	global enemyDamage
	global enemyAttacks
	enemyIndex = random.randint(1,3)
	if enemyIndex == 1:
		eSelection = "knifeMan"
		enemyDamage = 5 + random.randint(1,8)
	elif enemyIndex == 2:
		eSelection = "dragon"
		enemyDamage = 15 + random.randint(1, 10)
	elif enemyIndex == 3:
		eSelection = "zach"
		enemyDamage = 50 + random.randint(-10, 10)
	enemyName = eData[eSelection]["name"]
	enemyHealth = eData[eSelection]["health"]
	enemyAttacks = eData[eSelection]["attacks"]
	begin_battle()

def enemy_attack(enemyDamage, enemyAttacks):
	global health
	for t in range(enemyAttacks):
		health = health - enemyDamage
		print("Your opponent deals " + str(enemyDamage) + " damage to you")
	print("Health = " + str(health))

#Runs the initial battle sequence and checks opponent's health as the battle continues
def battle():
	global gold
	global exp
	print("Attack (1)")
	battle_choice = 0
	try:
		battle_choice = int(input("What would you like to do? "))
	except:
		battle()
	if health <= 0:
		print("You have been defeated. You lose all but 15 of your gold. Go heal and come back when you become a real man!!!")
		gold = 15
	if battle_choice == 1:
		attack(strength, speed)
	if enemyHealth > 0:
		enemy_attack(enemyDamage, enemyAttacks)
	if enemyHealth <= 0:
		print("Your opponent, the " + str(enemyName) + ", has been defeated!")
		exp += 50
		
#Loops the battle sequence and tells what enemy you get
def begin_battle():
	global gold
	global enemyHealth
	time.sleep(1)
	print("The Gate to the Arena opens. The crowd cheers. You see your opponent, the " + str(enemyName) + ". Prepare for combat!")
	while True:
		if enemyHealth < 0:
			break
		elif health <= 0:
			gold = 15
			break
		else:
			battle()

#List main choices for the Arena and Weapon
def hubChoice():
	if 'sword' not in inventory:
		print("0. Go get a weapon")
	print("1. Go Into The Arena")
	print("2. Go to the church (Heal)")
	print("Save game (S)")
	print("Quit (Q)")

#Defines the equations for the player attacking opponents
def attack(strength, speed):
	global damage
	global enemyHealth
	if 'sword' in inventory:
		damage *= 2
	elif strength > 0:
		damage += (strength * 0.5)
	for d in range(attacks):
		damage += random.randint(1,10)
		enemyHealth = enemyHealth - damage
		print("You deal " + str(damage) + " damage to the " + enemyName)
	damage = 5
	time.sleep(1)
	print("Enemy Health = " + str(enemyHealth))

#game intro and main battle sequence
gameOver = False
print("You are a level " + str(level) + " adventurer. A new arena has opened up recently and you have been exited to try it out. You are advised to grab a weapon from the storehouse but it's optional. Type the number of what you would like to pick")
while gameOver == False:
	if 'sword' not in inventory:
		print("I thought I told you to get a weapon. Im not mad, I'm disappointed.")
	else:
		print("You are a level " + str(level) + " adventurer. Since you have a weapon and are ready to fight its reccomened to enter the Arena, Or you can check on the shop or do whatever, no one's gonna check.")
	hubChoice()
	try:
		choice = input("What would you like to do? ")
	except:
		break
	if choice.upper() == "S":
			saveGame()
	if choice.upper() == "Q":
			quitGame()
	if 'sword' not in inventory:
		if choice == "0":
			inventory.append("sword")
			print("You have picked up a sword. You are now ready to fight in the Arena!")
			hubChoice()
			try:
				choice = int(input("What would you like to do? "))
			except:
				break
		elif choice == "1":
			print("You have entered the Arena, Prepared for combat you wait as your opponent is randomly generated for you, How convienient for you!")
			enemy_random()
			begin_battle()
		elif choice == "2":
			print("Ah, Adventurerer would you like to heal for only 15 gold pieces? (Y/N)")
			heal_choice = input("Do you want to heal for 15 Gold?")
			if heal_choice.upper() == "Y":
				if gold >= 15:
					gold = gold - 15
					health = 100
				if heal_choice.upper() == "N":
					print("Wow! You're poor! get out of my church you filthy Hobo!")
		else:
			print("u stUpid why u put iN wron ge")
	else:
		if choice == 1 and health >= 1:
			print("You have entered the Arena, Prepared for combat you wait as your opponent is randomly generated for you. How convenient!")
			enemy_random()
			begin_battle()
		elif choice == 1:
			print("your too weak, yuor'e loser haha go to bed")
		elif choice == 2:
			print("Ah, Adventurerer... Would you like to heal for the low low price of 15 gold pieces? (Y/N)")
			heal_choice = input("Do you want to heal for 15 Gold?")
			if heal_choice.upper() == "Y":
				if gold >= 15:
					gold = gold - 15
					health = 100
					print("You have been fully healed. O Praise be our Lord and Savior the Giant Flying Spaghetti Monster")
			if heal_choice.upper() == "N" :
				print("Wow! You're poor! get out of my church you filthy Hobo!")
				gameOver = True
				print("haha bye")
				break
			else:
				print("huh?")
		else:
			print("u stupid why u put in wron g numbEr")