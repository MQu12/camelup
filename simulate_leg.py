# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 21:46:32 2021

@author: Dr. P
"""

from camelup import race_state
from camels import racing_camel, crazy_camel
from matplotlib import pyplot as plt
import monte_carlo

racing_colours = ['red','green','orange','blue','purple']
crazy_colours = ['black','white']

camel_list = []

camel_list.append( racing_camel(0,0) )
camel_list.append( racing_camel(1,0) )
camel_list.append( racing_camel(2,1) )
camel_list.append( racing_camel(3,2) )
camel_list.append( racing_camel(4,2) )
camel_list.append( crazy_camel(0,15) )
camel_list.append( crazy_camel(1,14) )

state = race_state(camel_list)

n=10000
winners = monte_carlo.simulate_leg_n_times(state,n)
plt.pie(winners,colors=racing_colours,autopct='%1.f%%')
plt.title('Leg win probability')
plt.show()

winners = monte_carlo.simulate_n_races(state,n)
plt.pie(winners,colors=racing_colours,autopct='%1.f%%')
plt.title('Race win probability')
plt.show()