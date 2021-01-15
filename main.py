import tkinter as tk
import numpy
import random
import time
"""
PLAYER STATS
"""
exp = 0
level = 1
health = 100
gold = 0
inventory = []

strength = 0
magik = 0
speed = 0
damage = 5
attacks = 1
'''
ENEMY EMPTY STATS
'''
enemy_name = "3rR0r" #Defines the Enemys name
enemy_health = 1337  #Defines how many hits the opponent can take
enemy_damage = 666  #Defines how much damage the opponent does to the player
enemy_attacks = 69  #Defines how many times the opponent attacks
"""
STUFF FOR CHOICES
"""

"""
ACTUAL GAME STUFF
"""
#Selects the enemy for when you eter the arena randomly
def enemy_random():
    global enemy_name
    global enemy_health
    global enemy_damage
    global enemy_attacks
    enemy = random.randint(1,2)
    if enemy == 1:
        enemy_name = "Guy With Knife"
        enemy_health = 25
        enemy_damage = 5 + random.randint(1,8)
        enemy_attacks = 2
        begin_battle()

    elif enemy == 2:
        enemy_name = "Black Dragon"
        enemy_health =150
        enemy_damage = 15 + random.randint(1, 10)
        enemy_attacks = 1
        begin_battle()

def enemy_attack(enemy_damage, enemy_attacks):
    global health
    for t in range(enemy_attacks):
        health = health - enemy_damage
        print("Your opponent deals " + str(enemy_damage) + " damage to you")
    print("Your health = " + str(health))

#Runs the initial battle sequence and checks opponent's health as the battle continues
def battle():
    global gold
    print("1. Attack")
    battle_choice = 0
    try:
        battle_choice = int(input("What would you like to do? "))
    except:
        battle()
    
    if health <= 0:
        print("You have been defeated you lose all but 15 of your gold, Now go heal and come back later!!!")
        gold = 15
    if battle_choice == 1:
        attack(strength, speed)
    if enemy_health > 0:
        enemy_attack(enemy_damage, enemy_attacks)
    if enemy_health <= 0:
        time.sleep(1)
        print("Your opponent the " + str(enemy_name) + " has been defeated!")
        
#Loops the battle sequence and tells what enemy you get
def begin_battle():
    global enemy_health
    time.sleep(1)
    print("The Gate of the Arena opens, Crowd Cheers can be heard as you exit the waiting area, You see your opponent " + str(enemy_name) + " Prepare for combat!")
    while True:
        if enemy_health < 0:
            break
        elif health <= 0:
            break
        else:
            battle()
        

#List main choices for the Arena and Weapon
def list_main_choice():
    if 'sword' not in inventory:
        print("1. Go get a weapon")
        print("2. Go Into The Arena")
        print("3. Go to the church (Heal)")
    elif 'sword' in inventory:
        print("1. Go Into The Arena")
        print("2. Go to the church (Heal)")

#Defines the equations for the player attacking opponents
def attack(strength, speed):
    global damage
    global enemy_health
    if 'sword' in inventory:
        damage *= 2
    elif strength > 0:
        damage += (strength * 0.5)
    for d in range(attacks):
        damage +=random.randint(1,10)
        enemy_health = enemy_health - damage
        print("You deal " + str(damage) + " damage to your opponent")
        damage = 5
        time.sleep(1)
    print("Enemy Health = " + str(enemy_health))

    
while True:
    if 'sword' not in inventory:
        print("You are a level " + str(level) + " adventurer a new arena has opened up recently and you have been exited to try it out, You have been recommended to go grab a weapon from the storehouse but its your choice. (Type the number of what you would like to pick)")
    elif 'sword' in inventory:
        print("You are a level " + str(level) + " adventurer. Since you have a weapon and are ready to fight its reccomened to enter the Arena, Or you can check on the shop or do whatever, no one's gonna check.")

    list_main_choice()
    choice = int(input("What would you like to do? "))

    if 'sword' not in inventory:
        if choice == 1:
            inventory.append("sword")
            print("You have picked up a sword, You are now ready to fight in the Arena!")
            list_main_choice()
            try:
                choice = int(input("What would you like to do? "))
            except:
                break
                
        elif choice == 2:
            print("You have entered the Arena, Prepared for combat you wait as your opponent is randomly generated for you, How convienient for you!")
            enemy_random()
            begin_battle()

        elif choice == 3:
            print("Ah, Adventurerer would you like to heal for only 15 gold pieces? (Type Y or N)")
            heal_choice = input("Do you want to heal for 15 Gold?")

            if heal_choice.upper() == "Y":
                if gold >= 15:
                    gold = gold - 15
                    health = 100
            if heal_choice == "N" or "n":
                print("Wow! Your poor get out of my church you filthy Hobo!")
        else:
            print("u stupid why u put in wron g numbEr")


    if 'sword' in inventory:
        if choice == 1 and health >= 1:
            print("You have entered the Arena, Prepared for combat you wait as your opponent is randomly generated for you, How convienient for you!")
            enemy_random()
            begin_battle()
        elif choice == 1:
            print("you are too weak, you loser haha go to bed")