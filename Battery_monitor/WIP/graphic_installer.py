import pygame
from pygame.locals import *
import subprocess

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Config Editor")

# Importa il modulo config
import test_file_py as config

font = pygame.font.Font(None, 36)

running = True
selected_menu_item = 0  # 0 rappresenta il valore da modificare, 1 rappresenta "Install", 2 rappresenta "Exit"

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_UP:
                selected_menu_item = (selected_menu_item - 1) % 3
            elif event.key == K_DOWN:
                selected_menu_item = (selected_menu_item + 1) % 3
            elif event.key == K_RETURN:
                if selected_menu_item == 0:
                    # Modifica il valore in config.py
                    config.value_to_modify += 1
                elif selected_menu_item == 1:
                    # Esegui lo script di installazione
                    install_script = subprocess.Popen(["bash", "install_script.sh"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                    install_output, install_error = install_script.communicate()
                    if install_script.returncode == 0:
                        print("Installazione completata con successo.")
                        print(install_output)
                    else:
                        print("Errore durante l'installazione.")
                        print(install_error)
                    input("Premi Invio per continuare.")
                elif selected_menu_item == 2:
                    running = False

    # Rappresenta il valore corrente
    value_text = font.render(f"Value to Modify: {config.value_to_modify}", True, (255, 255, 255))
    install_text = font.render("Install", True, (255, 255, 255))
    exit_text = font.render("Exit", True, (255, 255, 255))

    screen.fill((0, 0, 0))

    # Rappresenta il menu
    if selected_menu_item == 0:
        pygame.draw.rect(screen, (255, 0, 0), (50, 50, 300, 50))
        pygame.draw.rect(screen, (0, 0, 0), (50, 150, 300, 50))
        pygame.draw.rect(screen, (0, 0, 0), (50, 250, 300, 50))
    elif selected_menu_item == 1:
        pygame.draw.rect(screen, (0, 0, 0), (50, 50, 300, 50))
        pygame.draw.rect(screen, (255, 0, 0), (50, 150, 300, 50))
        pygame.draw.rect(screen, (0, 0, 0), (50, 250, 300, 50))
    elif selected_menu_item == 2:
        pygame.draw.rect(screen, (0, 0, 0), (50, 50, 300, 50))
        pygame.draw.rect(screen, (0, 0, 0), (50, 150, 300, 50))
        pygame.draw.rect(screen, (255, 0, 0), (50, 250, 300, 50))

    screen.blit(value_text, (50, 50))
    screen.blit(install_text, (50, 150))
    screen.blit(exit_text, (50, 250))

    pygame.display.flip()

pygame.quit()
