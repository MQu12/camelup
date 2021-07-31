# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 16:19:19 2021

@author: Dr. P
"""

class camel:
    
    def __init__(self,id,position=0,stack_position=0):
        self.id = id
        self.position = position
        self.stack_position = stack_position
        self.total_movement = 0
        
    def camel_direction(self):
        raise NotImplementedError
        
    def __str__(self):
        return f'{self.__class__.__name__} no {self.id} at {self.position}, y = {self.stack_position}'
    
    def __repr__(self):
        return str(self)

    def __eq__(self,other):
        if self.id == other.id and self.position == other.position and self.stack_position == other.stack_position and self.total_movement == other.total_movement:
            return True
        else:
            return False

    def deepcopy(self):
        raise NotImplementedError
        
class racing_camel(camel):
    
    def deepcopy(self):
        c = racing_camel(self.id,self.position,self.stack_position)
        c.total_movement = self.total_movement
        return c

    def camel_direction(self):
        return 1
    
class crazy_camel(camel):

    def deepcopy(self):
        c = crazy_camel(self.id,self.position,self.stack_position)
        c.total_movement = self.total_movement
        return c

    def camel_direction(self):
        return -1
    