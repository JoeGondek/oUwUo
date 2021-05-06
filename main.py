import sys
import arena
import church
import json
import shop

####################################################################################################

def getData():
	global pData
	global sData
	global exp
	global level																							
	global health																							
	global gold
	global inventory #<----------------- calls all the global variables
	global strength
	global magik
	global damage
	global attacks
	global points
	global vList
	global pList
	global points
	global skills
	global mana
	global maxhealth
	pData = json.load(open('data/playerStats.json'))
	sData = json.load(open('data/skills.json'))
	exp = pData["exp"]
	level = pData["level"]
	health = pData["health"]
	gold = pData["gold"]
	inventory = pData["inventory"]	#<---------------- sets the variables as the values are in a dictionary (See playerStats.json)
	strength = pData["strength"]
	magik = pData["magik"]
	damage = pData["damage"]
	attacks = pData["attacks"]
	skills = pData["skills"]
	points = pData["points"]
	mana = pData["mana"]
	maxhealth = pData["maxhealth"]
	vList = [exp, level, health, gold, inventory, strength, magik, damage, attacks, skills, points, mana]
	pList = ["exp", "level", "health", "gold", "inventory", "strength", "magik", "damage", "attacks", "skills", "points", "mana"]
def saveGame():									#Saves the variables whilst notifying the player#
	print("Saving...")
	quietSave()
	print("Saved.")
def quietSave():								#Saves the variables without telling the player#
	for item in pList:
		pData[item] = vList[pList.index(item)]
	print(pData)
	with open('data/playerStats.json', 'w') as f:
		json.dump(pData, f)

####################################################################################################

def quitGame():					#Ends the program so that the player can move on with life
	print("Bye!")
	sys.exit()

####################################################################################################

#List main choices for the Arena and Weapon
def hubChoice():
	if 'sword' not in inventory:
		print("0. Go get a weapon")
	print("1. Go Into The Arena")
	print("2. Go to the church (Heal)")
	print("3. Buy skills and items")
	print("Save game (S)")
	print("Quit (Q)")

#game intro
gameOver = False
print("You are a level 1 adventurer. A new arena has opened up recently and you have been excited to try it out. You are advised to grab a weapon from the storehouse but it's optional. Type the number next to what you would like to pick.")

while gameOver == False:
	getData()	#<------------- Gets all of the variables above and loads them
	hubChoice()
	try:
		choice = input("What would you like to do? ")
	except:
		continue
	if choice.upper() == "S":
			saveGame()
	if choice.upper() == "Q":
			quitGame()
	if 'sword' not in inventory:	#<------------- Checks if the player has the sword to remove the choice
		if choice == "0":	#<------------ Picks up sword that buffs the players damage
			inventory.append("sword")
			quietSave()
			print("You have picked up a sword. You are now ready to fight in the Arena!")
		elif choice == "1":	#<------------- Enters the Arena for the main combat to begin (See Arena.py)
			print("You have entered the Arena prepared for combat. You wait as your opponent is randomly generated for you. How convienient!")
			arena.begin_battle()
		elif choice == "2":	#<------------- Sends player into church where they can heal (See Church.py)
			print("Ah, Adventurerer! would you like to heal for only 15 gold pieces? (Y/N)")
			church.healMenu()
		else:
			print("u stUpid why u put iN wron ge")
	else:
		if choice == "1" and health[0] >= 1:	#<-------------- Makes sure before entering arena that the player isnt dead
			arena.begin_battle()
		elif choice == "1":
			print("your too weak, yuor'e loser haha go to bed")
		elif choice == "2":
			print("Ah, Adventurerer! would you like to heal for only 15 gold pieces? (Y/N)")
			church.healMenu()
			print("You are currently level: " + str(level[0]))
		elif choice == "3":
			quietSave()
			shop.shoppe()
		else:
			print("u stupid why u put in wrog numbEr")
	if health[0] <= 0 and gold[0] < 15:
		gameOver = True
print("G A M E  O V E R")