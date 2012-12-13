'''
Created on Dec 8, 2012

@author: halbertstone
'''
import unittest
import game.pieces.piece as p
import game.pieces.color as color
import game.pieces.data as data




class Test(unittest.TestCase):


    def setUp(self):
                
        print " ----- "
        print " -- Test Case: {0}".format(self._testMethodName)
        print " ----- "
        


    def tearDown(self):
        pass

    def test_piece_constructor(self):
        my_piece = p.Piece("cQ","white","a1")
        print my_piece.get_location()
        

    def test_move_calculate_valid_move_targets(self):
        my_move = p.Piece(data.Data.K,"black","a5")
        al=my_move.calculate_valid_move_targets()
        print al,my_move.get_location(),my_move.piece_color
#        
#
    def test_move_detrmine_extent_possible(self):
        my_move = p.Piece(data.Data.Q,color.Color()["black"],"a4")
        am=my_move.detrmine_extent_possible('e5')
        print my_move.piece_color
        print am
        

    def test_move_detrmine_kill_occurs(self):
        my_move = p.Piece(data.Data.pc,color.Color()["white"], "b4")
        an=my_move.detrmine_kill_occurs()
        print an
        print my_move.id
        print my_move.get_location()
        print my_move.inplay
        print my_move.piece_color
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_move']
    unittest.main()