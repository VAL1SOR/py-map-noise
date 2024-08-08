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

pygame.init()

screen = pygame.display.set_mode((w, h))
noise = make_noise(seed, w, h)
for i in range(h):
  for j in range(w):
    c = int(255 * noise[i][j])
    screen.set_at((j, i), (c, c, c))

pygame.display.flip()
pygame.image.save(screen, "noise.png")
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()