import pygame
import sys
import random
from sprites import *
from pygame.locals import *
from os import path
"""Imports python modules"""


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

"""game settings"""
WINDOWWIDTH = 800   # 16 * 64 or 32 * 32 or 64 * 16
WINDOWHEIGHT = 900  # 16 * 48 or 32 * 24 or 64 * 12
FIELDWIDTH = 255
FIELDHEIGHT = 255
TOTALBOMBS = 16
FPS = 60
TITLE = "Bombsweeper"
BGCOLOR = DARKGREY
FONT_NAME = 'agency fb'
MARGIN = 5
TILESIZE = 32
TILEWIDTH = 32
TILEHEIGHT = 32
WIDTH = 1000
HEIGHT = 1000
GRIDWIDTH = (WIDTH / TILESIZE)
GRIDHEIGHT = (HEIGHT / TILESIZE)

class Asset(pygame.sprite.Sprite):
    def __init__(self, game, x, y, colour):
        self.groups = pygame.sprite.Group()
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.image.fill(colour)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

class Tile(Asset):
   def __init__(self, x, y):
      self.image = pygame.image.load('tile.png').convert()
   def update(self):
      self.rect.x = self.x * TILESIZE
      self.rect.y = self.y * TILESIZE

   def num(self):
      for x in range(FIELDWIDTH):
        for y in range(FIELDHEIGHT):
            if not grid[x][y] == '1':
                count = 0
                if x != 0: 
                    if grid[x-1][y] == '1':
                        count += 1
                    if y != 0: 
                        if grid[x-1][y-1] == '1':
                            count += 1
                    if y != FIELDHEIGHT-1: 
                        if grid[x-1][y+1] == '1':
                            count += 1
                if x != FIELDWIDTH-1: 
                    if grid[x+1][y] == '1':
                        count += 1
                    if y != 0: 
                        if grid[x+1][y-1] == '1':
                            count += 1
                    if y != FIELDHEIGHT-1: 
                        if grid[x+1][y+1] == '1':
                            count += 1
                if y != 0: 
                    if grid[x][y-1] == '1':
                        count += 1
                if y != FIELDHEIGHT-1: 
                    if grid[x][y+1] == '1':
                        count += 1
                grid[x][y] = '%s' %(count)


class Bomb(Asset):
   def __init__(self, x, y):
      self.image = pygame.image.load('bomb.png').convert()


def main():

   pygame.init()
   screen = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
   screen.fill(BLACK)
   all_sprites = Asset.groups
   pygame.display.set_caption(TITLE)
   clock = pygame.time.Clock()
   pygame.key.set_repeat(500, 100)
   #load_data()
   gameWon = False
   font_name = pygame.font.match_font(FONT_NAME)
   while True:
      new(screen)
      run(clock, gameWon, all_sprites)



"""
   Initialises Game, setting the display according to constants,
   loads in data and sets up other game aspects
"""


def load_data():
   game_folder = path.dirname(__file__)
   map_data = []
   with open(path.join(game_folder, 'map.txt')) as f:
      for line in f:
         map_data.append(line)
   return map_data


"""Loads in the map design from a text file, and appends onto an array"""


def new(screen):
   grid = []

   for row in range(FIELDHEIGHT):
      grid.append([])
      for column in range(FIELDWIDTH):
         grid[row].append('0')

   placeBombs(grid)

   for row in range(FIELDHEIGHT):
      for column in range(FIELDWIDTH):
         colour = DARKGREY
         if grid[row][column] == '1':
            #Bomb()
            pass
         pygame.draw.rect(screen,colour,[(MARGIN + TILEWIDTH) * column + MARGIN, (MARGIN + TILEHEIGHT) * row + MARGIN, TILEWIDTH, TILEHEIGHT])
         Tile(column, row)
      return grid


   Tile.num()
"""Sets up the game board when starting a new game by instantiating sprites"""


def run(clock, gameWon, all_sprites):
   playing = True
   while playing:
      dt = clock.tick(FPS) / 1000
      events()
      update(gameWon)
      draw(all_sprites)


"""
   Calls functions while the program is running
"""


def quit():
   pygame.quit()
   sys.exit()


"""
   Prevents an error being raised when closing the pygame window, because
   the game recognises the user input to quit
"""


def update(gameWon):
   #Tile.update()

   while gameWon is not True:
      pass



"""
   Updates positions and states of all sprites per frame
"""




def draw(all_sprites):
   screen.fill(BGCOLOR)
   all_sprites.draw(screen)
   pygame.display.flip()




def events():
    leftClick = False
    rightClick = False

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
         quit()

      if event.type == pygame.KEYDOWN:
         if event.key == pygame.K_ESCAPE:
            quit()

      if pygame.mouse.get_pressed()[0] is True:
         print(pygame.mouse.get_pos())
         leftClick = True
      if pygame.mouse.get_pressed()[2] is True:
         rightClick = True

      return leftClick, rightClick


def placeBombs(grid):
   bombCount = 0
   xy = [] 
   while bombCount < TOTALBOMBS: 
      x = random.randint(0,FIELDWIDTH-1)
      y = random.randint(0,FIELDHEIGHT-1)
      xy.append([x,y])
      if xy.count([x,y]) > 1: 
         xy.remove([x,y]) 
      else: 
         grid[x][y] = '1' 
         bombCount += 1
   



if __name__ == '__main__':
   main()