'''
Created on Oct 4, 2012

@author: inesmeya
'''
import unittest
from numpy import array
from numpy import vectorize
from numpy import log
from numpy.testing import assert_allclose
import inspect
from model.db_builder import DbBuilder
from model.stop_words_stemmer import StopWordsStemmer
import model.math_utils as math_utils

class WorkFlow(object):
    docs = None
    
    title_index = None
    word_index  = None
    
    count_mat = None
    tf_mat = None
    
    n_docs = None
    df_vec = None
    idf_vec = None
    log_idf = None
    
    wieghts_mat = None
    #fill_order = None
    
    def __init__(self):
        self.fill_order =[]

    def __setattr__(self, name, value):
        if name != 'fill_order':
            self.fill_order.append(name)                   
        object.__setattr__(self, name, value)
        
    def __repr__(self):
        l = ["{}:\n{}\n".format(name, getattr(self, name)) for name in self.fill_order]
        r = '\n'.join(l)
        return r
    
    def __str__(self):
        return self.__repr__()
        
class DocumentStub(object):
    raw_text = None 
    title = None
    
    def __init__(self, title, raw_text):
        self.title = title
        self.raw_text = raw_text
        
Doc = DocumentStub          


     
def simple_wf():
    wf = WorkFlow()

    
    # declare docs:
    wf.docs = [
        Doc("Testing advanced 1",  "a b c c c d d d d e"),
        Doc("Testing advanced 2", "a a a a a b c c c d d d e e"),
        Doc("Testing advanced 3", "b b b b f f f f"),
    ]
    
    # declare preprocessing
    wf.title_index = [ doc.title for doc in wf.docs] 
    wf.word_index =  ['a', 'b', 'c', 'd', 'e', 'f']
    
    # prepare tf matrix     
    wf.count_matrix = array([ 
        [1, 5, 0], #a 
        [1, 1, 4], #b 
        [3, 3, 0], #c 
        [4, 3, 0], #d 
        [1, 2, 0], #e 
        [0, 0, 4], #f 
    ])      
    count_to_tf = vectorize(math_utils.count_to_tf)
    wf.tf_mat = count_to_tf(wf.count_matrix)

    # prepare lidf vector: log of inverted df
    wf.n_docs       = float(len(wf.docs))                
    wf.df_vec       = array([2.0, 3.0, 2.0, 2.0, 2.0, 1.0])
    wf.idf_vec      = wf.n_docs / wf.df_vec
    wf.log_idf_vec  = log(wf.idf_vec)
    wf.wieghts_mat  = wf.tf_mat * wf.log_idf_vec[:,None]
    
    return wf


class Test(unittest.TestCase):
    def test_migration(self):
        """tests that new form of test equals to old one  from test__advanced_doc"""

        expected = array([
        [ 0.40546511,  1.05803603,  0.        ],
        [ 0.        ,  0.        ,  0.        ],
        [ 0.85091406,  0.85091406,  0.        ],
        [ 0.9675591 ,  0.85091406,  0.        ],
        [ 0.40546511,  0.6865121 ,  0.        ],
        [ 0.        ,  0.        ,  2.62161231]])  
        
        wf = simple_wf()
        actual = wf.wieghts_mat
        
        assert_allclose(actual, expected)
        #print wf
        
    def test__advanced_doc(self):
        """tests that new form of test equals to old one  from test__advanced_doc"""

        expected_wf = simple_wf()
        
        builder = DbBuilder(StopWordsStemmer())
        for doc in expected_wf.docs:
            builder.add_document(doc)
        
        actual_wf = WorkFlow()
        
        builder.build(actual_wf) 
        
        assert_allclose(actual_wf.df_vec,expected_wf.df_vec)    
        assert_allclose(actual_wf.wieghts_mat, expected_wf.wieghts_mat)

    

if __name__ == "__main__":
    unittest.main()











#for colname,col in Listing.columns:
#    print colname,'=>',col.creation_order

class Result(object):
    creation_counter = 0
    def __init__(self):
        self.creation_order = Result.creation_counter
        Result.creation_counter+=1

class ListingMeta(type):
    def __new__(cls, classname, bases, classDict):
        cls = type.__new__(cls, classname, bases, classDict)
        cls.columns = sorted(inspect.getmembers(cls,lambda o:isinstance(o,Result)),key=lambda i:i[1].creation_order) 
        cls.nb_columns = len(cls.columns)
        return cls

class Listing(object):
    __metaclass__ = ListingMeta
    mycol2 = Result()
    mycol3 = Result()
    zut = Result()
    cool = Result()
    menfin = Result()
    a = Result()


