import pygame, math
import random
pygame.init()


class GameInformation:
    def __init__(self, correct):
        self.correct = correct


class Game:
    """
    To use this class simply initialize and instance and call the .loop() method
    inside of a pygame event loop (i.e while loop). Inside of your event loop
    you can call the .draw() and .move_paddle() methods according to your use case.
    Use the information returned from .loop() to determine when to end the game by calling
    .reset().
    """
    SCORE_FONT = pygame.font.SysFont("comicsans", 40)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    YELLOW = (255, 255, 0)
    GREEN = (0, 255, 0)
    

    def __init__(self, window, window_width, window_height):
        self.window_width = window_width
        self.window_height = window_height
        self.start_time = pygame.time.get_ticks()
        self.elapsed_time = 0

        pygame.draw.rect(window, self.BLACK, (50, 50, 450, 5))
        pygame.draw.rect(window, self.BLACK, (50, 100, 450, 5))
        pygame.draw.rect(window, self.BLACK, (50, 150, 450, 5))
        pygame.draw.rect(window, self.BLACK, (50, 200, 450, 5))
        pygame.draw.rect(window, self.BLACK, (50, 250, 450, 5))
        pygame.draw.rect(window, self.BLACK, (50, 300, 450, 5))
        pygame.draw.rect(window, self.BLACK, (50, 350, 450, 5))
        pygame.draw.rect(window, self.BLACK, (50, 400, 450, 5))
        pygame.draw.rect(window, self.BLACK, (50, 450, 450, 5))
        pygame.draw.rect(window, self.BLACK, (50, 500, 450, 5))
        
        pygame.draw.rect(window, self.BLACK, (50, 50, 5, 450))
        pygame.draw.rect(window, self.BLACK, (100, 50, 5, 450))
        pygame.draw.rect(window, self.BLACK, (150, 50, 5, 450))
        pygame.draw.rect(window, self.BLACK, (200, 50, 5, 450))
        pygame.draw.rect(window, self.BLACK, (250, 50, 5, 450))
        pygame.draw.rect(window, self.BLACK, (300, 50, 5, 450))
        pygame.draw.rect(window, self.BLACK, (350, 50, 5, 450))
        pygame.draw.rect(window, self.BLACK, (400, 50, 5, 450))
        pygame.draw.rect(window, self.BLACK, (450, 50, 5, 450))
        pygame.draw.rect(window, self.BLACK, (500, 50, 5, 455))

        self.correct = 0
        self.original_puzzle = [5, 6, 1, 8, 4, 7, 9, 2, 3, 
                        3, 7, 9, 5, 2, 1, 6, 8, 4, 
                        4, 2, 8, 9, 6, 3, 1, 7, 5, 
                        6, 1, 3, 7, 8, 9, 5, 4, 2, 
                        7, 9, 4, 6, 5, 2, 3, 1, 8, 
                        8, 5, 2, 1, 3, 4, 7, 9, 6, 
                        9, 3, 5, 4, 7, 8, 2, 2, 1, 
                        1, 4, 6, 2, 9, 5, 8, 3, 7, 
                        2, 8, 7, 3, 1, 6, 4, 5, 9]
        self.values = self.original_puzzle.copy()
        self.window = window
    
    def update_board(self, window):
        # Clear the board first (optional, if needed)
        self.window.fill(self.WHITE)  # Assuming WHITE is the background color
        #self.reset()
        pygame.draw.rect(window, self.BLACK, (50, 50, 450, 5))
        pygame.draw.rect(window, self.BLACK, (50, 100, 450, 5))
        pygame.draw.rect(window, self.BLACK, (50, 150, 450, 5))
        pygame.draw.rect(window, self.BLACK, (50, 200, 450, 5))
        pygame.draw.rect(window, self.BLACK, (50, 250, 450, 5))
        pygame.draw.rect(window, self.BLACK, (50, 300, 450, 5))
        pygame.draw.rect(window, self.BLACK, (50, 350, 450, 5))
        pygame.draw.rect(window, self.BLACK, (50, 400, 450, 5))
        pygame.draw.rect(window, self.BLACK, (50, 450, 450, 5))
        pygame.draw.rect(window, self.BLACK, (50, 500, 450, 5))
        
        pygame.draw.rect(window, self.BLACK, (50, 50, 5, 450))
        pygame.draw.rect(window, self.BLACK, (100, 50, 5, 450))
        pygame.draw.rect(window, self.BLACK, (150, 50, 5, 450))
        pygame.draw.rect(window, self.BLACK, (200, 50, 5, 450))
        pygame.draw.rect(window, self.BLACK, (250, 50, 5, 450))
        pygame.draw.rect(window, self.BLACK, (300, 50, 5, 450))
        pygame.draw.rect(window, self.BLACK, (350, 50, 5, 450))
        pygame.draw.rect(window, self.BLACK, (400, 50, 5, 450))
        pygame.draw.rect(window, self.BLACK, (450, 50, 5, 450))
        pygame.draw.rect(window, self.BLACK, (500, 50, 5, 455))
        # Loop through all positions on the board
        for location in range(81):  # For a 9x9 Sudoku board, there are 81 positions
            value = self.values[location]
            if value != 0:  # Only render non-empty values
                score_text = self.SCORE_FONT.render(f"{value}", 1, self.BLACK)
                self.window.blit(score_text, ((location % 9) * 50 + 70, (location // 9) * 50 + 45))

        # Update the display
        pygame.display.update()


    def check_state(self, state, location):
        info = []
        row = location // 9
        col = location % 9
        square_row_start = (row // 3) * 3
        square_col_start = (col // 3) * 3
        for index, num in enumerate(state):
            current_row = index // 9
            current_col = index % 9
            if (current_row == row or current_col == col) and index != location:
                info.append(num)
            if (square_row_start <= current_row < square_row_start + 3) and (square_col_start <= current_col < square_col_start + 3) and index != location:
                info.append(num)
        if state[location] in info:
            return False
        return True
    
    def find_empty(self, state):
        for i in range(9):
            for j in range(9):
                if state[i * 9 + j] == 0:
                    return (i * 9 + j)
        return None
    
    def backtracking(self, state):
        location = self.find_empty(state)
        if location is None:
            return True
        
        for choice in range(1,10):
            state[location] = choice
            self.update_board(self.window)
            if self.check_state(state, location):
                if self.backtracking(state):
                    return state
            state[location] = 0   
        return False

