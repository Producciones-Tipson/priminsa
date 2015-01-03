#!/usr/bin/python
# -*- coding:utf-8 -*-

#Priminsa es un juego independiente producido por el José Santos
#Lertora como proyecto de producciones tipson.

import pygame
from random import *

pygame.init() #iniciar los modulos de pygame

#-----------------------ventana principal----------------------------
ventana=pygame.display.set_mode([1000,600])
pygame.display.set_caption("Priminsa (BETA)")
fondo=(0,0,0)
ventana.fill((0,0,0))
#pygame.display.toggle_fullscreen()
#--------------------------------------------------------------------

#----------------------muros invisibles------------------------------
murarriba=pygame.Rect(0,-500,1000,500)
murabajo=pygame.Rect(0,600,1000,500)
vm=0
#--------------------------------------------------------------------

#-----------------------------player---------------------------------
posx=625
posy=375
vx=0
vy=0
player=pygame.Rect(posx,posy,25,25)
score=0
vida=5
modo=0
#--------------------------------------------------------------------

#------------------------------texto---------------------------------
texto=pygame.font.Font(None,40)
blanco=(255,255,255)
inicio=texto.render("aplasta espacio para iniciar ",0,blanco)
tipson=texto.render("#byproduccionestipson",0,blanco)
textalmas=texto.render("ALMAS: ",0, blanco)
textscore=texto.render("SCORE: ",0, blanco)
over=pygame.font.Font(None,120)
gameo=over.render("GAME OVER",0,blanco)
#--------------------------------------------------------------------

velocidad=-15#velocidad de los boques de la gran priminsa

#---------------------------puntos-----------------------------------
listpuntos=[]
for x in range(1000):
        ancho=randrange(10,70)
        alto=randrange(10,70)
        x=randrange(1000,210000)
        y=randrange(10,550)        
        listpuntos.append(pygame.Rect(x,y,ancho,alto))
#--------------------------------------------------------------------

#------------------------obstaculos----------------------------------
listobstaculos=[]
for x in range(3000):
        ancho=randrange(10,70)
        alto=randrange(10,70)
        x=randrange(1000,210000)
        y=randrange(10,550)
        listobstaculos.append(pygame.Rect(x,y,ancho,alto))
#--------------------------------------------------------------------

#---------------------------almas------------------------------------
listalmas=[]
for x in range(10):
        ancho=randrange(30,90)
        alto=randrange(30,90)
        x=randrange(1000,210000)
        y=randrange(10,550)
        listalmas.append(pygame.Rect(x,y,ancho,alto))
#--------------------------------------------------------------------

reloj=pygame.time.Clock()#reloj princpal

#-------------------pantalla de inicio-------------------------------
while modo==0:
        ventana.fill(fondo)
        for event in pygame.event.get():#salida
                if event.type == pygame.QUIT:
                        pygame.quit()
                if event.type == pygame.KEYDOWN:#inicio
                        if event.key == pygame.K_SPACE:
                                modo=1
                        if event.key == pygame.K_F11:
                                pygame.display.toggle_fullscreen()
        ventana.blit(inicio,(320,50))
        reloj.tick(10)
        #-----------------------explicacion--------------------------
        pygame.draw.rect(ventana,(0,200,0),(370,180,20,20))
        textverde=texto.render("genera puntos",0,blanco)
        ventana.blit(textverde,(400,175))
        pygame.draw.rect(ventana,(200,0,0),(370,230,20,20))
        textrojo=texto.render("quita almas",0,blanco)
        ventana.blit(textrojo,(400,225))
        pygame.draw.rect(ventana,(255,255,255),(370,280,20,20))
        textblanco=texto.render("genera almas (vida)",0,blanco)
        ventana.blit(textblanco,(400,275))
        advertencia=texto.render("los filos te empujan",0,blanco)
        ventana.blit(advertencia,(375,325))
        #------------------------------------------------------------

	textf11=texto.render("F11=fullscreen",0,blanco)
	#ventana.blit(textf11,(0,570))

        ventana.blit(tipson,(680,570)) #byproduccionestipson

        pygame.display.update()
#--------------------------------------------------------------------

while modo == 1:#loop principal(el verdadero juego)

        ventana.fill(fondo)

        pygame.draw.rect(ventana,(200,200,0),player)#dibujar player

        #-----------------habilitar muros invisibles-----------------
        #los muros estan desactivados hasta nuevo aviso
        if player.colliderect(murarriba):
                vm+=1
        if player.colliderect(murabajo):
                vm-=1
        #------------------------------------------------------------

        #----------------------graficar texto------------------------
        strvida= str(vida)
        strscore= str(score)
        contalmas=texto.render(strvida,0,blanco)
        contscore=texto.render(strscore,0,blanco)
        ventana.blit(textalmas,(50,20))
        ventana.blit(contalmas,(160,20))
        ventana.blit(textscore,(750,20))
        ventana.blit(contscore,(860,20))
        #------------------------------------------------------------

        for event in pygame.event.get():

                #---------------------controles----------------------
                if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RIGHT:
                                vm=0
                                vx+=10
                        if event.key == pygame.K_LEFT:
                                vm=0
                                vx-=10
                        if event.key == pygame.K_UP:
                                vm=0
                                vy-=15
                        if event.key == pygame.K_DOWN:
                                vm=0
                                vy+=15
                        if event.key == pygame.K_F11:
                                pygame.display.toggle_fullscreen()
                                
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
	player.move_ip(0,vm)#impacto contra los muros

        reloj.tick(35)#regular la velacidad del juego (FPS)

        for obsta in listobstaculos:
                pygame.draw.rect(ventana,(200,0,0),obsta)
                obsta.move_ip(velocidad,0)
                if player.colliderect(obsta):
                        obsta.move_ip(-1000,0)
                        vida -= 1
                        print "una vida menos"
                        print "te quedan ",vida," almas"

        for punto in listpuntos:
                pygame.draw.rect(ventana,(0,200,0),punto)
                punto.move_ip(velocidad,0)
                if player.colliderect(punto):
                        punto.move_ip(-1000,0)
                        score += 10
                        print "score: ", score

        for alma in listalmas:
                pygame.draw.rect(ventana,(255,255,255),alma)
                alma.move_ip(velocidad,0)
                if player.colliderect(alma):
                        alma.move_ip(-1000,0)
                        vida += 1
                        print "una vida más"
                        print "ahora tienes ",vida," almas"

        if score == 10000:
                modo=10000

        if vida <= 0:#GAME OVER!!!!
                print "GAME OVER!!!!"
                if score >= 8000:
                        modo=10000
                else:
                        modo=2

        pygame.display.update()

#-----------------------------DIOS-----------------------------------
while modo==10000:
        dios=over.render("DIOS!!!",0,blanco)
        ventana.blit(dios,(350,125))
        strscore=str(score)
        finalscore=over.render(strscore,0,blanco)
        ventana.blit(finalscore,(450,275))
        reloj.tick(10)
        for event in pygame.event.get():
                if event.type==pygame.QUIT:
                        print"""
                        Padre nuestro,
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
			if event.key == pygame.K_SPACE:
                        	print "tu score fue de ",score
                        	modo+=1

        ventana.blit(gameo,(250,125))
        strscore=str(score)
        finalscore=over.render(strscore,0,blanco)
        ventana.blit(finalscore,(450,300))
        reloj.tick(10)

        pygame.display.update()
pygame.quit()
