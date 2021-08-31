import pygame
import random

#créer une classe pour gérez cette comète
class Comet(pygame.sprite.Sprite):

    def __init__(self, comet_event):
        super().__init__()
        #définir l'image associé a cette comète
        self.image = pygame.image.load('assets/comet.png')
        self.rect = self.image.get_rect()
        self.velocity = random.randint(1, 3)
        self.rect.x = random.randint(20, 1300)
        self.rect.y = - random.randint(0, 800)
        self.comet_event = comet_event

    def remove(self):
        self.comet_event.all_comets.remove(self)

        #vérifier si le nombre de comètes es de 0
        if len(self.comet_event.all_comets) == 0:
            #remettre la barre a 0
            self.comet_event.reset_percent()
            #apparaitre les premiers monstres
            self.comet_event.game.spawn_monster()
            self.comet_event.game.spawn_monster()

    def fall(self):
        self.rect.y += self.velocity

        #ne tombe pas sur le sol
        if self.rect.y >= 550:
            #effacer la boule de feu
            self.remove()

            #vérifier si il n'y a plus de boules de feu sur le jeu
            if len(self.comet_event.all_comets) == 0:
                #remettre la jauge de vie au départ
                self.comet_event.reset_percent()
                self.comet_event.fall_mode = False

        #vérifier si la boule de feu touche le joueur
        if self.comet_event.game.check_collision(self, self.comet_event.game.all_player):
            #retirer la boule de feu
            self.remove()
            #subir 20 point de dégats
            self.comet_event.game.player.damage(20)
