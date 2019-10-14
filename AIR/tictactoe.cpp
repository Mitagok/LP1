#include <stdio.h>
#include <stdlib.h>
#include <iostream>

using namespace std;

#define ERROR_COLOR "\033[1;31m"
#define HUMAN_COLOR "\033[1;36m"
#define COMPUTER_COLOR "\033[1;35m"
#define DEFAULT_COLOR "\033[0m"

char HUMAN = 'O';
char COMPUTER = 'X';
char EMPTY = ' ';

int currentCursorRow = 10;

int rowPositions[3] = {4, 6, 8};
int columnPositions[3] = {3, 7, 11};

void changeCursorPosition(int row, int column=0) {
    printf("\033[%d;%dH", row, column);
}

struct Move {
    unsigned short int x = 0;
    unsigned short int y = 0;
};

class Tictactoe {
    char** board;
    int filledBlocks;

public:
    Tictactoe() {
        filledBlocks = 0;
        board = (char**) malloc(3 * sizeof(char*));

        for(int i=0; i<3; i+=1) {
            board[i] = (char*) malloc(3 * sizeof(char));

            for(int j=0; j<3; j+=1) {
                board[i][j] = EMPTY;
            }
        }
    }

    bool checkWin(char player) {
        for(int i=0; i<3; i+=1) {
            if(board[i][0] == player && board[i][1] == player && board[i][2] == player) 
                return true;

            if(board[0][i] == player && board[1][i] == player && board[2][i] == player)
                return true;
        }
        
        if(board[0][0] == player && board[1][1] == player && board[2][2] == player)
            return true;

        if(board[0][2] == player && board[1][1] == player && board[2][0] == player)
            return true;

        return false;
    }

    Move min_max_algorithm() {
        int score = 65535;
        Move move;

        for(int i=0; i<3; i+=1) {
            for(int j=0; j<3; j+=1) {
                if(board[i][j] == EMPTY) {
                    board[i][j] = COMPUTER;

                    int tempScore = maxSearch();

                    if(tempScore < score) {
                        score = tempScore;
                        move.x = i;
                        move.y = j;
                    }

                    board[i][j] = EMPTY;
                }
            }
        }

        return move;
    }

    int maxSearch() {
        if(checkWin(HUMAN)) return 10;
        else if(checkWin(COMPUTER)) return -10;
        else if(filledBlocks==9) return 0;

        int tempScore;
        int score = -65535;
        for(int i=0; i<3; i+=1) {
            for(int j=0; j<3; j+=1) {
                if(board[i][j] == EMPTY) {
                    board[i][j] = HUMAN;
                    tempScore = minSearch();
                    score = (score > tempScore)? score : tempScore;
                    board[i][j] = EMPTY;
                }
            }
        }

        return score;
    }

    int minSearch() {
        if(checkWin(HUMAN)) return 10;
        else if(checkWin(COMPUTER)) return -10;
        else if(filledBlocks==9) return 0;

        int tempScore;
        int score = -65535;
        for(int i=0; i<3; i+=1) {
            for(int j=0; j<3; j+=1) {
                if(board[i][j] == EMPTY) {
                    board[i][j] = HUMAN;
                    tempScore = minSearch();
                    score = (score < tempScore)? score : tempScore;
                    board[i][j] = EMPTY;
                }
            }
        }

        return score;
    }

    void displayBlock(int row, int column, char player) {
        if(player == HUMAN) {
            printf(HUMAN_COLOR);
            printf("\033[%d;%dH%c", rowPositions[row], columnPositions[column], HUMAN);
        }
        else if(player == COMPUTER) {
            printf(COMPUTER_COLOR);
            printf("\033[%d;%dH%c", rowPositions[row], columnPositions[column], COMPUTER);
        }
        changeCursorPosition(currentCursorRow);
        printf(DEFAULT_COLOR);
    }

    void play() {
        bool turn = true;
        bool invalidInput = true;
        bool playOn = true;
        int x, y;
        while(playOn) {
            if(turn) {
                do {
                    printf("Enter your move: : ");
                    scanf("%d %d", &x, &y);
                    if(x < 0 || x > 2 || y < 0 || y > 2 || board[x][y]!=EMPTY) {
                        printf(ERROR_COLOR);
                        printf("Invalid Move\n");
                        printf(DEFAULT_COLOR);
                        invalidInput = true;
                        currentCursorRow += 1;
                    }
                    else
                        invalidInput = false;

                    currentCursorRow += 1;
                }while(invalidInput);

                board[x][y] = HUMAN;
                displayBlock(x, y, HUMAN);

                if(checkWin(HUMAN)) {
                    printf("***** PLAYER WINS *****");
                    playOn = false;
                }
            }
            else {
                Move move = min_max_algorithm();
                printf("Computer plays at (%d, %d)\n", move.x, move.y);
                currentCursorRow += 1;
                board[move.x][move.y] = COMPUTER;
                displayBlock(move.x, move.y, COMPUTER);

                if(checkWin(COMPUTER)) {
                    printf("***** COMPUTER WINS *****");
                    playOn = false;
                }
            }

            if(filledBlocks == 9 && playOn == true) {
                printf("***** GAME TIE *****");
                playOn = false;
            }

            turn = !turn;
        }
        printf("\n");
    }
}game;


int main() {
    // Clear Terminal Screen
    printf("\033[2J\033[1;1H");

    printf("Human : %c\nComputer : %c\n", HUMAN, COMPUTER);
    
    printf("+-----------+\n");
    printf("|   |   |   |\n");
    printf("+-----------+\n");
    printf("|   |   |   |\n");
    printf("+-----------+\n");
    printf("|   |   |   |\n");
    printf("+-----------+\n");
    
    game.play();

    printf(DEFAULT_COLOR);

    return 0;
}
