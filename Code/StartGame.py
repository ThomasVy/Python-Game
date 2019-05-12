from Attack import * 
from InputsOutputs import *
from Character import *

def main():
    base_health = 10
    player = Player(getHealth(), getType(), getName())
    stage = 1
    enemy = Enemy(base_health, choice(list(TYPEMOVES)), "Enemy "+str(stage))
    gameOver = False
    while not gameOver:
        displayhealth(player, enemy)
        playerTurn(player, enemy)
        displayhealth(player, enemy)
        enemy.do_damage(player)
        if stage == 4:
            break
        if enemy.isDead:
            displayhealth(player, enemy)
            player.level_up()
            stage += 1
            base_health += 5
            enemy = Enemy(base_health, choice(list(TYPEMOVES)), "Enemy "+str(stage))
        if player.isDead:
            displayhealth(player, enemy)
            gameOver = True
    displayLoseScreen()

if __name__ == "__main__":
    main()
