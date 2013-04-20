#Taken from 
#     http://allmybrain.com/2007/10/19/similarity-of-texts-the-vector-space-model-with-python/


import re
import porter
from numpy import zeros,dot
from numpy.linalg import norm

__all__=['compare']

# import real stop words
stop_words = [ 'i', 'in', 'a', 'to', 'the', 'it', 'have', 'haven\'t', 'was', 'but', 'is', 'be', 'from' ]
#stop_words = [w.strip() for w in open('english.stop','r').readlines()]
#print stop_words

splitter=re.compile ( "[a-z\-']+", re.I )


def _text_to_wordlist(text):
    return splitter.findall(text)


class WordsDb(object):
    def __init__(self, stemmer):
        self.stemmer = stemmer
        self.all_words = {}
        
    def _stem(self,word):
        return self.stemmer.stem(word,0,len(word)-1)

    def add_article(self,text):
        for word in _text_to_wordlist(text):
            self._add_word(word)
    
    def _add_word(self,word):
        """
        Adds a word the a dictionary for words/count
        first checks for stop words
    	the converts word to stemmed version
        """
        word=word.lower() 
        if word not in stop_words:
            steamed_word = self._stem(word) 
            self.all_words.setdefault(steamed_word,0)
            self.all_words[steamed_word] += 1

    def bulid(self):
        
        print self.all_words
        
        # build an index of words_arr so that we know the word positions for the vector
        self.word_idx=dict() # word-> ( position, count )
        words_arr= self.all_words.keys()
        words_arr.sort()
        
        #print words_arr
        for i in range(len(words_arr)):
            worddata = WordData( word=words_arr[i], index=i, count=self.all_words[words_arr[i]])
            self.word_idx[words_arr[i]] = worddata
        
        del words_arr
        
        print self.word_idx

    def classify(self,text):
        v=zeros(len(self.word_idx) )
        for word in _text_to_wordlist(text):
            keydata=self.word_idx.get(self._stem(word).lower(), None)
            if keydata: v[keydata.index] = 1
        return v



class WordData(object):
    def __init__(self,word, index, count):
        self.word = word
        self.index = index
        self.count = count
        
    def __str__(self):
        return "{} => count: {}; index: {}\n".format(self.word, self.count, self.index)
    
    def __repr__(self):
        return self.__str__()
        


def compare(doc1,doc2):
    """ strip all punctuation but - and '
        convert to lower case
        store word/occurance in dict
    """
    
    words_db = WordsDb(stemmer=porter.PorterStemmer())

    for text in [doc1,doc2]:
        words_db.add_article(text) 
        
    words_db.bulid()
 
    v1 = words_db.classify(doc1)
    v2 = words_db.classify(doc2)

    print v1
    print v2
    
    return float(dot(v1,v2) / (norm(v1) * norm(v2)))
 
 
if __name__ == '__main__':
    print "Running Test..." 
    doc1="I like to eat chicken\nnoodle soup."
    doc2="I have read the book \"Chicken noodle soup for the soul\"."
    print "Using Doc1: %s\n\nUsing Doc2: %s\n" % ( doc1, doc2 )
    print "Similarity %s" % compare(doc1,doc2)


