from Attack import * 
from random import randint
from random import choice
import ast

class Character:
    def __init__(self, type, health, name, level=1):
        self.type = Type(type)
        self.moveList = [Attack("Tackle", "NORMAL", 100, 5)] # default move is tackle
        self.currentHealth = health
        self.maxHealth = health
        self.isDead = False
        self.name = name
        self.level = level

    def level_up(self):
        self.level += 1
        self.maxHealth += 10
        self.currentHealth = self.maxHealth
        if self.level % self.level == 0:
            global TYPEMOVES
            move = None
            while move in self.moveList:
                which_type = randint(0, 2)  # 0 - normal move, 1 - type move
                if which_type == 1:
                    move = choice(TYPEMOVES[self.type.typeName])
                else:
                    move = choice(TYPEMOVES["NORMAL"])
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
            self.isDead = True

class Player(Character):
    def __init__(self, health, element,  name):
        super(Player, self).__init__(element, health, name)


class Enemy(Character):
    def __init__(self, health, element, name):
        super(Enemy, self).__init__(element, health, name)

    def do_damage(self, opponent):
        attack = choice(self.moveList)
        attack_damage = attack.get_damage(opponent.type)
        print(self.name + " used " + colored(attack.attackName, 'green')
              + ". It did " + colored(str(attack_damage)+'\n', 'red'))
        opponent.take_damage(attack_damage)
        return False
