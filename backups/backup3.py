import json

def getData():
	global pData
	global exp
	global level
	global health
	global gold
	global inventory
	global strength
	global magik
	global speed
	global damage
	global attacks
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