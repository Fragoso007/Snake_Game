import pygame
import random

pygame.init()
pygame.display.set_caption('Snake Python Game')
largura, altura = 600, 400
screen = pygame.display.set_mode((largura, altura))
relogio = pygame.time.Clock()

preta = (0,0,0)
branca = (255,255,255)
vermelha = (255,0,0)
verde = (0,255,0)

snake_size = 10
snake_speed = 20

def run_game():
    end_game = False

    while not end_game:
        screen.fill(preta)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                end_game = True