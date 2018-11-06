import random
import math
from livewires import games

games.init(screen_width = 640, screen_height = 480, fps = 50)

class Player(games.Sprite):
    waitTime = 50
    waitCounter = 0
    canShoot = True
    def update(self):
        if games.keyboard.is_pressed(games.K_RIGHT):
            self.angle += 1
        if games.keyboard.is_pressed(games.K_LEFT):
            self.angle -= 1
        if games.keyboard.is_pressed(games.K_UP) and self.y > 50:
            self.y -= 1
        if games.keyboard.is_pressed(games.K_DOWN) and self.y < 430:
            self.y += 1

        if games.keyboard.is_pressed(games.K_SPACE) and Player.canShoot == True:
            newBullet = Bullet(self.x, self.y, self.angle + 90)
            games.screen.add(newBullet)
            Player.canShoot = False
            Player.waitCounter = 0
        if Player.canShoot == False:
            Player.waitCounter += 1
        if Player.waitCounter >= Player.waitTime:
            Player.canShoot = True

class Bullet(games.Sprite):
    image = games.load_image("bullet.png")
##    BUFFER = 40
    VELOCITY_FACTOR = 7

    def __init__(self, playerX, playerY, playerAngle):
        angle = playerAngle * math.pi / 180 
##        bufferX = Bullet.BUFFER * math.sin(angle)
        x = playerX + 60
        y = playerY + 30

        dx = Bullet.VELOCITY_FACTOR * math.sin(angle)
        dy = Bullet.VELOCITY_FACTOR * -math.cos(angle)

        super(Bullet, self).__init__(image = Bullet.image, x = x, y = y, dx = dx, dy = dy)

    def update(self):
        if self.x > games.screen.width + 100:
            self.destroy()
            
class Piranha(games.Sprite):
    def __init__(self, image, x, y, dx, dy):
        super(Piranha, self).__init__(image = image, x = x, y = y, dx = dx, dy = dy)

    def update(self):
        self.x -= 1
        if self.x <= 100:
            self.x = 100



def main():
    wallImage = games.load_image("waterbackground.jpg", transparent = False)
    games.screen.background = wallImage

    dockImage = games.load_image("dock.gif")
    dock = games.Sprite(image = dockImage, x = 0, y = 240)
    games.screen.add(dock)

    playerImage = games.load_image("playerImage.jpg")
    player = Player(image = playerImage, x = 45, y = 240)
    games.screen.add(player)

    for i in range(8):
        x = random.randint(700, 2000)
        y = random.randint(20, 460)
        piranhaImage = games.load_image("piranha.jpg")
        piranha = Piranha(image = piranhaImage, x = x, y = y, dx = -.25, dy = 0)
        games.screen.add(piranha)


    


    games.screen.mainloop()

main()

