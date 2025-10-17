import pygame
import random

size = 100
speed = 1
#type "random" to randomize, more 
start = "glider gun"
chance = 19
mouseClicked = False
active = False

#what is a neighbor?
directions8 = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
directions4 = [(0, 1), (1, 0), (0, -1), (-1, 0)]
directions6 = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, -1), (-1, 1)]
directions4r2 = [(0, 1), (1, 0), (0, -1), (-1, 0), (0, 2), (2, 0), (0, -2), (-2, 0)]
directionsUp = [(0, 1), (1, 1), (-1, 1),(0, -1)]

#interesting rulesets
life = [[3], [2, 3]]
highLife = [[3, 6], [2, 3]]
dayNight = [[3, 6, 7, 8], [3, 4, 6, 7, 8]]
seeds = [[2],[]]

#this one has a lot of game potential but idk if there is time to implement it
inkspot = [[3],[0,1,2,3,4,5,6,7,8]]

blinkers = [[3,4,5],[2]]
coral = [[3],[4,5,6,7,8]]
twoByTwo = [[3,6],[1,2,5]]


#rules for cellular automata
rules = life
#rules.append(directions8)


#directions8 is the default neighborhood
try:
    rules[2]
except IndexError:
    rules.append(directions8)

#initialize stuff
pygame.init()
pygame.display.set_caption("Cellular Tomato :)")
windowSize = 600
boxSize = int(windowSize/(size-1))
screen = pygame.display.set_mode((windowSize, windowSize))
clock = pygame.time.Clock()
running = True
lifeGrid = []

#create the grid
for c in range(size):
    die = []
    for d in range(size):
        if start == "random":
            something = int(random.randint(0, chance)/10)
            die.append(something)
        else:
            die.append(0)
    lifeGrid.append(die)

def renderCurrentState():
    for i in range(size):
        for j in range(size):            
            if lifeGrid[i][j] == "growing":
                lifeGrid[i][j] = 1

            elif lifeGrid[i][j] == "dying":
                lifeGrid[i][j] = 0
            pygame.draw.rect(screen, pygame.Color(5, 255*int(lifeGrid[i][j]), 5, 255), ((i)*boxSize, (j)*boxSize, boxSize, boxSize), border_radius=0)            
      

def getNextStep(lifeGrid):
    a, b = size, size

    for i in range(a):
        for j in range(b):
            liveNbrs = 0

            for dirX, dirY in rules[2]:
                (x, y) = (i + dirX, j + dirY)

                #if 0 <= x < a and 0 <= y < b and (lifeGrid[x][y] == 1 or lifeGrid[x][y] == "dying"):

                    liveNbrs += 1


            if lifeGrid[i][j] == 0 and liveNbrs in rules[0]:
                lifeGrid[i][j] = "growing"

            elif (lifeGrid[i][j] == 1) and not(liveNbrs in rules[1]):
                lifeGrid[i][j] = "dying"                
            
    renderCurrentState()

#some start presets
if start == "glider":
    lifeGrid[2][2] = 1
    lifeGrid[3][3] = 1
    lifeGrid[3][4] = 1
    lifeGrid[2][4] = 1
    lifeGrid[1][4] = 1

elif start == "inkspot":
    lifeGrid[12][2] = 1
    lifeGrid[12][3] = 1
    lifeGrid[12][4] = 1
    lifeGrid[11][7] = 1
    lifeGrid[10][47] = 1

elif start == "r":
    f = int(size/2)
    lifeGrid[f+2][f+2] = 1
    lifeGrid[f+3][f+2] = 1
    lifeGrid[f+2][f+3] = 1
    lifeGrid[f+1][f+3] = 1
    lifeGrid[f+2][f+4] = 1
elif start == "glider gun":
    #is there a more convenient way to do this? probably.
    lifeGrid[ 5 ][ 29 ] = 1
    lifeGrid[ 6 ][ 27 ] = 1
    lifeGrid[ 6 ][ 29 ] = 1
    lifeGrid[ 7 ][ 17 ] = 1
    lifeGrid[ 7 ][ 18 ] = 1
    lifeGrid[ 7 ][ 25 ] = 1
    lifeGrid[ 7 ][ 26 ] = 1
    lifeGrid[ 7 ][ 39 ] = 1
    lifeGrid[ 7 ][ 40 ] = 1
    lifeGrid[ 8 ][ 16 ] = 1
    lifeGrid[ 8 ][ 20 ] = 1
    lifeGrid[ 8 ][ 25 ] = 1
    lifeGrid[ 8 ][ 26 ] = 1
    lifeGrid[ 8 ][ 39 ] = 1
    lifeGrid[ 8 ][ 40 ] = 1
    lifeGrid[ 9 ][ 5 ] = 1
    lifeGrid[ 9 ][ 6 ] = 1
    lifeGrid[ 9 ][ 15 ] = 1
    lifeGrid[ 9 ][ 21 ] = 1
    lifeGrid[ 9 ][ 25 ] = 1
    lifeGrid[ 9 ][ 26 ] = 1
    lifeGrid[ 10 ][ 5 ] = 1
    lifeGrid[ 10 ][ 6 ] = 1
    lifeGrid[ 10 ][ 15 ] = 1
    lifeGrid[ 10 ][ 19 ] = 1
    lifeGrid[ 10 ][ 21 ] = 1
    lifeGrid[ 10 ][ 22 ] = 1
    lifeGrid[ 10 ][ 27 ] = 1
    lifeGrid[ 10 ][ 29 ] = 1
    lifeGrid[ 11 ][ 15 ] = 1
    lifeGrid[ 11 ][ 21 ] = 1
    lifeGrid[ 11 ][ 29 ] = 1
    lifeGrid[ 12 ][ 16 ] = 1
    lifeGrid[ 12 ][ 20 ] = 1
    lifeGrid[ 13 ][ 17 ] = 1
    lifeGrid[ 13 ][ 18 ] = 1

while running:

    pygame.mouse.set_visible(False)
    (mouseX, mouseY) = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouseClicked = True
        elif event.type == pygame.MOUSEBUTTONUP:
            mouseClicked = False
        if event.type == pygame.KEYDOWN:
            active = True
            #simulation runs when a key is being pressed.
        elif event.type == pygame.KEYUP:
            active = False

    renderCurrentState()
    
    #draw mouse
    pygame.draw.rect(screen, pygame.Color(255, 100, 255, 255), (int((mouseX/boxSize))*boxSize, int((mouseY/boxSize))*boxSize, boxSize, boxSize), border_radius=0)
    if mouseClicked and not active:
        try:
            lifeGrid[int((mouseX/boxSize))][int((mouseY/boxSize))] = 1
        except IndexError:
            "Pretty please don't give an index error, thanks" #this needs to be here or python will yell at you.
            
    if active:
        getNextStep(lifeGrid)
    
    pygame.display.flip()

    pygame.time.delay(speed)

    clock.tick(60)

pygame.quit()










            
    