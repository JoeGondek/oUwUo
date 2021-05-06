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

def shoppe():
	getData()
	choice = input("items or skills? (I/S)")
	if choice.upper() == "S" and points[0] >= 1:
		print("You have " + str(points[0]) + " skill points")
		print("Which stat would you like to improve?\nHealth (H)\nStrength (S)\nMagic (M)\nUnlock New Skill (3 Points)(U)")
		choice = input("Selection: ")
		if choice.upper() == "H":
			health[0] += 10
			maxhealth[0] += 10
		if choice.upper() == "S":
			strength[0] += 1
		if choice.upper() == "M":
			magik[0] += 1
		if choice.upper() == "U" and points[0] >= 3:
			skills.append(sData[str(len(skills) + 1)])
			points[0] -= 2
		else:
			print("You don't have enough skill points for a skill")
		points[0] -= 1
		print("You have " + str(points[0]) + " skill points left.")
	else:
		print("You don't have enough levels to upgrade skills! come back when you have more levels.")
	mana[0] = magik[0]
	quietSave()
	exit