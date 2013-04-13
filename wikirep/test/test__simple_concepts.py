# -*- coding: utf-8 -*-

from model.concept import Concept
import unittest
import test_utils
from model import db_builder
from model import stemmers
from model.stemmers import StopWordsStemmer
from model.semantic_interpreter import SemanticComparer


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

business_text = """Jeff Hirsch’s recommendation to reduce risk was prescient. He based his bearish call on the fact that the stock market had run up [23.52%] since its October 2011 low, was nearing the end of its strongest seasonal period and was losing momentum. His timing was spot on. The Dow Jones Industrial average began tumbling on cue, peaking on May 1 before retreating. In May the Dow has fallen 6% to 12,420 and has suffered losses 16 of 21 sessions, including Wednesday’s 161-point drop …
Brian Belski, chief investment strategist at BMO Capital Markets, says making “wholesale portfolio changes” based on seasonality is “dangerous.” While the math may add up on paper, it’s unlikely to be a winning strategy in the real world because investors lack the discipline to get in and out as required.
—Adam Shell: “‘Sell in May’ Stock Strategy Certainly Held Up This Year,” USA Today, May 30, 2012
Thank you, Brian Belski. Thank you, Jeff Hirsch.
The singular distinction, as we begin the fourth-quarter dash, is no one is in this market. Even the select few, 142?, are on their Bloomberg mobile app at 4 a.m. with one eye on Spain, one eye on Obama/Romney, and the third-eye blind to Big Corporate behavior. This has been a spectacular and lonely advance. (The DJIA has advanced 23.52% in 12 months, vanquishing the single-digit gloomsters.)
Hirsch, of the definitive Stock Traders Almanac, nailed the short-term pause of April, May, and a smidgin of June. Belski, of Bank of Montreal (BMO) (I’ll say BMO when the Habs start winning again), and others of courage nailed—absolutely nailed—this twisted 2012.
2013 beckons. The Red Sox need a lobotomy—excuse me, pitching. There will be a first Wednesday of November. And Big Business will do whatever it takes. Repeat: whatever it takes. Where were you in May? Where are you this October?
Buy in October and stay. Discuss.
"""

entertainment_text ="""Giuseppe Verdi's musically magnificent Il Trovatore is, by modern lights, an opera almost at war with itself, weighed down by the now-cliched melodrama of Salvatore Cammarano libretto (adapted from a play by Antonio Garcia Gutierrez), even while it is carried aloft by some of Verdi's most passionate and enduring compositions.
But when the Canadian Opera enters the fray between a leaden libretto and a soaring score, their audience almost always emerges victorious.
For the second time in less than a decade, the COC is showcasing a production of Verdi's tragic opera that ranks as a must-see for opera-philes. This time out, it is a production from Opera de Marseille, under the direction of Charles Roubaud and it opened at the Four Seasons Saturday, with conductor Marco Guidarini marshalling the impressive skills of the COC Orchestra to maximum effect.
In staging Il Trovatore, Roubaud deals with the challenges of the tale -- a story of two brothers, separated at infancy, who grow up on opposite sides of the political spectrum, only to fall in love with the same woman -- with appealing wisdom and dispatch.
"""

class TestSimpleConcepts(test_utils.TestBase):
    
    def test_distinct_concepts(self):
        #arrange:
        stemmer = StopWordsStemmer()
        builder = db_builder.DbBuilder(stemmer)
        
        #HACK:
        for c in distinct_concepts:
            builder.concepts_list.append(c)
            
        db = builder.build()
        
        texts = [technology_text, business_text, entertainment_text]
        
        #act:
        actual_vectors = map(db.get_text_centroid, texts)
        
        # this is example of results
        #[ 0.01241579  0.          0.        ]
        #[ 0.          0.00310828  0.        ]
        #[ 0.          0.          0.00777915]        
        
        # since results are depends on inside algorithms
        # we check only 0 / not 0
        positive = lambda x: self.assertGreater(x, 0.0)
        zero = lambda x: self.assertAlmostEqual(x, 0.0)
        
        # use functions for readability
        tech_vector =    [positive, zero, zero]
        business_vector =[zero, positive, zero]
        ent_vector =     [zero, zero, positive]        
        
        #define excpected vectors
        expected_vectors = [tech_vector, business_vector, ent_vector]
        
        # assert:
        for expected,actual in zip(expected_vectors, actual_vectors):
            for f,val in zip(expected,actual):
                #workaround to handle that x is a sparse matrix
                f(val[0,0])
        
    def test_intersection_concepts(self):
        #splitter = SimpleSplitter()
        
        stemmer = stemmers.get_default_stemmer()
        
        tech_set = set(stemmer.process_text(technology_text))
        busi_set = set(stemmer.process_text(business_text))
        ente_set = set(stemmer.process_text(entertainment_text))
        
        tech_busi = tech_set.intersection(busi_set)
        tech_ente = tech_set.intersection(ente_set)
        busi_busi = tech_set.intersection(ente_set)
         
        print "tech_busi", len(tech_busi), tech_busi
        print "tech_ente", len(tech_ente), tech_ente
        print "busi_busi", len(busi_busi), busi_busi        
           
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()