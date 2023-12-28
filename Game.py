import os
class Game():
    #X = 1
    #O = 0
    #table[y][x] ZAPAMIENTAC!
    def __init__(self):
        self.CurrentPlayerTurn = 1
        self.NumberOfPlayer = 0
        self.table = [[None,None,None],
                     [None,None,None],
                     [None,None,None]]
    def reset(self): 
        self.table = [[None,None,None],
                     [None,None,None],
                     [None,None,None]]
    def istie(self):
        for y  in range(3):
             for x in range(3):
                  if self.table[y][x] == None: 
                      print("tie w funkcji")
                      return False
        return True

    def isWin(self):
         pass
    
    def check(self):
         if self.isWin() == 1: return 1
         if self.isWin() == 0: return 0
         if self.istie(): return 3
         return 
    
    def move(self, b):
         if self.NumberOfPlayer == 2:
            if self.CurrentPlayerTurn == 1: 
                mv = self.Playermove()
                self.table[mv[0]][mv[1]] = 1
                self.CurrentPlayerTurn = 0
                return
            if self.CurrentPlayerTurn == 0:
                mv = self.Playermove()
                self.table[mv[0]][mv[1]] = 0
                self.CurrentPlayerTurn = 1
                return
         else:
             if self.CurrentPlayerTurn == 1:
                mv = self.Playermove()
                self.table[mv[0]][mv[1]] = 1
                self.CurrentPlayerTurn = 0
                return
             if self.CurrentPlayerTurn == 0:
                 mv = b.move(self.table) 
                 self.table[mv[0]][mv[1]] = 0   
                 self.CurrentPlayerTurn = 1
                 return
    def Playermove(self):
        while True:
            qy = int(input("Give row cordinate\n>"))
            qx = int(input("Give colum cordinate\n>"))
            qy -= 1
            qx -= 1
            if qy > 2 or qx > 2:
                self.draw(error=1)
            else:
                if self.table[qy][qx] != None:
                    self.draw(error=2)
                else: break
        
        return [qy,qx]
         
         
    def draw(self, error=None):
            os.system('cls')
            drawtable = [[],[],[]]
            for y in range(3):
                for x in range(3):
                    if self.table[y][x] == None:
                        drawtable[y].append(' ')
                    elif self.table[y][x] == 1:
                        drawtable[y].append('X')
                    else:
                        drawtable[y].append('O')
            draw = [
               ["    ",drawtable[0][0]," │ ",drawtable[0][1]," │ ",drawtable[0][2]," "],
               ["   ───┼───┼───"],
               ["    ",drawtable[1][0]," │ ",drawtable[1][1]," │ ",drawtable[1][2]," "],
               ["   ───┼───┼───"],
               ["    ",drawtable[2][0]," │ ",drawtable[2][1]," │ ",drawtable[2][2]," "],
               ["\n"]
            ]
            print("+----------------------+")
            print("| Tic Tac Toe by Artur |")
            print("+----------------------+")
            print('\n\n')
            for t in draw:
                row = ''.join(t)
                print(row)
           
           
            

            if error == 1:
                print("\n\nCordinates are out of range!")
            if error == 2:
                print("\n\nThis place is taken!")
            if error == None:
                print("\n\n")
            if self.NumberOfPlayer == 2:
                if self.CurrentPlayerTurn == 1:
                    print("Player X move")
                if self.CurrentPlayerTurn == 0:
                    print("Player O move")
            else: 
                if self.CurrentPlayerTurn == 1: 
                    print("\n\nPlayer X move")

    def run(self, b):
        try:
            print("Tic Tac Toe by arturek9")
            while True:
                try:
                    self.NumberOfPlayer = int(input("Game for 1 or 2 Player? 1/2\n>"))
                    if self.NumberOfPlayer == 1 or self.NumberOfPlayer == 2: break
                    os.system('cls')
                    print("Wrong number of players!")
                except:
                    os.system('cls')
                    print("Wrong value!")
                
                

            self.reset()
            while True:
                while True:
                    self.draw()
                    self.move(b)
                    if self.check() != 0:
                        if self.check == 1: 
                            if self.NumberOfPlayer == 1:
                              #  os.system('cls')
                                print("Bot Win!")
                                break
                            else:
                              #  os.system('cls')
                                print("Player O Win!")
                                break
                        if self.check == 1: 
                           # os.system('cls')
                            print("Player X Win!")
                            break
                        if self.check == 2: 
                           # os.system('cls')
                            print("Tie!")
                            break
                while True:
                    q = input("Would you like to play another game? Y/N").lower()
                    if q == 'y' or q == 'n': break
                    print("Wrong input!")
                if q == 'n':
                    exit()
        except KeyboardInterrupt:
            os.system('cls')
            print("Game closed by user")
            exit()


        


