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