# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 21:55:43 2021

@author: Dr. P
"""

from camels import racing_camel,crazy_camel
from matplotlib import pyplot as plt
from camelup import race_state
import constants
import numpy as np
import pandas as pd

racing_colours = ['red','green','orange','blue','purple']
crazy_colours = ['black','white']

def plot_state(state, leg_win_probs=None, race_win_probs=None, race_lose_probs=None):
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
    
    fig1 = plt.figure(facecolor='white')
    axis_main = plt.axes()
    axis_main.axes.get_yaxis().set_visible(False)
    axis_main.text(0.02,0.95,f'Leg {state.leg_num}', transform=axis_main.transAxes)
    axis_main.text(0.02,0.90,f'After {state.num_moves} moves', transform=axis_main.transAxes)
    
    for camel in state.camel_list:
        
        if type(camel) == racing_camel:
            col = racing_colours[camel.id]
            axis_main.scatter(camel.position+0.2,camel.stack_position,color=col,s=camel_size,marker=constants.racingCamelMarker)
            
        else:
            col = crazy_colours[camel.id]
            axis_main.scatter(camel.position-0.3,camel.stack_position,color=col,s=camel_size,edgecolors='black',marker=constants.crazyCamelMarker)
            
    axis_main.set_xlim(-1,state.track_length)
    axis_main.set_xticks(np.arange(0, state.track_length+1, 1.0))
    axis_main.set_ylim(-0.5,7.5)
    
    axis_moved_camels = fig1.add_axes([0.12,0.5,0.1,0.3])
    axis_moved_camels.axis('off')
    
    xpos = np.zeros(state.racing_camel_count+1)
    ypos = np.arange(0,state.racing_camel_count+1)/(state.racing_camel_count+1)
    camel_display = pd.DataFrame([xpos,ypos]).T
    
    axis_moved_camels.scatter(camel_display[0],
                camel_display[1],
                s=300,color=racing_colours+['black'],marker=constants.racingCamelMarker)
    
    for unmoved_camel in state.camels_to_move:
        if unmoved_camel == 'crazy':
            camel_display.drop(state.racing_camel_count,inplace=True)
        else:
            camel_display.drop(unmoved_camel,inplace=True)
    
    axis_moved_camels.scatter(camel_display[0],
                camel_display[1],
                s=150,linewidth=1,color='black',marker='X',edgecolor='white')
    
    axis_moved_camels.set_ylim(-0.15,1)
    
    if type(leg_win_probs) == np.ndarray:
        axis_leg_probs = fig1.add_axes([0.22,0.51,0.1,0.23])
        axis_leg_probs.text(0,4.8,'Win leg')
        axis_leg_probs.axis('off')
        axis_leg_probs.barh(np.arange(state.racing_camel_count),leg_win_probs,align='center',color=racing_colours+['black'])
        axis_leg_probs.set_xlim(0,1)
        for i,value in enumerate(leg_win_probs):
            axis_leg_probs.text(0.5,i-0.3,f'{round(value,2)}')
    
    if type(race_win_probs) == np.ndarray:
        axis_race_probs = fig1.add_axes([0.35,0.51,0.1,0.23])
        axis_race_probs.text(0,4.8,'Win race')
        axis_race_probs.axis('off')
        axis_race_probs.barh(np.arange(state.racing_camel_count),race_win_probs,align='center',color=racing_colours+['black'])
        axis_race_probs.set_xlim(0,1)
        for i,value in enumerate(race_win_probs):
            axis_race_probs.text(0.5,i-0.3,f'{round(value,2)}')
            
    if type(race_lose_probs) == np.ndarray:
        axis_lose_probs = fig1.add_axes([0.48,0.51,0.1,0.23])
        axis_lose_probs.text(0,4.8,'Lose race')
        axis_lose_probs.axis('off')
        axis_lose_probs.barh(np.arange(state.racing_camel_count),race_lose_probs,align='center',color=racing_colours+['black'])
        axis_lose_probs.set_xlim(0,1)
        for i,value in enumerate(race_lose_probs):
            axis_lose_probs.text(0.5,i-0.3,f'{round(value,2)}')
    
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
    
def plot_area(race_winners_list):
    
    winners_df = pd.DataFrame(race_winners_list)
    winners_df.plot.area(color=racing_colours)
    
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