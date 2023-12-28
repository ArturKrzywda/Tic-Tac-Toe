#Do zrobienia:
#-Napisanie Bota
#-Napisanie funkcji sprawdziającej wygraną
#-Naprawienie funkcji sprawdzającej remis
#-Zrobienie bezpiecznika w player move żeby nie dało się dać innego typu nisz int

import Bot
import Game
print("Test gitignore")
def main():
    b = Bot.Bot()
    g = Game.Game()
    g.run(b)


if __name__ == '__main__':
    main()
