from livewires import games

games.init(screen_width = 640, screen_height = 480, fps = 50)

wallImage = games.load_image("waterbackground.jpg", transparent = False)
games.screen.background = wallImage

dockImage = games.load_image("dock.gif")
dock = games.Sprite(image = dockImage, x = 0, y = 240)
games.screen.add(dock)

games.screen.mainloop()
