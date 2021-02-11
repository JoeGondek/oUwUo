import json
import avoidingcircles as gd

def healMenu():
	gd.getData()
	heal_choice = input("Heal for 15 Gold? ")
	if heal_choice.upper() == "Y" and gd.gold >= 15:
		gd.gold -= 15
		gd.health = 100
		print("You have been fully healed. O Praise be our Lord and Savior the Giant Flying Spaghetti Monster")
	elif heal_choice.upper() == "N" or gd.gold < 15:
		print("Wow! You're poor! Get out of my church you filthy hobo!")
	else:
		print("huh?")
		healMenu()