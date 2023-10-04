import pygame
import pygame_menu
import subprocess

X_RESOLUTION = 800
Y_RESOLUTION = 480

pygame.init()
surface = pygame.display.set_mode((X_RESOLUTION, Y_RESOLUTION))

def set_difficulty(value, difficulty):
    # Do the job here !
    pass

def start_the_game():
    # Do the job here !
    pass

def install_pip():
    update_process = subprocess.Popen('sudo apt-get update', stdout=subprocess.PIPE, shell=True)
    update_output, error = update_process.communicate()
    pip_install_process = subprocess.Popen('sudo apt-get install python-pip', stdout=subprocess.PIPE, shell=True)
    pip_install_output, error = pip_install_process.communicate()
    output = update_output + b"\n\n" + pip_install_output
    output_text = output.decode('utf-8')
    print(output_text)

    font = pygame.font.Font(None, 20)
    output_lines = output_text.split("\n")
    for i, line in enumerate(output_lines):
        text = font.render(line, True, pygame.Color("white"))
        surface.blit(text, (20, 200 + 20 * i))

def install_batt_mon():
    pass

def install_disp_inf():
    pass


menu = pygame_menu.Menu('Silver-Boy settings', X_RESOLUTION, Y_RESOLUTION,
                       theme=pygame_menu.themes.THEME_BLUE)

menu.add.text_input('Name : ', default='John Doe')
menu.add.selector('Difficulty :', [('Hard', 1), ('Easy', 2)], onchange=set_difficulty)
menu.add.button('Install Python-PIP', install_pip)
menu.add.button('Install Battery-Monitor', install_batt_mon)
menu.add.button('Install Display-Info', install_disp_inf)
menu.add.button('Quit', pygame_menu.events.EXIT)

menu.mainloop(surface)