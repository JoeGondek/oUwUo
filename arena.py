import random
import json

burn = False
stun = False
resist = False

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
	levelThreshold = 500 * level[0]
	if exp[0] >= levelThreshold:
		level[0] += 1
		points[0] += 3
		exp[0] -= levelThreshold

def resetEffects():
	global stun
	global resist
	global burn
	stun = False
	resist = False
	burn = False

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
		print("You have entered the Arena, Prepared for combat you wait as your opponent is randomly generated for you. How convenient!")
		print("The Gate to the Arena opens. The crowd cheers. You see your opponent, the " + enemyName + ". Prepare for combat!")
		battle()
		exit

def enemy_attack():
	global health
	global stun
	global resist
	global enemyDamage
	global yourTurn
	if stun == False:
		for t in range(enemyAttacks):
			if resist == True:
				health[0] -= (enemyDamage * 0.5)
			else:
				health[0] -= enemyDamage
			print("Your opponent deals " + str(enemyDamage) + " damage to you.")
			if health[0] < 0:
				health[0] = 0
		print("HEALTH: " + str(health[0]))
	yourTurn = True
	resist = False
	stun = False

def attack():
	global damage
	global resist
	global yourTurn
	global enemyHealth
	if burn == True:
		enemyHealth -= 5
		print("Enemy burns for 5 damage!")
	if resist == False:
		if 'sword' in inventory:
			damage[0] *= 2
		for d in range(attacks[0]):
			damage[0] += random.randint(1,10)
			enemyHealth -= (damage[0] + (strength[0] * 0.5))
			print("You deal " + str(damage[0] + (strength[0] * 0.5)) + " damage to the " + enemyName)
	else:
		print("You waited your turn to resist the enemy")
	print("ENEMY HEALTH: " + str(enemyHealth))
	damage[0] = 5
	yourTurn = False

def skillz():
	global stun
	global burn
	global resist
	print("Current Mana: " + str(mana[0]))
	for i in range(len(skills)):
		print("(" + str(i) + ") " + str(skills[i]["name"]) + " - " + str(skills[i]["mana"]) + " Mana")
	pick = int(input("PICK THY SKILL!!! (-1 to exit)"))
	if pick == -1:
		exit
	elif mana[0] >= skills[pick]["mana"]:
		if "stun" in skills[pick]["effects"]:
			stun = True
		elif "burn" in skills[pick]["effects"]:
			burn = True
		elif "resist" in skills[pick]["effects"]:
			resist = True
		else:
			resetEffects()
		mana[0] -= skills[pick]["mana"]
		damage[0] *= skills[pick]["multiplier"]
		print("You use " + str(skills[pick]["name"]))
		pick = -2
		attack()
		print(stun)
		print(burn)
		print(resist)
	else:
		print("Not enough mana!")
		skillz()

def battle():
	global stun
	global burn
	global resist
	global yourTurn
	yourTurn = True
	global battling
	if random.randint(1,100) == 1:
		yourTurn = False
		print("The enemy was quick and struck you first!")
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
			if enemyHealth > 0 and yourTurn == False:
				enemy_attack()
				resist = False
			if enemyHealth <= 0:
				print("Your opponent, the " + enemyName + ", has been defeated!")
				gold[0] += 100
				exp[0] += 600
				levelUp()
				quietSave()
				battling = False
				exit
	resetEffects()