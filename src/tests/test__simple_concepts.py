# -*- coding: utf-8 -*-

from model.concept import Concept
import unittest
from tests import test_utils
from model import db_builder
from model.stop_words_stemmer import StopWordsStemmer
from model.semantic_interpreter import SemanticInterpreter


#those concepts have distinct set of words
distinct_concepts = [
      
    Concept(1, "Technology", 
    [
         'computer', 'technology', 'system',
         'service',  'site',       'phone', 
         'internet', 'machine' 
    ]),
           
    Concept(2, "Business",
    [
        'store', 'product', 'sales', 'sell',
        'business', 'advertising','market', 
        'consumer'
    ]),
    
    Concept(3, "Entertainment",
    [            
        'play', 'film', 'production', 
        'movie', 'theater', 'stage'
        'star', 'director', 
    ])
        
] # end of distinct_concepts
        

technology_text = """
App.net just announced some price changes to its Twitter-like service focused on unlimited API usage. The major change is a much needed 40 percent price drop for its yearly subscription. It now costs $36 per year. In addition to adjusting existing plans, the company is announcing another plan to try out the service. You can subscribe for $5 a month while you are uncertain about using the service or not.

The blog post introducing the change emphasizes the momentum as the main reason for those changes. User adoption is a critical part of any social network. $50 per year was certainly too pricey for many Twitter users. Existing users will get a time extension on their subscriptions.

Developers still have to spend $100 per year to use the API. But App.net recently announced an incentive for developers. Beginning October 1, App.net will give $20,000 per month to developers for the most successful third-party apps or services. The incentive program is reminiscent of RIM’s investment to foster app development.

According to Dalton Caldwell, the service just crossed the 20,000 user mark. The original pricing was designed for 10,000 users. The service now costs less per user due to economies of scale. As always for a young startups, salaries are the main concern. If Caldwell thinks that it can keep a strong team working on the service with that new pricing scheme, then it makes sense.

The service could go even further and bet on a huge increase of signups. It doesn’t seem that it has reached its tipping point yet because only around 8,000 users have signed up since the end of the fundraising period.
"""


class TestSimpleConcepts(test_utils.TestBase):
    
    def test_print(self):
        stemmer = StopWordsStemmer()
        builder = db_builder.DbBuilder(stemmer)
        
        #HACK:
        for c in distinct_concepts:
            builder.concepts_list.append(c)
            
        db = builder.build()
        
        #print db.words_index
        #print db.get_titles_index()
        #print db.wieght_matrix
        
        si = SemanticInterpreter(db, stemmer)
        
        v = si.build_weighted_vector(technology_text)
        #print v
        
            
        
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()