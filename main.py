import pygame
import time

size = 13

pygame.init()
pygame.display.set_caption("Sporesdale Bioraiders")
windowSize = 600
boxSize = int(windowSize/(size-1))
screen = pygame.display.set_mode((windowSize, windowSize))
clock = pygame.time.Clock()
running = True
lifeArray = []

for b in range(25):
    lifeArray.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    #lifeArray.append([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])


def checkCells(xCheck, yCheck):
    naybors = 0
    #nayborsAdd = 0
    for y in range(-1, 3, 1):
        for x in range(-1, 3, 1):
            if (x != 0 or y != 0):
                if (lifeArray[yCheck+x][xCheck+y] == 2 or lifeArray[yCheck+x][xCheck+y] == 1):
                    naybors = naybors + 1
                       
    return naybors


while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("black")


    # i'll pythonify this later
    '''
    for (int i = 1; i < size; i++) {
        for (int j = 1; j < size; j++){
            lifeArray[j][i] = 0;
        }
    }
    //printf("grid cleared\n");

    //change stuff here
    lifeArray[5][5] = 1;
    //lifeArray[2][1] = 1;
    //lifeArray[2][2] = 1;
    //lifeArray[5][8] = 1;
    for (int s = 0; s < 10; s++) {
        for (int i = 1; i < size; i++) {
            for (int j = 1; j < size; j++){
                printf("%d", lifeArray[j][i]);
                if (lifeArray[j][i] == 1) {
                    if ((checkCells(j, i) > 3) || (checkCells(j, i) < 2)) {
                        lifeArray[j][i] = -1;
                        //printf("\nthis cell is dying\n");
                        //printf("%d", checkCells());
                    }
                }
                if (lifeArray[j][i] == 0) {
                    if (checkCells(j, i) == 3) {
                        lifeArray[j][i] = 2;
                        //printf("\nthis cell is growing\n");
                        //printf("%d", checkCells());
                    }
                
                }
            }
            printf("\n");
        }
        printf("\n\n");
        for (int i = 1; i < size; i++) {
            for (int j = 1; j < size; j++){
                if (lifeArray[j][i] == -1) {
                    lifeArray[j][i] = 0;
                }
                if (lifeArray[j][i] == 2) {
                    lifeArray[j][i] = 1;


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

