import random, pygame, sys
from pygame.locals import *
pygame.init()

black = (255,255,255)
yellow = (200,200,50)
grey = (150, 150, 150)
white = (0,0,0)
green=(0,205,0)
lightGreen=(153,255,204)
whiteGreen = (50, 50, 50)









font = pygame.font.SysFont("Helvetica neue", 40)
bigFont = pygame.font.SysFont("Helvetica neue", 80)
smallFont = pygame.font.SysFont("Helvetica neue", 30)

youWin = bigFont.render("You Win!",       True, lightGreen)
youLose = bigFont.render("You Lose!",     True, lightGreen)
playAgain = smallFont.render("Press Tab to Restart", True, whiteGreen)






def checkGuess(turns, word, userGuess, window):
    renderList = ["","","","",""]
    spacing =0
    guessColourCode = [grey,grey,grey,grey,grey]

    window.fill(black, (0, 80, 600, 100))

    for x in range(0,5):
        if userGuess[x] in word:
            guessColourCode[x] = yellow

        if word[x] == userGuess[x]:
            guessColourCode[x] = green

    list(userGuess)

    for x in range(0,5): #handles the coloring stuff?
        renderList[x] = font.render(userGuess[x], True, black)
        pygame.draw.rect(window, guessColourCode[x], pygame.Rect(115 +spacing, 204+ (turns*60), 41, 41)) #pygame.Rect(60 +spacing, 50+ (turns*80), 50, 50))
        window.blit(renderList[x], (126 + spacing, 213 + (turns*60))) #window.blit(renderList[x], (70 + spacing, 50 + (turns*80))) s[acing += 80
        spacing+=55
#110 + (x * 55), 200 + (y * 60), 50, 50), 2)
    if guessColourCode == [green,green,green,green,green]:
        return True



def main():
    game()
    screen = pygame.display.set_mode((600, 800))
    logo = pygame.image.load("jordle.png").convert()
    n_logo = pygame.transform.scale(logo, (300, 150))
    screen.blit(n_logo, (150, 150))
    #pygame.display.flip()
    pygame.display.update()




def game():
    file = open("wordList.txt", "r")
    wordList = file.readlines()  # creates list that contains each line of the text file as an element?
    word = wordList[
        random.randint(0, len(wordList) - 1)].upper()  # holds randomly selected word in the text file in all uppercase?

    height = 600
    width = 500

    FPS = 30
    clock = pygame.time.Clock()

    window = pygame.display.set_mode((width, height))  # does this create the render window?
    window.fill(black)  # fills surface with a solid color?

    guess = ""

    print(word)

    for x in range(0, 5):  # wat is purpose of other draw lines?
        for y in range(0, 5):
            pygame.draw.rect(window, grey, pygame.Rect(110 + (x * 55), 200 + (y * 60), 50, 50), 2)

    pygame.display.set_caption("Wordle!")
    window.blit(playAgain, (140, 520))

    turns = 0
    win = False

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:  # closes window when X clicked
                pygame.exit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                guess += event.unicode.upper()

                if event.key == K_RETURN and win == True:
                    main()

                if event.key == K_RETURN and turns == 6:
                    main()

                if event.key == pygame.K_BACKSPACE or len(guess) > 5:
                    guess = guess[:-1]

                if event.key == K_RETURN and len(guess) > 4:
                    win = checkGuess(turns, word, guess, window)
                    turns += 1
                    guess = ""
                    window.fill(black, (0,600, 600, 200))

                if event.key == K_TAB:
                    game()

                if event.key == K_BACKSPACE:
                    guess=""
                    window.fill(black, (0, 80, 600, 100))

        window.fill(black, (0, 600, 600, 200))
        renderGuess = font.render(guess, True, (70, 70, 70))
        window.blit(renderGuess, (200, 140))


        if win == True:
            window.blit(youWin, (90, 200))


        if turns == 6 and win != True:
            window.blit(youLose, (90, 200))
            window.blit(playAgain, (60, 500))
            # screen.blit(text, (width / 2 + 50, height / 2))
        pygame.display.update()
        clock.tick(FPS)



main()














    

                

    

