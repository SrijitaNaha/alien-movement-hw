import pgzrun

TITLE = "Alien Movement"
WIDTH, HEIGHT = 800, 600

alien = Actor('alien')
alien.pos = 400, 300

alien_y_speed = 2

def draw():
    screen.clear()
    screen.fill(("#FFD23F"))
    alien.draw()

def update():
    global alien_y_speed
    alien.y += alien_y_speed
    if alien.top < 0 or alien.bottom > HEIGHT:
        alien_y_speed = -alien_y_speed

pgzrun.go()