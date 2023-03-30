import pygame
import os

# initialize pygame
pygame.init()

# set the window size
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500

# create the window
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# set the window title
pygame.display.set_caption("Music Player")

# set the font and font size
font = pygame.font.SysFont(None, 25)

# set the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# set the directory where the music files are located
music_directory = "C:\music"

# get a list of all the music files in the directory
music_files = os.listdir(music_directory)

# create a list of the music files with their full paths
music_paths = [os.path.join(music_directory, file) for file in music_files]

# set the current song index to 0
current_song_index = 0

# load the first song
pygame.mixer.music.load(music_paths[current_song_index])

# play the song
pygame.mixer.music.play()

# create a function to display the current song name
def display_current_song():
    current_song = music_files[current_song_index]
    text = font.render(current_song, True, WHITE)
    window.blit(text, (10, 10))

# create a game loop
running = True
while running:

    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # check for key presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # pause or unpause the music
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()

            elif event.key == pygame.K_LEFT:
                # go to the previous song
                current_song_index -= 1
                if current_song_index < 0:
                    current_song_index = len(music_paths) - 1
                pygame.mixer.music.load(music_paths[current_song_index])
                pygame.mixer.music.play()

            elif event.key == pygame.K_RIGHT:
                # go to the next song
                current_song_index += 1
                if current_song_index > len(music_paths) - 1:
                    current_song_index = 0
                pygame.mixer.music.load(music_paths[current_song_index])
                pygame.mixer.music.play()

    # clear the window
    window.fill(BLACK)

    # display the current song name
    display_current_song()

    # update the window
    pygame.display.update()

# quit pygame
pygame.quit()
