'''
Created on Oct 1, 2012

@author: roeib

import os 
import unittest

import test_utils as test_utils
from parsers import wrappers
 not working due to wikipage changes on server
class TestWikiParser(test_utils.TestBase):

    def test__get_wiki_page(self):
        import xml.etree.ElementTree as ET
        cur_dir = os.path.dirname(os.path.abspath(__file__))
        expected_result_path = os.path.join(cur_dir ,"expected_results/knowledge_raw_text.txt")

        #init expected xml
        tree = ET.parse(expected_result_path)
        expected_doc = tree.getroot()
        
               
        #handle actual xml
        clean_page = wrappers.get_wiki_page_clean("Knowledge")
        actual_doc = ET.fromstring(clean_page)
        
        self.assertEqual(actual_doc.tag, 'doc', "Root element is expected to 'doc'")
        
        for key in expected_doc.attrib.keys():
            self.assertEqual(expected_doc.attrib[key], actual_doc.attrib[key], 
                "mismatch value at attribute {}.\nExpected: {}\nActual: {}".format(key, expected_doc, actual_doc))
            
        if expected_doc.text != actual_doc.text:
            import difflib
            s = difflib.SequenceMatcher(a=expected_doc.text, b=actual_doc.text)
            for block in s.get_matching_blocks():
                print "match at a[%d] and b[%d] of length %d" % block
            self.fail()
#            print "mismatch inner text.\nExpected: {}\nActual: {}".format(expected_doc.text, actual_doc.text))

    def test__get_wiki_page_clean(self):
        pass
        

if __name__ == "__main__":
    unittest.main()

'''