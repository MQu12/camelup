# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 21:55:43 2021

@author: Dr. P
"""

from camels import racing_camel,crazy_camel
from matplotlib import pyplot as plt
from camelup import race_state
import constants

racing_colours = ['red','green','orange','blue','purple']
crazy_colours = ['black','white']

def plot_state(state):
    '''
    Plot the positions of each camel

    Parameters
    ----------
    state : race_state
        State of the race.

    Returns
    -------
    None.

    '''
    
    camel_size = 2900
    
    plt.figure()
    
    for camel in state.camel_list:
        
        if type(camel) == racing_camel:
            col = racing_colours[camel.id]
            plt.scatter(camel.position,camel.stack_position,color=col,s=camel_size,marker=constants.racingCamelMarker)
            
        else:
            col = crazy_colours[camel.id]
            plt.scatter(camel.position,camel.stack_position,color=col,s=camel_size,edgecolors='black',marker=constants.crazyCamelMarker)
            
    plt.xlim(-1,state.track_length)
    plt.ylim(-0.5,7.5)
    plt.show()
    
def plot_win_probs(winners,title):
    '''
    Plot the probability of wins per camel as a pie chart.

    Parameters
    ----------
    winners : array(int)
        Array of wins per camel.
    title : str
        Title of the pie chart.

    Returns
    -------
    None.

    '''
    
    plt.pie(winners,colors=racing_colours,autopct='%1.f%%')
    plt.title(title)
    plt.show()
    
def main():
    camel_list = []
    
    camel_list.append( racing_camel(0,0) )
    camel_list.append( racing_camel(1,0) )
    camel_list.append( racing_camel(2,1) )
    camel_list.append( racing_camel(3,2) )
    camel_list.append( racing_camel(4,2) )
    camel_list.append( crazy_camel(0,15) )
    camel_list.append( crazy_camel(1,14) )
    
    state = race_state(camel_list)
    
    plot_state(state)
    
if __name__ == "__main__":
    main()