import numpy as np
import pygame
import sys
import math

BLUE = (0, 0,255)
RED = (255,0,0)
Black = (0,0,0)
white = (255,255,255)
YELLO = (255,255,0)


ROW_C = 6
COL_C =7

def create():
    bor = np.zeros((ROW_C,COL_C))
    return bor

def dropp( bor, row,selection,piece):
    bor[row][selection] = piece

    


def is_valide(bor, selection):
    return bor[ROW_C-1][selection] == 0

def get_next_open(bor, selection):
    for r in range(ROW_C):
        if bor[r][selection] == 0:
            return r

def pbor(bor):
    print(np.flip(bor, 0))

def winning_move(bor,piece):
    # check all the horigential location
    for c in range(COL_C-3):
        for r in range(ROW_C):
            if bor[r][c] == piece and bor[r][c+1] == piece  and bor[r][c+2] == piece and bor[r][c+3] == piece:
                return True
    # check all the vertical location
    for c in range(COL_C):
        for r in range(ROW_C-3):
            if bor[r][c] == piece and bor[r+1][c] == piece  and bor[r+2][c] == piece and bor[r+3][c] == piece:
                return True
# possitivly sloped sloped digonal
    for c in range(COL_C-3):
        for r in range(ROW_C-3):
            if bor[r][c] == piece and bor[r+1][c+1] == piece  and bor[r+2][c]+2 == piece and bor[r+3][c+3] == piece:
                return True


#check negativly sloped digonal
    for c in range(COL_C-3):
        for r in range(3,ROW_C):
            if bor[r][c] == piece and bor[r-1][c+1] == piece  and bor[r-2][c]+2 == piece and bor[r-3][c+3] == piece:
                return True

def draw_board(bor):
    for c in range(COL_C):
        for r in range(ROW_C):
            pygame.draw.rect( screen,BLUE, (c*SQUARESIZE, r*SQUARESIZE + SQUARESIZE, SQUARESIZE, SQUARESIZE) )
            
            pygame.draw.circle( screen, Black, (int(c*SQUARESIZE + SQUARESIZE/2),int( r*SQUARESIZE + SQUARESIZE + SQUARESIZE/2)),RADIUS)# pygame only accepts int type
    for c in range(COL_C):
        for r in range(ROW_C):       
            if bor[r][c] == 1:
                pygame.draw.circle( screen, RED, (int(c*SQUARESIZE + SQUARESIZE/2),height- int( r*SQUARESIZE  + SQUARESIZE/2)),RADIUS)# pygame only accepts int type
            elif bor[r][c] == 2:
                pygame.draw.circle( screen, YELLO, (int(c*SQUARESIZE + SQUARESIZE/2),height- int( r*SQUARESIZE  + SQUARESIZE/2)),RADIUS)# pygame only accepts int type
    pygame.display.update()



def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

bor = create()

print (pbor(bor))
game_over = False
turn = 0

pygame.init()
SQUARESIZE = 100

width = COL_C * SQUARESIZE
height = (ROW_C +1) * SQUARESIZE

size = (width, height)
RADIUS = int(SQUARESIZE/2 -5)
screen = pygame.display.set_mode(size)
draw_board(bor)
pygame.display.update()

myfont = pygame.font.SysFont("monospace", 75)  

while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEMOTION:
                pygame.draw.rect(screen,Black,(0,0,width,SQUARESIZE))
                posx = event.pos[0]
                if turn == 0:
                    pygame.draw.circle(screen,RED,(posx, int(SQUARESIZE/2)),RADIUS)
                else:
                    pygame.draw.circle(screen,YELLO,(posx, int(SQUARESIZE/2)),RADIUS)
            pygame.display.update()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.draw.rect(screen,Black,(0,0,width,SQUARESIZE))
                #print("")
        
                # #ask1 player to input
                if turn == 0:
                    posx = event.pos[0]
                    selection = int(math.floor(posx/SQUARESIZE))
                    #selection = int(input("player one selecte between 0-6 : "))

                    if is_valide(bor, selection):
                        row = get_next_open(bor, selection)
                        dropp(bor, row, selection,1)
                        if winning_move(bor, 1):
                            lable = myfont.render("Player one won!",1,RED)
                            screen.blit(lable, (40,10))
                            #print("player one won ! congrats")
                            # if winning_move == True:
                            #     screen.fill(Black)
                            #     message("Press ENTER-Play Again or END-Quit", white)
                            #     pg.display.update()
    
                            #     for event in pygame.event.get():
                            #         if event.type == pygame.KEYDOWN:
                            #             game_over = True
                            #         elif event.key == pygame.K_RETURN:   
                            #             replay()
                            game_over = True

                # #ask player to input
                else:
                    posx = event.pos[0]
                    selection = int(math.floor(posx/SQUARESIZE)) 
                    #selection = int(input("player two selecte between 0-6 : "))
                    if is_valide(bor, selection):
                        row = get_next_open(bor, selection)
                        dropp(bor, row, selection,2)
                        if winning_move(bor, 2):
                            lable = myfont.render("Player two won!",2,YELLO)
                            screen.blit(lable, (40,10))
                            #print("player two won ! congrats")
                            # if winning_move == True:
                            #     screen.fill(Black)
                            #     message("Press ENTER-Play Again or END-Quit", white)
                            #     pg.display.update()
    
                            #     for event in pygame.event.get():
                            #         if event.type == pygame.KEYDOWN:
                            #             game_over = True
                            #         elif event.key == pygame.K_RETURN:   
                            #             replay()
                            game_over = True
                    

                pbor(bor)
                draw_board(bor)
                turn += 1
                turn = turn % 2
                if game_over:
                    pygame.time.wait(3000)
    
