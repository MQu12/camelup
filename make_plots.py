# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 21:55:43 2021

@author: Dr. P
"""
import constants
if constants.USE_CPP_CLASSES:
    from cpp_camels import race_state, racing_camel, crazy_camel
else:
    from camels import racing_camel,crazy_camel
    from camelup import race_state

from matplotlib import pyplot as plt
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
    axis_main.text(0.02,0.95,f'Leg {state.get_leg_num()}', transform=axis_main.transAxes)
    axis_main.text(0.02,0.90,f'After {state.get_num_moves()} moves', transform=axis_main.transAxes)
    
    for i in range(len(state.get_camel_list())):
        
        camel = state.get_camel_list()[i]

        if type(camel) == racing_camel:
            col = constants.RACING_COLOURS[camel.id]
            axis_main.scatter(camel.position+0.2,camel.stack_position,color=col,s=camel_size,marker=constants.racingCamelMarker)
            
        else:
            col = constants.CRAZY_COLOURS[camel.id]
            axis_main.scatter(camel.position-0.3,camel.stack_position,color=col,s=camel_size,edgecolors='black',marker=constants.crazyCamelMarker)
            
    axis_main.set_xlim(-1,state.get_track_length())
    axis_main.set_xticks(np.arange(0, state.get_track_length()+1, tick_spacing))
    axis_main.set_ylim(-0.5,ymax)
    
    xpanel_offset = 0
    if state.get_n_racing_camels() + state.get_n_crazy_camels() < 8:
        axis_moved_camels = fig1.add_axes([0.12,0.5,0.1,0.3])
        axis_moved_camels.axis('off')
        
        xpos = np.zeros(state.get_n_racing_camels()+1)
        ypos = np.arange(0,state.get_n_racing_camels()+1)/(state.get_n_racing_camels()+1)
        camel_display = pd.DataFrame([xpos,ypos]).T
        
        axis_moved_camels.scatter(camel_display[0],
                    camel_display[1],
                    s=300,color=constants.RACING_COLOURS[:state.get_n_racing_camels()]+['black'],marker=constants.racingCamelMarker)
        
        for unmoved_camel in state.get_camels_to_move():
            if unmoved_camel == 'crazy' or unmoved_camel == -1:
                camel_display.drop(state.get_n_racing_camels(),inplace=True)
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
        
        cols = np.array(state.get_camels_moved_this_leg())
        cols = np.where(cols=='crazy',-1,cols).astype(int)
        xpos = np.arange(0,len(cols))/(state.get_n_racing_camels()+1)
        
        ypos = np.zeros(len(xpos))
        camel_display = pd.DataFrame([xpos,ypos]).T
        axis_moved_camels.scatter(camel_display[0],
                    camel_display[1],
                    s=200,color=np.array(constants.RACING_COLOURS[:state.get_n_racing_camels()]+['black'])[cols],marker=constants.racingCamelMarker)
        axis_moved_camels.set_xlim(-0.05,1)
    
    if type(leg_win_probs) == np.ndarray:
        event_probability_sublpot(fig1, [0.22+xpanel_offset,0.51,0.1,0.23], 'Win leg', leg_win_probs, state)
    
    if type(race_win_probs) == np.ndarray:
        event_probability_sublpot(fig1, [0.35+xpanel_offset,0.51,0.1,0.23], 'Win race', race_win_probs, state)
            
    if type(race_lose_probs) == np.ndarray:
        event_probability_sublpot(fig1, [0.48+xpanel_offset,0.51,0.1,0.23], 'Lose race', race_lose_probs, state)
    
    if len(state.get_leg_winners()) > 0:
        axis_last_leg_winner = fig1.add_axes([0.6,0.6,0.3,0.2])
        axis_last_leg_winner.axis('off')
        axis_last_leg_winner.scatter(0,0,color=constants.RACING_COLOURS[state.get_leg_winners()[-1]],s=400,marker=constants.racingCamelMarker)
        axis_last_leg_winner.text(-0.033,-0.018,'Previous\nleg winner',ha='center')
    
    if constants.PLOT_METHOD == 0:
        plt.show()
    elif constants.PLOT_METHOD == 1:
        plt.savefig(f'plots/dump/race_state_move_{state.get_num_moves()}.png')
    
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
        axis_leg_probs.barh(np.arange(state.get_n_racing_camels()), values, align='center', color=constants.RACING_COLOURS)
    
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
    if constants.PLOT_METHOD == 0:
        plt.show()
    elif constants.PLOT_METHOD == 1:
        plt.savefig('plots/dump/winners_pie.png')
    
def plot_area(race_winners_list,sort='winners'):
    '''
    Plot an area plot of the win/lose probabilities per camel

    Parameters
    ----------
    race_winners_list : list(np.ndarray)
        List of win probs per camel per step.

    Returns
    -------
    None.

    '''
    
    winners_df = pd.DataFrame(race_winners_list)
    fig, ax = plt.subplots()
    ax.stackplot(winners_df.index, winners_df.values.T,colors=constants.RACING_COLOURS)
    ax.set_ylim(0,winners_df.iloc[0].sum())
    ax.set_xlim(0,len(winners_df)-1)
    if constants.PLOT_METHOD == 0:
        plt.show()
    elif constants.PLOT_METHOD == 1:
        plt.savefig(f'plots/dump/{sort}_area.png')
    
def plot_movement_per_camel(final_state):
    
    movement_array = []
    
    for i in range(len(final_state.get_camel_list())):
        camel = final_state.get_camel_list()[i]
        if type(camel) == racing_camel:
            movement_array.append(camel.total_movement)

    movement_array = np.array(movement_array)
    ypos = np.zeros(len(movement_array))
    
    for i, move in enumerate(movement_array):
        count = list(movement_array[:i]).count(move)
        ypos[i] += count
    
    plt.figure(facecolor='white')
    axis_main = plt.axes()
    axis_main.scatter(movement_array, ypos, color=constants.RACING_COLOURS[:final_state.get_n_racing_camels()], marker=constants.racingCamelMarker, s=400, zorder=1 )  
    axis_main.set_xticks(np.arange(movement_array.min(), movement_array.max()+1))
    axis_main.axes.get_yaxis().set_visible(False)
    
    move_range = movement_array.max() - movement_array.min()
    axis_main.set_ylim(-0.5,(move_range*16/20))
    axis_main.set_xlabel('Movement per camel')
    
    if constants.PLOT_METHOD == 0:
        plt.show()
    elif constants.PLOT_METHOD == 1:
        plt.savefig('plots/dump/movement_per_camel.png')
    
def plot_move_efficiency_per_camel(final_state):
    
    movement_array = []
    distance_array = []
    
    for i in range(len(final_state.get_camel_list())):
        camel = final_state.get_camel_list()[i]
        if type(camel) == racing_camel:
            movement_array.append(camel.total_movement)
            distance_array.append(camel.position)
            
    eff_array = np.array(distance_array)/np.array(movement_array)
    xpos = np.arange(0,len(eff_array))
      
    plt.figure(facecolor='white')
    ax = plt.axes()
    ax.bar(xpos,eff_array,color=constants.RACING_COLOURS, zorder=0)     
    ax.scatter(xpos,eff_array, color=constants.RACING_COLOURS[:final_state.get_n_racing_camels()], marker=constants.racingCamelMarker, edgecolors='white', s=400, zorder=1)  
    ax.axes.get_xaxis().set_visible(False)
    ax.set_ylabel('Distance covered per movement')
    if constants.PLOT_METHOD == 0:
        plt.show()
    elif constants.PLOT_METHOD == 1:
        plt.savefig('plots/dump/movement_efficiency.png')
    
def plot_leg_winners(final_state):
    
    winner_per_leg = np.array(constants.RACING_COLOURS[:final_state.get_n_racing_camels()])[final_state.get_leg_winners()]
    xpos = np.arange(1,len(winner_per_leg)+1)
    ypos = np.zeros(len(winner_per_leg))
    
    plt.figure(facecolor='white')
    ax = plt.axes()
    ax.scatter(xpos,ypos, color=winner_per_leg, marker=constants.racingCamelMarker, s=90)
    ax.axes.get_yaxis().set_visible(False)
    ax.set_xlabel('Leg')
    ax.set_title('Winner per leg')
    if constants.PLOT_METHOD == 0:
        plt.show()
    elif constants.PLOT_METHOD == 1:
        plt.savefig('plots/dump/leg_winners.png')
    
def plot_leg_wins_per_camel(final_state):
    
    wins = np.bincount(np.array(final_state.get_leg_winners()))
    x = np.arange(0,len(wins))
    cols = constants.RACING_COLOURS[:len(wins)]
    
    plt.figure(facecolor='white')
    ax = plt.axes()
    ax.bar(x,wins,color=cols,zorder=0)
    ax.scatter(x,wins,color=cols, marker=constants.racingCamelMarker, edgecolors='white', s=400, zorder=1)  
    ax.axes.get_xaxis().set_visible(False)
    ax.set_xlabel('Camel')
    ax.set_ylabel('Leg wins')
    if constants.PLOT_METHOD == 0:
        plt.show()
    elif constants.PLOT_METHOD == 1:
        plt.savefig('plots/dump/leg_wins_per_camel.png')
    
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