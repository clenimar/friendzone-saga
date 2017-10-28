# coding: utf-8

import pygame
from pygame.locals import *

class Garota(object):
	def __init__(self, mapa, imagem):
		self.image = pygame.image.load(imagem)
		self.x = 544
		self.y = 432
		self.mapa = mapa
		self.rect = self.image.get_rect()
		self.rect.top, self.rect.left = self.y, self.x
		self.velocidader = 4
		
	def mover(self):
		tecla = pygame.key.get_pressed()
		
		if tecla[K_DOWN] and not(self.mapa.colisao_muro(self.rect.move(0, -self.velocidader))) and not(self.mapa.colisaoCadeadoFechado(self.rect.move(0, -self.velocidader), True)):
			self.y -= self.velocidader
			self.rect.move_ip(0, -self.velocidader)
		elif tecla[K_UP] and not(self.mapa.colisao_muro(self.rect.move(0, self.velocidader))) and not(self.mapa.colisaoCadeadoFechado(self.rect.move(0, self.velocidader), True)):
			self.y += self.velocidader
			self.rect.move_ip(0, self.velocidader)
		if tecla[K_LEFT] and not(self.mapa.colisao_muro(self.rect.move(self.velocidader, 0))) and not(self.mapa.colisaoCadeadoFechado(self.rect.move(self.velocidader, 0), True)):
			self.x += self.velocidader
			self.rect.move_ip(self.velocidader,0)
		elif tecla[K_RIGHT] and not(self.mapa.colisao_muro(self.rect.move(-self.velocidader, 0))) and not(self.mapa.colisaoCadeadoFechado(self.rect.move(-self.velocidader, 0), True)):
			self.x -= self.velocidader
			self.rect.move_ip(-self.velocidader, 0)

	def draw(self, surface):
		for i in range(2):
			surface.blit(self.image, (self.x, self.y))
