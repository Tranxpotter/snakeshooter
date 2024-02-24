import pygame
pygame.init()
from scenes import *
from game import Game


SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = (1280, 720)



def main():
    game = Game(SCREEN_SIZE)
    clock = pygame.time.Clock()
    dt = 0
    running = True
    scenes:dict[int, Scene] = {
        0:TitleScreen(game),
        1:MenuScreen(game)
    }
    screen = pygame.display.set_mode(SCREEN_SIZE)
    
    while running:
        curr_scene = scenes.get(game.state)
        if not curr_scene:
            print("Missing scene for state:", game.state)
            running = False
            break
        events = pygame.event.get()
        
        for event in events:
            if event.type == pygame.QUIT:
                running = False
            curr_scene.handle_event(event)
        
        curr_scene.update(dt)
        
        screen.fill((0,0,0))
        curr_scene.draw(screen)
        
        pygame.display.update()
        
        
        
        dt = clock.tick(60) / 1000
    
    pygame.quit()






if __name__ == "__main__":
    main()