import sys
import pygame
import math
import random

class Snake:
    def __init__(self):
        self.length = 1
        self.position = [((screen_width/2), (screen_height/2))]
        self.direction = random.choice([up, down, left, right])
        self.color = (20,25,60)
        self.score = 0
    def go_to_position(self):
        return self.position[0]
    def changeDirection(self, point):
        print("point[0] = {}, point[1] = {}".format(point[0],point[1]))
        if self.length>1 and (point[0]* -1 , point[1]* -1) == self.direction:
            return
        else:
            self.direction = point
    def move(self):
        # check the current position
        current = self.go_to_position()
        x, y = self.direction
        new_destination = (((current[0]+(x*gridsize))%screen_width), (current[1]+(y*gridsize))%screen_height)
        print(new_destination)
        if len(self.position)> 2 and new_destination in self.position[2:]:
            self.GameOver()
        else:
            self.position.insert(0,new_destination)
            if len(self.position) > self.length:
                self.position.pop()
    

    def GameOver(self):
        self.length = 1
        self.position = [((screen_width/2), (screen_height/2))]
        self.direction = random.choice([up, down, left, right])
        self.color = (20,25,60)
        self.score = 0

    def drawSnake(self, surface):
        for p in self.position:
            r = pygame.Rect((p[0], p[1]), (gridsize,gridsize))
            pygame.draw.rect(surface, self.color, r)
            pygame.draw.rect(surface, (93,216, 228), r, 1)
    

    def SnakeMouvement(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    self.changeDirection(down)
                if event.key == pygame.K_UP:
                    self.changeDirection(up)
                if event.key == pygame.K_LEFT:
                    self.changeDirection(left)
                if event.key == pygame.K_RIGHT:
                    self.changeDirection(right)
                


class Food:
    def __init__(self):
        self.position = (0,0)
        self.color = (255,0,0)
        self.icon = pygame.image.load("Snake/ressources/apple.png")
        self.RandomPosition()
    
    def RandomPosition(self):
        self.position = (random.randint(0,grid_width- 1)*gridsize,random.randint(0,grid_height-1)*gridsize)
    
    def drawFood(self, surface):
        for x in self.position:
            r = pygame.Rect((self.position[0], self.position[1]), (gridsize, gridsize))
            #pygame.draw.rect(surface, self.color, r)
            #pygame.draw.rect(surface, (93, 216, 228), r, 1)
def drawGrid(surface):
    for y in range(0, int(grid_height)):
        for x in range(0, int(grid_width)):
            if (x+y)%2 == 0:
                r = pygame.Rect((x*gridsize, y*gridsize), (gridsize,gridsize))
                pygame.draw.rect(surface,(93,216,228), r)
            else:
                rr = pygame.Rect((x*gridsize, y*gridsize), (gridsize,gridsize))
                pygame.draw.rect(surface, (84,194,205), rr)

screen_width = 480
screen_height = 480

gridsize = 20
grid_width = screen_width/gridsize
grid_height = screen_height/gridsize

up = (0,-1)
down = (0,1)
left = (-1,0)
right = (1,0)

def main():
    pygame.init()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((screen_width, screen_height), 0, 32)
    #Change the title of the screen
    pygame.display.set_caption("Snake")
    # Change icon of the game
    icon = pygame.image.load('Snake/ressources/snake.png')
    # background image
    pygame.display.set_icon(icon)
    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()
    
    drawGrid(surface)
    # Instanciate the snake and the food
    snake = Snake()
    food = Food()
    def FoodIcon(x,y):
        screen.blit(food.icon,(x,y))
    myfont = pygame.font.SysFont("newfont",16)

    while (True):
        screen.fill((20,20,20))
        clock.tick(10)
        snake.SnakeMouvement()
        drawGrid(surface)
        snake.move()
        if snake.go_to_position() == food.position:
            snake.length += 1 # Increase the length
            snake.score += 1 # Increase the score
            food.RandomPosition() # Randomize the position of food
        snake.drawSnake(surface)
        food.drawFood(surface)
        screen.blit(surface, (0,0))
        text = myfont.render("Score {0}".format(snake.score), 1, (0,0,0))
        screen.blit(text, (5,10)) # Draw text on screen
        FoodIcon(food.position[0],food.position[1])
        pygame.display.update()

main()