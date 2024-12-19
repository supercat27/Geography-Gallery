import pygame as pg


pg.init()

screen = pg.display.set_mode((1100, 880))
pg.display.set_caption("Guess the European Country!")

europe_map = pg.image.load("assets/europe_map_png.png")

class highlight:
    def __init__(self, country, path):
        self.country = country
        self.path = path
        self.image = pg.image.load(path).convert_alpha()

countries = {
    "Albania": highlight("Albania", "assets/albania.png"),
    "Andorra": highlight("Andorra", "assets/andorra.png"),
    "Armenia": highlight("Armenia", "assets/armenia.png"),
    "Austria": highlight("Austria", "assets/austria.png"),
    "Azerbaijan": highlight("Azerbaijan", "assets/azerbaijan.png"),
    "Belarus": highlight("Belarus", "assets/belarus.png"),
    "Belgium": highlight("Belgium", "assets/belgium.png"),
    "Bosnia and Herzegovina": highlight("Bosnia and Herzegovina", "assets/bosnia.png"),
    "Bulgaria": highlight("Bulgaria", "assets/bulgaria.png"),
    "Croatia": highlight("Croatia", "assets/croatia.png"),
    "Cyprus": highlight("Cyprus", "assets/cyprus.png"),
    "Czech Republic": highlight("Czech Republic", "assets/czech.png"),
    "Denmark": highlight("Denmark", "assets/denmark.png"),
    "Estonia": highlight("Estonia", "assets/estonia.png"),
    "Finland": highlight("Finland", "assets/finland.png"),
    "France": highlight("France", "assets/france.png"),
    "Georgia": highlight("Georgia", "assets/georgia.png"),
    "Germany": highlight("Germany", "assets/germany.png"),
    "Greece": highlight("Greece", "assets/greece.png"),
    "Hungary": highlight("Hungary", "assets/hungary.png"),
    "Iceland": highlight("Iceland", "assets/iceland.png"),
    "Ireland": highlight("Ireland", "assets/ireland.png"),
    "Italy": highlight("Italy", "assets/italy.png"),
    "Kosovo": highlight("Kosovo", "assets/kosovo.png"),
    "Latvia": highlight("Latvia", "assets/latvia.png"),
    "Liechtenstein": highlight("Liechtenstein", "assets/liechtenstein.png"),
    "Lithuania": highlight("Lithuania", "assets/lithuania.png"),
    "Luxembourg": highlight("Luxembourg", "assets/luxembourg.png"),
    "Moldova": highlight("Moldova", "assets/moldova.png"),
    "Montenegro": highlight("Montenegro", "assets/montenegro.png"),
    "Netherlands": highlight("Netherlands", "assets/netherlands.png"),
    "North Macedonia": highlight("North Macedonia", "assets/macedonia.png"),
    "Norway": highlight("Norway", "assets/norway.png"),
    "Poland": highlight("Poland", "assets/poland.png"),
    "Portugal": highlight("Portugal", "assets/portugal.png"),
    "Romania": highlight("Romania", "assets/romania.png"),
    "Russia": highlight("Russia", "assets/russia.png"),
    "Serbia": highlight("Serbia", "assets/serbia.png"), 
    "Slovakia": highlight("Slovakia", "assets/slovakia.png"),
    "Slovenia": highlight("Slovenia", "assets/slovenia.png"),
    "Spain": highlight("Spain", "assets/spain.png"),
    "Sweden": highlight("Sweden", "assets/sweden.png"),
    "Switzerland": highlight("Switzerland", "assets/switzerland.png"),
    "Turkiye": highlight("Turkiye", "assets/turkiye.png"),
    "Ukraine": highlight("Ukraine", "assets/ukraine.png"),
    "United Kingdom": highlight("United Kingdom", "assets/uk.png"),

}


class Textbox:
    def __init__(self, x, y, width, height, color, text=""):
        self.rect = pg.Rect(x, y, width, height)
        self.color = pg.Color(color)
        self.text = ''
        self.txt_surface = pg.font.Font(None, 32).render(text, True, self.color)
        self.active = False











country_name = "Germany"
country_highlight = countries[country_name]
print(f"Country: {country_highlight.country}, Path: {country_highlight.path}")

running = True

clock = pg.time.Clock()

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    screen.fill("white")
    screen.blit(europe_map, (0, 0))

    # Example of blitting a country image
    screen.fill("white")
    screen.blit(country_highlight.image, (0, 0))

    pg.display.flip()
    clock.tick(60) 

pg.quit()
