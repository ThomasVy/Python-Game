from Type import *
from termcolor import colored
from random import randint

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

TYPEMOVES = {"FIRE": [Attack("Fireball", "FIRE", 100, 8)],
               "WATER": [Attack("Water Gun", "WATER", 100, 8)],
               "LEAF": [Attack("Razor Leaf", "LEAF", 100, 8)],
               "NORMAL": [Attack("Slam", "NORMAL", 100, 6.5)]}