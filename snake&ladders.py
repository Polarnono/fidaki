import pygame
import sys


pygame.init()

#screen size
size_x = 800
size_y = 800
screen = pygame.display.set_mode((size_x,size_y))

tile_size = 80

#colors
BG = (225,225,225)
YELLOW = (255,255,0)
RED = (255,0,0)
BLACK=(0,0,0)

#dictionaries
snakes = {97:78,95:56,88:24,63:18,36:6,48:26,32:10}
ladder = {1:38,4:14,8:30,21:42,28:76,71:92,86:99}

#Draws red background every odd number (called before the number is drawn on the grid)
def draw_bg_grid(x,y):
    pygame.draw.rect(screen,RED,(x,y,tile_size,tile_size))

def find_pos(tile_number):
    row=(100-tile_number)//10
    col=(tile_number-1)%10
    y=row*80+40
    if (row%2 == 0):
        x =(9-col)*80+40
    else:
        x=col*80+40
    return(x,y)

def draw_num(tile_size):
    font = pygame.font.Font(None,36)

#Making the numbers go in a Zig-Zag Pattern. Explanation: Splitting the rows in even and odds and then applying the equation (removing from the 100 due to 0 being the top left corner): (100 - [the number of the row]*10).
#Then based on the direction we want to go we remove simply the col_indx if we want left to right or reverse it by doing 9-col_indx. 

    for y in range (0, size_y, tile_size):
        row_indx=(y//80)
        if (y//80) % 2 == 0:
            for x in range(0, size_x, tile_size):
                col_indx=(x//80)
                number=100-(row_indx*10)-col_indx
                if (number%2)!=0: 
                    draw_bg_grid(x,y)
                txt_img= font.render(str(number),True,BLACK)
                text_rect= txt_img.get_rect()
                text_rect.center = (x+40,y+40)
                screen.blit(txt_img,text_rect)
        else:
            for x in range(0,size_x,tile_size):
                col_indx=(x//80)
                number=100-(row_indx*10)-(9-col_indx)
                if (number%2)!=0: 
                    draw_bg_grid(x,y)
                txt_img= font.render(str(number),True,BLACK)
                text_rect= txt_img.get_rect()
                text_rect.center = (x+40,y+40)
                screen.blit(txt_img,text_rect)


def draw_grid(tile_size):
    screen.fill(BG)

    #draws vertical lines
    for x in range(tile_size, size_x, tile_size):
        pygame.draw.line(screen,YELLOW,(x,0),(x,size_y))

    #draw horizontal lines
    for y in range(tile_size, size_y, tile_size):
        pygame.draw.line(screen,YELLOW, (0,y), (size_x,y))



run = True ;

#MAIN LOOP
while ( run == True):

    print("p[os]",find_pos(42))

    draw_grid(tile_size)

    draw_num(tile_size)
    
    for event in pygame.event.get() :
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_ESCAPE:
                run = False



    pygame.display.update()
    