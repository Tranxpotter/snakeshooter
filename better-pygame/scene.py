from abc import ABC, abstractmethod

import pygame

from ._constants import ON_TRANSITION_END

class Scene(ABC):
    '''Abstract base class for Scene
    
    Methods
    ----------
    handle_event:
        Used to handle event for the Scene and its elements
    update:
        Called to update the elements inside the Scene with time delta since last call
    draw:
        Called to draw the elements of the Scene onto the screen
    
    Use Example
    --------------
    class TitleScene(Scene):
        def __init__(self):
        
        def handle_event(self, event):
            if event.type == '''
    @abstractmethod
    def handle_event(self, event:pygame.Event):...
    
    @abstractmethod
    def update(self, dt:float):...
    
    @abstractmethod
    def draw(self, screen:pygame.Surface):...
    
    def set_enter_transition(self, transition):
        self._enter_transition = transition
    
    def set_exit_transition(self, transition):
        self._exit_transition = transition
    

class SceneManager:
    '''Manager of Scenes
    
    '''
    def __init__(self, screen_size:tuple[int, int], scenes:dict[str, Scene], default_scene:str|None = None) -> None:
        '''
        screen_size: tuple[int, int]
            Defaulted screen size
        scenes: dict[str, Scene]
            Pass in all the scenes and their key as string as identifier
        default_scene: str
            key of the first scene that is selected, if not provided, the first scene provided will be the default
        '''
        self.screen_size = screen_size
        self.scenes = scenes
        if not default_scene:
            keys = list(scenes.keys())
            if len(keys) > 0:
                self.default_scene = keys[0]
            else:
                self.default_scene = None
        else:
            if default_scene not in scenes.keys():
                raise ValueError(f"Default scene {default_scene} not in scenes")
            self.default_scene = default_scene
        if not self.default_scene:
            self.curr_scene = None
            print("Scene Manager missing default scene.")
        else:
            self.curr_scene = scenes[self.default_scene]
        
        self._transitioning = False
        
    
    def change_scene(self, scene_key:str):
        if scene_key not in self.scenes.keys():
            raise ValueError(f"Scene {scene_key} not in scenes")
        self.curr_scene = self.scenes[scene_key]
    
    def handle_event(self, event:pygame.Event):
        if not self.curr_scene:
            return
        self.curr_scene.handle_event(event)
    
    def update(self, dt:float):
        if not self.curr_scene:
            return
        self.curr_scene.update(dt)
    
    def draw(self, screen:pygame.Surface):
        if not self.curr_scene:
            return
        self.curr_scene.draw(screen)
        
       

    
    






