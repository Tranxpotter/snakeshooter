from utils import *

class Snake:
    def __init__(self, pos:tuple[int, int], arena_size:tuple[int, int], length:int = 4, max_hp:int = 10, speed:int|float = 3, attack:int|float = 10, skills:dict = {}, effects:dict = {}) -> None:
        self.pos = pos
        self.arena_size = self.arena_width, self.arena_height = arena_size
        self.direction = (1, 0)
        self.length = length
        
        self.base_max_hp = max_hp
        self.hp = max_hp
        self.base_speed = speed
        self.attack = attack
        self.skills = skills
        self.effects = effects
        
        self.segments = []
        propagate_direction = vector_opp(self.direction)
        curr_pos = pos
        next_pos = pos
        
        #Snake segments initialize :skull: hope this goes well this is not gunna be ez
        stage = 1
        rows_below_head = arena_size[1] - pos[1] - 1
        rows_below_head_is_odd = rows_below_head % 2
        for i in range(length):
            curr_pos = next_pos
            self.segments.append(curr_pos)
            next_pos = vector_add(curr_pos, propagate_direction)
            if stage == 1 or stage == 3:
                if rows_below_head_is_odd:
                    turn_condition = next_pos[0] < 0 or next_pos[0] == self.arena_width-1 
                else:
                    turn_condition = next_pos[0] < 1 or next_pos[0] == self.arena_width
                
                if turn_condition:
                    if next_pos[1] == self.arena_height-1:
                        propagate_direction = (0, -1)
                        stage = 2
                        continue
                    propagate_direction = vector_opp(propagate_direction)
                    next_pos = vector_add(curr_pos, (0, 1))
                
                if stage == 3 and next_pos == pos:
                    raise ValueError("Snake segments initialization failed. Snake length too long!")
            
            elif stage == 2:
                if next_pos[1] == 0:
                    stage = 3
                    if rows_below_head_is_odd:
                        propagate_direction = vector_opp(self.direction)
                    else:
                        propagate_direction = self.direction
        #END OF SNAKE SEGMENT INITIALIZE IT WORKED LOL HOW well it wasnt as hard as I thought xd its pretty simple in the end with many reusable parts
        





























