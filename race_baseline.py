# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 22:00:22 2021

@author: Dr. P
"""

import time
import constants
import monte_carlo
import make_plots

if constants.USE_CPP_CLASSES:
    from cpp_camels import race_state
else:
    from camelup import race_state


constants.RANDOM_SEED = 420

start_time = time.time()

state = race_state()

race_winners_list = []
race_losers_list = []

final_state,all_states_list = monte_carlo.simulate_race(state,True)
for state in all_states_list:
    
    leg_winners = monte_carlo.simulate_leg_n_times(state, 1000)
    race_winners, race_losers = monte_carlo.simulate_n_races(state,1000)
    
    make_plots.plot_state(state,leg_winners/leg_winners.sum(), race_winners/race_winners.sum(), race_losers/race_losers.sum())
    
    race_winners_list.append(race_winners)
    race_losers_list.append(race_losers)
    
make_plots.plot_area(race_winners_list,'winners')
make_plots.plot_area(race_losers_list,'losers')
make_plots.plot_movement_per_camel(final_state)
make_plots.plot_move_efficiency_per_camel(final_state)
make_plots.plot_leg_winners(final_state)
make_plots.plot_leg_wins_per_camel(final_state)

print(f'Ran script in {time.time() - start_time}s')