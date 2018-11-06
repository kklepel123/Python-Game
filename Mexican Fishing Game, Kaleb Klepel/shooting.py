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
            newArrow = Arrow(self.x, self.y, self.angle + 90)
            games.screen.add(newArrow)
            Player.canShoot = False
            Player.waitCounter = 0
        if Player.canShoot == False:
            Player.waitCounter += 1
        if Player.waitCounter >= Player.waitTime:
            Player.canShoot = True
            
class Arrow(games.Sprite):
    image = games.load_image("arrow.png")
    BUFFER = 40
    VELOCITY_FACTOR = 7

    def __init__(self, playerX, playerY, playerAngle):
        angle = playerAngle * math.pi / 180 
        bufferX = Arrow.BUFFER * math.sin(angle)
        x = playerX + bufferX
        y = playerY - 35

        dx = Arrow.VELOCITY_FACTOR * math.sin(angle)
        dy = Arrow.VELOCITY_FACTOR * -math.cos(angle)

        super(Arrow, self).__init__(image = Arrow.image, x = x, y = y, dx = dx, dy = dy)

    def update(self):
        if self.x > games.screen.width + 100:
            self.destroy()

def main():
    wallImage = games.load_image("waterbackground.jpg", transparent = False)
    games.screen.background = wallImage

    playerImage = games.load_image("playerImage.jpg")
    player = Player(image = playerImage, x = 45, y = 240)
    games.screen.add(player)

    games.screen.mainloop()

main()


            
