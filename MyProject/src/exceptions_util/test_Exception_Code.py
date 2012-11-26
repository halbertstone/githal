'''
Created on Nov 25, 2012

@author: halbertstone
'''
import unittest
import exceptions_util.exception_code as ec


class Test(unittest.TestCase):


    def test_found_code_message(self):
        try:
            raise ec.Exceptiton_Code(1001)
        except ec.Exceptiton_Code as e:
            print e

    def test_not_found_code_message(self):
        try:
            raise ec.Exceptiton_Code(13)
        except ec.Exceptiton_Code as e:
            print e


    def test_2001_message(self):
        try:
            raise ec.Exceptiton_Code(2001)
        except ec.Exceptiton_Code as e:
            print e

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()