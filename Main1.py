from galinha import Galinha
from carros import Carro
from telas import Tela
import pygame as pg
from pygame.locals import *


def galinhabater():
    global tela, vidas, galinha, carro_1, carro_2, carro_3, carro_4

    if galinha.rect.colliderect(carro_1) or galinha.rect.colliderect(carro_2) or galinha.rect.colliderect(carro_3) or \
            galinha.rect.colliderect(carro_4):
        galinha.x = 0
        vidas -= 1
        font = pg.font.Font('freesansbold.ttf', 32)

        text = font.render("Vidas: " + str(vidas), True, (0, 255, 0), (255, 0, 0))

        textRect = text.get_rect()

        textRect.topleft = (10, 10)
        tela.image.blit(text, textRect)
        print(vidas)
        if vidas <= 0:
            vidas = 0
            tela.image = tela.imagem2
            tela_group.add(tela)
            galinha.kill()
            carros_group.empty()


def mudarLevel():
    global tela, galinha, galinha_group, carro_1, carro_2, carro_3, carro_4

    if galinha.x >= LARGURA + 200 and not tela.image == tela.imagem3:
        carro_1 = Carro(1, 2, 1)
        carro_2 = Carro(2, 2, 1)
        carro_3 = Carro(3, 2, 1)
        carro_4 = Carro(4, 2, 1)
        galinha_group.add(galinha)
        carros_group.empty()
        carros_group.add(carro_1, carro_2, carro_3, carro_4)
        tela.image = tela.imagem3
        tela.setSize(0, 0)
        tela_group.add(tela)
        galinha.x = 0


def teclaSecreta():
    galinha.x = LARGURA + 140


def returnin():
    tela.image = tela.imagem1


def vitoria():
    global carros_group
    if galinha.x >= LARGURA + 150 and tela.image == tela.imagem3:
        print("ganhou")
        tela.image = tela.imagem4

        galinha.kill()
        carros_group.empty()


LARGURA = 600
ALTURA = 850
pg.init()
tela_jogo = pg.display.set_mode((ALTURA, LARGURA))
pg.display.set_caption("ATRAVESSE")
clock = pg.time.Clock()

font = pg.font.Font("visitor2.ttf", 20)


def escrever(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect) #encaixar o texto ao botão


click = False


def menu():
    global click
    while True:
        tela.image = tela.imagem5
        escrever('MENU', font, (255, 255, 255), tela_jogo, 20, 20)

        mx, my = pg.mouse.get_pos() # checar posições do mouse

        iniciar = pg.Rect(50, 100, 200, 50) # botões
        ajuda = pg.Rect(50, 200, 200, 50)

        if iniciar.collidepoint((mx, my)):
            if click:
                jogo()

        if ajuda.collidepoint((mx, my)):
            if click:
                # printar instruções e depois voltar ao menu principal
                menu()
                pass
        pg.draw.rect(tela_jogo, (255, 0, 0), iniciar)
        pg.draw.rect(tela_jogo, (255, 0, 0), ajuda)

        click = False
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                pg.exit()
            if event.type == MOUSEBUTTONDOWN: # quando clico o botão do mouse esq
                if event.button == 1:
                    click = True
        pg.display.update()


vidas = 6
tela = Tela()
tela_group = pg.sprite.Group()
tela_group.add(tela)

galinha = Galinha()
galinha_group = pg.sprite.Group()
galinha_group.add(galinha)

carro_1 = Carro(1, 1, 1)
carro_2 = Carro(2, 1, 1)
carro_3 = Carro(3, 1, 1)
carro_4 = Carro(4, 1, 1)

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
        pg.display.update()
        vitoria()

    pg.quit()


if __name__ == "__main__":
    menu()
