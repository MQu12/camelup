# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 22:11:28 2021

@author: Dr. P
"""

from camelup import race_state
from camels import racing_camel, crazy_camel
import random
import numpy as np

def test_random_camel_is_picked_when_crazy_camels_are_apart(mocker):
    
    mocker.patch('random.randint')
    mocker.patch('numpy.random.choice')
    
    camel_list = []
    camel_list.append( crazy_camel(0,5) )
    camel_list.append( crazy_camel(1,6) )
    
    state = race_state(camel_list)

    state.pick_crazy_camel()
    
    random.randint.assert_called_once_with(0,1)
    np.random.choice.assert_not_called()

def test_top_camel_is_picked_when_crazy_camels_are_stacked(mocker):
    
    mocker.patch('random.randint')
    mocker.patch('numpy.random.choice')
    
    camel_list = []
    camel_list.append( crazy_camel(0,5) )
    camel_list.append( crazy_camel(1,5) )

    state = race_state(camel_list)

    crazy_camel_no = state.pick_crazy_camel()
    
    random.randint.assert_not_called()
    np.random.choice.assert_not_called()
    
    assert crazy_camel_no == 1
    
def test_camel_carrying_racing_camels_is_picked(mocker):
    
    mocker.patch('random.randint')
    mocker.patch('numpy.random.choice')
    
    camel_list = []
    camel_list.append( racing_camel(0,5) )
    camel_list.append( crazy_camel(0,9) )
    camel_list.append( crazy_camel(1,5) )

    state = race_state(camel_list)
    state.camel_list[0].stack_position = 1
    state.camel_list[2].stack_position = 0

    crazy_camel_no = state.pick_crazy_camel()
    
    random.randint.assert_not_called()
    np.random.choice.assert_not_called()
    
    assert crazy_camel_no == 1
    
def test_camel_picked_at_random_when_both_crazy_camels_are_carrying(mocker):
    
    mocker.patch('random.randint')
    npmocker = mocker.patch('numpy.random.choice')
    
    camel_list = []
    camel_list.append( racing_camel(0,5) )
    camel_list.append( racing_camel(1,9) )
    camel_list.append( crazy_camel(0,9) )
    camel_list.append( crazy_camel(1,5) )

    state = race_state(camel_list)
    state.camel_list[0].stack_position = 1
    state.camel_list[2].stack_position = 0
    state.camel_list[1].stack_position = 1
    state.camel_list[3].stack_position = 0

    state.pick_crazy_camel()
    
    random.randint.assert_not_called()
    np.random.choice.assert_called_once()
    np.testing.assert_array_equal(npmocker.call_args[0][0],np.array([0,1]))
    
def test_camel_at_bottom_of_stack_is_picked_when_there_is_a_racing_camel_between_two_crazy_camels(mocker):
    
    mocker.patch('random.randint')
    mocker.patch('numpy.random.choice')
    
    camel_list = []
    camel_list.append( racing_camel(0,5) )
    camel_list.append( crazy_camel(0,5) )
    camel_list.append( crazy_camel(1,5) )
    
    state = race_state(camel_list)
    state.camel_list[0].stack_position = 1
    state.camel_list[1].stack_position = 0
    
    crazy_camel_no = state.pick_crazy_camel()
    
    random.randint.assert_not_called()
    np.random.choice.assert_not_called()
    
    assert crazy_camel_no == 0
    
def test_crazy_camel_carrying_racing_camels_is_picked_over_crazy_carrying_crazy(mocker):
    
    mocker.patch('random.randint')
    mocker.patch('numpy.random.choice')
    
    camel_list = []
    camel_list.append( racing_camel(0,5) )
    camel_list.append( crazy_camel(0,5) )
    camel_list.append( crazy_camel(1,7) )
    camel_list.append( crazy_camel(2,7) )
    
    state = race_state(camel_list)
    state.camel_list[0].stack_position = 1
    state.camel_list[1].stack_position = 0
    
    crazy_camel_no = state.pick_crazy_camel()
    
    random.randint.assert_not_called()
    np.random.choice.assert_not_called()
    
    assert crazy_camel_no == 0
    
def test_one_of_crazy_camels_carrying_racing_camels_is_picked_over_lone_crazy(mocker):
    
    mocker.patch('random.randint')
    npmocker = mocker.patch('numpy.random.choice')
    
    camel_list = []
    camel_list.append( racing_camel(0,5) )
    camel_list.append( racing_camel(1,7) )
    camel_list.append( crazy_camel(0,5) )
    camel_list.append( crazy_camel(1,7) )
    camel_list.append( crazy_camel(2,9) )
    
    state = race_state(camel_list)
    state.camel_list[0].stack_position = 1
    state.camel_list[2].stack_position = 0
    state.camel_list[1].stack_position = 1
    state.camel_list[3].stack_position = 0
    
    state.pick_crazy_camel()
    
    random.randint.assert_not_called()
    np.random.choice.assert_called_once()
    np.testing.assert_array_equal(npmocker.call_args[0][0],np.array([0,1]))
    
def test_crazy_camel_picked_at_random_when_two_are_on_top_of_two_others(mocker):
    
    mocker.patch('random.randint')
    npmocker = mocker.patch('numpy.random.choice')
    
    camel_list = []
    camel_list.append( crazy_camel(0,5) )
    camel_list.append( crazy_camel(1,5) )
    camel_list.append( crazy_camel(2,9) )
    camel_list.append( crazy_camel(3,9) )
    
    state = race_state(camel_list)
    
    state.pick_crazy_camel()
    
    random.randint.assert_not_called()
    np.random.choice.assert_called_once()
    np.testing.assert_array_equal(npmocker.call_args[0][0],np.array([1,3]))