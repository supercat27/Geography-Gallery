import pygame as pg
import random
import pygame_textinput
import time as t
import os

pg.init()
pg.font.init()

screen = pg.display.set_mode((1100, 880))
pg.display.set_caption("Guess the European flag!")

# Using system fonts
font1 = pg.font.SysFont("Times New Roman", 36,)
font2 = pg.font.SysFont("Times New Roman", 48)

# Initialize text input with custom font
textinput_manager = pygame_textinput.TextInputManager()
textinput_visualizer = pygame_textinput.TextInputVisualizer(manager=textinput_manager, font_object=font1)

# Function to load images from a folder into a dictionary
def load_images_from_folder(folder):
    images = {}
    for filename in os.listdir(folder):
        if filename.endswith(".png"):  # You can add other image formats if needed
            country_name = os.path.splitext(filename)[0]  # Get the country name from the filename
            path = os.path.join(folder, filename)
            images[country_name] = pg.image.load(path).convert_alpha()
    return images

# Load flag images from the "assets/europe_flags" folder
flags = load_images_from_folder("assets/europe_flags")

europe_map = pg.image.load("assets/europe_map_png.png")

# Select a random flag to start
flag_name = random.choice(list(flags.keys()))
flag = flags[flag_name]
print(f"Flag to guess: {flag_name}")

running = True
clock = pg.time.Clock()

while running:
    events = pg.event.get()
    for event in events:
        if event.type == pg.QUIT:
            running = False

    textinput_visualizer.update(events)

    for event in events:
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RETURN:
                guess = textinput_visualizer.value.lower()
                textinput_visualizer.value = ""
                print(guess)
                if guess == flag_name.lower():
                    print("Correct!")
                    screen.blit(font2.render("Correct!", True, "black"), (10, 50))
                    pg.display.flip()
                    t.sleep(1)
                    del flags[flag_name]
                    if flags:
                        flag_name = random.choice(list(flags.keys()))
                        flag = flags[flag_name]
                        print(f"New Flag: {flag_name}")
                    else:
                        print("No more flags to guess!")
                        running = False
                else:
                    print("Incorrect! Try again.")
                    screen.blit(font2.render("Incorrect!", True, "black"), (10, 50))
                    pg.display.flip()
                    t.sleep(1)
            elif event.key == pg.K_ESCAPE:
                textinput_visualizer.value = ""  # Clear the text input when backspace or escape is pressed

    screen.fill("grey")

    screen.blit(europe_map, (0, 0))

    # Calculate the position to center the flag on the screen
    flag_rect = flag.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))

    # Display the current flag to guess
    screen.blit(flag, flag_rect.topleft)

    # Calculate the position to center the text input box below the flag
    textinput_rect = textinput_visualizer.surface.get_rect(center=(screen.get_width() // 2, flag_rect.bottom + 30))

    # Draw the text input box
    screen.blit(textinput_visualizer.surface, textinput_rect.topleft)

    screen.blit(font1.render(f"Remaining Countries: {len(flags)}", True, "black"), (10, 10))

    pg.display.flip()
    clock.tick(60)

pg.quit()