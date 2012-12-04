'''
Created on Nov 25, 2012

@author: halbertstone
'''
import unittest
from game import board


class Test(unittest.TestCase):

    

    def setUp(self):
        
        print " ----- "
        print " -- Test Case: {0}".format(self._testMethodName)
        print " ----- "
        
        pass


    def tearDown(self):
        pass


    def test_black_pieces(self):
        tboard = board.Board()
        print "AssertTrue Black castleBQ found at 'a8'"
        self.assertTrue("a8" == tboard.black_pieces.get("castleBQ"), "Black castleBQ location NOT a8")
        print "AssertTrue Black knightBQ found at 'b8'"
        self.assertTrue("b8" == tboard.black_pieces.get("knightBQ"), "Black knightBQ location NOT b8")
        print "AssertTrue Black bishopBQ found at 'c8'"
        self.assertTrue("c8" == tboard.black_pieces.get("bishopBQ"), "Black bishopBQ location NOT c8")
        print "AssertTrue Black Queen found at 'd8'"
        self.assertTrue("d8" == tboard.black_pieces.get("queenB"), "Black queen location NOT d8")
        print "AssertTrue Black King found at 'e8'"
        self.assertTrue("e8" == tboard.black_pieces.get("kingB"), "Black king location NOT d8")
        print "AssertTrue Black bishopBK found at 'f8'"
        self.assertTrue("f8" == tboard.black_pieces.get("bishopBK"), "Black bishopBK location NOT f8")
        print "AssertTrue Black knightBK found at 'g8'"
        self.assertTrue("g8" == tboard.black_pieces.get("knightBK"), "Black knightBK location NOT g8")
        print "AssertTrue Black castleBK found at 'h8'"
        self.assertTrue("h8" == tboard.black_pieces.get("castleBK"), "Black castleBK location NOT h8")
 

    def test_white_pieces(self):
        ttboard = board.Board()
        print "AssertTrue White castleWQ found at 'a1'"
        self.assertTrue("a1" == ttboard.white_pieces.get("castleWQ"), "White castleWQ location NOT a1")
        print "AssertTrue White knightWQ found at 'b1'"
        self.assertTrue("b1" == ttboard.white_pieces.get("knightWQ"), "White knightWQ location NOT b1")     
        print "AssertTrue White bishopWQ found at 'c1'"
        self.assertTrue("c1" == ttboard.white_pieces.get("bishopWQ"), "White bishopWQ location NOT c1")       
        print "AssertTrue White Queen found at 'd1'"
        self.assertTrue("d1" == ttboard.white_pieces.get("queenW"), "White queen location NOT d1")        
        print "AssertTrue White King found at 'e1'"
        self.assertTrue("e1" == ttboard.white_pieces.get("kingW"), "White king location NOT e1")       
        print "AssertTrue White bishopWK found at 'f1'"
        self.assertTrue("f1" == ttboard.white_pieces.get("bishopWK"), "White bishopWK location NOT f1")
        print "AssertTrue White knightWK found at 'g1'"
        self.assertTrue("g1" == ttboard.white_pieces.get("knightWK"), "White kightWK location NOT g1")        
        print "AssertTrue White King found at 'h1'"
        self.assertTrue("h1" == ttboard.white_pieces.get("castleWK"), "White castleWK location NOT h1")


    def test_map_position(self):
        tboard = board.Board()
        print "AssertTrue that position 'c4' maps to 24x24_board_domain indices [10,11]"
        mapped = tboard.decode_position("c4")
        self.assertTupleEqual((10, 11), mapped, "Board.decode_position failed got {0}".format(mapped))

        print "AssertTrue that position 'a1' maps to 24x24_board_domain indices [8,8]"
        mapped = tboard.decode_position("a1")
        self.assertTupleEqual((8, 8), mapped, "Board.decode_position failed got {0}".format(mapped))

        print "AssertTrue that position 'h8' maps to 24x24_board_domain indices [15,15]"
        mapped = tboard.decode_position("h8")
        self.assertTupleEqual((15, 15), mapped, "Board.decode_position failed got {0}".format(mapped))

    def test_index_to_position(self):
        tboard = board.Board()
        boardPosition = tboard.index_to_board_position([8,8])
        print("AssertTrue that board index [8,8] is game position 'a1'")
        self.assertTrue('a1'== boardPosition,"Expected [8,8] to be position 'a1' got {0}".format(boardPosition))
        
        boardPosition = tboard.index_to_board_position([15,15])
        print("AssertTrue that board index [15,15] is game position 'h8'")
        self.assertTrue('h8'== boardPosition,"Expected [15,15] to be position 'h8' got {0}".format(boardPosition))
        
        boardPosition = tboard.index_to_board_position([14,14])
        print("AssertTrue that board index [14,14] is game position 'g7'")
        self.assertTrue('g7'== boardPosition,"Expected [14,14] to be position 'g7' got {0}".format(boardPosition))

        boardPosition = tboard.index_to_board_position([9,9])
        print("AssertTrue that board index [9,9] is game position 'b2'")
        self.assertTrue('b2'== boardPosition,"Expected [9,9] to be position 'b2' got {0}".format(boardPosition))
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
    