# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 22:00:22 2021

@author: Dr. P
"""

from camelup import race_state
from camels import racing_camel, crazy_camel
import monte_carlo
import make_plots
from matplotlib import pyplot as plt
import random

camel_list = []
    
camel_list.append( racing_camel(0,0) )
camel_list.append( racing_camel(1,0) )
camel_list.append( racing_camel(2,1) )
camel_list.append( racing_camel(3,2) )
camel_list.append( racing_camel(4,2) )
camel_list.append( crazy_camel(0,15) )
camel_list.append( crazy_camel(1,14) )

state = race_state(camel_list)

random.seed(1)

race_winners_list = []

final_state,all_states_list = monte_carlo.simulate_race(state,True)
for state in all_states_list:
    make_plots.plot_state(state)
    plt.show()
    
    winners = monte_carlo.simulate_n_races(state,1000)
    
    race_winners_list.append(winners)
    
make_plots.plot_area(race_winners_list)