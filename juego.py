import pygame
import sys
import subprocess
import time

# Configuración inicial
pygame.init()
width, height = 800, 600  
screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
mar_imagen = pygame.image.load('imagenes/mar.jpg')
mar_imagen = pygame.transform.scale(mar_imagen, (width, height))
barco_imagen = pygame.image.load('imagenes/barco.png')
barco_imagen = pygame.transform.scale(barco_imagen, (100, 100))
isla1_imagen = pygame.image.load('imagenes/isla1.png')
isla1_imagen = pygame.transform.scale(isla1_imagen, (100, 100))
isla2_imagen = pygame.image.load('imagenes/isla2.png')
isla2_imagen = pygame.transform.scale(isla2_imagen, (100, 100))
isla3_imagen = pygame.image.load('imagenes/isla3.png')
isla3_imagen = pygame.transform.scale(isla3_imagen, (100, 100))
cofre_imagen = pygame.image.load('imagenes/cofre.png')
cofre_imagen = pygame.transform.scale(cofre_imagen, (100, 100))
img_salir = pygame.image.load("imagenes/salir.png")
img_salir = pygame.transform.scale(img_salir, (30, 30))
btn_salir_rect = img_salir.get_rect(topleft=(width - 60, 20))
barco_x, barco_y = width // 10, height // 2
isla1_x, isla1_y = width // 4, height // 4
isla2_x, isla2_y = width // 1.5, height // 40
isla3_x, isla3_y = width // 2, height // 1.5
cofre_x, cofre_y = width // 1.5, height // 4
ejecutar_juegoLaberinto = False
ejecutar_juegoMonedas = False
ejecutar_juegoDisparar = False
ejecutar_cofre = False

# Bucle principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if isla1_x <= event.pos[0] <= isla1_x + 100 and isla1_y <= event.pos[1] <= isla1_y + 100:
                destination_x, destination_y = isla1_x, isla1_y
                ejecutar_juegoLaberinto = True
            elif isla2_x <= event.pos[0] <= isla2_x + 100 and isla2_y <= event.pos[1] <= isla2_y + 100:
                destination_x, destination_y = isla2_x, isla2_y
                ejecutar_juegoMonedas = True
            elif isla3_x <= event.pos[0] <= isla3_x + 100 and isla3_y <= event.pos[1] <= isla3_y + 100:
                destination_x, destination_y = isla3_x, isla3_y
                ejecutar_juegoDisparar = True
            elif cofre_x <= event.pos[0] <= cofre_x + 100 and cofre_y <= event.pos[1] <= cofre_y + 100:
                destination_x, destination_y = cofre_x, cofre_y
                ejecutar_cofre = True
            elif btn_salir_rect.collidepoint(event.pos):
                running = False

            step_x, step_y = (destination_x - barco_x) / 50, (destination_y - barco_y) / 50

            for _ in range(50):
                barco_x += step_x
                barco_y += step_y
                screen.blit(mar_imagen, (0, 0))
                screen.blit(isla1_imagen, (isla1_x, isla1_y))
                screen.blit(isla2_imagen, (isla2_x, isla2_y))
                screen.blit(isla3_imagen, (isla3_x, isla3_y))
                screen.blit(cofre_imagen, (cofre_x, cofre_y))
                screen.blit(barco_imagen, (barco_x, barco_y))
                screen.blit(img_salir, (width - 100, 20))
                pygame.display.flip()

    if ejecutar_juegoLaberinto:
        time.sleep(1)
        subprocess.run(["python", "juegoLaberinto.py"])
        ejecutar_juegoLaberinto = False
    elif ejecutar_juegoMonedas:
        time.sleep(1)
        subprocess.run(["python", "juegoMonedas.py"])
        ejecutar_juegoMonedas = False
    elif ejecutar_juegoDisparar:
        time.sleep(1)
        subprocess.run(["python", "juegoDisparar.py"])
        ejecutar_juegoDisparar = False
    elif ejecutar_cofre:
        time.sleep(1)
        subprocess.run(["python", "cofre.py"])
        ejecutar_cofre = False

    screen.blit(mar_imagen, (0, 0))
    screen.blit(isla1_imagen, (isla1_x, isla1_y))
    screen.blit(isla2_imagen, (isla2_x, isla2_y))
    screen.blit(isla3_imagen, (isla3_x, isla3_y))
    screen.blit(cofre_imagen, (cofre_x, cofre_y))
    screen.blit(barco_imagen, (barco_x, barco_y))
    screen.blit(img_salir, (width - 60, 20))
    pygame.display.flip()

pygame.quit()
sys.exit()

