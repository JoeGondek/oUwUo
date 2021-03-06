import json

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
def quietSave():								#Saves the variables without telling the player#
	for item in pList:
		pData[item] = vList[pList.index(item)]
	print(pData)
	with open('data/playerStats.json', 'w') as f:
		json.dump(pData, f)

def healMenu():
	getData()
	heal_choice = input("Heal for 15 Gold? ")
	if heal_choice.upper() == "Y" and gold[0] >= 15:
		gold[0] -= 15
		health[0] = maxhealth[0]
		print("You have been fully healed. O Praise be our Lord and Savior the Giant Flying Spaghetti Monster")
		quietSave()
	elif heal_choice.upper() == "N" or gold[0] < 15:
		print("Wow! You're poor! Get out of my church you filthy hobo!")
	else:
		print("huh?")
		healMenu()