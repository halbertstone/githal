'''
Created on Nov 17, 2012

@author: halbertstone
'''

import exceptions_util.exception_code as ec
import numpy.core as npcore


class Board(object):
    '''
    classdocs
    
    board is a 24 x 24 matrix where the 
    central 8 x 8 is the traditional playing area.
    The central area is referenced by Column (a, b, c, d, e, f, g, h)
    and Row (1 2 3 4 5 6 7 8) during game play so these need to be
    mapped onto the 24x24 matrix 'board_domain'. see Board.decode_position
    
    000000000000000000000000
    000000000000000000000000
    000000000000000000000000
    000000000000000000000000
    000000000000000000000000
    000000000000000000000000
    000000000000000000000000
    000000000000000000000000
 8  000000001111111100000000
 7  000000001111111100000000
 6  000000001111111100000000
 5  000000001111111100000000    
 4  000000001111111100000000
 3  000000001111111100000000
 2  000000001111111100000000
 1  000000001111111100000000
    000000000000000000000000
    000000000000000000000000
    000000000000000000000000
    000000000000000000000000
    000000000000000000000000
    000000000000000000000000
    000000000000000000000000
    000000000000000000000000
            abcdefgh                

    '''
    #create an oversized array with the 8x8 board in the center
    board=npcore.zeros((24,24))
    
    board[8:16,8:16]=1
    
    black_pieces={}
    white_pieces={}
    
    
    position_dict={}
    inverse_dict=dict([(v,k) for (k,v) in position_dict.items()])
    
    #I'm going to create a lookup table (python dictionary) so that input moves like 'b1'
    #correspond to the correct indices int the array e.g position_dict['b1'] will return (8,9)
    columns=['a','b','c','d','e','f','g','h']
    column_index=npcore.arange(8,16)
    column_map={}
    column_map.update(zip(columns,column_index))
    
    rows=['1','2','3','4','5','6','7','8']
    row_index=npcore.arange(8,16)
    row_map={}
    row_map.update(zip(rows,row_index))
    '''
    #   Board_domain is 24x24 to provide a buffer region
    #   notation to set the value of matrix positions columns 8 thru 15 by rows 8 thru 15 to one
    '''
    board=npcore.zeros((24,24)) 
   # board[8:16,8:16]=1     
    
    def decode_position(self,position):
      
        '''
        Maps the human position string to the internal game matrix
        Chess board of 8x8 notes positions as Column,Row where column is a,b,c,d,e,f,g,h and row is 1,2,3,4,5,6,7,8
        Given a piece position "c4" decode this to board matrix indices
        such that it is located on the 8x8 center matrix within the 24x24 board_domain 
        where column is in 0-23, and row is in 0-23
        Example "c4" of the 8x8 game-board maps to board_domain[10,11]
        
        Exception Raised:  exceptions_util.exception_code.Exception_Code(2001)
        '''
        p=position.strip()
        if(len(p)!=2):
            raise ec.Exceptiton_Code(2001)
        
        c=p[0]
        board_column=self.column_map.get(c)

        r=p[1]
        board_row=self.row_map.get(r)

        return (board_column,board_row)
    
    def index_to_board_position(self,colrow):
        '''
        converts 2Dim index [col,row] to chess board position using columns a-h and rows 1-8
        '''
        if(len(colrow)!=2):
            raise ec.Exceptiton_Code(2002)
        for x in colrow:
            if ((x < 8 ) or (x > 15)):
                raise ec.Exceptiton_Code(2003)
        col = self.columns[colrow[0]-len(self.columns)]
        row = self.rows[colrow[1]-len(self.rows)]
        pos = "{0}{1}".format(col,row)
        return pos
        
                
            
        
    
    def __init__(self):
        '''
        Constructor
        '''
        self.white_pieces= dict(castleWQ='a1'  ,w_a="a2"
                                ,knightWQ='b1', w_b="b2"
                                ,bishopWQ='c1', w_c="c2"
                                ,queenW='d1', w_d="d2"
                                ,kingW='e1', w_e="e2"
                                ,bishopWK='f1', w_f="f2"
                                ,knightWK='g1', w_g="g2"
                                ,castleWK='h1', w_h="h2"
                                )
        
        self.black_pieces= dict(castleBQ='a8' , b_a="a7"
                                ,knightBQ='b8', b_b="b7"
                                ,bishopBQ='c8', b_c="c7"
                                ,queenB='d8'   , b_d="d7"
                                ,kingB='e8'  , b_e="e7"
                                ,bishopBK='f8', b_f="f7"
                                ,knightBK='g8', b_g="g7"
                                ,castleBK='h8', b_h="h7"
                                )
        dead_black={}
        dead_white={}
  



        


