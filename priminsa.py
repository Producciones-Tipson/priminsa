# !/usr/bin/python
# -*- coding:utf-8 -*-

#Priminsa es unjuego independiente producido por el SR. José Santos Lertora.

import pygame
from random import *

pygame.init() #iniciar los modulos de pygame

#-----------------------ventana principal----------------------------
ventana=pygame.display.set_mode([700,400])
pygame.display.set_caption("Priminsa (BETA)")
fondo=(0,0,0)
#--------------------------------------------------------------------


#-----------------------------player---------------------------------
posx=325
posy=175
vx=0
vy=0
player=pygame.Rect(posx,posy,25,25)
score=0
vida=5
modo=0
#--------------------------------------------------------------------

#------------------------------texto---------------------------------
texto=pygame.font.Font(None,30)
blanco=(255,255,255)
inicio=texto.render("aplasta espacio para iniciar ",0,blanco)
tipson=texto.render("#byproduccionestipson",0,blanco)
textalmas=texto.render("ALMAS: ",0, blanco)
textscore=texto.render("SCORE: ",0, blanco)
over=pygame.font.Font(None,90)
gameo=over.render("GAME OVER",0,blanco)
#--------------------------------------------------------------------

velocidad=-15#velocidad de los boques de la gran priminsa

#---------------------------puntos-----------------------------------
listpuntos=[]
for x in range(1000):
        ancho=randrange(10,50)
        alto=randrange(10,50)
        x=randrange(700,210000)
        y=randrange(10,350)        
        listpuntos.append(pygame.Rect(x,y,ancho,alto))
#--------------------------------------------------------------------

#------------------------obstaculos----------------------------------
listobstaculos=[]
for x in range(3000):
        ancho=randrange(10,50)
        alto=randrange(10,50)
        x=randrange(700,210000)
        y=randrange(10,350)
        listobstaculos.append(pygame.Rect(x,y,ancho,alto))
#--------------------------------------------------------------------

#---------------------------almas------------------------------------
listalmas=[]
for x in range(10):
        ancho=randrange(30,90)
        alto=randrange(30,90)
        x=randrange(700,210000)
        y=randrange(10,350)
        listalmas.append(pygame.Rect(x,y,ancho,alto))
#--------------------------------------------------------------------

reloj=pygame.time.Clock()#reloj princpal

#-------------------pantalla de inicio-------------------------------
while modo==0:
        for event in pygame.event.get():#salida
                if event.type == pygame.QUIT:
                        pygame.quit()
                if event.type == pygame.KEYDOWN:#inicio
                        if event.key == pygame.K_SPACE:
                                modo=1
        ventana.blit(inicio,(220,50))
        #-----------------------explicacion--------------------------
        pygame.draw.rect(ventana,(0,200,0),(270,125,20,20))
        textverde=texto.render("genera puntos",0,blanco)
        ventana.blit(textverde,(300,125))
        pygame.draw.rect(ventana,(200,0,0),(270,175,20,20))
        textrojo=texto.render("quita almas",0,blanco)
        ventana.blit(textrojo,(300,175))
        pygame.draw.rect(ventana,(255,255,255),(270,225,20,20))
        textblanco=texto.render("genera almas (vida)",0,blanco)
        ventana.blit(textblanco,(300,225))
        #------------------------------------------------------------

        ventana.blit(tipson,(470,370))

        pygame.display.update()
#--------------------------------------------------------------------

while modo == 1:#loop principal(el verdadero juego)

        ventana.fill(fondo)

        pygame.draw.rect(ventana,(200,200,0),player)

        #----------------------graficar texto------------------------
        strvida= str(vida)
        strscore= str(score)
        contalmas=texto.render(strvida,0,blanco)
        contscore=texto.render(strscore,0,blanco)
        ventana.blit(textalmas,(50,20))
        ventana.blit(contalmas,(150,20))
        ventana.blit(textscore,(350,20))
        ventana.blit(contscore,(450,20))
        #------------------------------------------------------------


        for event in pygame.event.get():

                #---------------------controles----------------------
                if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RIGHT:
                                vx+=15
                        if event.key == pygame.K_LEFT:
                                vx-=15
                        if event.key == pygame.K_UP:
                                vy-=15
                        if event.key == pygame.K_DOWN:
                                vy+=15
                        if event.key == pygame.K_F11:
                                pygame.display.toggle_fullscreen
                                
                if event.type == pygame.KEYUP:
                        if event.key == pygame.K_RIGHT:
                                vx=0
                        if event.key == pygame.K_LEFT:
                                vx=0
                        if event.key == pygame.K_UP:
                                vy=0
                        if event.key == pygame.K_DOWN:
                                vy=0
                #----------------------------------------------------
                
                if event.type == pygame.QUIT:#salida (alt+f4)
                        pygame.quit()

        #movimiento fluido
        player.move_ip(vx,0)
        player.move_ip(0,vy)

        reloj.tick(40)#regular la velacidad del juego (FPS)

        for obsta in listobstaculos:
                pygame.draw.rect(ventana,(200,0,0),obsta)
                obsta.move_ip(velocidad,0)
                if player.colliderect(obsta):
                        obsta.move_ip(-700,0)
                        vida -= 1
                        print "una vida menos"
                        print "te quedan ",vida," almas"

        for punto in listpuntos:
                pygame.draw.rect(ventana,(0,200,0),punto)
                punto.move_ip(velocidad,0)
                if player.colliderect(punto):
                        punto.move_ip(-700,0)
                        score += 10
                        print "score: ", score

        for alma in listalmas:
                pygame.draw.rect(ventana,(255,255,255),alma)
                alma.move_ip(velocidad,0)
                if player.colliderect(alma):
                        alma.move_ip(-700,0)
                        vida += 1
                        print "una vida más"
                        print "ahora tienes ",vida," almas"

        if score == 10000:
                modo=10000

        if vida <= 0:#GAME OVER!!!!
                print "GAME OVER!!!!"
                modo=2

        pygame.display.update()

#-----------------------------DIOS-----------------------------------
while modo==10000:
        dios=over.render("DIOS!!!",0,blanco)
        ventana.blit(dios,(250,125))
        for event in pygame.event.get():
                if event.type==pygame.QUIT:
                        print"""Padre nuestro,
                        que estás en el cielo,
                        santificado sea tu Nombre;
                        venga a nosotros tu reino;
                        hágase tu voluntad 
                        en la tierra como en el cielo.
                        
                        Danos hoy nuestro pan de cada día;
                        perdona nuestras ofensas,
                        como también nosotros perdonamos 
                        a los que nos ofenden;
                        no nos dejes caer en la tentación,
                        y líbranos del mal. Amén."""
                        pygame.quit()
        pygame.display.update()
#--------------------------------------------------------------------

while modo==2:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        pygame.quit()

                if event.type==pygame.KEYDOWN:
                        print "tu score fue de ",score
                        modo+=1

        ventana.blit(gameo,(150,125))
        strscore=str(score)
        finalscore=over.render(strscore,0,blanco)
        ventana.blit(finalscore,(300,300))

        pygame.display.update()
pygame.quit()
