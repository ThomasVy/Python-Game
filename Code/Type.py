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