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

def levelUp():
	getData()
	levelThreshold = 500 * level[0]
	if exp[0] >= levelThreshold:
		level[0] += 1
		exp[0] -= levelThreshold
		#quietSave()