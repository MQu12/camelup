# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 22:00:22 2021

@author: Dr. P
"""

from camelup import race_state
from camels import racing_camel, crazy_camel
import monte_carlo
import make_plots
import random

camel_list = []
    
camel_list.append( racing_camel(0,0) )
camel_list.append( racing_camel(1,0) )
camel_list.append( racing_camel(2,1) )
camel_list.append( racing_camel(3,2) )
camel_list.append( racing_camel(4,2) )
camel_list.append( crazy_camel(0,15) )
camel_list.append( crazy_camel(1,14) )

state = race_state()

random.seed(3)

race_winners_list = []

final_state,all_states_list = monte_carlo.simulate_race(state,True)
for state in all_states_list:
    
    leg_winners = monte_carlo.simulate_leg_n_times(state, 1000)
    race_winners = monte_carlo.simulate_n_races(state,1000)
    
    make_plots.plot_state(state,leg_winners/leg_winners.sum(),race_winners/race_winners.sum())
    
    race_winners_list.append(race_winners)
    
make_plots.plot_area(race_winners_list)