#include <stdio.h>
#include <stdlib.h>

int boxSize = 25;
int lifeArray[13][13];

int checkCells();

int** createGrid(int size1, int size2) {
    int** matrix = (int**)malloc(size1 * sizeof(int*));

    if (matrix == NULL) {
        printf("what the frisk\n");
        exit(1);
    }

    for (int i = 0; i < size1; i++) {  
        matrix[i] = 0;   
    }

    return matrix;
}

void freeMatrix(int** matrix, int size) {
    for (int i = 0; i < size; i++) {
        free(matrix[i]);
    }
    free(matrix);
}

int main() {
    int size = 13;
    int** lifeArray = createGrid(size, size);

    for (int i = 1; i < 13; i++) {
        for (int j = 1; j < 13; j++){
            lifeArray[j][i] = 0;
        }
    }
    //printf("grid cleared\n");

    //change stuff here
    lifeArray[1][2] = 1;
    lifeArray[2][1] = 1;
    lifeArray[2][2] = 1;
    //lifeArray[5][8] = 1;
    for (int s = 0; s < 4; s++) {
        for (int i = 1; i < 13; i++) {
            for (int j = 1; j < 13; j++){
                printf("%d", lifeArray[j][i]);
                if (lifeArray[j][i] == 1) {
                    if ((checkCells(i, j) > 3) || (checkCells(i, j) < 2)) {
                        lifeArray[j][i] = -1;
                        //printf("\nthis cell is dying\n");
                        //printf("%d", checkCells());
                    }
                }
                if (lifeArray[j][i] == 0) {
                    if (checkCells(i, j) == 3) {
                        lifeArray[j][i] = 2;
                        //printf("\nthis cell is growing\n");
                        //printf("%d", checkCells());
                    }
                
                }
            }
            printf("\n");
        }
        printf("\n\n");
        for (int i = 1; i < 13; i++) {
            for (int j = 1; j < 13; j++){
                if (lifeArray[j][i] == -1) {
                    lifeArray[j][i] = 0;
                }
                if (lifeArray[j][i] == 2) {
                    lifeArray[j][i] = 1;
                }
    
            }
    
        }
    }
    freeMatrix(lifeArray, size);
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



