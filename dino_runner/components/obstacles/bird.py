import random 

from dino_runner.components.obstacles.obstacles import Obstacle
from dino_runner.utils.constants import BIRD


class Bird(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)

    def bird(self):
        self.image = BIRD[0] if self.step_index < 5 else BIRD[1]
        self.dino_rect.x = 300
        self.dino_rect.y = 300
        self.step_index += 1
        