
# coding: utf-8

import pygame
from muro import *
from item import *
from pygame.locals import *

class Mapa(object):
	def __init__(self, nivel):
		
		if nivel == 1:
			
			self.coord = ['oooooooooooooooooooo',
			'o--------oo--------o',
			'o-ooo-oo-oo-oo-ooo-o',
			'o-ooo----------ooo-o',
			'o-----oooooooo-----o',
			'o-o-o----4-----o-o-o',
			'o-o---ooooo5oo---o-o',
			'o-o-o-oo6oo-oo-o-o-o',
			'o-----oo----oo-----o',
			'ooo-o-oooooooo-o-ooo',
			'o------2-----------o',
			'o-oooo-o-oo-o-oooo-o',
			'o-oooo-oooooo-oooo-o',
			'o------------------o',
			'o-oooo-o-oo-o-oooo-o',
			'o-oooo-o-oo-o-oooo-o',
			'o--1-----oo--------o',
			'o-oooo-oooooo-oooo-o',
			'o-------3----------o',
			'oooooooooooooooooooo']
			
		elif nivel == 2:
			
			self.coord = ['oooooooooooooooooooo',
			'o--------oo--------o',
			'o-ooo-oo-oo-oo-ooo-o',
			'o-ooo----------ooo-o',
			'o2----oooooooo-----o',
			'o-o-o----------o-o-o',
			'o-o---ooooo5oo---o-o',
			'o-o-o-oo6oo-oo-o-o-o',
			'o-----oo----oo-----o',
			'ooo-o-oooooooo-o-ooo',
			'o------------------o',
			'o-oooo-o-oo-o-oooo-o',
			'o-oooo-oooooo-oooo-o',
			'o-------------4----o',
			'o-oooo-o-oo-o-oooo-o',
			'o-oooo-o-oo-o-oooo-o',
			'o--------oo--------o',
			'o-oooo-oooooo-oooo-o',
			'o---------1-----3--o',
			'oooooooooooooooooooo']
			
		elif nivel == 3:
			
			self.coord = ['oooooooooooooooooooo',
			'o--------oo--------o',
			'o-ooo-oo-oo-oo-ooo-o',
			'o-ooo---1------ooo-o',
			'o--2--oooooooo-----o',
			'o-o-o----------o-o-o',
			'o-o---ooooo5oo---o-o',
			'o-o-o-oo6oo-oo-o-o-o',
			'o-----oo----oo-----o',
			'ooo-o-oooooooooooooo',
			'o------------o-----o',
			'o-oooo--ooo--o-----o',
			'o-oooo-ooooo-o-----o',
			'o----4-------5-ooo-o',
			'o-oooo-o-o-o-o-ooo-o',
			'o-oooo-o-o-o-ooooo-o',
			'o--------o---o-----o',
			'o-oooo-ooooo-o-----o',
			'o------------o-----o',
			'oooooooooooooooooooo']
		
		
		self.x, self.y = 0, 0
		
		self.paredes = []
		self.itens = {}
		self.item_ativo = {}
		self.itens[5] = []
		
		for linha in self.coord:
			for coluna in linha:
				if coluna == "o":
					self.paredes.append(Muro(self.x, self.y))
				elif coluna == "1":
					self.itens[1] = Item(self.x,self.y, 'static/images/item_depressao.png')
				elif coluna == "2":
					self.itens[2] = Item(self.x,self.y, 'static/images/item_desespero.png')
				elif coluna == "3":
					self.itens[3] = Item(self.x,self.y, 'static/images/item_carencia.png')
				elif coluna == "4":
					self.itens[4] = Item(self.x,self.y, 'static/images/chave.png')
				elif coluna == "5":
					self.itens[5].append(Item(self.x,self.y, 'static/images/cadeado.png'))
				elif coluna == "6":
					self.itens[6] = Item(self.x,self.y, 'static/images/porta.png')
				self.x += 32
			self.y += 24
			self.x = 0
		
	def draw(self, surface):
		for parede in self.paredes:
			parede.draw(surface)
		for item in self.itens.values():
			if type(item) == list:
				for cadeado in item:
					cadeado.draw(surface)
			else:
				item.draw(surface)
			
	def colisao_muro(self, rect):
		for parede in self.paredes:
			if parede.rect.colliderect(rect):
				return True
		return False
		
	def colisao_item(self, rect):
		for chave in self.itens:
			item = self.itens[chave]
			if chave != 5:
				if item.rect.colliderect(rect):
					self.item_ativo[chave] = True
	
	def colisaoCadeadoFechado(self, rect, garota=False):
		if self.itens.has_key(5):
			for i in range(len(self.itens[5])):
				if self.itens[5][i].rect.colliderect(rect):
					if not garota:
						if self.item_ativo.has_key(4):
							if self.item_ativo[4]:
								del self.itens[5][i]
								if not self.itens[5]:
									self.item_ativo[4] = False
								return False
					return True
	
	def colisaoPorta(self, rect):
		porta = self.itens[6]
		if porta.rect.colliderect(rect):
			return True
		
	def colisaoDeCorpos(self, rect1, rect2):
		if rect1.colliderect(rect2):
			return True
		return False
