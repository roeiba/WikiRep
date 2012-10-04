'''
Created on Oct 4, 2012

@author: inesmeya
'''
import unittest


class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def test_paired_tranformation(self):
        
        # default imput values
 
        compare = lambda EXPECTED, actual: self.assertEqual(EXPECTED, actual)
        def log(_DATA,_data):
            print "Expected:"
            print _DATA
            print 
            print "Actual:"
            print _data
            
        
        init_data = [1,2]
        
        
               
        # create new arrays for DATA:EXCPECTED, data:actual
        DATA = list(init_data)
        data = list(init_data)
        
        # perform paired transformations
        for EXPECTED, method in []:
            
            # conveer:
            data = method(data) 
            
            # perform validation
            compare(EXPECTED,data)
            
            log(DATA,data)
            
            
        
        
        
        
        f =3 
        return f, init_data


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_paired_tranformation']
    unittest.main()