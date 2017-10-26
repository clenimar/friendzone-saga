# coding: utf-8
# projeto

import pygame, pygame.font, sys
from models.personagem import *
from models.garota import *
from models.inimigo import *
from models.item import *
from pygame.locals import *
from models.mapa import *

def caixa_de_texto(screen, message, (x, y)):
    fontobject=pygame.font.Font('static/fonts/8-BIT WONDER.ttf', 16)
    if len(message) != 0:
        screen.blit(fontobject.render(message, 1, (255, 0, 0)),(x,y))
	pygame.display.flip()
	
def carregaImagem(imagem, (x, y)):
	tela.blit(pygame.image.load('%s' % imagem), (x, y))
	
def apagaItem(item_id):
	if mapa.itens.has_key(item_id):
		del mapa.itens[item_id]

# PRINCIPAL:	
RESOLUCAO = (640,540)
FPS = 30

tela = pygame.display.set_mode(RESOLUCAO)
fundo = pygame.image.load("static/images/background.png")
tela.blit(fundo, (0,0))
clock = pygame.time.Clock()
pygame.display.set_caption("FRIENDZONE SAGA")

VIDA_RES = {1:'static/images/life_1.png', 2:'static/images/life_2.png', 3:'static/images/life_3.png',0:'static/images/blank.png'}
PERSONAGEM_RES = {1: 'static/images/m_m.png', 2: 'static/images/i_m.png', 3: 'static/images/g_m.png', 4: 'static/images/u_f.png', 5: 'static/images/x_f.png', 6: 'static/images/o_f.png'}

def inicializar(nivel):
	global inimigos
	global heroi
	global garota
	global morreu
	global mapa
	global imagem_inimigo
	if vidas != 0:
		carregaIntro(nivel)
	tela.blit(fundo, (0,0))
	mapa = Mapa(nivel)
	inimigos = []
	imagem_inimigo = INIMIGO_RES[nivel]
	heroi = Heroi(mapa, imagem_heroi)
	if nivel == 2:
		inimigo.velocidade = 4
	if nivel == 3:
		garota = Garota(mapa, imagem_garota)
		inimigo.velocidade = 5
	for i in range(len(inimigos_pos)):
		inimigos.append(Inimigo(mapa, inimigos_pos[i]))
	morreu = False
	

menu_inicio = True
while menu_inicio:
	carregaImagem('static/images/MENU.png', (0,0))
	pygame.display.update()
	tecla = pygame.key.get_pressed()
	if tecla[K_s]:
		menu_inicio = False
	for evento in pygame.event.get():
		if evento.type == pygame.QUIT or pygame.key.get_pressed()[K_ESCAPE]:
			sys.exit()

tela.blit(fundo, (0,0))
sexo_per = ''

def selecionaPers():
	global imagem_heroi
	global sexo_per
	seleciona_personagem = True
	espera = False
	while seleciona_personagem:
		carregaImagem('static/images/seleciona_pers.png', (215,90))
		pygame.display.update()
		tecla = pygame.key.get_pressed()
		if tecla[K_m]:
			imagem_heroi = 'static/images/m_m.png'
			espera = True
			sexo_per = 'm'
		elif tecla[K_i]:
			imagem_heroi = 'static/images/i_m.png'
			espera = True
			sexo_per = 'm'
		elif tecla[K_g]:
			imagem_heroi = 'static/images/g_m.png'
			espera = True
			sexo_per = 'm'
		elif tecla[K_u]:
			imagem_heroi = 'static/images/u_f.png'
			espera = True
			sexo_per = 'f'
		elif tecla[K_x]:
			imagem_heroi = 'static/images/x_f.png'
			espera = True
			sexo_per = 'f'
		elif tecla[K_o]:
			imagem_heroi = 'static/images/o_f.png'
			espera = True
			sexo_per = 'f'
		if espera:
			carregaImagem('static/images/w_cont.png', (130,200))
			if tecla[K_w]:
				seleciona_personagem = False
		for evento in pygame.event.get():
			if evento.type == pygame.QUIT or pygame.key.get_pressed()[K_ESCAPE]:
				sys.exit()

def selecionaAmor(sexo_per):
	global imagem_garota
	seleciona_amor = True
	espera = False
	while seleciona_amor:
		tecla = pygame.key.get_pressed()
		if sexo_per == 'm':
			carregaImagem('static/images/seleciona_amor_f.png', (204,250))
			pygame.display.update()
			if tecla[K_a]:
				imagem_garota = 'static/images/u_f.png'
				espera = True
			elif tecla[K_b]:
				imagem_garota = 'static/images/x_f.png'
				espera = True
			elif tecla[K_c]:
				imagem_garota = 'static/images/o_f.png'
				espera = True
		else:
			carregaImagem('static/images/seleciona_amor_m.png', (204,250))
			pygame.display.update()
			if tecla[K_a]:
				imagem_garota = 'static/images/m_m.png'
				espera = True
			elif tecla[K_b]:
				imagem_garota = 'static/images/i_m.png'
				espera = True
			elif tecla[K_c]:
				imagem_garota = 'static/images/g_m.png'
				espera = True
		if espera:
			carregaImagem('static/images/w_cont.png', (130,360))
			if tecla[K_w]:
				seleciona_amor = False
		for evento in pygame.event.get():
			if evento.type == pygame.QUIT or pygame.key.get_pressed()[K_ESCAPE]:
				sys.exit()
				
