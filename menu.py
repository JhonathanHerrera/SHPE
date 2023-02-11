import pygame
import sys
pygame.init()
from constants import *

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


#def draw_text(text,font,text_col,x,y):
    #new = font.render(text, True, text_col)
    #screen.blit(new,(x,y))

pygame.display.set_caption("Jordle")


def make_screen():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    logo_img = pygame.image.load("jordle.png").convert()
    new_logo = pygame.transform.scale(logo_img, (300, 150))
    bg_img = pygame.image.load("backgroundnew.jpg").convert()
    new_bg = pygame.transform.scale(bg_img, (700, 800))
    screen.blit(new_bg, (0, 0))

    start_img = pygame.image.load("start.png").convert()
    exit_img = pygame.image.load("quit.png").convert()
    new_start = pygame.transform.scale(start_img, (200, 100))
    new_exit = pygame.transform.scale(exit_img, (200, 100))
    screen.blit(new_start, (195, 500))
    screen.blit(new_exit, (195, 600))
    screen.blit(new_logo, (150, 150))

    pygame.display.flip()
    font = pygame.font.SysFont("arialblack", 40)
run = True
change = False
done = False
WIDTH = 600
HEIGHT = 800
font = pygame.font.SysFont("arialblack",40)
font_two = pygame.font.SysFont("arialblack",20)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
logo_img = pygame.image.load("jordle.png").convert()
new_logo = pygame.transform.scale(logo_img, (300, 150))
bg_img = pygame.image.load("backgroundnew.jpg").convert()
new_bg = pygame.transform.scale(bg_img, (700, 800))
screen.blit(new_bg, (0, 0))


start_img = pygame.image.load("start.png").convert()
exit_img = pygame.image.load("quit.png").convert()
new_start = pygame.transform.scale(start_img, (200, 100))
new_exit = pygame.transform.scale(exit_img, (200, 100))
screen.blit(new_start, (195, 500))
screen.blit(new_exit, (195, 600))
screen.blit(new_logo, (150, 150))
start_surface = font_two.render("Press (space) To Start!", 0, LINE_COLOR)
start_rectangle = start_surface.get_rect(center=(WIDTH // 2,
                                                    HEIGHT - 190))
screen.blit(start_surface, start_rectangle)
end_surface = font_two.render("Press (Q) To Exit!", 0, LINE_COLOR)
end_rectangle = end_surface.get_rect(center=(WIDTH // 2,
                                                    HEIGHT - 110))
screen.blit(end_surface, end_rectangle)
pygame.display.flip()

while run:
    WIDTH = 600
    HEIGHT = 800

    if change == True:
        #print("STOP")

        game = pygame.display.set_mode((WIDTH, HEIGHT))
        #game.blit(new_bg, (0, 0))
        game.fill(BG_COLOR) #from the constants file
        print("g")
        change_surface = font.render("*INSERT GAME HERE*", 0, LINE_COLOR)
        change_rectangle = change_surface.get_rect(center=(WIDTH // 2,
                                                         HEIGHT // 2 - 160))
        screen.blit(change_surface, change_rectangle)
        change = False

    elif done == True:
        gone = pygame.display.set_mode((WIDTH, HEIGHT))
        gone.fill(BG_COLOR)
        print("BYE")
        bye_surface = font.render("THANK YOU FOR PLAYING!", 0, LINE_COLOR)
        bye_rectangle = bye_surface.get_rect(center=(WIDTH // 2,
                                                           HEIGHT // 2 - 160))
        screen.blit(bye_surface, bye_rectangle)
        #byebye_surface = font.render("Press Q Again To Exit", 0, LINE_COLOR)
        #byebye_rectangle = byebye_surface.get_rect(center=(WIDTH // 2,
                                                     #HEIGHT // 2 - 100))
        #screen.blit(byebye_surface, byebye_rectangle)
        done = False
        #pygame.quit()
        #if event.type == pygame.KEYDOWN:
        #if event.key == pygame.k_q:
            #pygame.quit()



    #else:

        #make_screen()
    #change = False

    #else:
        #break
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                change = True
                #pygame.display.update()
            elif event.key == pygame.K_q:
                #pygame.quit()
                done = True
            else:
                change = False
        if event.type == pygame.QUIT:
            run = False
            print("QUIT")

    pygame.display.update()
pygame.quit()