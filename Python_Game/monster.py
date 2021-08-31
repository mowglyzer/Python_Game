import pygame
import random
import animation


#créer une class qui va gérer la notion de monstre sur notre jeu
class Monster(animation.AnimateSprite):

    def __init__(self, game):
        super().__init__("mummy")
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 0.3
        self.rect = self.image.get_rect()
        self.rect.x = 1300 + random.randint(0, 300)
        self.rect.y = 540
        self.velocity = 1
        self.start_animation()

    def damage(self, amount):
        #infliger les dégats
        self.health -= amount

        #vérifier si son nouveau nombre de points de vie es >= 0
        if self.health <= 0:
            #réapparaitre comme un nouveau monstre
            self.rect.x = 1300 + random.randint(0, 300)
            self.velocity = 1 + random.randint(1, 2)
            self.health = self.max_health

            #si la barre d'évenement es chargé a 100%
            if self.game.comet_event.is_full_loaded():
                #retirer du jeu
                self.game.all_monsters.remove(self)

                # appel de la méthode pour déclencher la pluie de comet
                self.game.comet_event.attempt_fall()

    def update_animation(self):
        self.animate(loop=True)

    def update_health_bar(self, surface):
        #déssiner notre barre de vie
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 10, self.rect.y - 20, self.max_health, 5])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 10, self.rect.y - 20, self.health, 5])

    def forward(self):
        #le déplacement ne se fait que s'il n'y a pas de collision avec un groupe de joueur
        if not self.game.check_collision(self, self.game.all_player):
            self.rect.x -= self.velocity
        #si le monstre es en collision avec le joueur
        else:
            #infliger des dégats ( au joueur )
            self.game.player.damage(self.attack)

