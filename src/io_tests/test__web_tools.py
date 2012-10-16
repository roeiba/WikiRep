'''
Created on Oct 15, 2012

@author: inesmeya
'''
import unittest
import parsers.web_tools as wt
import StringIO
import xml.etree.ElementTree as etree
import os


class TestGetXmlPage(unittest.TestCase):
    def gen_test_wiki_xmlpage(self, get_func):
        xml = get_func('Southern_Cross_Expedition')
        r = xml.index('<title>Southern Cross Expedition</title>')
        self.assertIsNotNone(r)

    def test_urllib(self):
        self.gen_test_wiki_xmlpage(wt.get_wiki_xmlpage_urllib)

    def test_wget(self):
        #we don't expect to find wget on windows station
        # lower is good
        osname = os.name.lower()
        if osname.find('win') > -1 or osname.find('nt') > -1:
            return
        self.gen_test_wiki_xmlpage(wt.get_wiki_xmlpage_wget)

    def test_get_wiki_xmlpage(self):
        self.gen_test_wiki_xmlpage(wt.get_wiki_xmlpage)


class TestMakeDump(unittest.TestCase):

    # --------------------------- Set up --------------------------------------
    used_files = ['test.xml.tmp']

    def remove_tmp_files(self):
        #select_from(used_files) >> where(os.path.exists) >> do(os.remove)
        for path in self.used_files:
            os.remove(path) if os.path.exists(path) else None

    # -------------------------------------------------------------------------
    def setUp(self):
        self.remove_tmp_files()

    def tearDown(self):
        self.remove_tmp_files()
    # -------------------------------------------------------------------------

    def test__string_dump__number_of_pages(self):
        titles = ['Ross_Ice_Shelf', 'Southern_Cross_Expedition', 'Ice_shelf']
        output = StringIO.StringIO()
        wt.make_articles_dump(titles, output)
        content = output.getvalue()
        output.close()
        self.assertEqual(content.count('<page>'), len(titles))

    def test__string_dump__valid_xml(self):
        titles = ['Ross_Ice_Shelf', 'Southern_Cross_Expedition', ' Ice_shelf']
        output = StringIO.StringIO()
        wt.make_articles_dump(titles, output)
        content = output.getvalue()
        output.close()

        root = etree.fromstring(content)
        pages = root.findall(wt.mk_tag('page'))

        self.assertEqual(len(pages), len(titles))

    def test__articles_dump_to_file(self):
        titles = ['Ross_Ice_Shelf', 'Southern_Cross_Expedition', 'Ice_shelf']
        wt.articles_dump_to_file(titles, 'test.xml.tmp')
        root = etree.parse('test.xml.tmp')
        pages = root.findall(wt.mk_tag('page'))
        self.assertEqual(len(pages), len(titles))

if __name__ == "__main__":
    unittest.main()
