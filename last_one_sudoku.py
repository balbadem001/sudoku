# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 17:17:33 2023

@author: ali.ozkara-ug
"""
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 16:09:33 2023

@author: ali.ozkara-ug
"""
import math
import random as random
import numpy as np



def sudoku(a,b):
    
    endgame = 0
    while endgame == 0: #create a list a by a
        the_list = np.zeros((1,b)).tolist()
        
        cp2= len(the_list)
        coor_y = 0
        while cp2 < a+1:
            
            my_arrlist = np.arange(1,b+1).tolist()
            cp1_list = []
            cp1 = len(cp1_list)
            
            while cp1 < b: # this while is for making a list of b
                num = random.choice(my_arrlist)
                
                cp1_list.append(num)
                my_arrlist.remove(num)
                cp1 = len(cp1_list)
            
            breakpoint = 0
            coor_y = 0
            while coor_y < len(the_list):
                
                coor_x = 0
                while coor_x < b:
                    if cp1_list[coor_x] != the_list[coor_y][coor_x]:
                        coor_x += 1
                    else:
                        breakpoint = 1
                        break
                if coor_x == b:
                    coor_y += 1
                else:
                    breakpoint = 2
                    break
            if breakpoint == 0 :
                the_list.append(cp1_list)
            cp2 = len(the_list)
        
    
        del the_list[0]
        listo = np.array(the_list)
        
    
        sublist = [] # look for the squares
        s = int(math.sqrt(a))
        for m in range(0,s):
            for n in range(0,s):
                for i in range(s):
                    for j in range(s):
                        tr = the_list[m*s+i][n*s+j]
                        sublist.append(tr)
                
        subarray = np.array(sublist).reshape(a,b)
    
        sublist = subarray.tolist()
        
        
        j = 0
        k = 0
        breakpoint3 = 0
        while j < a:
            i = 0
            while i < a:
                if sublist[j].count((sublist[j][i])) == 1:
                    i += 1
                    k += 1
                elif sublist[j].count((sublist[j][i])) == 2:
                    breakpoint3 == 1

                    break
            if breakpoint3 == 1:
                break
            j += 1
        if k == a*a:
            endgame = 1
            print("finished")
        else:
            k = 0
    print(listo)



print("What is the shape of your sudoku")
a = int(input("Height"))


if math.sqrt(a) !=  math.floor(math.sqrt(a)):
    print("Please choose a square number")
else:
    b = int(input("Lenght"))
    if math.sqrt(b) !=  math.floor(math.sqrt(b)):
        print("Please choose a square number")
    else:
        print(sudoku(a,b))


