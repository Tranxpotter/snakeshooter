from abc import ABC, abstractmethod
import pygame
import pygame_gui
import fonts
from utils import *
from game import Game
class Scene:
    @abstractmethod
    def __init__(self, *args, **kwargs) -> None:...
    
    @abstractmethod
    def handle_event(self, event:pygame.Event) -> None:...
    
    @abstractmethod
    def update(self, dt:float) -> None:...
    
    @abstractmethod
    def draw(self, screen:pygame.Surface) -> None:...

class TitleScreen(Scene):
    def __init__(self, game:Game) -> None:
        self.game = game
        screen_size = game.screen_size
        self.screen_size = self.screen_width, self.screen_height = screen_size
        
        self.ui_manager = pygame_gui.UIManager(screen_size, "themes/titlescreen.json")
        
        self.bg_img = pygame.image.load("assets/titlescreen_bg.png")
        
        title_rect = pygame.Rect(0, -30, 600, 52)
        title_text = "Snake Shooter"
        self.title = pygame_gui.elements.UILabel(title_rect, 
                                                 title_text, 
                                                 self.ui_manager,
                                                 object_id=pygame_gui.core.ObjectID("#title_text", "@title_label"),
                                                 anchors={"center":"center"}
                                                 )

        
        start_btn_rect = pygame.Rect(0, 50, 200, 30)
        start_btn_text = "Start"
        self.start_btn = pygame_gui.elements.UIButton(start_btn_rect,
                                                      start_btn_text,
                                                      self.ui_manager,
                                                      anchors={"center":"center"},
                                                      object_id=pygame_gui.core.ObjectID("#start_btn", "@friendly_btn"))
        
        menu_btn_rect = pygame.Rect(0, 90, 200, 30)
        meun_btn_text = "Menu"
        self.menu_btn = pygame_gui.elements.UIButton(menu_btn_rect,
                                                      meun_btn_text,
                                                      self.ui_manager,
                                                      anchors={"center":"center"},
                                                      object_id=pygame_gui.core.ObjectID("#menu_btn", "@friendly_btn"))

        
    
    def handle_event(self, event: pygame.Event) -> None:
        self.ui_manager.process_events(event)
        
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == self.start_btn:
                self.game.state = 2
            
            elif event.ui_element == self.menu_btn:
                self.game.state = 1
            
        
    
    def update(self, dt: float) -> None:
        self.ui_manager.update(dt)
    
    def draw(self, screen: pygame.Surface) -> None:
        screen.blit(self.bg_img, (0, 0))
        self.ui_manager.draw_ui(screen)
        
        
        


class MenuScreen(Scene):
    def __init__(self, game:Game) -> None:
        self.game = game
        screen_size = game.screen_size
        
        self.bg_img = pygame.image.load("assets/menu_bg.png")
        
        self.ui_manager = pygame_gui.UIManager(screen_size, "themes/menuscreen.json")
        
        back_btn_rect = pygame.Rect(30, 30, 100, 50)
        self.back_btn = pygame_gui.elements.UIButton(back_btn_rect, 
                                                     "back",
                                                     self.ui_manager,
                                                     anchors={"top":"top", "left":"left"},
                                                     object_id=pygame_gui.core.ObjectID("#back_btn", "@danger_btn"))
    
    def handle_event(self, event: pygame.Event) -> None:
        self.ui_manager.process_events(event)
        
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == self.back_btn:
                self.game.state = 0
    
    def update(self, dt: float) -> None:
        self.ui_manager.update(dt)
    
    def draw(self, screen: pygame.Surface) -> None:
        screen.blit(self.bg_img, (0, 0))
        self.ui_manager.draw_ui(screen)

























