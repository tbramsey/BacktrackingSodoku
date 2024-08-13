# https://neat-python.readthedocs.io/en/latest/xor_example.html
from game import Game
import pygame
import random
import time

pygame.init()


class SudokuGame:
    def __init__(self, window, width, height):
        self.window = pygame.display.set_mode((width, height))
        window.fill((255, 255, 255))
        pygame.display.flip()
        self.game = Game(window, width, height)
        self.game.update_board(window)
        
        
        
    def backtracking_alg(self):
        for y in range(50):
            for x in range(random.randrange(70,71)):
                self.game.values[random.randrange(0,81)] = 0
            self.game.backtracking(self.game.values)
        
        #time.sleep(10)

    def test_drive(self):
        location_input = ""  
        location = None      
        prev = None
        run = True
        for x in range(random.randrange(1,71)):
            self.game.values[random.randrange(0,81)] = 0
        self.game.update_board(window)
        
        while run:
            value = 0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break
                if event.type == pygame.KEYDOWN:
                    if event.unicode.isdigit():
                        if prev == location:
                            location_input += event.unicode
                        else:
                            value = int(event.unicode)
                            prev = location
                    if event.key == pygame.K_RETURN:
                        if location_input:
                            location = int(location_input)
                            location_input = ""         
            if value != 0 and location < 81:
                #self.game.reset()
                self.game.values[location] = value
                self.game.update_board(window)

    
if __name__ == '__main__':
    width, height = 600, 600
    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Sudoku")
    sudoku = SudokuGame(window, width, height)
    sudoku.game.update_board(window)
    sudoku.backtracking_alg()
    
