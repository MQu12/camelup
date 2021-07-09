# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 21:46:32 2021

Script to check updated results against baselines

@author: Dr. P
"""

from camelup import race_state
from camels import racing_camel, crazy_camel
import monte_carlo
import make_plots
import os.path
import numpy as np
import random

n=1000

def init_race():
    camel_list = []
    
    camel_list.append( racing_camel(0,0) )
    camel_list.append( racing_camel(1,0) )
    camel_list.append( racing_camel(2,1) )
    camel_list.append( racing_camel(3,2) )
    camel_list.append( racing_camel(4,2) )
    camel_list.append( crazy_camel(0,15) )
    camel_list.append( crazy_camel(1,14) )
    
    state = race_state(camel_list)

    return state

def run_leg_baseline(state,plot=False):
    random.seed(1)
    leg_winners = monte_carlo.simulate_leg_n_times(state,n)
    if plot:
        make_plots.plot_win_probs(leg_winners,'Leg win probability')
    return leg_winners

def run_race_baseline(state,plot=False):
    random.seed(1)
    race_winners = monte_carlo.simulate_n_races(state,n)
    if plot:
        make_plots.plot_win_probs(race_winners,'Race win probability')
    return race_winners
    
def create_baselines():
    
    state = init_race()
    
    folder = 'baselines/'
    leg1000_name = 'leg1000_baseline.npy'
    race1000_name = 'race1000_baseline.npy'
    
    if not os.path.isfile(folder+leg1000_name):
        leg1000_array = run_leg_baseline(state)
        with open(folder+leg1000_name, 'wb') as f:
            np.save(f, leg1000_array)
        print(f'Created new baseline {folder+leg1000_name}')
    else:
        print(f'Baseline {folder+leg1000_name} already exists, skipping')
    
    if not os.path.isfile(folder+race1000_name):
        race1000_array = run_race_baseline(state)
        with open(folder+race1000_name, 'wb') as f:
            np.save(f, race1000_array)
        print(f'Created new baseline {folder+race1000_name}')
    else:
        print(f'Baseline {folder+race1000_name} already exists, skipping')
    

def main():
    state = init_race()
    run_leg_baseline(state,True)
    run_race_baseline(state,True)
    
if __name__ == "__main__":
    main()