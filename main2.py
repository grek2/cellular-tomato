import pygame
import time

size = 25

pygame.init()
pygame.display.set_caption("Sporesdale Bioraiders")
windowSize = 600
boxSize = int(windowSize/(size-1))
screen = pygame.display.set_mode((windowSize, windowSize))
clock = pygame.time.Clock()
running = True
lifeArray = []


#creates array
for b in range(25):
    #lifeArray.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    lifeArray.append([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])

"""
for i in range(1, size-2, 1):
    for j in range(1, size-2, 1):
        lifeArray[j][i] = 0
"""

#adds stuff  

lifeArray[6][6] = 1
lifeArray[6][7] = 1
lifeArray[6][8] = 1


#check how many neighbors
def checkCells(xCheck, yCheck):
    naybors = 0
    #nayborsAdd = 0
    for x in range(-1, 2, 1):
        for y in range(-1, 2, 1):
            if not(x == 0 and y == 0):
                #print(yCheck)
                #print("\n")
                #print(yCheck+y)
                if (lifeArray[yCheck+y][xCheck+x] == 1):
                    naybors = naybors + 1
                       
    return naybors


while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("white")
    
    for s in range(1):
        for j in range(1, size-2, 1):
            for i in range(1, size-2, 1):
                #print("\r", lifeArray[j][i])
                #pygame.draw.rect(screen, pygame.Color(j*5, 255*int(lifeArray[j][i]), 100*int(lifeArray[j][i])+i*5, 255), ((j-1)*boxSize, (i-1)*boxSize, boxSize, boxSize), border_radius=0)
                pygame.draw.rect(screen, pygame.Color(checkCells(i, j)*30, 255*int(lifeArray[j][i]), 0, 255), ((j-1)*boxSize, (i-1)*boxSize, boxSize, boxSize), border_radius=0)
                if (lifeArray[j][i] == 1):
                    if ((checkCells(j, i) > 3) or (checkCells(j, i) < 2)):
                        lifeArray[j][i] = -1
                        
                    
                
                if (lifeArray[j][i] == 0):
                    if (checkCells(j, i) == 3):
                        lifeArray[j][i] = 2
                    
                                          
            #print("\n")
            #print(lifeArray)
        
        #sets stuff
        for i in range(1, size-2, 1):
            for j in range(1, size-2, 1):
                if (lifeArray[j][i] == -1):
                    lifeArray[j][i] = 0
                
                if (lifeArray[j][i] == 2):
                    lifeArray[j][i] = 1


    #didnt work, dont uncommnet this v
    """
    for x in range(1, size, 1):
        for y in range(1, size, 1):
            #if lifeArray[int(x/boxSize)][int(y/boxSize)] != 0:
                 #pygame.draw.rect(screen, pygame.Color(lifeArray[int(x/boxSize)][int(y/boxSize)]), (y, x, boxSize, boxSize), border_radius=0)
            
            if int(lifeArray[x][y]) == 1:
                pygame.draw.rect(screen, pygame.Color(255, 0, 0, 255), (y*boxSize, x*boxSize, boxSize, boxSize), border_radius=0)
                if checkCells(y, x) > 3 or checkCells(y, x) < 2:
                    lifeArray[x][y] = -1
                    print(lifeArray[x][y], " is dead")
            else:
                pygame.draw.rect(screen, pygame.Color(255, 255, 255, 255), (y*boxSize, x*boxSize, boxSize, boxSize), border_radius=0)
                if checkCells(y, x) == 3:
                    lifeArray[x][y] = 2
                    print(lifeArray[x][y], " is live")


    for x in range(1, size, 1):
        for y in range(1, size, 1):
            if int(lifeArray[x][y]) == -1:
                lifeArray[x][y] = 0
                #eeee = 0

            elif int(lifeArray[x][y]) == 2:
                lifeArray[x][y] = 1
                #eeee = 1
    """


    pygame.display.flip()

    pygame.time.delay(500)

    clock.tick(60)

pygame.quit()

