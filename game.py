import pygame 
from grid import Grid
from blocks import *
import random

class Game:
    def __init__(self):
        self.grid = Grid()
        self.blocks = [IBlock(),JBlock(),LBlock(),OBlock(),SBlock(),TBlock()]
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.game_over = False
        self.score = 0
        self.rotate_sound = pygame.mixer.Sound("sounds/rotate.ogg")
        self.clear_sound = pygame.mixer.Sound("sounds/clear.ogg")
        pygame.mixer.music.load("sounds/music.ogg")
        pygame.mixer.music.play(-1)


    def update_score (self, line_cleared , move_down):
        if line_cleared == 1:
            self.score += 100
        elif line_cleared == 2:
            self.score += 300 
        elif line_cleared == 3:
            self.score += 500
        self.score += move_down

    def reset(self):
        self.grid.reset()
        self.blocks = [IBlock(),JBlock(),LBlock(),OBlock(),SBlock(),TBlock()]
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.score = 0

    def block_fits(self):
        tiles = self.current_block.get_cell_positions()
        for tile in tiles:
            if self.grid.is_empty(tile.row , tile.column) == False:
                return False
        return True 

    def get_random_block(self):
        if len(self.blocks) == 0: 
            self.blocks = [IBlock(),JBlock(),LBlock(),OBlock(),SBlock(),TBlock()]
        block = random.choice(self.blocks)
        self.blocks.remove(block)
        return block
    
    def move_left(self):
        self.current_block.move(0,-1)
        if self.block_inside()== False or self.block_fits() == False:
            self.current_block.move(0,1)

    
    def move_right(self):
        self.current_block.move(0,1)
        if self.block_inside()== False or self.block_fits() == False:
            self.current_block.move(0,-1)


    def move_down(self):
        self.current_block.move(1,0)
        if self.block_inside()== False or self.block_fits()== False:
            self.current_block.move(-1,0 )
            self.lock_block()

    def lock_block(self):
        tiles = self.current_block.get_cell_positions()
        for position in tiles:
            self.grid.grid[position.row][position.column] = self.current_block.id
        self.current_block = self.next_block
        self.next_block = self.get_random_block()
        rows_cleared = self.grid.clear_full_rows()
        if rows_cleared > 0:
            self.clear_sound.play()
            self.update_score(rows_cleared , 0)
        if self.block_fits() == False:
            self.game_over = True
    
    def rotate(self):
        self.current_block.rotate()
        if self.block_inside() == False:
            self.current_block.undo_rotation()
        else:
            self.rotate_sound.play()

    def block_inside(self):
        tiles = self.current_block.get_cell_positions()
        for tile in tiles:
            if self.grid.is_inside(tile.row, tile.column) == False: 
                return False
        return  True

    def draw(self,screen):
        self.grid.draw(screen)
        self.current_block.draw(screen ,11 ,11)
        if self.next_block.id == 1:       # L block
            self.next_block.draw(screen , 310, 286)
        elif self.next_block.id == 2:   # J Blobk
            self.next_block.draw(screen , 317 , 286)
        elif self.next_block.id == 3:    # I block
            self.next_block.draw(screen , 300 , 300)
        elif self.next_block.id == 4:   # O block
            self.next_block.draw(screen , 300 , 286)
        elif self.next_block.id == 5:   # S block
             self.next_block.draw(screen , 310 , 286)
        elif self.next_block.id == 6:   # T block
            self.next_block.draw(screen , 315 , 286)
        else:                           # Z block
            self.next_block.draw(screen , 312 , 286)




