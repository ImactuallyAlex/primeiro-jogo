import random
import pygame
import sys
from pygame.locals import * 
from sys import exit

pygame.init()

iniciar_janelas = True

while True :
# Estabelecimento das variáveis
    contagem_de_pontos = 0

    largura = 640
    altura = 480

    player1_movement_y = True
    player1_movement_x = True
# Inicialização das janelas
    if iniciar_janelas == True :
        menu = True
        pausa = False
        tela_derrota = False
    jogo = True
# Posição inicial do player
    x_player1 = 300
    y_player1 = 0
# Posição inicial dos desenhos da tela
    polygon1_y1 = 160

    x_rect1 = -380
    y_rect1 = 440
    largura_rect1 = 640
    altura_rect1 = 40

    posiçãox_texto = 350
    posiçãoy_texto = 20

    lista_posições_rect = [-640,-530,-380,-230,-120]
# Variáveis essenciais para que a janela possa aparecer
    tela = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption('Meu primeiro jogo')
    velocidade = pygame.time.Clock()
    v = 200
    contagem1 = 0
    fonte = pygame.font.SysFont(None, 55)
    fonte_titulo = pygame.font.SysFont(None, 80)
    fonte_menor = pygame.font.SysFont(None, 40)

    while menu == True :
        tela.fill((0,0,0))
        for event in pygame.event.get() :
            if event.type == KEYDOWN :
                if event.key == K_s and polygon1_y1 < 380:
                    polygon1_y1 = polygon1_y1 + 110
                if event.key == K_w and polygon1_y1 > 160:
                    polygon1_y1 = polygon1_y1 - 110
                if event.key == K_SPACE and polygon1_y1 == 160 :
                    menu = False
                elif event.key == K_SPACE and polygon1_y1 == 270 :
                    print('nada acontece ainda')
                elif event.key == K_SPACE and polygon1_y1 == 380 :
                    pygame.quit()
                    exit()
            if event.type == QUIT :
                pygame.quit()
                exit()
                
        titulo = fonte_titulo.render('Nome do jogo',True,(255,255,255))
        tela.blit(titulo, (130,50))

        pygame.draw.rect(tela, (0,0,200), (120,150,400,60))
        op1 = fonte.render('Jogar',True,(255,255,255))
        tela.blit(op1, (270,160))
        pygame.draw.rect(tela, (0,0,200), (120,260,400,60))
        op2 = fonte.render('Opções',True,(255,255,255))
        tela.blit(op2, (255,270))
        pygame.draw.rect(tela, (0,0,200), (120,370,400,60))
        op3 = fonte.render('Sair',True,(255,255,255))
        tela.blit(op3, (285,380))

        pygame.draw.polygon(tela, (0,255,55), ((60,polygon1_y1), (60,polygon1_y1 + 40), (100,polygon1_y1 + 20)))

        pygame.display.update()

    while jogo == True :

        x_rect2 = largura_rect1 + x_rect1 + 120
        y_rect2 = y_rect1
        largura_rect2 = 640
        altura_rect2 = 40

        velocidade.tick(v)
        tela.fill((0,0,0))
        for event in pygame.event.get() :
            if event.type == KEYDOWN :
                if event.key == K_d and x_player1 < 600 and player1_movement_x:
                    x_player1 = x_player1 + 150
                if event.key == K_a and x_player1 > 0 and player1_movement_x:
                    x_player1 = x_player1 - 150
                if event.key == K_ESCAPE :
                    pausa = True
                    while pausa == True :
                        tela.fill((0,0,0))
                        for event in pygame.event.get() :
                            if event.type == KEYDOWN :
                                if event.key == K_s and polygon1_y1 < 380:
                                    polygon1_y1 = polygon1_y1 + 110
                                if event.key == K_w and polygon1_y1 > 160:
                                    polygon1_y1 = polygon1_y1 - 110
                                if event.key == K_SPACE and polygon1_y1 == 160 :
                                    pausa = False
                                elif event.key == K_SPACE and polygon1_y1 == 270 :
                                    pausa = False
                                    iniciar_janelas = True
                                    jogo = False
                            if event.type == QUIT :
                                pygame.quit()
                                exit()
                        
                        titulo_pausa = fonte_titulo.render('Jogo pausado',True,(255,255,255))
                        tela.blit(titulo_pausa, (130,50))

                        pygame.draw.rect(tela, (0,0,200), (195,150,250,60))
                        op1_pausa = fonte.render('Retomar',True,(255,255,255))
                        tela.blit(op1_pausa, (250,160))
                        pygame.draw.rect(tela, (0,0,200), (195,260,250,60))
                        op2_pausa = fonte.render('Sair',True,(255,255,255))
                        tela.blit(op2_pausa, (285,270))

                        pygame.draw.polygon(tela, (0,255,55), ((135,polygon1_y1), (135,polygon1_y1 + 40), (175,polygon1_y1 + 20)))

                        pygame.display.update()
            if event.type == QUIT :
                pygame.quit()
                exit()
        
        pygame.draw.rect(tela, (0,255,0), (x_rect1,y_rect1,largura_rect1,altura_rect1))
        pygame.draw.rect(tela, (0,255,0), (x_rect2,y_rect2,largura_rect2,altura_rect2))
        if y_player1 == y_rect1 - 59 and not(x_player1 in range(largura_rect1 + x_rect1, x_rect2)) :
            tela_derrota = True
        while tela_derrota == True :
            tela.fill((0,0,0))
            for event in pygame.event.get() :
                if event.type == KEYDOWN :
                    if event.key == K_s and polygon1_y1 < 380:
                        polygon1_y1 = polygon1_y1 + 110
                    if event.key == K_w and polygon1_y1 > 160:
                        polygon1_y1 = polygon1_y1 - 110
                    if event.key == K_SPACE and polygon1_y1 == 160 :
                        tela_derrota = False
                        iniciar_janelas = False
                        jogo = False
                    elif event.key == K_SPACE and polygon1_y1 == 270 :
                        tela_derrota = False
                        iniciar_janelas = True
                        jogo = False
                if event.type == QUIT :
                    pygame.quit()
                    exit()
                        
            titulo_pausa = fonte_titulo.render('Derrota',True,(255,0,0))
            tela.blit(titulo_pausa, (220,50))

            pygame.draw.rect(tela, (0,0,200), (195,150,250,60))
            op1_derrota = fonte_menor.render('Jogar novamente',True,(255,255,255))
            tela.blit(op1_derrota, (205,165))
            pygame.draw.rect(tela, (0,0,200), (195,260,250,60))
            op2_derrota = fonte.render('Menu',True,(255,255,255))
            tela.blit(op2_derrota, (270,270))

            pygame.draw.polygon(tela, (0,255,55), ((135,polygon1_y1), (135,polygon1_y1 + 40), (175,polygon1_y1 + 20)))

            pygame.display.update()

        if y_player1 in range(y_rect1 - 59,y_rect1 + 40) :
            player1_movement_x = False
        if y_player1 < y_rect1 - 59 or y_player1 > y_rect1 + 40 :
            player1_movement_x = True

        pygame.draw.rect(tela, (255,0,0), (x_player1,y_player1,40,60))
        if y_player1 >= altura :
            y_player1 = 0
            x_rect1 = random.choice(lista_posições_rect) 
            contagem_de_pontos = contagem_de_pontos + 1
            contagem1 = contagem1 + 1
            if contagem1 == 5 :
                v = v + 20
                contagem1 = 0
        if player1_movement_y == True :
            y_player1 = y_player1 + 1

        texto = fonte.render(f'Pontuação = {contagem_de_pontos}',True,(255,255,255))
        if contagem_de_pontos >= 100 :
            posiçãox_texto = 330
        tela.blit(texto, (posiçãox_texto,posiçãoy_texto))

        pygame.display.update()
