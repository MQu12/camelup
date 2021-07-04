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
        
    def camel_type(self):
        raise NotImplementedError
        
class racing_camel(camel):
    
    def camel_direction(self):
        return 1
    
class crazy_camel(camel):
    
    def camel_direction(self):
        return -1
    