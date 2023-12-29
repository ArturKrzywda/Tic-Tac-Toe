import random
#funkcja move zwraca kordynaty [y,x]
#Algorytm MinMax
class Bot():
    def __init__(self):
        pass
    def move(self, table, difficulty=None):
        while True:
            y = random.randint(0,2)
            x = random.randint(0,2)
            if table[y][x] == None:
                return [y,x]