# GameOfLife.py
# Skrolli 2016.3 - skrolli.fi/numerot

# Game of Life -toteutus Pythonilla, tehnyt Jiggawatt Skrolli-lehteen (Python 3 -päivitys jtsiren)

import os

moore_nb = [
(-1,-1), (0,-1), (1,-1),
(-1, 0),         (1, 0),
(-1, 1), (0, 1), (1, 1),
]

def surround(pos):
    return [(pos[0]+nb[0], pos[1]+nb[1]) for nb in moore_nb]

class GameOfLife():
    def __init__(self):        
        self.board = {
                  (0,-1):1, (1,-1):1,
                  (-1,0):1, (0, 0):1,
                  (0, 1):1,
        }

        self.birth = [3]
        self.survival = [2, 3]
        
        self.turn = 0

        self.pos = [0, 0]
        self.w = 64
        self.h = 20

    def neighbours(self, area):
        return len( [cell for cell in area if cell in self.buffer] )

    def prompt(self):
        return input("%s. vuoro - Enter jatkaaksesi, w/a/s/d skrollataksesi, muutoin 'q' \n>" % self.turn)

    def user_input(self):
        typed = self.prompt()

        while typed in ['w','s','a','d']:
            if typed == 'w':
                self.pos[1] -= self.h // 2
            elif typed == 's':
                self.pos[1] += self.h // 2              
            elif typed == 'a':
                self.pos[0] -= self.w // 2
            elif typed == 'd':
                self.pos[0] += self.w // 2

            self.draw("Skrollattu, nyt keskitetty pisteeseen " + str(self.pos[0]) + "," + str(self.pos[1]))

            return self.user_input()  # Rekursiota niin kauan, että ei enää skrollata
        
        return typed

    def store(self):
        self.buffer = [cell for cell in self.board]

    def iterate(self):
        self.store()        # Luo bufferin kopioimalla avaimet laudasta
        dead_cells = {}  # Oma bufferinsa mahd. uusille soluille - ei tarkisteta turhia alueita

        for alive in self.buffer:
            live_nbs = 0
            neighbours = surround(alive)

            for cell in neighbours:
                if cell not in self.buffer:  # Kuollut reunasolu
                    dead_cells[cell] = 1
                else:
                    live_nbs += 1

            if live_nbs not in self.survival:
                del self.board[alive]  # Kuolee
 
        for dead in dead_cells:
            if self.neighbours(surround(dead)) in self.birth:
                self.board[dead] = 1  # Syntyy

    def draw(self, msg):
        os.system('cls')
        print(msg + '\n')
        print(' ' + ('+' * (self.w+2)))
        
        for y in range(self.pos[1]-self.h // 2, self.pos[1]+self.h // 2):
            line = ' +'
            
            for x in range(self.pos[0]-self.w // 2, self.pos[0]+self.w // 2):
                line += '0' if (x,y) in self.board else ' '

            print(line + '+')
            
        print(' ' + ('+' * (self.w+2)) + '\n')

    def process(self):
        if self.turn > 0:
            self.iterate()
            
        self.draw("")
        return self.user_input() != 'q'
        
################ Main ################

life = GameOfLife()
while life.process():
    life.turn += 1