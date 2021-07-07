# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 15:55:25 2021

@author: Dr. P
"""

from camels import racing_camel, crazy_camel
import matplotlib.pyplot as plt
import random
import numpy as np
from copy import deepcopy

track_length = 16
leg_length = 5
max_roll = 3
min_roll = 1

racing_colours = ['red','green','orange','blue','purple']
crazy_colours = ['black','white']

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
    final_state : list[camel]
        Updated list.
    game_end : bool
        True if a racing camel has crossed the finish line. False if not.

    '''

    target_camel_stack_pos = camel_list[camel_no].stack_position
    init_camel_pos = camel_list[camel_no].position
    
    camels_to_move = []
    camels_at_destination = 0
    
    game_end = False
    
    final_state = deepcopy(camel_list)
    
    for i,camel in enumerate(camel_list):
        
        if camel.position == init_camel_pos and camel.stack_position >= target_camel_stack_pos:
            camels_to_move.append(i)
            
        if camel.position == final_pos:
            camels_at_destination += 1
            
    for camel_id in camels_to_move:
        final_state[camel_id].position = final_pos
        final_state[camel_id].stack_position += (camels_at_destination - target_camel_stack_pos)
    
    if final_pos >= track_length:
        game_end = True
    
    return final_state, game_end

def pick_crazy_camel(camel_list,racing_camel_count):
    '''
    Pick a crazy camel to move based on game rules.
    1. If a crazy camel is directly atop another, move it
    2. If only one crazy camel is carrying racing camels, move it
    3. Otherwise, pick one at random

    Parameters
    ----------
    camel_list : list[camel]
        List of camels.
    racing_camel_count : int
        Number of racing camels.

    Returns
    -------
    crazy_camel_no : int
        ID of the crazy camel to move.

    '''
    
    crazy_camel_no = -1
    
    crazy_camel_0 = camel_list[racing_camel_count]
    crazy_camel_1 = camel_list[racing_camel_count+1]
    
    # check if either crazy camel is carrying any racing camels
    crazy_camel_0_is_carrying = False
    crazy_camel_1_is_carrying = False
    
    for i in range(0,racing_camel_count):
        if not crazy_camel_0_is_carrying and crazy_camel_0.position == camel_list[i].position:
            if camel_list[i].stack_position > crazy_camel_0.stack_position:
                crazy_camel_0_is_carrying = True
        if not crazy_camel_1_is_carrying and crazy_camel_1.position == camel_list[i].position:
            if camel_list[i].stack_position > crazy_camel_1.stack_position:
                crazy_camel_1_is_carrying = True
        if crazy_camel_0_is_carrying and crazy_camel_1_is_carrying:
            break
    
    # if one crazy camel is directly on top of another, move it
    if crazy_camel_0.position == crazy_camel_1.position and abs(crazy_camel_0.stack_position - crazy_camel_1.stack_position) == 1:
        if crazy_camel_0.stack_position > crazy_camel_1.stack_position:
            crazy_camel_no = 0
        else:
            crazy_camel_no = 1
    
    # if only one crazy camel is carrying racing camels, move it
    elif crazy_camel_0_is_carrying != crazy_camel_1_is_carrying:
        if crazy_camel_0_is_carrying:
            crazy_camel_no = 0
        else:
            crazy_camel_no = 1
        
    # otherwise, pick one at random
    else:
        crazy_camel_no = random.randint(0,crazy_camel_count-1)
        
    if crazy_camel_no == -1:
        raise ValueError('Crazy camel number should not be -1')
        
    return crazy_camel_no

def advance_camel(camel_list,racing_camel_count,crazy_camel_count,camels_to_move):
    '''
    Advance a camel at random

    Parameters
    ----------
    camel_list : list[camel]
        List of camels.
    racing_camel_count : int
        Number of racing camels.
    crazy_camel_count : int
        Number of crazy camels.
    camels_to_move : list
        List of camels yet to move.

    Returns
    -------
    updated_camel_list : list[camel]
        Updated list of camels.
    camels_to_move : list
        Same as input list but with moved camel removed.
    game_end : bool
        True if a racing camel has crossed the finish line. False if not.
    '''
    
    camel_no = camels_to_move[random.randint(0,len(camels_to_move)-1)]
    
    roll = random.randint(min_roll,max_roll)
    
    game_end = False
    
    if camel_no != 'crazy':
        # advance racing camel
        camel = camel_list[camel_no]
        final_pos = camel.position + roll
        updated_camel_list,game_end = move_camel_to(camel_list, camel_no, final_pos)
        
    else:
        # advance crazy camel
        crazy_camel_no = pick_crazy_camel(camel_list,racing_camel_count)
        camel = camel_list[racing_camel_count+crazy_camel_no]
        final_pos = camel.position - roll
        updated_camel_list,_ = move_camel_to(camel_list, racing_camel_count+crazy_camel_no, final_pos)
    
    camels_to_move.remove(camel_no)
    
    return updated_camel_list, camels_to_move, game_end
    
def get_leader(camel_list):
    '''
    Get camel at the front

    Parameters
    ----------
    camel_list : list[camel]
        List of camels.

    Returns
    -------
    leading_camel_id : int
        ID of the leading camel.

    '''
    
    largest_forward = 0
    largest_upward = 0
    leading_camel_id = 0
    
    for camel in camel_list:
        if type(camel) == crazy_camel:
            continue
        if camel.position > largest_forward or camel.position == largest_forward and camel.stack_position > largest_upward:
            largest_forward = camel.position
            largest_upward = camel.stack_position
            leading_camel_id = camel.id
        else:
            continue
        
    return leading_camel_id
            
    
def plot_state(camel_list):
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
    
    for camel in camel_list:
        
        if type(camel) == racing_camel:
            col = racing_colours[camel.id]
            plt.scatter(camel.position,camel.stack_position,color=col)
            
        else:
            col = crazy_colours[camel.id]
            plt.scatter(camel.position,camel.stack_position,color=col,edgecolors='black')
            
    plt.xlim(-1,track_length)
    plt.ylim(-0.5,7.5)
    plt.show()

def simulate_leg(camel_list, output_all=False):
    '''
    Simulate a leg of the race

    Parameters
    ----------
    camel_list : list[camel]
        Starting positions of camels.
    output_all : bool, optional
        If true, a list of list of camels will be ouput
        detailing the state of the race after each die roll.
        The default is False.

    Returns
    -------
    camel_list : list[camel]
        Finishing positions of camels
    all_states_list: list[list[camel]]
        List of list of camel states after each die roll.
        Only output if output_all is true.
    game_end : bool
        True if a racing camel has crossed the finish line. False if not.
    
    '''
    
    all_states_list = None
    if output_all:
        all_states_list = []
    
    camels_to_move = [i for i in range(racing_camel_count)]
    camels_to_move.append('crazy')
    
    for i in range(leg_length):
        camel_list, camels_to_move, game_end = advance_camel(camel_list,racing_camel_count,crazy_camel_count,camels_to_move)
        if output_all:
            all_states_list.append(camel_list)
        if game_end:
            break
        
    return camel_list, all_states_list, game_end

def simulate_leg_n_times(camel_list,n):
    '''
    Simulate a leg n times

    Parameters
    ----------
    camel_list : list[camel]
        List of camels.
    n : int
        Number of iterations.

    Returns
    -------
    winners : array[float]
        Wins per camel.

    '''

    winners = np.zeros(racing_camel_count)
    
    for i in range(n):
        final_state,_,_ = simulate_leg(camel_list)
        leader = get_leader(final_state)
        winners[leader] += 1
        
    return winners

def simulate_race(camel_list, output_all=False):
    
    game_end = False
    final_state = deepcopy(camel_list)
    
    all_states_list = [camel_list]
    
    while not game_end:
        final_state, leg_states, game_end = simulate_leg(final_state, output_all)
        if output_all:
            all_states_list += leg_states
        
    return final_state, all_states_list

def simulate_n_races(camel_list,n):
    
    winners = np.zeros(racing_camel_count)
    
    for i in range(n):
        final_state,_ = simulate_race(camel_list)
        winner = get_leader(final_state)
        winners[winner] += 1
        
    return winners

'''
n=10000
winners = simulate_leg_n_times(camel_list,n)
plt.pie(winners,colors=racing_colours,autopct='%1.f%%')
plt.title('Leg win probability')
plt.show()
winners = simulate_n_races(camel_list,n)
plt.pie(winners,colors=racing_colours,autopct='%1.f%%')
plt.title('Race win probability')
plt.show()
'''

#TODO test pick_crazy_camel function
#TODO add extra file to run experiments
#TODO add running probs for an entire race

'''
final_state,all_states_list = simulate_race(camel_list,True)
for state in all_states_list:
    plot_state(state)
    plt.show()
'''