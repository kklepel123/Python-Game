# Sound and Music
# Demonstrates playing sound and music files

from livewires import games

games.init(screen_width = 640, screen_height = 480, fps = 50)

# load a sound file
bulletSound = games.load_sound("MLG Gun Shot Sound Effect 2.wav")

# load the music file
games.music.load("Jaws Theme Song.wav")

choice = None
while choice != "0":

    print(
    """
    Sound and Music
    
    0 - Quit
    1 - Play missile sound
    2 - Loop missile sound
    3 - Stop missile sound
    4 - Play theme music
    5 - Loop theme music
    6 - Stop theme music
    """
    )
    
    choice = input("Choice: ")
    print()

    # exit
    if choice == "0":
        print("Good-bye.")

    # play missile sound
    elif choice == "1":
        bulletSound.play()
        print("Playing missile sound.")

    # loop missile sound
    elif choice == "2":
        loop = int(input("Loop how many extra times? (-1 = forever): "))
        bulletSound.play(loop)
        print("Looping missile sound.")

    # stop missile sound
    elif choice == "3":
        bulletSound.stop()
        print("Stopping missile sound.")

    # play theme music
    elif choice == "4":
        games.music.play()
        print("Playing theme music.")

    # loop theme music
    elif choice == "5":
        loop = int(input("Loop how many extra times? (-1 = forever): "))
        games.music.play(loop)
        print("Looping theme music.")

    # stop theme music
    elif choice == "6":
        games.music.stop()
        print("Stopping theme music.")
                 
    # some unknown choice
    else:
        print("\nSorry, but", choice, "isn't a valid choice.")
  
input("\n\nPress the enter key to exit.")

