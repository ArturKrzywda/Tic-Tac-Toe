#Do zrobienia:
#-Napisanie Bota
#-Napisanie funkcji sprawdziającej wygraną


#   _______ _      _ 
#  |__   __(_)    | |
#     | |   _  ___| |
#     | |  | |/ _ \ |
#     | |  | |  __/_|
#     |_|  |_|\___(_)

#   ____        _    __          ___       _ 
#  |  _ \      | |   \ \        / (_)     | |
#  | |_) | ___ | |_   \ \  /\  / / _ _ __ | |
#  |  _ < / _ \| __|   \ \/  \/ / | | '_ \| |
#  | |_) | (_) | |_     \  /\  /  | | | | |_|
#  |____/ \___/ \__|     \/  \/   |_|_| |_(_)

#   _____  _                         __  __          ___       _ 
#  |  __ \| |                       /_ | \ \        / (_)     | |
#  | |__) | | __ _ _   _  ___ _ __   | |  \ \  /\  / / _ _ __ | |
#  |  ___/| |/ _` | | | |/ _ \ '__|  | |   \ \/  \/ / | | '_ \| |
#  | |    | | (_| | |_| |  __/ |     | |    \  /\  /  | | | | |_|
#  |_|    |_|\__,_|\__, |\___|_|     |_|     \/  \/   |_|_| |_(_)
#                   __/ |                                        
#                  |___/                                         
                                           
#   _____  _                         ___   __          ___       _ 
#  |  __ \| |                       |__ \  \ \        / (_)     | |
#  | |__) | | __ _ _   _  ___ _ __     ) |  \ \  /\  / / _ _ __ | |
#  |  ___/| |/ _` | | | |/ _ \ '__|   / /    \ \/  \/ / | | '_ \| |
#  | |    | | (_| | |_| |  __/ |     / /_     \  /\  /  | | | | |_|
#  |_|    |_|\__,_|\__, |\___|_|    |____|     \/  \/   |_|_| |_(_)
#                   __/ |                                          
#                  |___/                                                                                             
      


import Bot
import Game

def main():
    b = Bot.Bot()
    g = Game.Game()
    g.run(b)


if __name__ == '__main__':
    main()
    