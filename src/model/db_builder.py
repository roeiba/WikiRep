'''
Created on Sep 28, 2012

@author: inesmeya
'''

from concept import Concept 
from model.database_wrapper import DatabaseWrapper
from model.build_utils import bulid_word_index, build_index_by_words, build_df, build_wieght_table

class DbBuilder(object):
    '''
    Current implementation doesn't check for concept duplications
    '''

    def __init__(self,stemmer):
        '''
        Constructor
        '''
        self._last_id = -1
        self.stemmer = stemmer
        self.concepts_list = []

    def _generate_concept_id(self):
        ''' @return: sequential id's for concepts '''
        self._last_id+=1
        return self._last_id
        
    def add_document(self,doc):
        """ Converts document to concept 
            @param doc: sould have title and raw_text
        """
        cid = self._generate_concept_id()
        word_list = self.stemmer.process_text(doc.raw_text)
        new_concept = Concept(cid, doc.title, word_list, doc.rev_id)
        self.concepts_list.append(new_concept)
         
    def build(self,wf=None):
        #unique enumeration of words
        word_index = bulid_word_index(self.concepts_list)
        
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

        
        
        
                