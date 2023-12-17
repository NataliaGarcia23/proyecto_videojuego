import pygame
import sys
import time

# Configuración inicial
pygame.init()
width, height = 800, 600
WHITE = (255, 255, 255)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Juego Laberinto")
BLACK = (0, 0, 0)
player_x, player_y = 1, 1
exit_x, exit_y = 8, 9
laberinto_resuelto = False
font = pygame.font.Font(None, 24)
fondo = pygame.image.load("imagenes/fondoArena.jpg")
fondo = pygame.transform.scale(fondo, (width, height))
circulo_img = pygame.image.load("imagenes/pirata2.png")
circulo_img = pygame.transform.scale(circulo_img, (40, 40))

# Crear imagen laberinto (1 = pared, 0 = pasillo)
laberinto = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 1, 0, 1, 0, 1],
    [1, 1, 1, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 1, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 1]
]

# Bucle principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_UP and laberinto[player_y - 1][player_x] == 0:
                player_y -= 1
            elif event.key == pygame.K_DOWN and laberinto[player_y + 1][player_x] == 0:
                player_y += 1
            elif event.key == pygame.K_LEFT and laberinto[player_y][player_x - 1] == 0:
                player_x -= 1
            elif event.key == pygame.K_RIGHT and laberinto[player_y][player_x + 1] == 0:
                player_x += 1
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if btn_salir.collidepoint(event.pos):
                running = False

    if player_x == exit_x and player_y == exit_y:
        mensaje = font.render('Felicidades, has resuelto el laberinto. El primer dígito es el 4', True, BLACK)
        screen.blit(mensaje, (width // 4, height // 1.2))
        pygame.display.flip()
        pygame.time.wait(3000)
        laberinto_resuelto = True

    screen.fill(WHITE)

    screen.blit(fondo, (0, 0))
    for y, row in enumerate(laberinto):
        for x, cell in enumerate(row):
            if cell == 1:
                pygame.draw.rect(screen, BLACK, (x * 40, y * 40, 40, 40)) 
            elif x == player_x and y == player_y:
                screen.blit(circulo_img, (x * 40, y * 40))

    img_salir = pygame.image.load("imagenes/salir.png")
    img_salir = pygame.transform.scale(img_salir, (30, 30))
    btn_salir = screen.blit(img_salir, (width - 60, 20))

    pygame.display.flip()

    if laberinto_resuelto:
        time.sleep(1)
        running = False

pygame.quit()
sys.exit()
