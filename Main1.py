from galinha import Galinha
from carros import Carro
from telas import Tela
import pygame as pg
from pygame.locals import *

click = False

def galinhabater():
    global tela, vidas, galinha, carro_1, carro_2, carro_3, carro_4, carros_group, click

    if galinha.rect.colliderect(carro_1) or galinha.rect.colliderect(carro_2) or galinha.rect.colliderect(carro_3) or \
            galinha.rect.colliderect(carro_4):
        galinha.x = 0
        vidas -= 1

        font = pg.font.Font('visitor2.ttf', 32)
        text = font.render("Vidas: " + str(vidas), True, (0, 255, 0), (255, 0, 0))
        textRect = text.get_rect()
        textRect.topleft = (10, 10)
        tela.image.blit(text, textRect)
        print(vidas)

        if vidas <= 0:
            vidas = 0
            galinha.kill()
            carros_group.empty()

            tela.image = tela.imagem2

            mx, my = pg.mouse.get_pos()  # checar posições do mouse

            retornarmenu = pg.Rect(300, 500, 240, 55)  # botões
            pg.draw.rect(tela_jogo, (0, 200, 200), retornarmenu)

            if retornarmenu.collidepoint((mx, my)):
                pg.draw.rect(tela_jogo, (0, 100, 100), retornarmenu)
                if click:
                    menu()

            escrever('MENU', font, (255, 255, 255), tela_jogo, 420, 525)

            click = False
            for event in pg.event.get():
                if event.type == QUIT:
                    pg.quit()
                if event.type == MOUSEBUTTONDOWN:  # quando clico o botão do mouse esq
                    if event.button == 1:
                        click = True
            pg.display.update()


def mudarLevel():
    global tela, galinha, galinha_group, carro_1, carro_2, carro_3, carro_4

    if galinha.x >= LARGURA + 200 and not tela.image == tela.imagem3:
        carro_1 = Carro(1, 2)
        carro_2 = Carro(2, 2)
        carro_3 = Carro(3, 2)
        carro_4 = Carro(4, 2)
        galinha_group.add(galinha)
        carros_group.empty()
        carros_group.add(carro_1, carro_2, carro_3, carro_4)
        tela.image = tela.imagem3
        tela.setSize(0, 0)
        tela_group.add(tela)
        galinha.x = 0


def teclaSecreta():
    galinha.x = LARGURA + 150


def instrucoes():
    pass


def vitoria():
    global carros_group, click

    if galinha.x >= LARGURA + 150 and tela.image == tela.imagem3:

        galinha.kill()
        carros_group.empty()

        tela.image = tela.imagem4

        font = pg.font.Font('visitor2.ttf', 32)
        mx, my = pg.mouse.get_pos()  # checar posições do mouse

        retornarmenu = pg.Rect(300, 500, 240, 55)  # botões
        pg.draw.rect(tela_jogo, (0, 200, 200), retornarmenu)

        if retornarmenu.collidepoint((mx, my)):
            pg.draw.rect(tela_jogo, (0, 100, 100), retornarmenu)
            if click:
                menu()

        escrever('MENU', font, (255, 255, 255), tela_jogo, 420, 525)

        click = False
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
            if event.type == MOUSEBUTTONDOWN:  # quando clico o botão do mouse esq
                if event.button == 1:
                    click = True
        pg.display.update()


LARGURA = 600
ALTURA = 850
pg.init()
tela_jogo = pg.display.set_mode((ALTURA, LARGURA))
pg.display.set_caption("ATRAVESSE")
clock = pg.time.Clock()

font = pg.font.Font("visitor2.ttf", 80)


def escrever(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.center = (x, y)
    surface.blit(textobj, textrect)


def menu():
    global click, vidas, carro_1, carro_2, carro_3, carro_4
    vidas = 6
    while True:
        # adicionar tela de fundo
        tela.image = tela.imagem5
        tela_group.draw(tela_jogo)
        escrever('MENU', font, (255, 255, 255), tela_jogo, 420, 50)

        mx, my = pg.mouse.get_pos()  # checar posições do mouse

        iniciar = pg.Rect(300, 150, 240, 55)  # botões
        ajuda = pg.Rect(300, 250, 240, 55)
        sair = pg.Rect(300, 350, 240, 55)

        pg.draw.rect(tela_jogo, (0, 200, 200), iniciar)
        pg.draw.rect(tela_jogo, (0, 200, 200), ajuda)
        pg.draw.rect(tela_jogo, (0, 200, 200), sair)

        if iniciar.collidepoint((mx, my)):
            pg.draw.rect(tela_jogo, (0, 100, 100), iniciar)
            if click:
                carro_1 = Carro(1, 1)
                carro_2 = Carro(2, 1)
                carro_3 = Carro(3, 1)
                carro_4 = Carro(4, 1)
                galinha_group.add(galinha)
                carros_group.empty()
                carros_group.add(carro_1, carro_2, carro_3, carro_4)
                tela.image = tela.imagem1
                tela.setSize(0, 0)
                tela_group.add(tela)
                galinha.x = 0
                jogo()

        if ajuda.collidepoint((mx, my)):
            pg.draw.rect(tela_jogo, (0, 100, 100), ajuda)
            if click:
                # printar instruções e depois voltar ao menu principal
                menu()

        if sair.collidepoint((mx, my)):
            pg.draw.rect(tela_jogo, (0, 100, 100), sair)
            if click:
                pg.quit()

        escrever('Iniciar', font, (255, 255, 255), tela_jogo, 420, 175)
        escrever('Ajuda', font, (255, 255, 255), tela_jogo, 420, 275)
        escrever('Sair', font, (255, 255, 255), tela_jogo, 420, 375)

        click = False
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                exit()
            if event.type == MOUSEBUTTONDOWN:  # quando clico o botão do mouse esq
                if event.button == 1:
                    click = True
        pg.display.update()


tela = Tela()
tela_group = pg.sprite.Group()
tela_group.add(tela)

galinha = Galinha()
galinha_group = pg.sprite.Group()
galinha_group.add(galinha)

carro_1 = Carro(1, 1)
carro_2 = Carro(2, 1)
carro_3 = Carro(3, 1)
carro_4 = Carro(4, 1)

carros_group = pg.sprite.Group()
carros_group.add(carro_1, carro_2, carro_3, carro_4)


def jogo():
    while True:
        clock.tick(60)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_b:
                    teclaSecreta()


        tela_group.draw(tela_jogo)
        galinha_group.draw(tela_jogo)
        carros_group.draw(tela_jogo)

        tela_group.update()

        galinha_group.update()
        mudarLevel()
        galinhabater()
        carros_group.update()
        vitoria()
        pg.display.update()

    pg.quit()

if __name__ == "__main__":
    menu()
