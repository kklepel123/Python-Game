import math, random
from livewires import games, color

games.init(screen_width = 640, screen_height = 480, fps = 50)

class Player(games.Sprite):
    """ The mexican player. """
    waitTime = 50
    waitCounter = 0
    canShoot = True
    chanceOfPiranhaSpawn = 100
    distanceOfPiranha = 1100
    """ The score is added in the addObjects of the PlayButton class """
    score = games.Text(value = 0, size = 60, color = color.red, top = 5,
                       right = games.screen.width - 10, is_collideable = False)
        
    def update(self):
        """ Rotate based on left and right arrow keys. """
        if games.keyboard.is_pressed(games.K_RIGHT):
            self.angle += 1.75
        if games.keyboard.is_pressed(games.K_LEFT):
            self.angle -= 1.75

        """ Move based on up and down arrow keys. """    
        if games.keyboard.is_pressed(games.K_UP) and self.y > 50:
            self.y -= 3
        if games.keyboard.is_pressed(games.K_DOWN) and self.y < 430:
            self.y += 3

        """ Fire missile if spacebar pressed and missile wait is over. """
        if games.keyboard.is_pressed(games.K_SPACE) and Player.canShoot == True:
            newBullet = Bullet(self.x, self.y, self.angle + 90)
            games.screen.add(newBullet)
            Player.canShoot = False
            Player.waitCounter = 0
        if Player.canShoot == False:
            Player.waitCounter += 1.5
        if Player.waitCounter >= Player.waitTime:
            Player.canShoot = True

        spawnPiranha = random.randint(1, Player.chanceOfPiranhaSpawn)
        if spawnPiranha == 1: 
            x = random.randint(700, Player.distanceOfPiranha)
            y = random.randint(20, 460)
            piranhaImage = games.load_image("piranha.jpg")
            piranha = Piranha(image = piranhaImage, x = x, y = y, dx = -.25, dy = 0)
            games.screen.add(piranha)

        winMessage = games.Message(value = "You Won!!",
                                    size = 90,
                                    color = color.red,
                                    x = games.screen.width/2,
                                    y = games.screen.height/2,
                                    lifetime = 5 * games.screen.fps,
                                    after_death = games.screen.quit,
                                    is_collideable = False)
##        levelMessage = games.Message(value = "Level 1",
##                size = 90,
##                color = color.red,
##                x = games.screen.width/2,
##                y = games.screen.height/2,
##                lifetime = 10,
##                is_collideable = False)
        
        if Player.score.value == 150:
            Player.chanceOfPiranhaSpawn = 75
            Player.distanceOfPiranha = 1000
        if Player.score.value == 350:
            Player.chanceOfPiranhaSpawn = 55
            Player.distanceOfPiranha = 950
        if Player.score.value == 500:
            Player.chanceOfPiranhaSpawn = 45
            Player.distanceOfPiranha = 850
        if Player.score.value == 750:
            Player.chanceOfPiranhaSpawn = 35
            Player.distanceOfPiranha = 750
        if Player.score.value == 1300:
            games.screen.clear()
            games.screen.add(winMessage)
            games.music.load("Sound Effect- I AM THE ONE!.wav")
            games.music.play()
           
class Bullet(games.Sprite):
    """ A bullet shot from the player's player. """
    image = games.load_image("bullet.png")
    VELOCITY_FACTOR = 7
    """ Fire bullet from certain position based on the angle of Player. """
    def __init__(self, playerX, playerY, playerAngle):
        angle = playerAngle * math.pi / 180
        originalPosition = playerX + 70
        if playerAngle == 90:
            y = playerY + 35
            x = originalPosition
        elif 450 >= playerAngle > 430:
            y = playerY + 25
            x = originalPosition
        elif 430 >= playerAngle > 410:
            y = playerY + 10
            x = originalPosition
        elif 410 >= playerAngle > 390:
            y = playerY - 5
            x = originalPosition
        elif 390 >= playerAngle > 360:
            y = playerY - 20
            x = playerX + 40
        if 90 < playerAngle <= 110:
            y = playerY + 35
            x = playerX + 65
        elif 110 < playerAngle <= 130:
            y = playerY + 45
            x = playerX + 60
        elif 130 < playerAngle <= 150:
            y = playerY + 55
            x = playerX + 40
        elif 150 < playerAngle <= 180:
            y = playerY + 50
            x = playerX + 15
        if 360 >= playerAngle > 180:
            y = playerY + 35
            x = playerX 
        dx = Bullet.VELOCITY_FACTOR * math.sin(angle)
        dy = Bullet.VELOCITY_FACTOR * -math.cos(angle)

        super(Bullet, self).__init__(image = Bullet.image, x = x, y = y, dx = dx, dy = dy)

    def update(self):
        bulletGoesOffScreen = self.x > games.screen.width + 100
        if bulletGoesOffScreen:
            self.destroy()

        """ Destroy piranha and bullet when they collide. """
        if self.overlapping_sprites:
            xValueExplosionLocation = self.x + 70
            for sprite in self.overlapping_sprites:
                sprite.destroy()
                Player.score.value += 10
                Player.score.right = games.screen.width - 10
            """ Blood explosion. """
            newExplosion = Explosion(x = xValueExplosionLocation, y = self.y)
            games.screen.add(newExplosion)
            self.destroy()
            
