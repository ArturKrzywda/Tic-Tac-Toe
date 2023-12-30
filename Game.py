import os
from sys import exit
    #X = 1
    #O = 0
    #table[y][x] ZAPAMIENTAC!
class Game():

    def __init__(self):
        self.CurrentPlayerTurn = 1
        self.NumberOfPlayer = 0
        self.table = [[None,None,None],
                     [None,None,None],
                     [None,None,None]]
    def reset(self, error=None): 
        self.table = [[None,None,None],
                     [None,None,None],
                     [None,None,None]]
        os.system("cls")
        print("+----------------------+")
        print("| Tic Tac Toe by Artur |")
        print("+----------------------+\n") 

        if error == 1: print("Wrong number of players!")
        if error == 2: print("Wrong value!")
        if error == None: print()
        try:
            self.NumberOfPlayer = int(input("Game for 1 or 2 Player? 1/2\n>"))
            if self.NumberOfPlayer == 1 or self.NumberOfPlayer == 2: return
            self.reset(error=1)
        except Exception as e:
            if e == KeyboardInterrupt:
                os.system('cls')
                print("Game closed by user")
                exit()
            self.reset(error=2)
   
    def istie(self): #Funkcja działa poprawnie
        for y  in range(3):
             for x in range(3):
                  if self.table[y][x] == None: 
                      return False
        print("tie w funkcji")          
        return True

    def isWin(self):
         pass
    
    def check(self): #Zwraca dobrze return 3
         if self.isWin() == 1: return 1 #X win
         if self.isWin() == 0: return 2 #O win
         if self.istie(): return 3 # Tie
         return False
    
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
            try:
                qy = int(input("Give row cordinate\n>"))
                qy -= 1
                if qy > 2: self.draw(error=1)
                else:
                    qx = int(input("Give colum cordinate\n>"))
                    qx -= 1
                    if qx > 2:
                        self.draw(error=1)
                    else:
                        if self.table[qy][qx] != None:
                            self.draw(error=2)
                        else: break
            except Exception as e:
                if e == KeyboardInterrupt:
                    print("Game closed by user")
                    exit()
                self.draw(error=3)
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
                ["     1   2   3\n"],
                ["1    ",drawtable[0][0]," │ ",drawtable[0][1]," │ ",drawtable[0][2]," "],
                ["    ───┼───┼───"],
                ["2    ",drawtable[1][0]," │ ",drawtable[1][1]," │ ",drawtable[1][2]," "],
                ["    ───┼───┼───"],
                ["3    ",drawtable[2][0]," │ ",drawtable[2][1]," │ ",drawtable[2][2]," "],
                ["\n"]
            ]
            print("+----------------------+")
            print("| Tic Tac Toe by Artur |")
            print("+----------------------+\n")
           #Do testowania czy Tie działa 
            print(self.scan)
            if self.pr == 1: print("tie w funkcji")
           ####
            for t in draw:
                row = ''.join(t)
                print(row)
            

            if error == 1:
                print("Cordinates are out of range!")
            if error == 2:
                print("This place is taken!")
            if error == 3:
                print("Wrong value!")
            if error == None:
                print()
            if self.NumberOfPlayer == 2:
                if self.CurrentPlayerTurn == 1:
                    print("Player X move")
                if self.CurrentPlayerTurn == 0:
                    print("Player O move")
            else: 
                if self.CurrentPlayerTurn == 1: 
                    print("Player X move")

    def run(self, b):
        try:
            self.reset()
            while True:
                self.draw()
                self.move(b)
                check = self.check()
                if check != False: #To to wogóle od nowa chyba trzeba napisac bo nie dziala
                    if check == 2: 
                        if self.NumberOfPlayer == 1:
                            os.system('cls')
                            input("Bot Win!\nPress Enter to continue\n")
                            break
                        else:
                            os.system('cls')
                            input("Player O Win!\nPress Enter to continue\n")
                            break
                    if check == 1: 
                        os.system('cls')
                        input("Player X Win!\nPress Enter to continue\n")
                        break
                    if check == 3: 
                        os.system('cls')
                        input("Tie!\nPress Enter to continue\n")
                        break
            while True: 

                q = input("Would you like to play another game? Y/N\n>").lower()
                if q == 'y' or q == 'n': 
                    if q == 'n':
                        exit()
                    else: 
                        self.run(b)
                        break
                print("Wrong input!")
        except KeyboardInterrupt:
            os.system('cls')
            print("Game closed by user")
            exit()


        


