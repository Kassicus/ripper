import pygame
import lib
import random

class BaseEnemy(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, size: int) -> None:
        pygame.sprite.Sprite.__init__(self)

        self.pos = pygame.math.Vector2(x, y)
        self.vel = pygame.math.Vector2()
        self.speed = 100
        self.health = 5

        self.particle_system = None
        self.drop_table = []
        self.drop_chance = 1

        self.image = pygame.Surface([size, size])
        self.image.fill(lib.color.red)
        self.image.set_colorkey(lib.color.red)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

    def update(self) -> None:
        self.pos += self.vel * lib.delta_time
        self.rect.center = self.pos

        if self.particle_system is not None:
            self.particle_system.update(self.pos.x, self.pos.y)

        if self.health <= 0:
            self.die()

    def die(self) -> None:
        #drop_draw = random.randint(1, 1)

        #if drop_draw == self.drop_chance:
            #drop = random.choice(self.drop_table)
            #instance = drop(self.pos.x, self.pos.y)
            #lib.world_reference.ground_items.add(instance)
            #lib.world_reference.world_camera.add(instance)

        self.kill()


class FollowEnemy(BaseEnemy):
    def __init__(self, x: int, y: int) -> None:
        super().__init__(x, y, 20)

        self.tag = "follower"

        self.speed = 70
        self.health = 5

    def follow_player(self) -> None:
        self.vel.x, self.vel.y = lib.get_vectors(self, lib.world_reference.player)


class FlyerEnemy(BaseEnemy):
    def __init__(self, x: int, y: int) -> None:
        super().__init__(x, y, 20)

        self.tag = "flyer follower"

        self.speed = 100
        self.health = 3

    def follow_player(self) -> None:
        self.vel.x, self.vel.y = lib.get_vectors(self, lib.world_reference.player)