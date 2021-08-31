import pygame

#definir la class qui va gérer le projectile de notre joueur
class Projectile(pygame.sprite.Sprite):

    #définir le constructeur de cette classe
    def __init__(self, player):
        super().__init__()
        self.velocity = 5
        self.player = player
        self.image = pygame.image.load('assets/projectile.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 120
        self.rect.y = player.rect.y + 80
        self.origin_image = self.image
        self.angle = 0

    def rotate(self):
        #tourner le projectile
        self.angle += 2
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def remove(self):
        self.player.all_projectile.remove(self)

    def move(self):
        self.rect.x += self.velocity
        self.rotate()

        #vérifier si le projectile entre en collision avec un monstre
        for monster in self.player.game.check_collision(self, self.player.game.all_monsters):
            #supprimer le projectile
            self.remove()
            #infliger des dégats
            monster.damage(self.player.attack)

        #verifier si notre projectile n'est plus présent sur l'écran
        if self.rect.x > 1200:
            #supprimmer le projectile en dehors de l'écran
            self.remove()
