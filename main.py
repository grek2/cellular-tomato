import pygame
import time

# pygame setup
pygame.init()
pygame.display.set_caption("Sporesdale Bioraiders")
windowSize = 600
boxSize = int(windowSize/24)
screen = pygame.display.set_mode((windowSize, windowSize))
clock = pygame.time.Clock()
running = True
lifeArray = []
x = 0
y = 0


def checkCells():
    naybors = 0 #i dont have time to spell shit correctly
    for c in range(-1, 2, 1):
        for d in range(-1, 2, 1):
            if int(c) != 0 or int(d) != 0:
                try:
                    #i have no idea what is going on help me
                        nayborsAdd = int(lifeArray[int(x/boxSize)+d][int(y/boxSize)+c])
                        #print("yes", c, d)
                        #print("Checking cell", lifeArray[int(x/boxSize)][int(y/boxSize)])
                        #print(nayborsAdd)
                        #print("coords: ", x/boxSize, y/boxSize)
                except IndexError:
                    check = 0
                #print("Index error")
            naybors += nayborsAdd
    #print("Neighbors ", naybors)
    return int(naybors)
    

for b in range(25):
    lifeArray.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    #lifeArray.append([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])

#lifeArray[0][0] = 1
lifeArray[5][1] = 1
lifeArray[6][0] = 1
lifeArray[6][1] = 1
lifeArray[7][2] = 1



while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")
    
    #lifeArray[0][23] = "blue"

    # RENDER YOUR GAME HERE


    for x in range(0, 600, boxSize):
        for y in range(0, 600, boxSize):
            #if lifeArray[int(x/boxSize)][int(y/boxSize)] != 0:
                 #pygame.draw.rect(screen, pygame.Color(lifeArray[int(x/boxSize)][int(y/boxSize)]), (y, x, boxSize, boxSize), border_radius=0)
            
            if int(lifeArray[int(x/boxSize)][int(y/boxSize)]) == 1:
                pygame.draw.rect(screen, pygame.Color(255, 0, 0, 255), (y, x, boxSize, boxSize), border_radius=0)
                if checkCells() > 3 or checkCells() < 2:
                    lifeArray[int(x/boxSize)][int(y/boxSize)] = 0 #-1
                    print(lifeArray[int(x/boxSize)][int(y/boxSize)], " is dead")
            else:
                pygame.draw.rect(screen, pygame.Color(255, 255, 255, 255), (y, x, boxSize, boxSize), border_radius=0)
                if checkCells() == 3:
                    lifeArray[int(x/boxSize)][int(y/boxSize)] = 1 #2
                    print(lifeArray[int(x/boxSize)][int(y/boxSize)], " is live")


    for x in range(0, 600, boxSize):
        for y in range(0, 600, boxSize):
            if int(lifeArray[int(x/boxSize)][int(y/boxSize)]) == -1:
                #lifeArray[int(x/boxSize)][int(y/boxSize)] = 0
                eeee = 0

            elif int(lifeArray[int(x/boxSize)][int(y/boxSize)]) == 2:
                #lifeArray[int(x/boxSize)][int(y/boxSize)] = 1
                eeee = 1

            else:
                #print("cell stays same", lifeArray[int(x/boxSize)][int(y/boxSize)])
                eeee = 2
                

    
    pygame.display.flip()

    pygame.time.delay(500)

    clock.tick(60)

pygame.quit()