'''
Created on Oct 24, 2012

@author: roeib
'''
import unittest
from test import test_utils 
from model import build_utils
import os
import timeit
from functools import partial

dump_file = os.path.join( os.path.dirname(__file__), "data_sets", "wiki_knowledge_output.xml") 
concepts_list = test_utils.get_concepts_list(dump_file)

class TestBuildWordIndexPerformances(test_utils.TestBase):
    """ Compares the performances of build_word_index vs build_word_index_back
        In order to achieve concepts list, we use db_builder 
    """ 
    def _method_tester(self, func):
        func_with_params = partial(func, concepts_list)
        timer = timeit.Timer(func_with_params)
        run_time = timer.timeit(10)
        print "Run time for {} is {}".format(func, run_time)
        
    def test__build_word_index(self):
        self._method_tester(build_utils.build_word_index)
    
    def test__build_word_index_back(self):
        self._method_tester(build_utils.build_word_index_back)

if __name__ == "__main__":
    unittest.main()
