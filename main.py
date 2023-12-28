#Do zrobienia:
#-Napisanie Bota
#-Napisanie funkcji sprawdziającej wygraną
#main task=>-Naprawienie funkcji sprawdzającej remis
#-Dodoanie __pycache__ do .gitignore


import Bot
import Game

def main():
    b = Bot.Bot()
    g = Game.Game()
    g.run(b)


if __name__ == '__main__':
    main()
 