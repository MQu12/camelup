# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 22:11:28 2021

@author: Dr. P
"""

from camelup import pick_crazy_camel
from camels import racing_camel, crazy_camel
import random

def test_random_camel_is_picked_when_crazy_camels_are_apart(mocker):
    
    mocker.patch('random.randint')
    
    camel_list = []
    camel_list.append( crazy_camel(0,5) )
    camel_list.append( crazy_camel(1,6) )

    pick_crazy_camel(camel_list,racing_camel_count=0)
    
    random.randint.assert_called_once()

def test_top_camel_is_picked_when_crazy_camels_are_stacked(mocker):
    
    mocker.patch('random.randint')
    
    camel_list = []
    camel_list.append( crazy_camel(0,5) )
    camel_list.append( crazy_camel(1,5) )
    
    camel_list[1].stack_position = 1

    crazy_camel_no = pick_crazy_camel(camel_list,racing_camel_count=0)
    
    random.randint.assert_not_called()
    
    assert crazy_camel_no == 1
    
def test_camel_carrying_racing_camels_is_picked(mocker):
    
    mocker.patch('random.randint')
    
    camel_list = []
    camel_list.append( racing_camel(0,5) )
    camel_list.append( crazy_camel(0,9) )
    camel_list.append( crazy_camel(1,5) )
    
    
    camel_list[0].stack_position = 1

    crazy_camel_no = pick_crazy_camel(camel_list,racing_camel_count=1)
    
    random.randint.assert_not_called()
    
    assert crazy_camel_no == 1
    
def test_camel_picked_at_random_when_both_are_carrying_crazy_camels(mocker):
    
    mocker.patch('random.randint')
    
    camel_list = []
    camel_list.append( racing_camel(0,5) )
    camel_list.append( racing_camel(1,9) )
    camel_list.append( crazy_camel(0,9) )
    camel_list.append( crazy_camel(1,5) )
    
    
    camel_list[0].stack_position = 1
    camel_list[1].stack_position = 1

    pick_crazy_camel(camel_list,racing_camel_count=2)
    
    random.randint.assert_called_once()
    
def test_camel_at_bottom_of_stack_is_picked_when_there_is_a_racing_camel_between_two_crazy_camels(mocker):
    
    mocker.patch('random.randint')
    
    camel_list = []
    camel_list.append( racing_camel(0,5) )
    camel_list.append( crazy_camel(0,5) )
    camel_list.append( crazy_camel(1,5) )
    
    
    camel_list[0].stack_position = 1
    camel_list[2].stack_position = 2

    crazy_camel_no = pick_crazy_camel(camel_list,racing_camel_count=1)
    
    random.randint.assert_not_called()
    
    assert crazy_camel_no == 0