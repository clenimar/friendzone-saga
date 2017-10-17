# coding: utf-8

import pygame
import random
from pygame.locals import *

class Inimigo(object):
	def __init__(self, mapa, posicao):
		self.imagem = pygame.image.load('inimigo.png')
		self.x, self.y = posicao
		self.mapa = mapa
		self.rect = self.imagem.get_rect()
		self.rect.top, self.rect.left = self.y, self.x
		self.direcao = random.randint(0,3)
		self.velocidade = 3
		
	def mover(self):
		tecla = pygame.key.get_pressed()

		if self.direcao == 0:
			if not(self.mapa.colisao_muro(self.rect.move(0, -self.velocidade))):
				self.y -= self.velocidade
				self.rect.move_ip(0, -self.velocidade)
			else:
				self.direcao = random.randint(0,3)
		elif self.direcao == 1:
			if not(self.mapa.colisao_muro(self.rect.move(0, self.velocidade))):
				self.y += self.velocidade
				self.rect.move_ip(0, self.velocidade)
			else:
				self.direcao = random.randint(0,3)
		if self.direcao == 2:
			if not(self.mapa.colisao_muro(self.rect.move(self.velocidade, 0))):
				self.x += self.velocidade
				self.rect.move_ip(self.velocidade,0)
			else:
				self.direcao = random.randint(0,3)
		elif self.direcao == 3:
			if not(self.mapa.colisao_muro(self.rect.move(-self.velocidade, 0))):
				self.x -= self.velocidade
				self.rect.move_ip(-self.velocidade, 0)
			else:
				self.direcao = random.randint(0,3)

	def draw(self, surface, imagem):
		surface.blit(pygame.image.load('%s' % imagem), (self.x, self.y))
