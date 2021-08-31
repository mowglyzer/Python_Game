import pygame
from projectile import Projectile
import animation

#creer une premiere class qui va representer notre joueur
class Player(animation.AnimateSprite):

    def __init__(self, game):
        super().__init__('player')
        self.game = game
        self.health = 150
        self.max_health = 100
        self.attack = 10
        self.velocity = 5
        self.all_projectile = pygame.sprite.Group()
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 500

    def damage(self, amount):
        if self.health - amount > amount:
            self.health -= amount
        else:
            #si le joueur n'a plus de point de vie
            self.game.game_over()

    def update_animation(self):
        self.animate()

    def update_health_bar(self, surface):
        #déssiner notre barre de vie
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 50, self.rect.y + 20, self.max_health, 7])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 50, self.rect.y + 20, self.health, 7])

    def launch_projectile(self):
        #creer une nouvelle instace de la classe projectile
        self.all_projectile.add(Projectile(self))
        #démarrer l'annimation du lancer
        self.start_animation()

    def move_right(self):
        #si le joueur n'est pas en collision avec une entité monster
        if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity

