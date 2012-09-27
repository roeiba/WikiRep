'''
Created on Sep 27, 2012

@author: roeib
'''
import re
class SimpleSplitter(object):
    """ Should be use to split string into list of words
        Currently used regular expression: "[a-z\-']+"
    """    
    def __init__(self):
        self.template =  re.compile ( "[a-z\-']+", re.I )

    def split(self,text):
        """ splits string text int list of words
            @param text: string
            @return: list of words 
        """
        return self.template.findall(text)