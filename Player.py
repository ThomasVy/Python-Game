from termcolor import colored

class Object:
    def __init__(self, health):
        self.moveList = {"tackle": 5} # default move is tackle
        self.health = health
        self.isAlive = True

    def get_health(self):
        return self.health

    def get_moves(self):
        return self.moveList

    def get_attack(self, move):  # string
        return self.moveList.get(move)

    def add_move(self, move):   # tuple
        self.moveList[move[0]] = move[1]

    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.isAlive = False

    def attack(self, move, opponent):  # string and Enemy object
        damage = self.get_attack(move)
        if damage is None:
            damage = 0
        opponent.take_damage(damage)

    @classmethod
    def hello(cls):
        pass


class Player(Object):
    def __init__(self, health=100):
        super(Player, self).__init__(health)


class Enemy(Object):
    def __init__(self, health=100):
        super(Enemy, self).__init__(health)


def display_health(player, enemy):
    print(colored("Enemy:\nHealth: "+str(enemy.get_health())+'\n', 'red'))
    print(colored("You:\nHealth: "+str(player.get_health())+ '\n', 'blue'))


if __name__ == "__main__":
    base_health = 50
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
    player = Player(player_health) # make an array of objects later
    enemy = Enemy(base_health)
    gameNotOver = True
    while gameNotOver:
        display_health(player, enemy)
        print("Moves:\n ", player.get_moves())
        move = input("It is your turn.\nChoose a move to attack with (Type its name)")
        player.attack(move, enemy)
        display_health(player, enemy)
        enemy.attack("tackle", player)
        if not enemy.isAlive:
            display_health(player, enemy)
            gameNotOver = False
            print("You Won")
        if not player.isAlive:
            display_health(player, enemy)
            gameNotOver = False
            print("You Lost")
    print("Game Over. Thanks for playing.")
