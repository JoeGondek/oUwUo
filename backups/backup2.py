import random
import json
import avoidingcircles as gd

eData = json.load(open('data/enemies.json'))
enemyIndex = str(random.randint(1,len(eData)))
enemyName = eData[enemyIndex]["name"]
enemyHealth = eData[enemyIndex]["health"]
enemyAttacks = eData[enemyIndex]["attacks"]
enemyDamage = eData[enemyIndex]["damage"]

def begin_battle():
	gd.getData()
	if gd.health <= 0:
		print("You are too weak to fight! Go restore your health.")
	else:
		print("The Gate to the Arena opens. The crowd cheers. You see your opponent, the " + enemyName + ". Prepare for combat!")
		battle()

def enemy_attack():
	gd.getData()
	for t in range(enemyAttacks):
		gd.health = gd.health - enemyDamage
		print("Your opponent deals " + str(enemyDamage) + " damage to you.")
	print("HEALTH: " + str(health))
	battle()

def attack():
	gd.getData()
	if 'sword' in gd.inventory:
		gd.damage *= 2
	elif gd.strength > 0:
		gd.damage += (gd.strength * 0.5)
	for d in range(gd.attacks):
		gd.damage += random.randint(1,10)
		enemyHealth = enemyHealth - gd.damage
		print("You deal " + str(gd.damage) + " damage to the " + enemyName)
	print("ENEMY HEALTH: " + str(enemyHealth))

def battle():
	print("Attack (1)")
	battle_choice = 0
	if gd.health <= 0:
		print("You have been defeated. You lose most of your gold. Go heal and come back when you become a real man!!!")
		gd.gold = round(gold * 0.25)
		gd.exp += 5
	else:
		try:
			battle_choice = int(input("What would you like to do? "))
		except:
			battle()
		if battle_choice == 1:
			attack()
		if enemyHealth > 0:
			enemy_attack()
		if enemyHealth <= 0:
			print("Your opponent, the " + str(enemyName) + ", has been defeated!")
			gd.gold += 100
			gd.exp += 100
	gd.quietSave()