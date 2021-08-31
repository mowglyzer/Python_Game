import pygame
import math
from game import Game
from player import Player
pygame.init()


#générez la fenêtre de notre jeu
pygame.display.set_caption("SHOOTER TROOPER")
screen = pygame.display.set_mode((1380, 700))

#importer et charger l'arrière plan de notre jeu
background = pygame.image.load('assets/bg.jpg')

#importer charger notre bannière
banner = pygame.image.load('assets/banner.png')
banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 3)

#importer charger notre button pour lancer le jeu
play_button = pygame.image.load('assets/button.png')
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 2.66)
play_button_rect.y = math.ceil(screen.get_height() / 1.95)


#charger notre jeu
game = Game()

#charger notre joueur
player = Player(game)

running = True

#boucle tan que cette condition es vraie
while running:

    #appliquer l'arriere plan de notre jeu
    screen.blit(background, (0, -200))

    #vérifier si notre jeu a commencer ou non
    if game.is_playing:
        #déclencher les instructions de la partie
        game.update(screen, game)
    #vérifier si notre jeu a commencer
    else:
        #ajouter mon écran de bienvenue
        screen.blit(play_button, play_button_rect)
        screen.blit(banner, banner_rect)


    #mettre a jour l'écran
    pygame.display.flip()

    #si le joueur ferme cette fenêtre
    for event in pygame.event.get():
        #que l'évenement es fermeture de fenêtre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("ferme")
        #detecter si un joueur lache une touche du clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            #detecter si la touche espace es enclenché pour lancer notre projectile
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()


        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False


        elif event.type == pygame.MOUSEBUTTONDOWN:
            #verification pour savoir si la souris es en collision avec le bouton jouer
            if play_button_rect.collidepoint(event.pos):
                #mettre le jeu en mode lancer
                game.start()