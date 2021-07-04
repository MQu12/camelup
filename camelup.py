# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 15:55:25 2021

@author: Dr. P
"""

from camels import racing_camel, crazy_camel

track_length = 16

#create camels
camel_list = []

camel_list.append( racing_camel(0,0) )
camel_list.append( racing_camel(1,0) )
camel_list.append( racing_camel(2,1) )
camel_list.append( racing_camel(3,2) )
camel_list.append( racing_camel(4,2) )
camel_list.append( crazy_camel(0,15) )
camel_list.append( crazy_camel(1,14) )

def set_stack(camel_list):
    
    positions = []
    
    for i in range(len(camel_list)):
        
        camels_on_tile = positions.count(camel_list[i].position)
        camel_list[i].stack_position = camels_on_tile
        positions.append(camel_list[i].position)

set_stack(camel_list)        