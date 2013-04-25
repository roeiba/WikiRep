#Taken from 
#     http://allmybrain.com/2007/10/19/similarity-of-texts-the-vector-space-model-with-python/

import re
from refs import porter
#from numpy import zeros,dot
#from numpy.linalg import norm

__all__=['compare']

# import real stop words
stop_words = [ 'i', 'in', 'a', 'to', 'the', 'it', 'have', 'haven\'t', 'was', 'but', 'is', 'be', 'from' ]
#stop_words = [w.strip() for w in open('english.stop','r').readlines()]
#print stop_words

class WordsDb(object):
    def __init__(self, concepts, stemmer=None):
        self.concepts = concepts
        stemmer.setdefault(porter.PorterStemmer())
        self.stemmer = stemmer
        self.all_words = {}
        self.words_concepts_table = {}
        self.splitter=re.compile ( "[a-z\-']+", re.I ) 
        
    def _stem(self,word):
        return self.stemmer.stem(word,0,len(word)-1)

    def add_concept(self,concept):
        #TODO check if already exist
        new_id = self.generate_concept_id()
        self.concepts[new_id] = concept
        
    def _text_to_wordlist(self, text):
        return self.splitter.findall(text)
    
    def _add_word(self,word):
        """
        Adds a word the a dictionary for words/count
        first checks for stop words
        the converts word to stemmed version
        """
        word=word.lower() 
        if word not in stop_words:
            steamed_word = self._stem(word) 
            if self.words_concepts_table.has_key(steamed_word):
                raise Exception("Word already exist")
            
            self.words_concepts_table[steamed_word] = self._get_word_concepts_dict(word)
            
    def _get_word_concepts_dict(self, word):
        word_dict = {}
        for concept in self.concepts.values():
            count = concept.get_word_count(word)
            if count:
                word_dict[concept.id] = count
        return word_dict
    
    def update_words_list(self):
        """ Updates the words list by inserting all the words in all concepts to a set """
        self.all_words = set()
        for concept in self.concepts:
            for word in concept.interate_words():
                self.all_words.add(word)
        print "Updated words list..." + self.all_words
        
    def bulid(self):
        """ All articles have been parsed during insertion, so concepts list and all_words are updated -  
            builds the words/concepts table """
        self.update_words_list()
        # build an index of words_arr so that we know the word positions for the vector
        self.word_idx=dict() # word-> ( position, count )
        words_arr= self.all_words.items()
        words_arr.sort()
        
        #print words_arr
        for word in words_arr:
            self._add_word(word)         
        del words_arr
        
        print self.word_idx

class WordData(object):
    def __init__(self,word, index, count):
        self.word = word
        self.index = index
        self.count = count
        
    def __str__(self):
        return "{} => count: {}; index: {}\n".format(self.word, self.count, self.index)
    
    def __repr__(self):
        return self.__str__()
        


