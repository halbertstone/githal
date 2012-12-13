'''
Created on Dec 9, 2012

@author: halbertstone
'''
import game.pieces.move as mv
import game.pieces.color as c
import game.pieces.data as d

class Piece(mv.Move):
    '''
    classdocs
    '''
    id=""
    
    location = ""

    inplay = True


    piece_color=('white', 'black')
    
        

    def set_location(self, location):
        self.location=location
    
    def get_location(self):
        return self.location
    
    

    def __init__(self,  game_pieces_data,  game_pieces_color, init_position):
        '''
        Constructor
        '''
        self.set_location(init_position)
        self.piece_color=game_pieces_color
        self.id=game_pieces_data
        
