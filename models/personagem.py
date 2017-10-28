# coding: utf-8

import pygame
import mapa
from pygame.locals import *

class Heroi(object):
	def __init__(self, mapa, imagem):
		self.image = pygame.image.load(imagem)
		self.x = 32
		self.y = 24
		self.mapa = mapa
		self.rect = self.image.get_rect()
		self.rect.top, self.rect.left = self.y, self.x
		self.velocidade = 4
		
		
		
	def mover(self):
		tecla = pygame.key.get_pressed()
		
		if tecla[K_DOWN] and not(self.mapa.colisao_muro(self.rect.move(0, self.velocidade))) and not(self.mapa.colisaoCadeadoFechado(self.rect.move(0, self.velocidade))):
			self.y += self.velocidade
			self.rect.move_ip(0, self.velocidade)
		elif tecla[K_UP] and not(self.mapa.colisao_muro(self.rect.move(0, -self.velocidade)))  and not(self.mapa.colisaoCadeadoFechado(self.rect.move(0, -self.velocidade))):
			self.y -= self.velocidade
			self.rect.move_ip(0, -self.velocidade)
		if tecla[K_LEFT] and not(self.mapa.colisao_muro(self.rect.move(-self.velocidade, 0))) and not(self.mapa.colisaoCadeadoFechado(self.rect.move(-self.velocidade, 0))):
			self.x -= self.velocidade
			self.rect.move_ip(-self.velocidade,0)
		elif tecla[K_RIGHT] and not(self.mapa.colisao_muro(self.rect.move(self.velocidade, 0))) and not(self.mapa.colisaoCadeadoFechado(self.rect.move(self.velocidade, 0))):
			self.x += self.velocidade
			self.rect.move_ip(self.velocidade, 0)

	def draw(self, surface):
		surface.blit(self.image, (self.x, self.y))
