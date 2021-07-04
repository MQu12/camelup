# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 15:55:25 2021

@author: Dr. P
"""

from camels import racing_camel, crazy_camel
import random

track_length = 16
max_roll = 3
min_roll = 1

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
    '''
    Set the stack positions of each camel

    Parameters
    ----------
    camel_list : list[camel]
        List of camels

    Returns
    -------
    None.

    '''
    
    positions = []
    
    for i in range(len(camel_list)):
        
        camels_on_tile = positions.count(camel_list[i].position)
        camel_list[i].stack_position = camels_on_tile
        positions.append(camel_list[i].position)

def get_number_of_camel_types(camel_list,camel_type):
    '''
    Count the amount of a type of camel

    Parameters
    ----------
    camel_list : list[camel]
        List of camels
    camel_type : class(camel)
        Type of camel to count

    Returns
    -------
    count : int
        Number of type of camel

    '''
    
    count = 0
    
    for camel in camel_list:
        if type(camel) == camel_type:
            count += 1
            
    return count

set_stack(camel_list)
racing_camel_count = get_number_of_camel_types(camel_list,racing_camel)
crazy_camel_count = get_number_of_camel_types(camel_list,crazy_camel)

def move_camel_to(camel_list,camel_no,final_pos):
    '''
    Move camel id in list to a particular location.
    Takes into account camel positions in stack.
    Camels above target are carried and the substack is put on top of a
    stack at the destination.

    Parameters
    ----------
    camel_list : list[camel]
        List of camels.
    camel_no : int
        Camel id.
    final_pos : int
        Target square.

    Returns
    -------
    camel_list : list[camel]
        Updated list.

    '''

    target_camel_stack_pos = camel_list[camel_no].stack_position
    init_camel_pos = camel_list[camel_no].position
    
    camels_to_move = []
    camels_at_destination = 0
    
    for camel in camel_list:
        
        if camel.position == init_camel_pos and camel.stack_position >= target_camel_stack_pos:
            camels_to_move.append(camel.id)
            
        if camel.position == final_pos:
            camels_at_destination += 1
            
    for camel_id in camels_to_move:
        camel_list[camel_id].position = final_pos
        camel_list[camel_id].stack_position += (camels_at_destination - target_camel_stack_pos)
    
    return camel_list

def advance_camel(camel_list,racing_camel_count,camels_to_move):
    
    camel_no = camels_to_move[random.randint(0,len(camels_to_move)-1)]
    
    advancement = random.randint(min_roll,max_roll)
    
    if camel_no != 'crazy':
        # advance racing camel
        
        #camel_list[camel_no]
        pass
    
    else:
        # advance crazy camel
        crazy_camel_no = random.randint(0,crazy_camel_count-1)
        pass
    
    