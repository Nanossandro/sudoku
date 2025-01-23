import numpy as np
import pygame
import random as rd
pygame.init()




def creatboard():
    for i in range (3):
        ligne1= ["_","_","_"," ","_","_","_"," ","_","_","_"]
        print("|".join(ligne1))

    print("")  

    for i in range (3):
        ligne1= ["_","_","_"," ","_","_","_"," ","_","_","_"]
        print("|".join(ligne1))

    print("")  

    for i in range (3):
        ligne1= ["_","_","_"," ","_","_","_"," ","_","_","_"]
        print("|".join(ligne1))       

            


        
print(creatboard())


""""
for i in range (9):
        for j in range (9):
            rd.shuffle(numbers)

numbers= [1,2,3,4,5,6,7,8,9]            
"""            