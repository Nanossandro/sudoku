import numpy as np
import random as rd
import pygame
from pygame.locals import *

pygame.init()

screen= pygame.display.set_mode((500,500))

pygame.display.set_caption("Sudoku solver")

image= pygame.image.load("sudoku.png")
fond = pygame.image.load("sudoku.png").convert()

run = True
while run:
    pygame.time.delay(100)
   
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run = False












""""
grille = [[0] * 9 for _ in range(9)]


numbers= [1,2,3,4,5,6,7,8,9] 


def verif():
    for i in range (9):
        for j in range (9):
               
            ale=rd.shuffle(numbers)
            grille ()


 


        
          


def creatboard(i ,j , ligne1):
    for i in range (3):
        ligne1= ["_","_","_"," ","_","_","_"," ","_","_","_"]
        verif()
        print("|".join(ligne1))


    print("")  

    for i in range (3):
        ligne1= ["_","_","_"," ","_","_","_"," ","_","_","_"]
        print("|".join(ligne1))

    print("")  

    for i in range (3):
        ligne1= ["_","_","_"," ","_","_","_"," ","_","_","_"]
        print("|".join(ligne1))


    rempli= [(i, j) for i in range 9 and for j in range 9 if ligne1 == "_"]       

    if rempli:
        ordi = rd.shuffle(numbers)
        ligne1[]



            


        
print(creatboard())




for ligne in grille:
    print(ligne)




"""
