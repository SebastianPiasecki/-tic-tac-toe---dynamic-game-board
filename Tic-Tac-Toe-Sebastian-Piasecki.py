import math

MARKER_X = 'X'
MARKER_O = 'O'
MARKER_BLANK = '-'
SIZE_BORDER = 3
SIZE_WIN = 3


def show_border(border: list) -> None:
    for line in border:
        print(*line)


border = [[MARKER_BLANK for j in range(SIZE_BORDER)] \
    for i in range(SIZE_BORDER)]


position = [MARKER_BLANK for i in range(SIZE_BORDER**2)]


def make_move(marker):
    check_input = False
    while not check_input:
        try:
            pole = int(input(f'Gdzie postawić {marker}: '))
            if pole >= 1 and pole <= SIZE_BORDER**2:
                x, y = -1, -1
                x = math.ceil(pole/SIZE_BORDER) - 1
                y = pole - (x*SIZE_BORDER) - 1
                if border[x][y] == MARKER_BLANK:
                    border[x][y] = marker
                    return
                else:
                    print("To pole nie jest puste.")
            else:
                print("Wprowadziles miejsce spoza zakresu.")
        except ValueError:
            print("Wprowadziles nieprawidlowe dane.\n")


def check_win(marker):
    neighbours = (
        ((0, -1), (0, 1)),
        ((-1, 0), (1, 0)),
        ((-1, -1), (1, 1)),
        ((-1, 1), (1, -1)),
    )
    for i in range(SIZE_BORDER):
        for j in range(SIZE_BORDER):
            pole = border[i][j]
            if pole == MARKER_BLANK:
                continue
            for n in neighbours:
                ile_sasiadow_takich_samych = 0
                for sasiedztwo in n:
                    if i + sasiedztwo[0] >= 0 and i + sasiedztwo[0] < SIZE_BORDER and j + sasiedztwo[1] >= 0 and j + sasiedztwo[1] < SIZE_BORDER and \
                        i + sasiedztwo[0] >= 0 and i + sasiedztwo[0] < SIZE_BORDER and j + sasiedztwo[1] >= 0 and j + sasiedztwo[1] < SIZE_BORDER:
                        if pole == border[i + sasiedztwo[0]][j + sasiedztwo[1]] and pole == border[i + sasiedztwo[0]][j + sasiedztwo[1]]:
                            ile_sasiadow_takich_samych += 1
                if ile_sasiadow_takich_samych == 2:
                    return True
    return False               

    #         if i-1 >= 0 and i+1 < SIZE_BORDER and j-1 >= 0 and j+1 < SIZE_BORDER:
    #             if border[i][j] == border[i][j+1] and border[i][j] == border[i][j-1] \
    #             or border[i][j] == border[i+1][j] and border[i][j] == border[i-1][j] \
    #             or border[i][j] == border[i+1][j+1] and border[i][j] == border[i-1][j-1] \
    #             or border[i][j] == border[i+1][j-1] and border[i][j] == border[i-1][j+1]  :
    #                 if border[i][j] != MARKER_BLANK:
    #                     return True
    # return False 
    

def gra():
    marker = MARKER_X
    czy_koniec_gry = False
    
    while not czy_koniec_gry:
        make_move(marker)
        show_border(border)
        czy_koniec_gry = check_win(marker)
        if marker == MARKER_X and not czy_koniec_gry:
            marker = MARKER_O
        elif marker == MARKER_O and not czy_koniec_gry:
            marker = MARKER_X    
        else:            
            print(f"Wygral gracz ze markerem {marker}")

gra()