import pygame
import sys

pygame.init()

# Configuración inicial
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Juego de Contraseña")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
fondo = pygame.image.load("imagenes/fondoArena.jpg")
fondo = pygame.transform.scale(fondo, (screen_width, screen_height))
font = pygame.font.Font(None, 36)
contrasena_correcta = "478"
imagen_path = "imagenes/cofre_resuelto.png"
imagen = pygame.image.load(imagen_path)
imagen = pygame.transform.scale(imagen, (300, 300))
img_salir = pygame.image.load("imagenes/salir.png")
img_salir = pygame.transform.scale(img_salir, (30, 30))
btn_salir_rect = img_salir.get_rect(topleft=(screen_width - 60, 20))

# Bucle principal
clock = pygame.time.Clock()
input_box = pygame.Rect(50, 100, 200, 30)
input_text = ""

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if input_text == contrasena_correcta:
                    mensaje = font.render("¡Enhorabuena! Has conseguido el tesoro.", True, BLACK)
                    screen.blit(mensaje, (50, 150))
                    pygame.display.flip()
                    pygame.time.wait(3000)
                    screen.blit(imagen, (300, 200))
                    pygame.display.flip()
                    pygame.time.wait(3000)
                    pygame.quit()
                    sys.exit()
                else:
                    mensaje = font.render("Contraseña incorrecta. Vuelve a intentarlo.", True, BLACK)
                    screen.blit(mensaje, (50, 150))
                    pygame.display.flip()
                    pygame.time.wait(2000)
                    input_text = ""
            elif event.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]
            else:
                input_text += event.unicode

        elif event.type == pygame.MOUSEBUTTONDOWN and btn_salir_rect.collidepoint(event.pos):
            pygame.quit()
            sys.exit()

    screen.blit(fondo, (0, 0))

    instrucciones = font.render("Ingresa la contraseña de 3 dígitos:", True, BLACK)
    screen.blit(instrucciones, (50, 50))
    pygame.draw.rect(screen, BLACK, input_box, 2)
    txt_surface = font.render(input_text, True, BLACK)
    width = max(200, txt_surface.get_width()+10)
    input_box.w = width
    screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
    screen.blit(img_salir, (screen_width - 60, 20))

    pygame.display.flip()
    clock.tick(30)
