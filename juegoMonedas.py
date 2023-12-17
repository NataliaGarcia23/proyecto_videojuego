import pygame
import sys
import random

# Configuración inicial
pygame.init()
screen_width = 400
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Juego monedas")
white = (255, 255, 255)
black = (0, 0, 0)
fondo = pygame.image.load("imagenes/fondoArena.jpg")
fondo = pygame.transform.scale(fondo, (screen_width, screen_height))
tamaño_pirata = 40
velocidad_pirata = 8
imagen_pirata = pygame.image.load('imagenes/pirata.png')
imagen_pirata = pygame.transform.scale(imagen_pirata, (tamaño_pirata, tamaño_pirata))
pirata_x = screen_width // 2
pirata_y = screen_height // 2
pirata_dx = 0
pirata_dy = 0
pirata = [(pirata_x, pirata_y)]
moneda = pygame.image.load('imagenes/moneda.png')
moneda = pygame.transform.scale(moneda, (tamaño_pirata, tamaño_pirata))
moneda_x = random.randint(0, (screen_width - tamaño_pirata) // tamaño_pirata) * tamaño_pirata
moneda_y = random.randint(0, (screen_height - tamaño_pirata) // tamaño_pirata) * tamaño_pirata
img_salir = pygame.image.load("imagenes/salir.png")
img_salir = pygame.transform.scale(img_salir, (30, 30))
btn_salir_rect = img_salir.get_rect(topleft=(screen_width - 60, 20))
puntos = 0
font = pygame.font.Font(None, 36)
def mostrar_puntos(x, y):
    score_display = font.render("Puntuación: " + str(puntos), True, white)
    screen.blit(score_display, (x, y))

# Bucle principal
running = True
while running:
    screen.blit(fondo, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and pirata_dy == 0:
                pirata_dx = 0
                pirata_dy = -tamaño_pirata
            if event.key == pygame.K_DOWN and pirata_dy == 0:
                pirata_dx = 0
                pirata_dy = tamaño_pirata
            if event.key == pygame.K_LEFT and pirata_dx == 0:
                pirata_dx = -tamaño_pirata
                pirata_dy = 0
            if event.key == pygame.K_RIGHT and pirata_dx == 0:
                pirata_dx = tamaño_pirata
                pirata_dy = 0

        if event.type == pygame.MOUSEBUTTONDOWN and btn_salir_rect.collidepoint(event.pos):
            running = False

    pirata_x += pirata_dx
    pirata_y += pirata_dy

    if pirata_x == moneda_x and pirata_y == moneda_y:
        moneda_x = random.randint(0, (screen_width - tamaño_pirata) // tamaño_pirata) * tamaño_pirata
        moneda_y = random.randint(0, (screen_height - tamaño_pirata) // tamaño_pirata) * tamaño_pirata
        puntos += 1
    else:
        pirata.pop()

    if (
        pirata_x < 0
        or pirata_x >= screen_width
        or pirata_y < 0
        or pirata_y >= screen_height
        or (pirata_x, pirata_y) in pirata
    ):
        running = False

    pirata.insert(0, (pirata_x, pirata_y))

    for segment in pirata:
        screen.blit(imagen_pirata, (segment[0], segment[1]))

    screen.blit(moneda, (moneda_x, moneda_y))
    mostrar_puntos(10, 10)

    screen.blit(img_salir, (screen_width - 60, 20))
    pygame.display.flip()
    pygame.time.Clock().tick(velocidad_pirata)

    if puntos >= 5:
        small_font = pygame.font.Font(None, 18)
        mensaje = small_font.render('Felicidades, has resuelto el juego. El segundo dígito es el 7', True, black)
        mensaje_rect = mensaje.get_rect(midtop=(screen_width // 2, screen_height // 4))
        screen.blit(mensaje, mensaje_rect)
        pygame.display.flip()
        pygame.time.wait(3000)
        running = False

pygame.quit()
sys.exit()
