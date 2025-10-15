import pygame
import random

size = 50
speed = 50
start = " "

pygame.init()
pygame.display.set_caption("Cellular Tomato :)")
windowSize = 600
boxSize = int(windowSize/(size-1))
screen = pygame.display.set_mode((windowSize, windowSize))
clock = pygame.time.Clock()
running = True

def getNextStep(lifeGrid):
    a, b = size, size

    #can have 4 or 8 neighbors. 
    directions8 = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    directions4 = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    directionsUp = [(0, 1), (1, 1), (-1, 1),(0, -1)]

    #rules for cellular automata.
    
    bornNbrs = [2]
    surviveNbrs = [2, 3]
    '''
    bornNbrs = [3, 6, 7, 8]
    surviveNbrs = [3, 4, 6, 7, 8]
    '''
    directions = directions8

    for i in range(a):
        for j in range(b):
            liveNbrs = 0

            for dirX, dirY in directions:
                (x, y) = (i + dirX, j + dirY)

                if 0 <= x < a and 0 <= y < b and (lifeGrid[x][y] == 1 or lifeGrid[x][y] == "dying"):
                    liveNbrs += 1


            if lifeGrid[i][j] == 0 and liveNbrs in bornNbrs:
                lifeGrid[i][j] = "growing"

            elif (lifeGrid[i][j] == 1) and not(liveNbrs in surviveNbrs):
                lifeGrid[i][j] = "dying"
                
            
    for i in range(a):
        for j in range(b):            
            if lifeGrid[i][j] == "growing":
                #pygame.draw.rect(screen, pygame.Color(0, 0, 255, 255), ((j)*boxSize, (i)*boxSize, boxSize, boxSize), border_radius=0)
                lifeGrid[i][j] = 1

            elif lifeGrid[i][j] == "dying":
                #pygame.draw.rect(screen, pygame.Color(255, 0, 0, 255), ((i)*boxSize, (j)*boxSize, boxSize, boxSize), border_radius=0)
                lifeGrid[i][j] = 0
            #else:
                #pygame.draw.rect(screen, pygame.Color(0, 255*int(lifeGrid[i][j]), 0, 255), ((j)*boxSize, (i)*boxSize, boxSize, boxSize), border_radius=0)        
            pygame.draw.rect(screen, pygame.Color(5, 255*int(lifeGrid[i][j]), 5, 255), ((i)*boxSize, (j)*boxSize, boxSize, boxSize), border_radius=0)
            #print(lifeGrid[i][j], end=" ")
        #print()


lifeGrid = []
for c in range(size):
    die = []
    for d in range(size):
        if start == "random":
            die.append(random.randint(0,1))
        else:
            die.append(0)
    lifeGrid.append(die)


#lifeGrid[1][1] = 1

lifeGrid[42][42] = 1
lifeGrid[43][43] = 1
lifeGrid[43][44] = 1
lifeGrid[42][44] = 1
lifeGrid[41][44] = 1 


while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("white")

    getNextStep(lifeGrid)

    pygame.display.flip()

    pygame.time.delay(speed)

    clock.tick(60)

pygame.quit()


'''
    for i in range(size):
        for j in range(size):
            pygame.draw.rect(screen, pygame.Color(255, 255*int(lifeGrid[i][j]), 0, 255), ((j)*boxSize, (i)*boxSize, boxSize, boxSize), border_radius=6)
'''










            
    