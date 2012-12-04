'''
Created on Nov 25, 2012

@author: halbertstone
'''

class Exceptiton_Code(Exception):
    '''
Usage:
    try:
        raise Exceptiton_Code(1000)
    except Exceptiton_Code as e:
        print "Received error with code:", e.code

    '''
    code='0'

    def __init__(self, code):
        '''
        Constructor
        '''
        self.code = code
        
    def __str__(self):
        msg = "{0}: ".format(self.code)
        if (self.error_messages.has_key(self.code)):
            msg += self.error_messages.get(self.code)
        else:
            msg += self.error_messages.get(100)
        return msg
    
    error_messages = {}
    error_messages[100]="Exception Error Code message NOT found in Exception_Code Class"
    error_messages[1001]="The error code 1001 has occurred"
    error_messages[2001]="Position string Not 2 characters: Chess game locations are Column,Row where columns are a-h and rows are 1-8"
    error_messages[2002]="Board Index; parameter must be list of length 2 representing column in range 8-15 and row in range 8-15"
    error_messages[2003]="Board Index value out of range: column in range 8-15 and row in range 8-15"
