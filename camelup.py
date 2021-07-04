# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 15:55:25 2021

@author: Dr. P
"""

import numpy as np
from camels import racing_camel, crazy_camel

number_of_racing_camels = 5
number_of_crazy_camels = 2
number_of_tiles = 16


def init_track(n_tiles):
    '''
    Generate the track
    
    Args:
        n_tiles (int): number of tiles
        
    Returns:
        track (list[list]): the track
    '''
    track = []
    
    for i in range(n_tiles):
        track.append([])
        
    return track

def generate_camels(n_racing,n_crazy):
    '''
    Generate the camels
    
    Parameters
    ----------
    n_racing : int
        Number of racing camels to generate
    n_crazy : int
        Number of crazy camels to generate

    Returns
    -------
    racing_camels : list[racing_camel]
        List of racing camels.
    crazy_camels : list[crazy_camels]
        List of crazy camels.

    '''
    
    racing_camels = []
    crazy_camels = []
    
    for i in range(n_racing):
        racing_camels.append(racing_camel(i))
    
    for i in range(n_crazy):
        crazy_camels.append(crazy_camel(i))
        
    return racing_camels, crazy_camels
    
track = init_track(number_of_tiles)
racing_camels, crazy_camels = generate_camels(number_of_racing_camels,number_of_crazy_camels)

# Add camels to track
track[0].append(racing_camels[0])
track[0].append(racing_camels[1])
track[1].append(racing_camels[2])
track[2].append(racing_camels[3])
track[2].append(racing_camels[4])

