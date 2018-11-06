from livewires import games

games.init(screen_width = 640, screen_height = 480, fps = 50)

wallImage = games.load_image("waterbackground.jpg", transparent = False)
games.screen.background = wallImage

bloodExplosionFiles = ["bloodexplosion1.jpg",
                   "bloodexplosion2.jpg",
                   "bloodexplosion3.jpg",
                   "bloodexplosion4.jpg",]
          
bloodExplosion = games.Animation(images = bloodExplosionFiles,
                            x = games.screen.width/2,
                            y = games.screen.height/2,
                            n_repeats = 0,
                            repeat_interval = 20)
games.screen.add(bloodExplosion)

games.screen.mainloop()
