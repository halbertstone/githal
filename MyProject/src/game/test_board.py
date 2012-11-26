'''
Created on Nov 25, 2012

@author: halbertstone
'''
import unittest
from game import board
import numpy as np

class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def test_black_pieces(self):
        tboard = board.Board()
        print "AssertTrue Black Queen found at 'd8'"
        self.assertTrue("d8" == tboard.black_pieces.get("queen"), "Black queen location NOT d8")

    def test_white_pieces(self):
        ttboard = board.Board()
        print "AssertTrue White Queen found at 'd1'"
        self.assertTrue("d1" == ttboard.white_pieces.get("queen"), "White queen location NOT d1")

    def test_map_position(self):
        tboard = board.Board()
        print "AssertTrue that position 'c4' maps to 24x24_board_domain indices [10,11]"
        mapped = tboard.decode_position("c4")
        self.assertTupleEqual((10, 11), mapped, "Board.decode_position failed got {0}".format(mapped))
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
    