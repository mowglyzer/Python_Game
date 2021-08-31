import pygame

#définir une classe qui va s'occupper des animations
class AnimateSprite(pygame.sprite.Sprite):

    #définir les choses a faire a la création de l'entité
    def __init__(self, sprite_name):
        super().__init__()
        self.image = pygame.image.load(f'assets/{sprite_name}.png')
        self.current_image = 0#commencer l'annimation a l'image 0
        self.images = animations.get(sprite_name)
        self.animation = False

    #définir une méthode pour démarrer l'annimation
    def start_animation(self):
        self.animation = True

    #définir une méthode pour animer le sprite
    def animate(self, loop=False):

        #vérifier si l'annimation es active
        if self.animation:

            #passer a l'image suivante
            self.current_image += 1

            #vérifier si on a atteint la fin de l'annimation
            if self.current_image >= len(self.images):
                #remettre l'annimation au départ
                self.current_image = 0

                #vérifier si l'annimation n'est pas en mode boucle
                if loop is False:
                    # désactivation de l'annimation
                    self.animation = False

            #modifier l'image précédente par la suivante
            self.image = self.images[self.current_image]

#définir une fonction pour charger les images d'un sprite
def load_animation_images(sprite_name):
    #charger les 24 images de ce sprite dans le dossier correspondant
    images = []
    #récupérer le chemin du dossier pour ce sprite
    path = f"assets/{sprite_name}/{sprite_name}"

    #boucler sur chaque images dans ce dossier
    for num in range(1, 24):
        image_path = path + str(num) + '.png'
        images.append(pygame.image.load(image_path))

    #renvoyer le contenue de la liste d'images
    return images


#définir un dictionnaire qui va contenir les images chargés de chaque sprite
# mummy -> [...mummy1.png,...mummy2.png,...]
# player -> [...player1.png,...player2.png,...]
animations = {
    'mummy': load_animation_images('mummy'),
    'player' : load_animation_images('player')
}
