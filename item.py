# coding: utf-8

import pygame
from pygame.locals import *

class Item(object):
	def __init__(self, x, y, res):
		self.image = pygame.image.load(res)
		self.rect = self.image.get_rect()
		self.rect.top, self.rect.left = y, x
		self.x = x
		self.y = y

	def draw(self, surface):
		surface.blit(self.image, (self.x, self.y))
