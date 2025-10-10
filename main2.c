#include <stdio.h>
#include <stdlib.h>

int boxSize = 25;
int size = 13;
int lifeArray[13][13];
int checkCells();


int main() {

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
                }
    
            }
    
        }
    }
}

int checkCells(int xCheck, int yCheck) {
    int naybors = 0;
    //int nayborsAdd = 0;
    for (int y = -1; y < 3; y++) {
        for (int x = -1; x < 3; x++) {
            if (x != 0 || y != 0) {
                if (lifeArray[yCheck+x][xCheck+y] == 2 || lifeArray[yCheck+x][xCheck+y] == 1) {
                    naybors++;
                    //printf("%d\n", xCheck);
                    //printf("found a neighbor"); 
                }
            }
        }
    }
    return naybors;
}



