from termcolor import colored
import numpy as np


class Type:
    def __init__(self, type): # FIRE WATER LEAF NORMAL
        self.type = type
        if type == 'FIRE':
            self.weakness = 'WATER'
            self.strong = 'LEAF'
        elif type == 'WATER':
            self.strong = 'FIRE'
            self.weakness = 'LEAF'
        elif type == 'LEAF':
            self.strong = 'WATER'
            self.weakness = 'FIRE'
        elif type == 'NORMAL':
            self.strong = None
            self.weakness = None
        else:
            print("invalid type. Exiting program")
            exit(1)

    def __str__(self):
        return self.type


class Attack:
    def __init__(self, name, type, accuracy, damage):
        self.attackName = name
        self.attackType = Type(type)
        self.attackAccuracy = accuracy
        self.attackDamage = damage

    def get_damage(self, opponentType):
        damage_taken = self.attackDamage
        accuracy_chance = np.random.randint(0, 101)
        if accuracy_chance > self.attackAccuracy:
            return 0
        if opponentType == self.attackType.strong:
            damage_taken = 2*self.attackDamage
        if opponentType == self.attackType.weakness:
            damage_taken = self.attackDamage/2
        return damage_taken

    def __str__(self):
        return colored("Name: " + self.attackName, 'green') + " Element: " + str(self.attackType)

    def __repr__(self):
        return str(self)


class Object:
    def __init__(self, type, health, name):
        self.type = Type(type)
        self.moveList = [Attack("tackle", "NORMAL", 100, 5)] # default move is tackle
        self.health = health
        self.isAlive = True
        self.name = name

    def do_damage(self, move_name, opponent):
        for attack in self.moveList:
            if attack.attackName == move_name:
                attack_damage = attack.get_damage(opponent.type)
                print(self.name + " used " + colored(str(attack), 'green')
                      + ". It did " + colored(str(attack_damage), 'red'))
                opponent.take_damage(attack_damage)
                return True
        return False

    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.isAlive = False

    @classmethod
    def hello(cls):
        pass


class Player(Object):
    def __init__(self, health, element,  name):
        super(Player, self).__init__(element, health, name)


class Enemy(Object):
    def __init__(self, health, element, name):
        super(Enemy, self).__init__(element, health, name)


def display_health(player, enemy):
    print(colored("Enemy: "+str(enemy.name)+"\nHealth: "+str(enemy.health)+'\n', 'red'))
    print(colored("You: "+str(player.name)+"\nHealth: "+str(player.health), 'blue'))


if __name__ == "__main__":
    base_health = 50
    player_name = input("What is your name?")
    starting_health = input("How much health would you like to start off with?")
    player_health = base_health
    while True:
        try:
            player_health = int(starting_health)
            if player_health >= 250 or player_health <= 0:
                raise ValueError
            else:
                break
        except ValueError:
            starting_health = input("Invalid. Please try again.\nHealth must be an integer and below 250")
    player_type = input("Enter your type(FIRE, WATER, LEAF, NORMAL):")
    player = Player(player_health, player_type,player_name) # make an array of objects later
    enemy = Enemy(base_health, "NORMAL", "Enemy One")
    gameNotOver = True
    while gameNotOver:
        display_health(player, enemy)
        print("Moves:\n ", player.moveList)
        move = input("It is your turn.\nChoose a move to attack with (Type its name)")
        while not player.do_damage(move, enemy):
            move = input("Invalid move.\nChoose a move to attack with (Type its name)")
        display_health(player, enemy)
        enemy.do_damage("tackle", player)
        if not enemy.isAlive:
            display_health(player, enemy)
            gameNotOver = False
            print("You Won")
        if not player.isAlive:
            display_health(player, enemy)
            gameNotOver = False
            print("You Lost")
    print("Game Over. Thanks for playing.")
