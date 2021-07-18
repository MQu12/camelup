# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 22:08:51 2021

@author: Dr. P
"""

from camelup import race_state
import monte_carlo
import make_plots
import constants

constants.RANDOM_SEED = 4

print('Initialising race')
bigstate = race_state(n_racing_camels=20,n_crazy_camels=8,n_crazy_dice=4,track_length=100,leg_length=20)

race_winners_list = []
race_losers_list = []
leg_winners_list = []

print('Simulating race')
final_state,all_states_list = monte_carlo.simulate_race(bigstate,True)

monte_carlo.reseed()

print('Calculating probabilities')
for state in all_states_list:
    
    leg_winners = monte_carlo.simulate_leg_n_times(state, 100)
    race_winners, race_losers = monte_carlo.simulate_n_races(state,100)
    
    make_plots.plot_state(state,leg_winners/leg_winners.sum(), 
                          race_winners/race_winners.sum(), 
                          race_losers/race_losers.sum(), 
                          camel_size=100,tick_spacing=5,ymax=32)

    race_winners_list.append(race_winners)
    race_losers_list.append(race_losers)
    leg_winners_list.append(leg_winners)
    
make_plots.plot_area(race_winners_list)
make_plots.plot_area(race_losers_list)
make_plots.plot_area(leg_winners_list)
make_plots.plot_movement_per_camel(final_state)
make_plots.plot_move_efficiency_per_camel(final_state)
make_plots.plot_leg_winners(final_state)
make_plots.plot_leg_wins_per_camel(final_state)