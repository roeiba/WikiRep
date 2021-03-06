'''
Created on Apr 24, 2013

@author: inesmeya
'''
import unittest
from wiki_knows import wiki_knowledge
from io_test_utils import getOutputFile, getInputFile
from model.stemmers import PorterStemmer
from model.semantic_interpreter import SemanticComparer



from model.logger import getTestLogger
_log = getTestLogger("wiki_exec")


def get_top(d,n):
    s = sorted(d.items(), key=lambda x: x[1], reverse=True)[:n]
    return s

"""

Articles
--------

    Politics, Technology, Computer, Nature, Art, 
    Busyness, Internet, Biology, Physics, Law, Economics, History,
    Education, War, Love, Emotion, Medicine, Research, Sociology,
    Wealth, Science


Code to download articles
-------------------------

    articles_titles = '''Politics, Technology, Computer, Nature, Art, 
                    Busyness, Internet, Biology, Physics, Law, Economics, History,
                    Education, War, Love, Emotion, Medicine, Research, Sociology,
                    Wealth, Science'''
    articles_titles  = map(lambda x: x.lstrip(), articles_titles.split(','))

    dump = getInputFile("many_articles_dump.xml")
    wiki_knowledge.make_dump(dump, articles_titles)


Parsed to index
---------------
        parsed_xml_path = getInputFile("many_articles_dump.parsed.xml")
        wdb_path = getInputFile("many_articles_dump.wdb")
        wiki_knowledge.build_database_wrapper_to_file(parsed_xml_path, wdb_path, PorterStemmer())
        
        #c = db_wrapper.get_readable_centroid(ibm_licence_text)
        #print c 
        
        #comp = SemanticComparer(db_wrapper)

"""


ibm_licence_text_full = '''
The following are terms of a legal downloader agreement (the "Agreement") regarding Your download of Content (as defined below) from this Website. IBM may change these terms of use and other requirements and guidelines for use of this Website at its sole discretion. This Website may contain other proprietary notices and copyright information the terms of which must be observed and followed. Any use of the Content in violation of this Agreement is strictly prohibited.

"Content" includes, but is not limited to, software, text and/or speech files, code, associated materials, media and /or documentation that You download from this Website. The Content may be provided by IBM or third-parties. IBM Content is owned by IBM and is copyrighted and licensed, not sold. Third-party Content is owned by its respective owner and is licensed by the third party directly to You. IBM's decision to permit posting of third-party Content does not constitute an express or implied license from IBM to You or a recommendation or endorsement by IBM of any particular product, service, company or technology.

The party providing the Content (the "Provider") grants You a nonexclusive, worldwide, irrevocable, royalty-free, copyright license to edit, copy, reproduce, publish, publicly display and/or perform, format, modify and/or make derivative works of, translate, re-arrange, and distribute the Content or any portions thereof and to sublicense any or all such rights and to permit sublicensees to further sublicense such rights, for both commercial and non-commercial use, provided You abide by the terms of this Agreement. You understand that no assurances are provided that the Content does not infringe the intellectual property rights of any other entity. Neither IBM nor the provider of the Content grants a patent license of any kind, whether expressed or implied or by estoppel. As a condition of exercising the rights and licenses granted under this Agreement, You assume sole responsibility to obtain any other intellectual property rights needed.

The Provider of the Content is the party that submitted the Content for Posting and who represents and warrants that they own all of the Content, (or have obtained all written releases, authorizations and licenses from any other owner(s) necessary to grant IBM and downloaders this license with respect to portions of the Content not owned by the Provider). All information provided on or through this Website may be changed or updated without notice. You understand that IBM has no obligation to check information and /or Content on the Website and that the information and/or Content provided on this Web site may contain technical inaccuracies or typographical errors.

IBM may, in its sole discretion, discontinue the Website, any service provided on or through the Website, as well as limit or discontinue access to any Content posted on the Website for any reason without notice. IBM may terminate this Agreement and Your rights to access, use and download Content from the Website at any time, with or without cause, immediately and without notice.

ALL INFORMATION AND CONTENT IS PROVIDED ON AN "AS IS" BASIS. IBM MAKES NO REPRESENTATIONS OR WARRANTIES, EXPRESS OR IMPLIED, CONCERNING USE OF THE WEBSITE, THE CONTENT, OR THE COMPLETENESS OR ACCURACY OF THE CONTENT OR INFORMATION OBTAINED FROM THE WEBSITE. IBM SPECIFICALLY DISCLAIMS ALL WARRANTIES WITH REGARD TO THE IMPLIED WARRANTIES OF NON-INFRINGEMENT, MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE. IBM DOES NOT WARRANT UNINTERRUPTED OR ERROR-FREE OPERATION OF ANY CONTENT. IBM IS NOT RESPONSIBLE FOR THE RESULTS OBTAINED FROM THE USE OF THE CONTENT OR INFORMATION OBTAINED FROM THE WEBSITE.

LIMITATION OF LIABILITY. IN NO EVENT WILL IBM BE LIABLE TO ANY PARTY FOR ANY DIRECT, INDIRECT, SPECIAL OR OTHER CONSEQUENTIAL DAMAGES FOR ANY USE OF THIS WEBSITE, THE USE OF CONTENT FROM THIS WEBSITE, OR ON ANY OTHER HYPER LINKED WEB SITE, INCLUDING, WITHOUT LIMITATION, ANY LOST PROFITS, BUSINESS INTERRUPTION, LOSS OF PROGRAMS OR OTHER DATA ON YOUR INFORMATION HANDLING SYSTEM OR OTHERWISE, EVEN IF IBM IS EXPRESSLY ADVISED OF THE POSSIBILITY OF SUCH DAMAGES.

The laws of the State of New York, USA govern this Agreement, without reference to conflict of law principles. The "United Nations Convention on International Sale of Goods" does not apply. This Agreement may not be assigned by You. The parties agree to waive their right to a trial by jury.

This Agreement is the complete and exclusive agreement between the parties and supersedes all prior agreements, oral or written, and all other communications relating to the subject matter hereof. For clarification, it is understood and You agree, that any additional agreement or license terms that may accompany the Content is invalid, void, and non-enforceable to any downloader of this Content including IBM.

If any section of this Agreement is found by competent authority to be invalid, illegal or unenforceable in any respect for any reason, the validity, legality and enforceability of any such section in every other respect and the remainder of this Agreement shall continue in effect.
'''


