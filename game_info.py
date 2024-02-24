class GameInfo:
    def __init__(self, screen_size:tuple[int, int], state:int = 0) -> None:
        self.screen_size = self.screen_width, self.screen_height = screen_size
        self.state = state