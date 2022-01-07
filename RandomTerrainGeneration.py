from perlin_noise import PerlinNoise
import matplotlib.pyplot as plt
import random
import pygame

rightCount = 0
downCount = 0

def exploreRight():
    global rightCount
    pic2 = [noise([1+rightCount/xpix, (i + downCount)/ypix]) for i in range(ypix)]
    rightCount = rightCount +1
    pic.append(pic2)
    del pic[0]
    #paint()

def exploreDown():
    global downCount
    pic2 = [noise([(i + rightCount)/xpix, 1+downCount/ypix]) for i in range(ypix)]
    downCount = downCount +1
    for i in range(xpix):
        pic[i].append(pic2[i])
        del pic[i][0]
    #paint()

def exploreUp():
    global downCount
    pic2 = [noise([(i + rightCount) / xpix, downCount / ypix]) for i in range(ypix)]
    downCount = downCount -1
    for i in range(xpix):
        pic[i].insert(0,pic2[i])
        del pic[i][xpix]
    #paint()

def exploreLeft():
    global rightCount
    pic2 = [noise([rightCount / xpix, (i + downCount) / ypix]) for i in range(ypix)]
    rightCount = rightCount - 1
    pic.insert(0,pic2)
    del pic[ypix]
    #paint()

def paint():
    for i in range(0, xpix):
        for j in range(0, ypix):
            if (pic[i][j] < waterElement):
                pygame.draw.rect(screen, BLUE, ((i-0) * pixelSize, (j-0) * pixelSize, pixelSize, pixelSize))
            elif (pic[i][j] < sandElement):
                pygame.draw.rect(screen, SAND, ((i-0) * pixelSize, (j-0) * pixelSize, pixelSize, pixelSize))
            elif (pic[i][j] < greenElement):
                pygame.draw.rect(screen, GREEN, ((i-0) * pixelSize, (j-0) * pixelSize, pixelSize, pixelSize))
            else:
                pygame.draw.rect(screen, STONE, ((i-0) * pixelSize, (j-0) * pixelSize, pixelSize, pixelSize))

    pygame.display.flip()


BLUE = (0,0,255)
SAND = (194,178,128)
GREEN = (0,128,0)
STONE = (145, 142, 133)

pygame.init()
screen = pygame.display.set_mode([1000,1000])

pixelSize = 10

noise = PerlinNoise(octaves=4, seed = random.randint(1,1000))
xpix, ypix = 100, 100
pic = [[noise([i/xpix, j/ypix]) for j in range(xpix)] for i in range(ypix)]
picList = [item for sublist in pic for item in sublist]
picList.sort()


waterElement = picList[int(xpix * ypix * 0.6)]
sandElement = picList[int(xpix * ypix * 0.7)]
greenElement = picList[int(xpix * ypix * 0.9)]

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
    if keys[pygame.K_UP]:
        exploreUp()
    if keys[pygame.K_LEFT]:
        exploreLeft()
    paint()
