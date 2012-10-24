'''
Created on Sep 28, 2012

@author: inesmeya
'''

from concept import Concept 
from model.database_wrapper import DatabaseWrapper
from model.build_utils import build_word_index, build_index_by_words, build_df, build_wieght_table
from model.logger import *

class DbBuilder(object):
    '''
        Not allowing duplications of IDs
        For testability - if the id is None, it will be auto generated.
    '''

    def __init__(self,stemmer):
        '''
        Constructor
        '''
        self._last_generated_id = 1
        self.stemmer = stemmer
        self.concepts_list = []
        self.ids = set()

    def _generate_concept_id(self, doc):
        ''' 
        @return: sequential id's for concepts 
        '''
        #for testability purposes
        if doc.id is None:
            while (self._last_generated_id in self.ids):
                self._last_generated_id += 1
            doc.id = self._last_generated_id
        
        if doc.id in self.ids:
            ERROR("id duplication:\n{}".format(doc))
            raise Exception("Document id already exist!")
        
        return doc.id
        
    def add_document(self,doc):
        """ Converts document to concept 
            @param doc: should have doc_id, rev_id, title and raw_text
        """
        cid = self._generate_concept_id(doc)
        word_list = self.stemmer.process_text(doc.raw_text)
        new_concept = Concept(cid, doc.title, word_list, doc.rev_id)
        self.concepts_list.append(new_concept)
        self.ids.add(doc.id)
         
    def build(self,wf=None):
        #unique enumeration of words
        word_index = build_word_index(self.concepts_list)
        
        #word => index in word_index
        index_by_word = build_index_by_words(word_index)
        
        # docs per word
        df_vec = build_df(index_by_word, self.concepts_list)
        
        # weight table not normalized
        T = build_wieght_table(df_vec, index_by_word, self.concepts_list)
        
        #DEBUG: if wf: wf.tf_mat = _build_wieght_table_tfi_only(df_vec, index_by_word, self.concepts_list)
        
        #TODO: add normalization
        db = DatabaseWrapper(T, self.concepts_list, word_index)
        
        if wf: 
            wf.word_index = word_index
            wf.df_vec = df_vec
            wf.wieghts_mat = T
        return db 

        
    def get_concepts_list(self):
        return self.concepts_list
        
                