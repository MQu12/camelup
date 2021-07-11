# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 21:41:58 2021

@author: Dr. P
"""

import constants

constants.RANDOM_SEED = 1

import numpy as np
import simulation_baseline

folder = 'baselines/'

def test_vs_leg_baseline():
    
    leg1000_name = 'leg1000_baseline.npy'
    
    with open(folder+leg1000_name, 'rb') as f:
        baseline = np.load(f)
        
    state = simulation_baseline.init_race()
    
    result = simulation_baseline.run_leg_baseline(state)

    np.testing.assert_array_equal(baseline,result)
    
def test_vs_race_baseline():
    
    race1000_name = 'race1000_baseline.npy'
    
    with open(folder+race1000_name, 'rb') as f:
        baseline = np.load(f)
        
    state = simulation_baseline.init_race()
    
    winners = simulation_baseline.run_race_baseline(state)

    np.testing.assert_array_equal(baseline,winners)
    
