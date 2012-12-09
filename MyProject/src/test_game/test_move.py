'''
Created on Dec 8, 2012

@author: halbertstone
'''
import unittest
import game.pieces.move as mv


class Test(unittest.TestCase):


    def setUp(self):
                
        print " ----- "
        print " -- Test Case: {0}".format(self._testMethodName)
        print " ----- "
        


    def tearDown(self):
        pass


    def test_move_calculate_valid_move_targets(self):
        my_move = mv.Move('f3')
        al=my_move.calculate_valid_move_targets()
        print al
        pass
    def test_move_detrmine_extent_possible(self):
        my_move = mv.Move("e5")
        am=my_move.detrmine_extent_possible('e5')
        print am
        pass
    def test_move_detrmine_kill_occurs(self):
        my_move = mv.Move("b6")
        an=my_move.detrmine_kill_occurs()
        print an
        pass



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_move']
    unittest.main()