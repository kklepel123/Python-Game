import random
from livewires import games

games.init(screen_width = 640, screen_height = 480, fps = 50)

class Piranha(games.Sprite):
    def __init__(self, image, x, y, dx, dy):
        super(Piranha, self).__init__(image = image, x = x, y = y, dx = dx, dy = dy)

    def update(self):
        self.x -= 1

def main():
    wallImage = games.load_image("waterbackground.jpg", transparent = False)
    games.screen.background = wallImage

    dockImage = games.load_image("dock.gif")
    dock = games.Sprite(image = dockImage, x = 0, y = 240)
    games.screen.add(dock)

##    piranhaImage = games.load_image("piranha.jpg")
##    piranha = games.Sprite(image = piranhaImage, x = 670, y = 240, dx = -.5, dy = 0)
##    games.screen.add(piranha)
##    piranhaImage = games.load_image("piranha.jpg")
    
    for i in range(8):
        x = random.randint(700, 1000)
        y = random.randint(0, games.screen.height)
        piranhaImage = games.load_image("piranha.jpg")
        piranha = Piranha(image = piranhaImage, x = x, y = y, dx = -.25, dy = 0)
        games.screen.add(piranha)  
        
    games.screen.mainloop()

main()

