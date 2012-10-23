'''
Created on Oct 15, 2012

@author: inesmeya
'''
import unittest
#import parsers.parse_tools as pt
import parsers.parse_tools as pt
from os.path import dirname, join 


class Test(unittest.TestCase):

    def test_extract_pages(self):
        '''regression check that extract_pages works well'''
        # template.format('id', ' title', 'length'); template = "{:<12}{:<30}{:>12}"
        expected =[
            (243478,      'Ross Ice Shelf',                       13734),
            (18798090,    'Southern Cross Expedition',            39110),
            (343246,      'Ice shelf',                             8262)
        ]
        test__parse_tools_xml =  join(dirname(__file__),'test__parse_tools.xml')
        
        actual = [(int(tid), title, len(text)) 
                  for tid, title, text, _ 
                  in pt.extract_pages(test__parse_tools_xml)]        

        self.assertSequenceEqual(actual, expected, "Assertion failure: \nActual={}\nExpected={}".format(actual, expected))

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()