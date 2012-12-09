'''
Created on Dec 5, 2012

@author: halbertstone
'''

class Move(object):
    '''
    Use as an abstract class from which to derive move engine for each piece type
    Or maybe a piece is a move   class piece(Move)
    '''

    def calculate_valid_move_targets(self):
        
        return (''' not implemented yet:
        implement algorithm corresponding with valid move actions for the corresponding piece
        ''')
        
    def detrmine_extent_possible(self, position):    
        '''
        implement algorithm to determine if any game piece blocks/limits extent of move
        '''
        return ('''not implemented yet:    
        List of valid move-to positions; 
        all valid unoccupied positions, up to first occupied position; then
        move extent limited to position adjacent to same color piece position, 
        move extent limited to the opposite color piece position (a kill)''')
    
    def detrmine_kill_occurs(self):    
        '''
        implement algorithm to determine if any game piece is being killed
        IS there an opposite color piece at the selected move target?
        '''
        return ("not implemented yet")
    
    position=''
    
    possibleTargets=[]

    def __init__(self, currentPosition):
        '''
        Constructor
        '''
        self.position=currentPosition
        self.possibleTargets=self.detrmine_extent_possible(self.position)
        