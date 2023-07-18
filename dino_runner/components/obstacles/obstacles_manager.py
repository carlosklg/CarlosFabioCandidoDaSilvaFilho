import pygame
import random

from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.utils.constants import SMALL_CACTUS
from dino_runner.utils.constants import LARGE_CACTUS
from dino_runner.utils.constants import BIRD


class ObstacleManager:
    def __init__(self):
        self.obstacles = []
        self.alternate_append_index = 0
        

    def update(self, game):
        if len(self.obstacles) == 0:
            self.alternate_append_index = random.randint(1, 2)
            if self.alternate_append_index % 2 == 0:
                self.obstacles.append(Cactus(SMALL_CACTUS))
            else:
                self.obstacles.append(Cactus(LARGE_CACTUS))
            
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(500)
                game.playing = False
                break

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)