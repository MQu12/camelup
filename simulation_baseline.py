# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 21:46:32 2021

@author: Dr. P
"""

from camelup import race_state
from camels import racing_camel, crazy_camel
import monte_carlo
import make_plots

camel_list = []

camel_list.append( racing_camel(0,0) )
camel_list.append( racing_camel(1,0) )
camel_list.append( racing_camel(2,1) )
camel_list.append( racing_camel(3,2) )
camel_list.append( racing_camel(4,2) )
camel_list.append( crazy_camel(0,15) )
camel_list.append( crazy_camel(1,14) )

state = race_state(camel_list)

n=1000
leg_winners = monte_carlo.simulate_leg_n_times(state,n)
make_plots.plot_win_probs(leg_winners,'Leg win probability')
race_winners = monte_carlo.simulate_n_races(state,n)
make_plots.plot_win_probs(race_winners,'Race win probability')