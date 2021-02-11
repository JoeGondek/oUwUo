import random
import json
import sys

import arena
import church
import avoidingcircles as gd
import s

####################################################################################################

def quitGame():
	print("Bye!")
	sys.exit()

####################################################################################################

#List main choices for the Arena and Weapon
def hubChoice():
	gd.getData()
	if 'sword' not in gd.inventory:
		print("0. Go get a weapon")
	print("1. Go Into The Arena")
	print("2. Go to the church (Heal)")
	print("Save game (S)")
	print("Quit (Q)")

#game intro and main battle sequence
gameOver = False
print("You are a level 1 adventurer. A new arena has opened up recently and you have been exited to try it out. You are advised to grab a weapon from the storehouse but it's optional. Type the number next to what you would like to pick.")

while gameOver == False:
	gd.getData()
	if 'sword' not in gd.inventory:
		print("I thought I told you to get a weapon. Im not mad, I'm disappointed.")
	hubChoice()
	try:
		choice = input("What would you like to do? ")
	except:
		continue
	if choice.upper() == "S":
			s.saveGame()
	if choice.upper() == "Q":
			quitGame()
	if 'sword' not in gd.inventory:
		if choice == "0":
			gd.inventory.append("sword")
			s.quietSave()
			print("You have picked up a sword. You are now ready to fight in the Arena!")
		elif choice == "1":
			print("You have entered the Arena prepared for combat. You wait as your opponent is randomly generated for you. How convienient!")
			arena.begin_battle()
			gd.getData()
		elif choice == "2":
			print("Ah, Adventurerer! would you like to heal for only 15 gold pieces? (Y/N)")
			church.healMenu()
			gd.getData()
		else:
			print("u stUpid why u put iN wron ge")
	else:
		if choice == "1" and gd.health >= 1:
			print("You have entered the Arena, Prepared for combat you wait as your opponent is randomly generated for you. How convenient!")
			arena.begin_battle()
			gd.getData()
		elif choice == "1":
			print("your too weak, yuor'e loser haha go to bed")
		elif choice == "2":
			print("Ah, Adventurerer! would you like to heal for only 15 gold pieces? (Y/N)")
			church.healMenu()
			gd.getData()
		elif choice.upper() == "S":
			s.saveGame()
		elif choice.upper() == "Q":
			quitGame()
		else:
			print("u stupid why u put in wron g numbEr")
print("G A M E  O V E R")