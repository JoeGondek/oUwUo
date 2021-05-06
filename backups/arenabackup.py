import random
import json

def getData():
	global pData
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
	pData = json.load(open('data/playerStats.json'))
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
	vList = [exp, level, health, gold, inventory, strength, magik, damage, attacks, skills, points, mana]
	pList = ["exp", "level", "health", "gold", "inventory", "strength", "magik", "damage", "attacks", "skills", "points", "mana"]
def quietSave():								#Saves the variables without telling the player#
	for item in pList:
		pData[item] = vList[pList.index(item)]
	print(pData)
	with open('data/playerStats.json', 'w') as f:
		json.dump(pData, f)

def levelUp():
	levelThreshold = 500 * level[0]
	if exp[0] >= levelThreshold:
		level[0] += 1
		points[0] += 3
		exp[0] -= levelThreshold

eData = json.load(open('data/enemies.json'))

def begin_battle():
	global battling
	battling = True
	global enemyName
	global enemyIndex
	global enemyHealth
	global enemyAttacks
	global enemyDamage
	getData()
	if health[0] <= 0:
		print("You are too weak to fight! Go restore your health.")
		exit
	else:
		enemyIndex = str(random.randint(1,len(eData)))
		enemyName = eData[enemyIndex]["name"]
		enemyHealth = eData[enemyIndex]["health"]
		enemyAttacks = eData[enemyIndex]["attacks"]
		enemyDamage = eData[enemyIndex]["damage"]
		print("The Gate to the Arena opens. The crowd cheers. You see your opponent, the " + enemyName + ". Prepare for combat!")
		battle()
		exit

def enemy_attack():
	global health
	for t in range(enemyAttacks):
		health[0] -= enemyDamage
		print("Your opponent deals " + str(enemyDamage) + " damage to you.")
	if health[0] < 0:
		health[0] = 0
	print("HEALTH: " + str(health[0]))

def attack():
	global damage
	global enemyHealth
	if 'sword' in inventory:
		damage[0] *= 2
	for d in range(attacks[0]):
		damage[0] += random.randint(1,10)
		enemyHealth -= (damage[0] + (strength[0] * 0.5))
		print("You deal " + str(damage[0] + (strength[0] * 0.5)) + " damage to the " + enemyName)
	print("ENEMY HEALTH: " + str(enemyHealth))
	damage[0] = 5

def skillz():
	pick = int(input("PICK THY SKILL!!!"))
	mana[0] -= skills[pick]["mana"]
	damage[0] *= skills[pick]["skilldamage"]
	attack()

def battle():
	global battling
	while battling == True:
		print("Attack (1)\nSkills (2)")
		battle_choice = 0
		if health[0] <= 0:
			print("You have been defeated. You lose most of your gold. Go heal and come back when you become a real man!!!")
			gold[0] = round(gold[0] * 0.25)
			exp[0] += 5
			levelUp()
			quietSave()
			battling = False
			exit
		else:
			try:
				battle_choice = int(input("What would you like to do? "))
			except:
				battle()
			if battle_choice == 1:
				attack()
			elif battle_choice == 2:
				skillz()
			else:
				print("Typo!")
			if enemyHealth > 0:
				enemy_attack()
			if enemyHealth <= 0:
				print("Your opponent, the " + enemyName + ", has been defeated!")
				gold[0] += 100
				exp[0] += 600
				levelUp()
				quietSave()
				battling = False
				exit