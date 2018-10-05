from termcolor import colored
from random import randint
from random import choice
import ast

class Type:
    def __init__(self, type): # FIRE WATER LEAF NORMAL
        self.typeName = type
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
        return self.typeName


class Attack:
    def __init__(self, name, type, accuracy, damage):
        self.attackName = name
        self.attackType = Type(type)
        self.attackAccuracy = accuracy
        self.attackDamage = damage

    def get_damage(self, opponentType):
        damage_taken = self.attackDamage
        accuracy_chance = randint(0, 101)
        if accuracy_chance > self.attackAccuracy:
            return 0
        if accuracy_chance > 95:
            damage_taken *= 1.25
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
    def __init__(self, type, health, name, level=1):
        self.type = Type(type)
        self.moveList = [Attack("Tackle", "NORMAL", 100, 5)] # default move is tackle
        self.currentHealth = health
        self.maxHealth = health
        self.isAlive = True
        self.name = name
        self.level = level

    def level_up(self):
        self.level += 1
        self.maxHealth += 10
        self.currentHealth = self.maxHealth
        if self.level % self.level == 0:
            global types_moves
            move = None
            while move in self.moveList:
                which_type = randint(0, 2)  # 0 - normal move, 1 - type move
                if which_type == 1:
                    move = choice(types_moves[self.type.typeName])
                else:
                    move = choice(types_moves["NORMAL"])
            self.moveList.append(move)

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
        self.currentHealth -= amount
        if self.currentHealth <= 0:
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

    def do_damage(self, opponent):
        attack = choice(self.moveList)
        attack_damage = attack.get_damage(opponent.type)
        print(self.name + " used " + colored(attack.attackName, 'green')
              + ". It did " + colored(str(attack_damage)+'\n', 'red'))
        opponent.take_damage(attack_damage)
        return False


def display_health(player, enemy):
    print(colored("Enemy: "+str(enemy.name)+ " Level: " + str(enemy.level)+"\nHealth: "+str(enemy.currentHealth)+'\n', 'red'))
    print(colored("You: "+str(player.name)+ " Level: " + str(player.level)+"\nHealth: "+str(player.currentHealth)+'\n', 'blue'))


types_moves = {"FIRE": [Attack("Fireball", "FIRE", 100, 8)],
               "WATER": [Attack("Water Gun", "WATER", 100, 8)],
               "LEAF": [Attack("Razor Leaf", "LEAF", 100, 8)],
               "NORMAL": [Attack("Slam", "NORMAL", 100, 6.5)]}

# with open('Moves.txt', 'r') as f:
#     s = f.read()
#     type_moves = ast.literal_eval(s)

if __name__ == "__main__":
    base_health = 10
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
    player_type = input("Enter your type(FIRE, WATER, LEAF, NORMAL):").upper()
    player = Player(player_health, player_type, player_name) # make an array of objects later
    stage = 1
    enemy = Enemy(base_health, choice(list(types_moves)), "Enemy "+str(stage))
    gameNotOver = True
    while gameNotOver:
        display_health(player, enemy)
        print("Moves:\n ", player.moveList)
        move = input("It is your turn.\nChoose a move to attack with (Type its name)")
        while not player.do_damage(move, enemy):
            move = input("Invalid move.\nChoose a move to attack with (Type its name)")
        display_health(player, enemy)
        enemy.do_damage(player)
        if stage == 4:
            break
        if not enemy.isAlive:
            display_health(player, enemy)
            player.level_up()
            base_health += 5
            enemy = Enemy(base_health, choice(list(types_moves)), "Enemy "+str(stage))
        if not player.isAlive:
            display_health(player, enemy)
            gameNotOver = False
            print("You Lost")
    print("Game Over. Thanks for playing.")
