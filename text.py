import pygame
import speech_recognition as sr

pygame.init()

display_width = 800
display_height = 600

black = (0, 0, 0)
alpha = (0, 90, 255)
white = (255, 255, 255)
red = (200, 0, 0)
green = (0, 200, 0)
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('GUI Speech Recognition')

gameDisplay.fill(white)
Img = pygame.image.load('Gallery Extra 2.jpg')
gameDisplay.blit(Img, (0, 1))


def close():
    pygame.quit()
    quit()


def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 30)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()


def text_objects(text, font):
    textSurface = font.render(text, True, alpha)
    return textSurface, textSurface.get_rect()


def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))

        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))

    smallText = pygame.font.SysFont("comicsansms", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x + (w / 2)), (y + (h / 2)))
    gameDisplay.blit(textSurf, textRect)


def logic():
    gameDisplay.blit(Img, (0, 0))
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print(' ')
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio)
            print(text)
            message_display(text+'.')
        except:
            message_display("Sorry, I could not recognize what you said.")

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        button("Speak!", 150, 450, 100, 50, green, bright_green, logic)
        button("Quit", 550, 450, 100, 50, red, bright_red, close)
        pygame.display.update()


if __name__ == '__main__':
    main()

