# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 22:08:51 2021

@author: Dr. P
"""

from camelup import race_state
import monte_carlo
import make_plots

bigstate = race_state(n_racing_camels=20,n_crazy_camels=5,track_length=100,leg_length=15)
newbigstate,_=monte_carlo.simulate_leg(bigstate)
leg_winners=monte_carlo.simulate_leg_n_times(newbigstate,100)
make_plots.plot_state(newbigstate,leg_winners/leg_winners.sum(),camel_size=100,tick_spacing=5,ymax=32)