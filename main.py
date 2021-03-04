import os
import sys
import pygame
from pygame.locals import *
import random
FPS=32
screenH = 511
screenW = 289
SCREEN = pygame.display.set_mode((screenW,screenH))
groundY = screenH*0.8
SPRITES = {}
SOUNDS = {}
playerPath = os.path.join("sprites","redbird-upflap.png")
bgPath = os.path.join("sprites","background-day.png")
pipePath = os.path.join("sprites","pipe-green.png")
# print(pipePath)
def genPipe():
    pipeH = SPRITES['pipes'][0].get_height()
    offset = screenH/3
    y2 = offset + random.randrange(0,int(screenH-SPRITES['base'].get_height() -1.2*offset))
    x = screenW+10
    y1=pipeH - y2 + offset
    pipe = [
        {'x': x , 'y' : -y1},
        {'x' : x, 'y' : y2}
    ]
    return pipe
    pass
def welcomeScreen():
    xPlayer = int(screenW/5)
    yPlayer = int(screenH - SPRITES['player'].get_height())/2
    xmessage = int(screenW - SPRITES['message'].get_width())/2
    yMessage = int(screenH*0.13)
    basex=0
    while True:
        for event in pygame.event.get():
            if event.type== QUIT or (event.type==KEYDOWN and event.key== K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type==KEYDOWN and(event.key==K_SPACE or event.key==K_UP):
                return
            else:
                SCREEN.blit(SPRITES['background'], (0, 0))
                SCREEN.blit(SPRITES['player'],(xPlayer,yPlayer))
                SCREEN.blit(SPRITES['message'],(xmessage,yMessage))
                SCREEN.blit(SPRITES['base'], (basex, groundY))

                pygame.display.update()
                FPSCLOCK.tick(FPS)

    pass

def startGame():
    score=0
    xPlayer = int(screenW / 5)
    yPlayer = int(screenW/2)
    pipes1 = genPipe()
    pipes2 = genPipe()
    upperPipes = [
        {'x' : screenW + 200 , 'y' : pipes1[0]['y']},
        {'x': screenW + 200 + screenW/2, 'y': pipes2[0]['y']},
        ]
    lowerPipes = [
        {'x': screenW + 200, 'y': pipes1[1]['y']},
        {'x': screenW + 200 + screenW/2, 'y': pipes2[1]['y']},
    ]
    pipeVelx = -4
    playerVelY = -9
    playerMaxVelY = 10
    playerMinVelY=-9
    playerAccY = 1
    playerFlapAccv = -8
    playerFlapped = False


    while True:
        for event in pygame.event.get():
            if event.type== QUIT or (event.type==KEYDOWN and event.key== K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type==KEYDOWN and(event.key==K_SPACE or event.key==K_UP):
                return



if __name__ == '__main__':
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    pygame.display.set_caption("Flappy Bird By Pranav Singhal",playerPath)
    SPRITES['numbers']=(
        pygame.image.load(os.path.join("sprites","0.png")).convert_alpha(),
        pygame.image.load(os.path.join("sprites", "1.png")).convert_alpha(),
        pygame.image.load(os.path.join("sprites", "2.png")).convert_alpha(),
        pygame.image.load(os.path.join("sprites", "3.png")).convert_alpha(),
        pygame.image.load(os.path.join("sprites", "4.png")).convert_alpha(),
        pygame.image.load(os.path.join("sprites", "5.png")).convert_alpha(),
        pygame.image.load(os.path.join("sprites", "6.png")).convert_alpha(),
        pygame.image.load(os.path.join("sprites", "7.png")).convert_alpha(),
        pygame.image.load(os.path.join("sprites", "8.png")).convert_alpha(),
        pygame.image.load(os.path.join("sprites", "9.png")).convert_alpha()
    )
    SPRITES['message']=pygame.image.load(os.path.join("sprites","message.png")).convert_alpha()
    SPRITES['base']=pygame.image.load(os.path.join("sprites","base.png")).convert_alpha()
    SPRITES['pipes']=(
        pygame.transform.rotate(pygame.image.load(pipePath).convert_alpha(),180),
        pygame.image.load(pipePath).convert_alpha()
    )
    SPRITES['background']=pygame.image.load(bgPath).convert()
    SPRITES['player']=pygame.image.load(playerPath).convert_alpha()
    SOUNDS['hit']=pygame.mixer.Sound(os.path.join("audio","hit.wav"))
    SOUNDS['die'] = pygame.mixer.Sound(os.path.join("audio", "die.wav"))
    SOUNDS['swoosh'] = pygame.mixer.Sound(os.path.join("audio", "swoosh.wav"))
    SOUNDS['wing'] = pygame.mixer.Sound(os.path.join("audio", "wing.wav"))
    SOUNDS['point'] = pygame.mixer.Sound(os.path.join("audio", "point.wav"))
    while True:
        welcomeScreen()
        startGame()
    pass
