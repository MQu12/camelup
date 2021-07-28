# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 18:06:32 2021

@author: Dr. P
"""

from copy import deepcopy
import numpy as np
import random
import constants

def reseed():
    random.seed(constants.RANDOM_SEED)
    np.random.seed(constants.RANDOM_SEED)

reseed()

def simulate_leg(prev_state, output_all=False):
    '''
    Simulate a leg of the race.

    Parameters
    ----------
    prev_state : race_state
        Previous race state.
    output_all : bool, optional
        Output all intermediate states. The default is False.

    Returns
    -------
    new_state : race_state
        New state of the race.
    all_states_list : list(race_state)
        List of all intermediate race states. Only output if output_all is true.

    '''
    
    all_states_list = None
    if output_all:
        all_states_list = []
    
    new_state = deepcopy(prev_state)
    
    camels_moved_in_leg = new_state.get_n_racing_camels() + new_state.get_n_crazy_dice() - len(new_state.camels_to_move)
    
    for i in range(new_state.leg_length-camels_moved_in_leg):
        if new_state.get_game_end():
            break
        new_state = advance_camel(new_state)
        if output_all:
            all_states_list.append(new_state)
        
    if not new_state.game_end:
        new_state.reset_leg()
        
    return new_state, all_states_list

def simulate_leg_n_times(state,n):
    '''
    Simulate a leg n times

    Parameters
    ----------
    state : race_state
        State of the race.
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
    '''
    Simulate an entire race once.

    Parameters
    ----------
    state : race_state
        Initial state of the race.
    output_all : bool, optional
        Output intermediate states. The default is False.

    Returns
    -------
    final_state : race_state
        Final state of the race after the first camel has crossed the line.
    all_states_list : list(race_state)
        List of all intermediate race states. Only output if output_all is true..

    '''
    
    final_state = deepcopy(state)
    
    all_states_list = [state]
    
    while not final_state.game_end:
        final_state, leg_states = simulate_leg(final_state, output_all)
        if output_all:
            all_states_list += leg_states
        
    return final_state, all_states_list

def simulate_n_races(state,n):
    '''
    Simulate a race n times from a starting state.

    Parameters
    ----------
    state : race_state
        Initial state of the race.
    n : int
        Number of iterations to perform.

    Returns
    -------
    winners : array(float)
        Array of wins per camel.

    '''
    
    winners = np.zeros(state.racing_camel_count)
    losers = np.zeros(state.racing_camel_count)
    
    for i in range(n):
        final_state,_ = simulate_race(state)
        winner = final_state.get_leader()
        loser = final_state.get_last_place()
        winners[winner] += 1
        losers[loser] += 1
        
    return winners, losers

def advance_camel(state):
    '''
    Advance a camel at random

    Parameters
    ----------
    state : race_state
        State of the race.

    Returns
    -------
    new_state : race_state
        State of the race after camel has moved.
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
    new_race_state.camels_moved_this_leg.append(camel_no)
    
    return new_race_state