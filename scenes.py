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
        
        self.ui_manager = pygame_gui.UIManager(screen_size, "themes/titescreen.json")
        
        title_rect = pygame.Rect(0, -30, 100, 30)
        title_text = "Snake Shooter"
        self.title = pygame_gui.elements.UILabel(title_rect, 
                                                 title_text, 
                                                 self.ui_manager,
                                                 object_id=pygame_gui.core.ObjectID("#title_text", "@title_label"),
                                                 anchors={"center":"center"}
                                                 )

        
        start_btn_rect = pygame.Rect(0, 30, 60, 30)
        start_btn_text = "Start"
        self.start_btn = pygame_gui.elements.UIButton(start_btn_rect,
                                                      start_btn_text,
                                                      self.ui_manager,
                                                      anchors={"center":"center"},
                                                      object_id=pygame_gui.core.ObjectID("#start_btn", "@friendly_btn"))
        
        menu_btn_rect = pygame.Rect(0, 70, 60, 30)
        meun_btn_text = "Menu"
        self.start_btn = pygame_gui.elements.UIButton(menu_btn_rect,
                                                      meun_btn_text,
                                                      self.ui_manager,
                                                      anchors={"center":"center"},
                                                      object_id=pygame_gui.core.ObjectID("#menu_btn", "@friendly_btn"))

        
    
    def handle_event(self, event: pygame.Event) -> None:
        self.ui_manager.process_events(event)
        
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == self.start_btn:
                self.game.state = 2
            
        
    
    def update(self, dt: float) -> None:
        self.ui_manager.update(dt)
    
    def draw(self, screen: pygame.Surface) -> None:
        self.ui_manager.draw_ui(screen)
        
        
        



























