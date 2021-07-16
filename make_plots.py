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

def plot_state(state, leg_win_probs=None, race_win_probs=None, race_lose_probs=None, **kwargs):
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
    if 'camel_size' in kwargs:
        camel_size = kwargs['camel_size']
        
    tick_spacing = 1.0
    if 'tick_spacing' in kwargs:
        tick_spacing = kwargs['tick_spacing']
        
    ymax = 7.5
    if 'ymax' in kwargs:
        ymax = kwargs['ymax']
    
    fig1 = plt.figure(facecolor='white')
    axis_main = plt.axes()
    axis_main.axes.get_yaxis().set_visible(False)
    axis_main.text(0.02,0.95,f'Leg {state.leg_num}', transform=axis_main.transAxes)
    axis_main.text(0.02,0.90,f'After {state.num_moves} moves', transform=axis_main.transAxes)
    
    for camel in state.camel_list:
        
        if type(camel) == racing_camel:
            col = constants.RACING_COLOURS[camel.id]
            axis_main.scatter(camel.position+0.2,camel.stack_position,color=col,s=camel_size,marker=constants.racingCamelMarker)
            
        else:
            col = constants.CRAZY_COLOURS[camel.id]
            axis_main.scatter(camel.position-0.3,camel.stack_position,color=col,s=camel_size,edgecolors='black',marker=constants.crazyCamelMarker)
            
    axis_main.set_xlim(-1,state.track_length)
    axis_main.set_xticks(np.arange(0, state.track_length+1, tick_spacing))
    axis_main.set_ylim(-0.5,ymax)
    
    xpanel_offset = 0
    if state.racing_camel_count + state.crazy_camel_count < 8:
        axis_moved_camels = fig1.add_axes([0.12,0.5,0.1,0.3])
        axis_moved_camels.axis('off')
        
        xpos = np.zeros(state.racing_camel_count+1)
        ypos = np.arange(0,state.racing_camel_count+1)/(state.racing_camel_count+1)
        camel_display = pd.DataFrame([xpos,ypos]).T
        
        axis_moved_camels.scatter(camel_display[0],
                    camel_display[1],
                    s=300,color=constants.RACING_COLOURS[:state.racing_camel_count]+['black'],marker=constants.racingCamelMarker)
        
        for unmoved_camel in state.camels_to_move:
            if unmoved_camel == 'crazy':
                camel_display.drop(state.racing_camel_count,inplace=True)
            else:
                camel_display.drop(unmoved_camel,inplace=True)
        
        axis_moved_camels.scatter(camel_display[0],
                    camel_display[1],
                    s=150,linewidth=1,color='black',marker='X',edgecolor='white')
        
        axis_moved_camels.set_ylim(-0.15,1)
    
    else:
        xpanel_offset = -0.08
        axis_moved_camels = fig1.add_axes([0.12,0.42,0.8,0.06])
        axis_moved_camels.axis('off')
        axis_moved_camels.text(-0.02,0.06,'Moved this leg:')
        
        cols = np.array(state.camels_moved_this_leg)
        xpos = np.arange(0,len(cols))/(state.racing_camel_count+1)
        
        if len(xpos) > 0:
            ypos = np.zeros(len(xpos))
            camel_display = pd.DataFrame([xpos,ypos]).T
            axis_moved_camels.scatter(camel_display[0],
                        camel_display[1],
                        s=200,color=np.array(constants.RACING_COLOURS[:state.racing_camel_count]+['black'])[cols],marker=constants.racingCamelMarker)
        axis_moved_camels.set_xlim(-0.05,1)
    
    if type(leg_win_probs) == np.ndarray:
        event_probability_sublpot(fig1, [0.22+xpanel_offset,0.51,0.1,0.23], 'Win leg', leg_win_probs, state)
    
    if type(race_win_probs) == np.ndarray:
        event_probability_sublpot(fig1, [0.35+xpanel_offset,0.51,0.1,0.23], 'Win race', race_win_probs, state)
            
    if type(race_lose_probs) == np.ndarray:
        event_probability_sublpot(fig1, [0.48+xpanel_offset,0.51,0.1,0.23], 'Lose race', race_lose_probs, state)
    
    plt.show()
    
def event_probability_sublpot(fig, shape, text, values, state):
    
    axis_leg_probs = fig.add_axes(shape)
    axis_leg_probs.text(0,4.8, text)
    axis_leg_probs.axis('off')
    axis_leg_probs.set_xlim(0,1)
    
    if len(values) > 5:
        top5 = pd.DataFrame(zip(values,constants.RACING_COLOURS)).sort_values(0).iloc[-5:]
        axis_leg_probs.barh(np.arange(5), top5[0], align='center', color=top5[1])
        
        for i,value in enumerate(top5[0]):
            axis_leg_probs.text(0.5,i-0.3,f'{round(value,2)}')
        
    else:
        axis_leg_probs.barh(np.arange(state.racing_camel_count), values, align='center', color=constants.RACING_COLOURS)
    
        for i,value in enumerate(values):
            axis_leg_probs.text(0.5,i-0.3,f'{round(value,2)}')
    
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
    
    plt.pie(winners,colors=constants.RACING_COLOURS,autopct='%1.f%%')
    plt.title(title)
    plt.show()
    
def plot_area(race_winners_list):
    
    winners_df = pd.DataFrame(race_winners_list)
    fig, ax = plt.subplots()
    ax.stackplot(winners_df.index, winners_df.values.T,colors=constants.RACING_COLOURS)
    ax.set_ylim(0,winners_df.iloc[0].sum())
    ax.set_xlim(0,len(winners_df)-1)
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