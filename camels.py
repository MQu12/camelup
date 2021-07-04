# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 16:19:19 2021

@author: Dr. P
"""

class camel:
    
    def __init__(self,id,position):
        self.id = id
        self.position = position
        
    def camel_type(self):
        raise NotImplementedError
        
class racing_camel(camel):
    
    def camel_direction(self):
        return 1
    
class crazy_camel(camel):
    
    def camel_direction(self):
        return -1
    