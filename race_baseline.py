# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 22:00:22 2021

@author: Dr. P
"""

from camelup import race_state
import monte_carlo
import make_plots
import random

state = race_state()

random.seed(420)

race_winners_list = []
race_losers_list = []

final_state,all_states_list = monte_carlo.simulate_race(state,True)
for state in all_states_list:
    
    leg_winners = monte_carlo.simulate_leg_n_times(state, 1000)
    race_winners, race_losers = monte_carlo.simulate_n_races(state,1000)
    
    make_plots.plot_state(state,leg_winners/leg_winners.sum(), race_winners/race_winners.sum(), race_losers/race_losers.sum())
    
    race_winners_list.append(race_winners)
    race_losers_list.append(race_losers)
    
make_plots.plot_area(race_winners_list)
make_plots.plot_area(race_losers_list)