import pygame,sys

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((800,800))
second_surface = pygame.Surface([100,200])
second_surface.fill((55,66,22))

kitten = pygame.image.load('kitten.jpg')
kitten_rect = kitten.get_rect(topleft = [100,200])


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((50,86,99))
    screen.blit(second_surface,(22,22))
    screen.blit(kitten,(kitten_rect))
    kitten_rect.right +=1

    pygame.display.flip()
    clock.tick(60)
