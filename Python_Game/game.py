import pygame
from player import Player
from monster import Monster
from comet_event import CometFallEvent

#creer une seconde class qui va représenter notre jeu
class Game():

    def __init__(self):
        #définir si notre jeu a commencé ou non
        self.is_playing = False
        #generer notre joueur
        self.all_player = pygame.sprite.Group()
        self.player = Player(self)
        self.all_player.add(self.player)
        #générez l'évenement
        self.comet_event = CometFallEvent(self)
        #groupe de monstres
        self.all_monsters = pygame.sprite.Group()
        self.pressed = {}

    def start(self):
        self.is_playing = True
        self.spawn_monster()
        self.spawn_monster()

    def game_over(self):
        #remettre le jeu a neuf, retirer les monstres, point de vie a 100%, jeu en attente
        self.all_monsters = pygame.sprite.Group()
        self.comet_event.all_comets = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self .comet_event.reset_percent()
        self.is_playing = False

    def update(self, screen, game):
        # appliquer l'image de notre joueur
        screen.blit(self.player.image, self.player.rect)

        # actualiser la barre de vie de notre player
        self.player.update_health_bar(screen)

        #actualiser la barre d'évenement du jeu
        self.comet_event.update_bar(screen)

        #actualiser l'annimation du joueur
        self.player.update_animation()

        # recupérer les projectiles du joueur
        for projectile in self.player.all_projectile:
            projectile.move()

        # recupérer les monstres de notre jeu
        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)
            monster.update_animation()

        #recuperer les comètes de notre jeu
        for comet in self.comet_event.all_comets:
            comet.fall()

        # appliquer l'ensemble des images de mon groupe de projectile
        self.player.all_projectile.draw(screen)

        # appliquer l'ensemble des images de mon groupe de monstres
        self.all_monsters.draw(screen)

        #appliquer l'ensemble des images de mon groupe de comètes
        self.comet_event.all_comets.draw(screen)

        # vérifier si le joueur souhaite aller a gauche ou a droite
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + game.player.rect.width < screen.get_width():
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_monster(self):
        monster = Monster(self)
        self.all_monsters.add(monster)

