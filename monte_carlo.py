# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 18:06:32 2021

@author: Dr. P
"""

from copy import deepcopy
import numpy as np
import random

def simulate_leg(prev_state, output_all=False):
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
    
    new_state = deepcopy(prev_state)
    
    for i in range(prev_state.leg_length):
        new_state = advance_camel(new_state)
        if output_all:
            all_states_list.append(new_state)
        if new_state.game_end:
            break
        
    new_state.reset_leg()
        
    return new_state, all_states_list

def simulate_leg_n_times(state,n):
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

    winners = np.zeros(state.racing_camel_count)
    
    for i in range(n):
        final_state,_ = simulate_leg(state)
        leader = final_state.get_leader()
        winners[leader] += 1
        
    return winners

def simulate_race(state, output_all=False):
    
    final_state = deepcopy(state)
    
    all_states_list = [state]
    
    while not state.game_end:
        final_state, leg_states = simulate_leg(final_state, output_all)
        if output_all:
            all_states_list += leg_states
        
    return final_state, all_states_list

def simulate_n_races(state,n):
    
    winners = np.zeros(state.racing_camel_count)
    
    for i in range(n):
        final_state,_ = simulate_race(state)
        winner = final_state.get_leader()
        winners[winner] += 1
        
    return winners

def advance_camel(state):
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
    
    new_race_state = deepcopy(state)
    
    camel_no = new_race_state.camels_to_move[random.randint(0,len(new_race_state.camels_to_move)-1)]
    
    roll = random.randint(new_race_state.min_roll,new_race_state.max_roll)
    
    if camel_no != 'crazy':
        # advance racing camel
        camel = new_race_state.camel_list[camel_no]
        final_pos = camel.position + roll
        new_race_state.move_camel_to(camel_no, final_pos)
        
    else:
        # advance crazy camel
        crazy_camel_no = new_race_state.pick_crazy_camel()
        camel = new_race_state.camel_list[new_race_state.racing_camel_count+crazy_camel_no]
        final_pos = camel.position - roll
        new_race_state.move_camel_to(new_race_state.racing_camel_count+crazy_camel_no, final_pos)
    
    new_race_state.camels_to_move.remove(camel_no)
    
    return new_race_state