ibm_licence_text = '''
The following are terms of a legal downloader agreement (the "Agreement") regarding Your download of Content (as defined below) from this Website. IBM may change these terms of use and other requirements and guidelines for use of this Website at its sole discretion. This Website may contain other proprietary notices and copyright information the terms of which must be observed and followed. Any use of the Content in violation of this Agreement is strictly prohibited.

"Content" includes, but is not limited to, software, text and/or speech files, code, associated materials, media and /or documentation that You download from this Website. The Content may be provided by IBM or third-parties. IBM Content is owned by IBM and is copyrighted and licensed, not sold. Third-party Content is owned by its respective owner and is licensed by the third party directly to You. IBM's decision to permit posting of third-party Content does not constitute an express or implied license from IBM to You or a recommendation or endorsement by IBM of any particular product, service, company or technology.
'''


class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def test__many_articles(self):
        wdb_path = getInputFile("many_articles_dump.wdb")
        db_wrapper = wiki_knowledge.load_db_wrapper_from_wdb(wdb_path)
                
        d = db_wrapper.get_readable_centroid(ibm_licence_text_full)

        top = get_top(d,5)
        self.assertIn("Computer", dict(top))

        d = db_wrapper.get_readable_centroid(ibm_licence_text)
        top = get_top(d,5)
        self.assertIn("Computer", dict(top))
                
        #comp = SemanticComparer(db_wrapper)
        
    def test__many_articles_files(self):
        wdb_path = getInputFile("many_articles_dump.wdb")
        text_path = getInputFile("ibm_licence.txt")
        d = wiki_knowledge.get_value_from_file(wdb_path, text_path)
        top = get_top(d,5)
        self.assertIn("Computer", dict(top))
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()