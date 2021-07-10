# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 15:55:25 2021

@author: Dr. P
"""

from camels import racing_camel, crazy_camel
import random

class race_state:

    def __init__(self, camel_list):
        '''
        Intialise the race state

        Parameters
        ----------
        camel_list : list(camel)
            Initial positions of each camel.

        Returns
        -------
        None.

        '''
        
        self.game_end = False
        
        self.track_length = 16
        self.leg_length = 5
        self.max_roll = 3
        self.min_roll = 1
        self.camel_list = camel_list
        
        self.racing_camel_count = self.get_number_of_camel_types(racing_camel)
        self.crazy_camel_count = self.get_number_of_camel_types(crazy_camel)
        
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
        
        crazy_camel_no = -1
        
        crazy_camel_0 = self.camel_list[self.racing_camel_count]
        crazy_camel_1 = self.camel_list[self.racing_camel_count+1]
        
        # check if either crazy camel is carrying any racing camels
        crazy_camel_0_is_carrying = False
        crazy_camel_1_is_carrying = False
        
        for i in range(0,self.racing_camel_count):
            if not crazy_camel_0_is_carrying and crazy_camel_0.position == self.camel_list[i].position:
                if self.camel_list[i].stack_position > crazy_camel_0.stack_position:
                    crazy_camel_0_is_carrying = True
            if not crazy_camel_1_is_carrying and crazy_camel_1.position == self.camel_list[i].position:
                if self.camel_list[i].stack_position > crazy_camel_1.stack_position:
                    crazy_camel_1_is_carrying = True
            if crazy_camel_0_is_carrying and crazy_camel_1_is_carrying:
                break
        
        # if one crazy camel is directly on top of another, move it
        if crazy_camel_0.position == crazy_camel_1.position and abs(crazy_camel_0.stack_position - crazy_camel_1.stack_position) == 1:
            if crazy_camel_0.stack_position > crazy_camel_1.stack_position:
                crazy_camel_no = 0
            else:
                crazy_camel_no = 1
        
        # if only one crazy camel is carrying racing camels, move it
        elif crazy_camel_0_is_carrying != crazy_camel_1_is_carrying:
            if crazy_camel_0_is_carrying:
                crazy_camel_no = 0
            else:
                crazy_camel_no = 1
            
        # otherwise, pick one at random
        else:
            crazy_camel_no = random.randint(0,self.crazy_camel_count-1)
            
        if crazy_camel_no == -1:
            raise ValueError('Crazy camel number should not be -1')
            
        return crazy_camel_no
        
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
    
    def __str__(self):
        
        output = ''
        
        for camel in self.camel_list:
            output += camel.__str__() + '\n'
    
        return output[:-1]
    
    def __repr__(self):
        return str(self)

#TODO merge branches
#TODO add custom marker for plotting
#TODO add running probs for an entire race