#Tocando mp3
import pygame
pygame.init()
pygame.mixer.music.load('Froid - Bicho de 7 Cabecas A Culpa e das Igrejas.mp3')
pygame.mixer.music.play()
pygame.event.wait()

