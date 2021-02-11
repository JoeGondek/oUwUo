import avoidingcircles as gd
import json

def saveGame():
	print("Saving...")
	with open('data/playerStats.json', 'w') as f:
		json.dump(gd.pData, f)
	print("Saved.")

def quietSave():
	with open('data/playerStats.json', 'w') as f:
		json.dump(gd.pData, f)