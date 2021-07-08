# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 21:55:43 2021

@author: Dr. P
"""

from camels import racing_camel
from matplotlib import pyplot as plt

racing_colours = ['red','green','orange','blue','purple']
crazy_colours = ['black','white']

def plot_state(game):
    '''
    Plot the positions of each camel

    Parameters
    ----------
    camel_list : list[camel]
        List of camels.

    Returns
    -------
    None.

    '''
    
    for camel in game.camel_list:
        
        if type(camel) == racing_camel:
            col = racing_colours[camel.id]
            plt.scatter(camel.position,camel.stack_position,color=col)
            
        else:
            col = crazy_colours[camel.id]
            plt.scatter(camel.position,camel.stack_position,color=col,edgecolors='black')
            
    plt.xlim(-1,game.track_length)
    plt.ylim(-0.5,7.5)
    plt.show()