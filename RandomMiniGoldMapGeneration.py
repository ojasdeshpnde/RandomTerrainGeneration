from perlin_noise import PerlinNoise
import matplotlib.pyplot as plt
import random
import pygame


def paint():
    for i in range(0, xpix):
        for j in range(0, ypix):
            if (pic[i][j] > waterElement and pic[i][j] < sandElement):
                if random.random() < 0.6:
                    pygame.draw.rect(screen, SAND, (i * pixelSize, j * pixelSize, pixelSize, pixelSize))

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


waterElement = picList[int(xpix * ypix * 0.7)]
sandElement = picList[int(xpix * ypix * 0.8)]

paint()
run = True

while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run =False