def selecionaInimigo(sexo_per):
	global INIMIGO_RES
	global INIMIGO_INTRO
	if sexo_per == 'm':
		INIMIGO_INTRO = {1: 'static/images/1_inimigo_1_pre.png', 2: 'static/images/1_inimigo_2_pre.png', 3: 'static/images/1_boss_pre.png'}
		INIMIGO_RES = {1: 'static/images/1_inimigo_1.png', 2: 'static/images/1_inimigo_2.png', 3: 'static/images/1_boss.png'}
	else:
		INIMIGO_RES = {1: 'static/images/2_inimigo_1.png', 2: 'static/images/2_inimigo_2.png', 3: 'static/images/2_boss.png'}
		INIMIGO_INTRO = {1: 'static/images/2_inimigo_1_pre.png', 2: 'static/images/2_inimigo_2_pre.png', 3: 'static/images/2_boss_pre.png'}		

def carregaIntro(nivel):
	tela.blit(fundo, (0,0))
	espera = True
	while espera:
		carregaImagem(INIMIGO_INTRO[nivel], (100,40))
		pygame.display.update()
		tecla = pygame.key.get_pressed()
		if tecla[K_SPACE]:
			espera = False
		for evento in pygame.event.get():
			if evento.type == pygame.QUIT or pygame.key.get_pressed()[K_ESCAPE]:
				sys.exit()
			
selecionaPers()
selecionaAmor(sexo_per)
selecionaInimigo(sexo_per)
nivel = 1
carregaIntro(nivel)

vidas = 3
inimigos = []
inimigos_pos = [(288,240), (448,144), (64,432), (576,264), (128,96)]
imagem_inimigo = INIMIGO_RES[nivel]
mapa = Mapa(nivel)
heroi = Heroi(mapa, imagem_heroi)
for i in range(len(inimigos_pos)):
	inimigos.append(Inimigo(mapa, inimigos_pos[i]))

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('static/sounds/smk_battle.mid')
pygame.mixer.music.play(2)

# JOGO:
jogando = True
gameOver = False
jogoGanho = False
morreu = False
seleciona = True

while jogando:
	tela.blit(fundo, (0,0))

	for evento in pygame.event.get():
		if evento.type == pygame.QUIT or pygame.key.get_pressed()[K_ESCAPE]:
			jogando = False
			sys.exit()	
						
	if morreu:
		vidas -= 1
		inicializar(nivel)
		
	
	if vidas == 0:
		gameOver = True
		pygame.mixer.music.load('static/sounds/smw_gameover.mid')
		pygame.mixer.music.play(2)

	carregaImagem('%s' % VIDA_RES[vidas], (32, 480))
	
	while gameOver:
		carregaImagem('static/images/gameover.png', (180,150))
		pygame.display.update()
		for evento in pygame.event.get():
			if evento.type == pygame.QUIT or pygame.key.get_pressed()[K_ESCAPE]:
				jogando = False
				sys.exit()
			elif pygame.key.get_pressed()[K_a]:
				gameOver = False
				nivel = 1
				inicializar(nivel)
				pygame.mixer.init()
				pygame.mixer.music.load('static/sounds/smk_battle.mid')
				pygame.mixer.music.play(2)
				vidas = 3
	while jogoGanho:
		carregaImagem('static/images/jogo_ganho.png', (0, 0))
		pygame.display.update()
		for evento in pygame.event.get():
			if evento.type == pygame.QUIT or pygame.key.get_pressed()[K_ESCAPE]:
				jogoGanho = False
				jogando = False
				sys.exit()
			elif pygame.key.get_pressed()[K_a]:
				jogoGanho = False
				tela.blit(fundo, (0,0))
				selecionaPers()
				selecionaAmor(sexo_per)
				selecionaInimigo(sexo_per)
				nivel = 1
				carregaIntro(nivel)
				inicializar(nivel)
			pygame.mixer.init()
			pygame.mixer.music.load('static/sounds/t16.wav')
			pygame.mixer.music.play(1)
		
	mapa.draw(tela)
	
	heroi.draw(tela)
	heroi.mover()
	
	if nivel == 3:
		garota.mover()
		garota.draw(tela)
		mapa.colisao_item(garota.rect)
		
	colisao = mapa.colisaoDeCorpos
	
	for inimigo in inimigos:
				inimigo.mover()
				inimigo.draw(tela, imagem_inimigo)
				if colisao(heroi.rect, inimigo.rect):
					morreu = True
				if nivel == 3:
					if colisao(garota.rect, inimigo.rect):
						morreu = True
		
	colisaoItem = mapa.colisao_item
	colisaoItem(heroi.rect)
	if mapa.item_ativo:
		if mapa.item_ativo.has_key(1):
			if mapa.item_ativo[1]:
				apagaItem(1)
				for inimigo in inimigos:
					inimigo.velocidade = 10
				mapa.item_ativo[1] = False
		if mapa.item_ativo.has_key(2):
			if mapa.item_ativo[2]:
				apagaItem(2)
				heroi.velocidade = -heroi.velocidade
				if nivel == 3:
					garota.velocidader = -garota.velocidader
				mapa.item_ativo[2] = False
		if mapa.item_ativo.has_key(3):
			if mapa.item_ativo[3]:
				apagaItem(3)
				imagem_inimigo = imagem_garota
				mapa.item_ativo[3] = False
		if mapa.item_ativo.has_key(4):
			if mapa.item_ativo[4]:
				apagaItem(4)
				carregaImagem('static/images/item_chave.png', (508,480))
				
	if mapa.colisaoPorta(heroi.rect):
		if nivel != 3:
			nivel += 1
			inicializar(nivel)
		else:
			if mapa.colisaoPorta(garota.rect):
				jogoGanho = True
		
	pygame.display.update()
	clock.tick(FPS)
