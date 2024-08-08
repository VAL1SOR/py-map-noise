import random
import pygame

w = 1000
h = 1000
seed = 48

def make_noise(seed, w, h):
    noise = []
    random.seed(seed)
    for i in range(h):
        row = []
        for j in range(w):
            row.append(random.random())
        noise.append(row)
    return noise

def smooth(noise):
    h = len(noise)
    w = len(noise[0])
    smooth_noise = []
    for i in range(0, h - 1):
        line = []
        for j in range(0, w - 1):
            neighbors = [
                noise[i][j],
                noise[i-1][j] if i > 0 else noise[i][j],
                noise[i+1][j] if i < h-1 else noise[i][j],
                noise[i][j-1] if j > 0 else noise[i][j],
                noise[i][j+1] if j < w-1 else noise[i][j],
                noise[i-1][j-1] if i > 0 and j > 0 else noise[i][j],
                noise[i-1][j+1] if i > 0 and j < w-1 else noise[i][j],
                noise[i+1][j-1] if i < h-1 and j > 0 else noise[i][j],
                noise[i+1][j+1] if i < h-1 and j < w-1 else noise[i][j],
            ]
            line.append(sum(neighbors) / len(neighbors))
        smooth_noise.append(line)
    return smooth_noise

pygame.init()

screen = pygame.display.set_mode((w, h))
noise = smooth(make_noise(seed, w, h))
for i in range(h - 1):
    for j in range(w - 1):
        c = int(255 * noise[i][j])
        screen.set_at((j, i), (c, c, c))

pygame.display.flip()
pygame.image.save(screen, "smooth_noise.png")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
