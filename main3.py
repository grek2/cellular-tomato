import pygame

size = 24

pygame.init()
pygame.display.set_caption("Sporesdale Bioraiders")
windowSize = 600
boxSize = int(windowSize/(size-1))
screen = pygame.display.set_mode((windowSize, windowSize))
clock = pygame.time.Clock()
running = True

def getNextStep(lifeGrid):
    a, b = len(lifeGrid), len(lifeGrid[0])

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]

    for i in range(a):
        for j in range(b):
            liveNbrs = 0

            for dirX, dirY in directions:
                x, y = i + dirX, j + dirY

                if 0 <= x < a and 0 <= y < b and (lifeGrid[x][y] == 1):
                    liveNbrs += 1


            if lifeGrid[i][j] == 1 and (liveNbrs < 2 or liveNbrs > 3):
                lifeGrid[i][j] = 3

            elif lifeGrid[i][j] == 0 and liveNbrs == 3:
                lifeGrid[i][j] = 2
            
    for i in range(a):
        for j in range(b):
                    
            if lifeGrid[i][j] == 3:
                lifeGrid[i][j] = 0
            elif lifeGrid[i][j] == 2:
                lifeGrid[i][j] = 1

            print(lifeGrid[i][j], end=" ")
        print()


lifeGrid = []
for c in range(size):
    die = []
    for d in range(size):
        die.append(0)
    lifeGrid.append(die)


#lifeGrid[1][1] = 1
lifeGrid[12][12] = 1
lifeGrid[12][13] = 1
lifeGrid[13][13] = 1


while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("white")
    
       


    pygame.display.flip()

    pygame.time.delay(500)

    clock.tick(60)

pygame.quit()










            
    