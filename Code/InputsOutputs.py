from Attack import * 
from termcolor import colored

def getName():
    return input("What is your name?")

def getHealth():
    while True:
        try:
            player_health = int(input("How much health would you like to start off with?"))
            if player_health >= 250 or player_health <= 0:
                raise ValueError
            else:
                return player_health
        except ValueError:
            starting_health = print("Invalid input.\nHealth must be an integer and below 250.")

def getType():
    while True:
        type = input("Enter your type(FIRE, WATER, LEAF, NORMAL):").upper()
        if(type in TYPEMOVES):
            return type
        else:
            print("Invalid Type.")
            
def displayhealth(player, enemy):
    print(colored("Enemy: "+str(enemy.name)+ " Level: " + str(enemy.level)+"\nHealth: "+str(enemy.currentHealth)+'\n', 'red'))
    print(colored("You: "+str(player.name)+ " Level: " + str(player.level)+"\nHealth: "+str(player.currentHealth)+'\n', 'blue'))

def displayLoseScreen():
    print("You Lost")
    print("Game Over! Thanks for playing this prototype!")

def playerTurn(player, enemy):
    print("Moves:\n ", player.moveList)
    while True:
        move = input("It is your turn.\nChoose a move to attack with (Type its name)")
        if(player.do_damage(move, enemy)):
            break
        move = print("Invalid move.")