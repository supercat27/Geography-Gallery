import pygame as pg
import random
import pygame_textinput
import time as t

# Initialize Pygame
pg.init()
pg.font.init()

# Set up the display
screen = pg.display.set_mode((1100, 880))
pg.display.set_caption("Guess the European Country!")

# Initialize fonts
font1 = pg.font.SysFont("Times New Roman", 36)
font2 = pg.font.SysFont("Times New Roman", 48)

# Load the map of Europe
europe_map = pg.image.load("assets/europe_map_png.png")

# Initialize text input
textinput_manager = pygame_textinput.TextInputManager()
textinput_visualizer = pygame_textinput.TextInputVisualizer(manager=textinput_manager, font_object=font1)

# Define a class to highlight countries
class highlight:
    def __init__(self, country, path):
        self.country = country
        self.path = path
        self.image = pg.image.load(path).convert_alpha()

# Dictionary to store country highlights
countries = {
    "Albania": highlight("Albania", "assets/europe_highlight/albania.png"),
    "Andorra": highlight("Andorra", "assets/europe_highlight/andorra.png"),
    "Armenia": highlight("Armenia", "assets/europe_highlight/armenia.png"),
    "Austria": highlight("Austria", "assets/europe_highlight/austria.png"),
    "Azerbaijan": highlight("Azerbaijan", "assets/europe_highlight/azerbaijan.png"),
    "Belarus": highlight("Belarus", "assets/europe_highlight/belarus.png"),
    "Belgium": highlight("Belgium", "assets/europe_highlight/belgium.png"),
    "Bosnia and Herzegovina": highlight("Bosnia and Herzegovina", "assets/europe_highlight/bosnia.png"),
    "Bulgaria": highlight("Bulgaria", "assets/europe_highlight/bulgaria.png"),
    "Croatia": highlight("Croatia", "assets/europe_highlight/croatia.png"),
    "Cyprus": highlight("Cyprus", "assets/europe_highlight/cyprus.png"),
    "Czech Republic": highlight("Czech Republic", "assets/europe_highlight/czech.png"),
    "Denmark": highlight("Denmark", "assets/europe_highlight/denmark.png"),
    "Estonia": highlight("Estonia", "assets/europe_highlight/estonia.png"),
    "Finland": highlight("Finland", "assets/europe_highlight/finland.png"),
    "France": highlight("France", "assets/europe_highlight/france.png"),
    "Georgia": highlight("Georgia", "assets/europe_highlight/georgia.png"),
    "Germany": highlight("Germany", "assets/europe_highlight/germany.png"),
    "Greece": highlight("Greece", "assets/europe_highlight/greece.png"),
    "Hungary": highlight("Hungary", "assets/europe_highlight/hungary.png"),
    "Iceland": highlight("Iceland", "assets/europe_highlight/iceland.png"),
    "Ireland": highlight("Ireland", "assets/europe_highlight/ireland.png"),
    "Italy": highlight("Italy", "assets/europe_highlight/italy.png"),
    "Kosovo": highlight("Kosovo", "assets/europe_highlight/kosovo.png"),
    "Latvia": highlight("Latvia", "assets/europe_highlight/latvia.png"),
    "Liechtenstein": highlight("Liechtenstein", "assets/europe_highlight/liechtenstein.png"),
    "Lithuania": highlight("Lithuania", "assets/europe_highlight/lithuania.png"),
    "Luxembourg": highlight("Luxembourg", "assets/europe_highlight/luxembourg.png"),
    "Moldova": highlight("Moldova", "assets/europe_highlight/moldova.png"),
    "Montenegro": highlight("Montenegro", "assets/europe_highlight/montenegro.png"),
    "Netherlands": highlight("Netherlands", "assets/europe_highlight/netherlands.png"),
    "North Macedonia": highlight("North Macedonia", "assets/europe_highlight/macedonia.png"),
    "Norway": highlight("Norway", "assets/europe_highlight/norway.png"),
    "Poland": highlight("Poland", "assets/europe_highlight/poland.png"),
    "Portugal": highlight("Portugal", "assets/europe_highlight/portugal.png"),
    "Romania": highlight("Romania", "assets/europe_highlight/romania.png"),
    "Russia": highlight("Russia", "assets/europe_highlight/russia.png"),
    "Serbia": highlight("Serbia", "assets/europe_highlight/serbia.png"), 
    "Slovakia": highlight("Slovakia", "assets/europe_highlight/slovakia.png"),
    "Slovenia": highlight("Slovenia", "assets/europe_highlight/slovenia.png"),
    "Spain": highlight("Spain", "assets/europe_highlight/spain.png"),
    "Sweden": highlight("Sweden", "assets/europe_highlight/sweden.png"),
    "Switzerland": highlight("Switzerland", "assets/europe_highlight/switzerland.png"),
    "Turkiye": highlight("Turkiye", "assets/europe_highlight/turkiye.png"),
    "Ukraine": highlight("Ukraine", "assets/europe_highlight/ukraine.png"),
    "United Kingdom": highlight("United Kingdom", "assets/europe_highlight/uk.png"),
}

# Function to select a new country
def select_new_country():
    return random.choice(list(countries.keys()))

# Select the first country
country_name = select_new_country()
country_highlight = countries[country_name]
# Main loop flag
running = True

# Clock to control the frame rate
clock = pg.time.Clock()

# Main loop
while running:
    events = pg.event.get()  # Get all events
    for event in events:
        if event.type == pg.QUIT:  # Check if the user wants to quit
            running = False

    # Update text input with the list of events
    textinput_visualizer.update(events)

    # Check if the user has pressed Enter or Backspace
    for event in events:
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RETURN:
                guess = textinput_visualizer.value.lower()
                textinput_visualizer.value = ""
                if guess == country_highlight.country.lower():  # Check if the guess is correct
                    screen.blit(font2.render("Correct!", True, "black"), (10, 50))  # Render "Correct!" on the screen
                    pg.display.flip()  # Update the display to show the "Correct!" message
                    t.sleep(1)  # Pause for a moment to allow the user to see the message
                    del countries[country_name]  # Remove the correctly guessed country from the list
                    country_name = select_new_country()  # Select a new country
                    country_highlight = countries[country_name]  # Update the highlighted country5
                else:
                    screen.blit(font2.render("Incorrect!", True, "black"), (10, 50))  # Render "Incorrect!" on the screen
                    pg.display.flip()
                    t.sleep(1)
            elif event.key == pg.K_ESCAPE:
                textinput_visualizer.value = ""  # Clear the text input when backspace is pressed

    # Fill the screen with white
    screen.fill("white")

    # Blit the current country image
    screen.blit(country_highlight.image, (0, 0))

    # Draw the text input box
    screen.blit(textinput_visualizer.surface, (10, 835))

    # Display the remaining countries count
    screen.blit(font1.render(f"Remaining Countries: {len(countries)}", True, "black"), (10, 10))

    # Update the display
    pg.display.flip()

    # Cap the frame rate at 60 FPS
    clock.tick(60)

# Quit Pygame
pg.quit()