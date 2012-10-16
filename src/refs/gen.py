'''
Created on Oct 9, 2012

@author: inesmeya
'''
import unittest


class Test(unittest.TestCase):


    def testName(self):
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
    
    
articles = 'River', 'busyness'
db_path  = 'db_123.xml'

builder = 0

for article in articles:
    builder.add(article)



# articles => db_set


class ConceptSuit(object):
    name = None
    id = None
    concepts = None
    
    
    def save_to_xml(self):
        pass
    
    def save_to_db(self,connection):
        pass
    
    