class Piranha(games.Sprite):
    """ Initializes piranha sprite. """
        
    def __init__(self, image, x, y, dx, dy):
        super(Piranha, self).__init__(image = image,
                                      x = x,
                                      y = y,
                                      dx = dx,
                                      dy = dy)
    
    def update(self):
        self.x -= 1
        endMessage = games.Message(value = "Game Over",
                                    size = 90,
                                    color = color.red,
                                    x = games.screen.width/2,
                                    y = games.screen.height/2,
                                    lifetime = 5 * games.screen.fps,
                                    after_death = games.screen.quit,
                                    is_collideable = False)
        
        piranhaReachesDock = self.x <= 100
        if piranhaReachesDock:
            self.x = 100
            games.screen.clear()
            games.screen.add(endMessage)

            
class Explosion(games.Animation):
    """ Explosion animation. """
    bloodExplosionFiles = ["bloodexplosion1.jpg",
                   "bloodexplosion2.jpg",
                   "bloodexplosion3.jpg",
                   "bloodexplosion4.jpg",]

    def __init__(self, x, y):
        super(Explosion, self).__init__(images = Explosion.bloodExplosionFiles,
                                        x = x, y = y,
                                        repeat_interval = 6, n_repeats = 1,
                                        is_collideable = False)
        
class PlayButton(games.Sprite):
    image = games.load_image("playButton.jpg")

    def __init__(self):
        super(PlayButton, self).__init__(image = PlayButton.image,
                                         x = games.screen.width / 2,
                                         y = games.screen.height / 2)

    def update(self):
        if games.mouse.is_pressed(0):
            self.destroy()
            addObjects()

def showInstructions(text, position):
    xValue = games.screen.width / 2
    messageSize = 20

    line = games.Text(value = text,
                      size = messageSize,
                      color = color.red,
                      x = xValue,
                      y = position)

    games.screen.add(line)

def addObjects():

    games.screen.clear()
    """ Establish background. """
    wallImage = games.load_image("waterbackground.jpg", transparent = False)
    games.screen.background = wallImage

    """ Create dock. """
    dockImage = games.load_image("dock.gif")
    dock = games.Sprite(image = dockImage, x = 0, y = 240, is_collideable = False)
    games.screen.add(dock)

    """ Create the player. """
    playerImage = games.load_image("playerImage.jpg")
    player = Player(image = playerImage, x = 45, y = 240, is_collideable = False)
    games.screen.add(player)

    games.screen.add(Player.score)

def main():
    startingHeightOfInstructions = 50
    spaceBetweenFirstAndSecondLines = 25
    spaceBetweenSecondAndThirdLines = 75
    spaceBetweenThirdAndFourthLines = 100
    clickToPlayPosition = 300
    
    showInstructions("Mexican Fishing", startingHeightOfInstructions)
    showInstructions("By: Kaleb Klepel", startingHeightOfInstructions + spaceBetweenFirstAndSecondLines)
    showInstructions("Press the arrow keys to move the player up and down and to rotate him. Press the spacebar to shoot.",
                     startingHeightOfInstructions + spaceBetweenSecondAndThirdLines)
    showInstructions("The game ends when one of the piranhas reaches the dock. Good Luck!",
                     startingHeightOfInstructions + spaceBetweenThirdAndFourthLines)
    showInstructions("Click to play", clickToPlayPosition) 

    playButton = PlayButton()
    games.screen.add(playButton)

    games.music.load("Jaws Theme Song.wav")
    games.music.play(-1)
    
    games.screen.mainloop()

""" Kick it off! """
main()
