# coding: utf-8

import pygame
from pygame.locals import *

class Muro(object):
	def __init__(self, x, y):
		self.image = pygame.image.load('static/images/muro_dark_side.jpg').convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.top, self.rect.left = y, x
		self.x = x
		self.y = y

	def draw(self, surface):
		surface.blit(self.image, (self.x, self.y))
