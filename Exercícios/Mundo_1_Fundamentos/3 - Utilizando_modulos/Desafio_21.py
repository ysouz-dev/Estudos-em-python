#Desafio: Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

print('=====Desafio 21=====')
import pygame
nome = str(input('Seja bem vindo! Qual seu nome para começarmos? '))
print('Olá {}, seja bem vindo ao nosso programa!'.format(nome))
pygame.init()
pygame.mixer_music.load('Sound_Desafio_21.mp3')
pygame.mixer_music.play(loops=1, )
pygame.mixer_music.set_volume(1)
input()
pygame.event.wait()