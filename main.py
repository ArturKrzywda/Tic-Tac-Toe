#Do zrobienia:
#-Napisanie Bota
#-Napisanie funkcji sprawdziającej wygraną
#-Naprawienie funkcji sprawdzającej remis
#-Zrobienie bezpiecznika w player move żeby nie dało się dać innego typu niż int
#-Naprawienie spacji w czsie błędu
#-Dodoanie __pycache__ do .gitignore


import Bot
import Game

def main():
    b = Bot.Bot()
    g = Game.Game()
    g.run(b)


if __name__ == '__main__':
    main()
