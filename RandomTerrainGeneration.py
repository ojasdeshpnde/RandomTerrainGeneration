from perlin_noise import PerlinNoise
import matplotlib.pyplot as plt
import random
import pygame

rightCount = 0
downCount = 0

def exploreRight():
    global rightCount
    pic2 = [noise([1+rightCount/xpix, i/ypix]) for i in range(ypix)]
    rightCount = rightCount +1
    del pic[0]
    pic.append(pic2)
    paint()

def exploreDown():
    global downCount
    pic2 = [noise([i/xpix, 1+downCount/ypix]) for i in range(ypix)]
    downCount = downCount +1
    for i in range(xpix):
        pic[i].append(pic2[i])
        del pic[i][0]
    paint()


def paint():
    for i in range(0, xpix):
        for j in range(0, ypix):
            if (pic[i][j] < waterElement):
                pygame.draw.rect(screen, BLUE, (i * pixelSize, j * pixelSize, pixelSize, pixelSize))
            elif (pic[i][j] < sandElement):
                pygame.draw.rect(screen, SAND, (i * pixelSize, j * pixelSize, pixelSize, pixelSize))
            else:
                pygame.draw.rect(screen, GREEN, (i * pixelSize, j * pixelSize, pixelSize, pixelSize))

    pygame.display.flip()


BLUE = (0,0,255)
SAND = (194,178,128)
GREEN = (0,128,0)

pygame.init()
screen = pygame.display.set_mode([1000,1000])

pixelSize = 10

noise = PerlinNoise(octaves=4, seed = random.randint(1,1000))
xpix, ypix = 100, 100
pic = [[noise([i/xpix, j/ypix]) for j in range(xpix)] for i in range(ypix)]
picList = [item for sublist in pic for item in sublist]
picList.sort()


waterElement = picList[int(xpix * ypix * 0.6)]
sandElement = picList[int(xpix * ypix * 0.8)]

paint()
run = True

while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run =False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        exploreRight()
    if keys[pygame.K_DOWN]:
        exploreDown()