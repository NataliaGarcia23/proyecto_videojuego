import pygame
import sys
import random
import time

# Configuración inicial
pygame.init()
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Juego de Disparar")
fondo = pygame.image.load("imagenes/fondoArena.jpg")
fondo = pygame.transform.scale(fondo, (screen_width, screen_height))
font = pygame.font.Font(None, 36)
small_font = pygame.font.Font(None, 24)
target_images = ["imagenes/pirata.png"]
img_salir = pygame.image.load("imagenes/salir.png")
img_salir = pygame.transform.scale(img_salir, (30, 30))
btn_salir_rect = img_salir.get_rect(topleft=(screen_width - 60, 20))
puntuacion = 0
objetivo_image, objetivo_rect = None, None

# Bucle principal
clock = pygame.time.Clock()
tiempo_inicial = time.time()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if objetivo_rect and objetivo_rect.collidepoint(x, y):
                puntuacion += 1
                objetivo_image = pygame.image.load(random.choice(target_images))
                objetivo_rect = objetivo_image.get_rect()
                objetivo_rect.x = random.randint(50, screen_width - 50)
                objetivo_rect.y = random.randint(50, screen_height - 50)
            elif btn_salir_rect.collidepoint(x, y):
                pygame.quit()
                sys.exit()

    tiempo_actual = time.time()
    tiempo_transcurrido = tiempo_actual - tiempo_inicial

    if tiempo_transcurrido > 1 or objetivo_image is None:
        objetivo_image = pygame.image.load(random.choice(target_images))
        objetivo_rect = objetivo_image.get_rect()
        objetivo_rect.x = random.randint(50, screen_width - 50)
        objetivo_rect.y = random.randint(50, screen_height - 50)
        tiempo_inicial = time.time()

    if puntuacion >= 5:
        mensaje = small_font.render('Felicidades, has resuelto el juego. El tercer dígito es el 8', True, BLACK)
        mensaje_rect = mensaje.get_rect(center=(screen_width // 2, screen_height // 2))
        screen.blit(mensaje, mensaje_rect)
        pygame.display.flip()
        pygame.time.wait(3000)
        pygame.quit()
        sys.exit()

    screen.blit(fondo, (0, 0))

    objetivo_rect.x = max(50, min(objetivo_rect.x, screen_width - 50))
    objetivo_rect.y = max(50, min(objetivo_rect.y, screen_height - 50))
    screen.blit(objetivo_image, objetivo_rect)
    puntuacion_texto = font.render("Puntuación: {}".format(puntuacion), True, BLACK)
    screen.blit(puntuacion_texto, (50, 50))
    screen.blit(img_salir, (screen_width - 60, 20))

    pygame.display.flip()
    clock.tick(60)

