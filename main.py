import pygame

def game(display, clock):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        pygame.display.update()
        clock.tick(60)




def main():
    pygame.init()

    display = pygame.display.set_mode([800,600])
    pygame.display.set_caption('Shooter')
    clock = pygame.time.Clock()

    while True:
        game(display, clock)

if __name__ == '__main__':
    main()


