# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 15:55:25 2021

@author: Dr. P
"""

from camels import racing_camel, crazy_camel
import random
import constants
import numpy as np

random.seed(constants.RANDOM_SEED)
np.random.seed(constants.RANDOM_SEED)

class race_state:

    def __init__(self, camel_list=None,
                 n_racing_camels=5, n_crazy_camels=2,
                 track_length=16, leg_length=5, min_roll=1, max_roll=3):
        '''
        Intialise the race state

        Parameters
        ----------
        camel_list : list(camel), optional
            Initial positions of each camel.
            If not provided, initial camel positions are randomised.
            The default is None.
        n_racing_camels : int, optional
            Number of racing camels. Only specify if not providig a list of camels.
            The default is 5.
        n_crazy_camels : int, optional
            Number of crazy camels. Only specify if not providig a list of camels.
            The default is 2.
        track_length : int, optional
            Length of race track. The default is 16.
        leg_length : int, optional
            Number of dice rolls/leg. Max value = number of racing camels + 1
            The default is 5.
        min_roll : int, optional
            Min dice roll value. The default is 1.
        max_roll : int, optional
            Max dice roll value. The default is 3.

        Returns
        -------
        None.

        '''
        
        self.game_end = False
        
        self.track_length = track_length
        self.leg_length = leg_length
        self.max_roll = max_roll
        self.min_roll = min_roll
        
        if camel_list:
            self.camel_list = camel_list
            self.racing_camel_count = self.get_number_of_camel_types(racing_camel)
            self.crazy_camel_count = self.get_number_of_camel_types(crazy_camel)
        else:
            self.camel_list = []
            self.racing_camel_count = n_racing_camels
            self.crazy_camel_count = n_crazy_camels
            for i in range(n_racing_camels):
                self.camel_list.append( racing_camel(i,random.randint(min_roll,max_roll)))

            for i in range(n_crazy_camels):
                self.camel_list.append( crazy_camel(i,random.randint(track_length-max_roll,track_length-min_roll)) )
        
        self.leg_num = 0
        self.num_moves = 0

        self.set_stack()
        self.reset_leg()
        
    def reset_leg(self):
        '''
        Reset the leg by marking all camels as unmoved. Should be run after each leg is complete.

        Returns
        -------
        None.

        '''
        
        self.camels_to_move = [i for i in range(self.racing_camel_count)]
        self.camels_to_move.append('crazy')
        self.leg_num += 1

    def set_stack(self):
        '''
        Set the stack positions of each camel. Should be run on any new camel list.
    
        Returns
        -------
        None.
    
        '''
        
        positions = []
        
        for i in range(len(self.camel_list)):
            
            camels_on_tile = positions.count(self.camel_list[i].position)
            self.camel_list[i].stack_position = camels_on_tile
            positions.append(self.camel_list[i].position)
    
    def get_number_of_camel_types(self,camel_type):
        '''
        Count the amount of a type of camel
    
        Parameters
        ----------
        camel_type : class
            Type of camel to count
    
        Returns
        -------
        count : int
            Number of type of camel
    
        '''
        
        count = 0
        
        for camel in self.camel_list:
            if type(camel) == camel_type:
                count += 1
                
        return count
    
    def move_camel_to(self,camel_no,final_pos):
        '''
        Move camel id in race to a particular location.
        Takes into account camel positions in stack.
        Camels above target are carried and the substack is put on top of a
        stack at the destination.
        race_state is updated to reflect the change.
    
        Parameters
        ----------
        camel_no : int
            Camel id.
        final_pos : int
            Target square.
    
        Returns
        -------
        None
    
        '''
    
        target_camel_stack_pos = self.camel_list[camel_no].stack_position
        init_camel_pos = self.camel_list[camel_no].position
        
        camels_to_move = []
        camels_at_destination = 0
        
        for i,camel in enumerate(self.camel_list):
            
            if camel.position == init_camel_pos and camel.stack_position >= target_camel_stack_pos:
                camels_to_move.append(i)
                
            if camel.position == final_pos:
                camels_at_destination += 1
                
        for camel_id in camels_to_move:
            self.camel_list[camel_id].position = final_pos
            self.camel_list[camel_id].stack_position += (camels_at_destination - target_camel_stack_pos)
        
        if final_pos >= self.track_length:
            self.game_end = True
    
        self.num_moves += 1
    
    def pick_crazy_camel(self):
        '''
        Pick a crazy camel to move based on game rules.
        1. If a crazy camel is directly atop another, move it
        2. If only one crazy camel is carrying racing camels, move it
        3. Otherwise, pick one at random
    
        Returns
        -------
        crazy_camel_no : int
            ID of the crazy camel to move.
    
        '''
        
        crazy_camel_list = [camel for camel in self.camel_list[self.racing_camel_count:]]
        
        # check if either crazy camel is carrying any racing camels
        crazy_camels_carrying = np.zeros(len(crazy_camel_list), dtype=bool)
        
        for i in range(0,self.racing_camel_count):
            #camels not in a stack cannpt be being carried
            if self.camel_list[i].stack_position == 0:
                continue
            for j, crazy_camel_j in enumerate(crazy_camel_list):
                if crazy_camels_carrying[j]:
                    continue
                if crazy_camel_j.position == self.camel_list[i].position and crazy_camel_j.stack_position + 1 == self.camel_list[i].stack_position:
                    crazy_camels_carrying[j] = True
        
        #if only one is carrying, return it
        if crazy_camels_carrying.sum() == 1:
            return np.where(crazy_camels_carrying==True)[0][0]
        
        #if others exist, pick one at random
        elif crazy_camels_carrying.sum() > 1:
            return np.random.choice(
                np.where(crazy_camels_carrying==True)[0]
                )
        
        # determine which (if any) crazy camels are directly on top of another
        crazy_id_carried_by_crazy = []
        for crazy1 in crazy_camel_list:
            for crazy2 in crazy_camel_list:
                if crazy1.position == crazy2.position and crazy1.stack_position == crazy2.stack_position + 1:
                    crazy_id_carried_by_crazy.append(crazy1.id)
        
        # if only one crazy camel sits directly atop another, return it
        if len(crazy_id_carried_by_crazy) == 1:
            return crazy_id_carried_by_crazy[0]
        # if more than once, pick one at random
        elif len(crazy_id_carried_by_crazy) > 1:
           return np.random.choice(crazy_id_carried_by_crazy)
       
        # otherwise, pick one at random
        return random.randint(0,self.crazy_camel_count-1)
        
    def get_leader(self):
        '''
        Get the racing camel at the front.
        If there is a stack leading, the camel at the top of the stack is returned.
    
        Returns
        -------
        leading_camel_id : int
            ID of the leading camel.
    
        '''
        
        largest_forward = 0
        largest_upward = 0
        leading_camel_id = 0
        
        for camel in self.camel_list:
            if type(camel) == crazy_camel:
                continue
            if camel.position > largest_forward or camel.position == largest_forward and camel.stack_position > largest_upward:
                largest_forward = camel.position
                largest_upward = camel.stack_position
                leading_camel_id = camel.id
            else:
                continue
            
        return leading_camel_id
    
    def get_last_place(self):
        '''
        Get the racing camel in last place.
        If a stack is furthest back, the camel at the bottom is chosen.

        Returns
        -------
        trailing_camel_id : int
            ID of the trailing camel.

        '''
        
        furthest_back = 1e10
        trailing_camel_id = 0
        
        for camel in self.camel_list:
            if type(camel) == crazy_camel:
                continue
            if camel.position < furthest_back and camel.stack_position == 0:
                furthest_back = camel.position
                trailing_camel_id = camel.id
            else:
                continue
            
        return trailing_camel_id
    
    def __str__(self):
        
        output = f'State after {self.num_moves} moves\nLeg {self.leg_num}'
        
        for camel in self.camel_list:
            output += ('\n'+camel.__str__())
    
        return output
    
    def __repr__(self):
        return str(self)