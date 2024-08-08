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
    if ((c / 255) * 100) <= 20:
       color = (36, 159, 222)
    elif ((c / 255) * 100) <= 40:
       color = (255, 252, 64)
    elif ((c / 255) * 100) <= 60:
       color = (89, 193, 53)
    elif ((c / 255) * 100) <= 80:
       color = (113, 65, 59)
    else:
       color = (66, 57, 52)
    screen.set_at((j, i), color)

pygame.display.flip()
pygame.image.save(screen, "map.png")
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()