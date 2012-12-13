'''
Created on Dec 12, 2012

@author: halbertstone
'''

class Color(object):
    '''
    classdocs
    '''

    color = {"white":"White","black":"Black"}

    def __getitem__(self,key):
        return self.color[key]
        