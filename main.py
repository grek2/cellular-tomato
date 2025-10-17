import pygame
import random

size = 100
speed = 1
#type "random" to randomize
start = "game"
chance = 19
mouseClicked = False
active = False
started = False
points = 0
DESTROYED = -5000
drawArea = 4
story = [
"""(Press ENTER to advance to next line of text)""",
"""Many, many universes away, in a place just like this one...""",
"""In a world in which the Cambrian Explosion never happened, sentient fungal lifeforms rule the earth.""",
"""No matter how different life is, sometimes things, in all universes, always stay the same.""",
"""They dance, love, cry, make art...""",
"""...and, of course...""",
"""build BADASS ROBOTS!!!""",
"""Their "Growbots" are very similar to the robots of Earth, except they're made entirely of living fungal matter.""",
"""...aaaaand there's also no upper bound on their size. And they're immortal. And they're horrible amalgamations of hundreds of writhing fungal components that don't move, just endlessly spread.""",
"""Basically just pretty much like human robots.""",
"""The Sporsdale Bio Raiders - one of the top Growbotics teams in New Fungus State, rivaled only by the New Rotchelle Mushroom Mechanics, are preparing for this year's LASTTech competition!""",
"""Unfortunately, they've got no bioprogrammers this year, and their Growbot doesn't know what to do!""",
"""So, they did what any engineering team members would do: instead of even attempting to learn how to code, they opened a portal to an alternate dimension - and they've asked YOU to help.""",
"""The Sporesdale Bio Raiders worked very very hard on their creeping horror, but we're probably going to get disqualified if we attempt to show it.""",
"""So we've helpfully abstracted the playing field down to a 100x100 grid of PIXELS!""",
"""GREEN PIXELS represent the body "cells" of the Growbot. The complex mycelial transfer mechanisms and energy flow dynamics that go into moving the Creeping Horror are a bit beyond the scope of this tutorial, but essentially, *if a cell has exactly three GREEN neighbors, it will turn GREEN. GREEN CELLS cannot die.""",
"""BLUE PIXELS represent the SCORING ZONES. When a cell that formerly housed a BLUE PIXEL turns GREEN, the Bio Raiders are awarded some number of POINTS (usually ranging from one to ten). Crucially, *different SCORING ZONES reward different amounts of POINTS*. In a radical move this year, LASTTech decided to *conceal the amount of POINTS each SCORING ZONE rewards to the player.* Part of the puzzle of this game - and of the Bio Raiders' challenge - is to figure that out mid-competition.""",
"""RED PIXELS represent the PENALTY ZONES. These work much the same as the SCORING ZONES, except they *subtract some number of POINTS from 1-10* rather than adding then. Again, *different groups of penalty zones subtract different amounts of POINTS*!""",
"""The Bio Raiders' ultimate goal is to earn as many POINTS as possible by covering the BLUE ZONES with GREEN PIXELS and avoiding GREEN PIXELS in the RED ZONES at all costs.""",
"""They'll achieve this by placing BODY CELLS of the robot strategically in order to hit the right points - with your guidance, of course!"""
"""Draw the BODY CELLS using your purple cursor and press SPACE to start the simulation.""",
"""Good luck, Human."""]

onColor = (5, 255, 5, 255)
offColor = (5, 5, 5, 255)
goodColor = (5, 5, 255, 255)
badColor = (255, 5, 5, 255)

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
rules = inkspot
#rules.append(directions8)


#directions8 is the default neighborhood
try:
    rules[2]
except IndexError:
    rules.append(directions8)

for c in story:
    uselessvar = input(c)


#initialize stuff
pygame.init()
pygame.display.set_caption("Sporesdale Bioraiders")
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

            if lifeGrid[i][j] == 1:
                pygame.draw.rect(screen, pygame.Color(onColor), ((i)*boxSize, (j)*boxSize, boxSize, boxSize), border_radius=0)            
            elif lifeGrid[i][j] == 0:
                pygame.draw.rect(screen, pygame.Color(offColor), ((i)*boxSize, (j)*boxSize, boxSize, boxSize), border_radius=0)            
            elif lifeGrid[i][j] < 0:
                pygame.draw.rect(screen, pygame.Color(badColor), ((i)*boxSize, (j)*boxSize, boxSize, boxSize), border_radius=0)            
            elif lifeGrid[i][j] > 1:
                pygame.draw.rect(screen, pygame.Color(goodColor), ((i)*boxSize, (j)*boxSize, boxSize, boxSize), border_radius=0)            
            

def getNextStep(lifeGrid, points):
    a, b = size, size

    for i in range(a):
        for j in range(b):
            liveNbrs = 0

            for dirX, dirY in rules[2]:
                (x, y) = (i + dirX, j + dirY)

                if 0 <= x < a and 0 <= y < b and (lifeGrid[x][y] == 1 or lifeGrid[x][y] == "dying"):
                    liveNbrs += 1
       
            if lifeGrid[i][j] == 0 and liveNbrs in rules[0]:
                lifeGrid[i][j] = "growing"

            elif (lifeGrid[i][j] == 1) and not(liveNbrs in rules[1]):
                lifeGrid[i][j] = "dying"

            elif (lifeGrid[i][j] < 0 or lifeGrid[i][j] > 1) and liveNbrs in rules[0] and lifeGrid[i][j] > -3000:
                print(lifeGrid[i][j], "points")               
                points += int(lifeGrid[i][j])
                if lifeGrid[i][j] == -1:
                    lifeGrid[i][j] = DESTROYED    
                else:
                    lifeGrid[i][j] = "growing"               
            
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

elif start == "game":
    for i in range(90,100):
        for j in range(90, 100):
            lifeGrid[i][j] = -5
            lifeGrid[89][j] = 10
            lifeGrid[i][j-90] = 5
            lifeGrid[i-5][15] = -1

    lifeGrid[97][28] = -10
    lifeGrid[15][26] = -3
    lifeGrid[15][27] = 3
    for i in range(50):
        lifeGrid[i][99] = 5
        lifeGrid[50][i] = 5
        lifeGrid[45][i-10] = -1
        
    for i in range(79, 100, 4):
        lifeGrid[i][50] = -7
        lifeGrid[i-1][50] = 10
    
    """
    example placement
    lifeGrid[ 7 ][ 11 ] = 1
    lifeGrid[ 8 ][ 9 ] = 1
    lifeGrid[ 9 ][ 11 ] = 1
    """
    lifeGrid[ 10 ][ 43 ] = 1
    lifeGrid[ 13 ][ 44 ] = 1
    lifeGrid[ 10 ][ 45 ] = 1
    lifeGrid[ 13 ][ 46 ] = 1



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
            started = True
            #you can draw until you start the simulation.
        elif event.type == pygame.KEYUP:
            if not started:
                active = False

    renderCurrentState()
    
    #draw mouse
    pygame.draw.rect(screen, pygame.Color(255, 100, 255, 255), (int((mouseX/boxSize))*boxSize/drawArea, int((mouseY/boxSize))*boxSize/drawArea, boxSize, boxSize), border_radius=0)
    if mouseClicked and not active:
        try:
            lifeGrid[int((mouseX/boxSize/drawArea))][int((mouseY/boxSize/drawArea))] = 1
        except IndexError:
            "Pretty please don't give an index error, thanks" #this needs to be here or python will yell at you.
            
    if active:
        getNextStep(lifeGrid, points)
    
    pygame.display.flip()

    pygame.time.delay(speed)

    clock.tick(60)

pygame.quit()
#print("Points:", points)










            
    