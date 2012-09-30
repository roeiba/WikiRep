'''
Created on Sep 30, 2012

@author: inesmeya
'''
import unittest




class Test__WikiExtractor(unittest.TestCase):

    def test_wiki_extractor_simple(self):
        import parsers.WikiExtractor as extractor
        #source = "http://en.wikipedia.org/wiki/Jack_Guynn"
        input_str= """<mediawiki
    xmlns="http://www.mediawiki.org/xml/export-0.7/"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.mediawiki.org/xml/export-0.7/ http://www.mediawiki.org/xml/export-0.7.xsd" version="0.7" xml:lang="en">
    <siteinfo>
        <sitename>Wikipedia</sitename>
        <base>http://en.wikipedia.org/wiki/Main_Page</base>
        <generator>MediaWiki 1.20wmf12</generator>
        <case>first-letter</case>
        <namespaces>
            <namespace key="-2" case="first-letter">Media</namespace>
            <namespace key="-1" case="first-letter">Special</namespace>
            <namespace key="0" case="first-letter" />
            <namespace key="1" case="first-letter">Talk</namespace>
            <namespace key="2" case="first-letter">User</namespace>
            <namespace key="3" case="first-letter">User talk</namespace>
            <namespace key="4" case="first-letter">Wikipedia</namespace>
            <namespace key="5" case="first-letter">Wikipedia talk</namespace>
            <namespace key="6" case="first-letter">File</namespace>
            <namespace key="7" case="first-letter">File talk</namespace>
            <namespace key="8" case="first-letter">MediaWiki</namespace>
            <namespace key="9" case="first-letter">MediaWiki talk</namespace>
            <namespace key="10" case="first-letter">Template</namespace>
            <namespace key="11" case="first-letter">Template talk</namespace>
            <namespace key="12" case="first-letter">Help</namespace>
            <namespace key="13" case="first-letter">Help talk</namespace>
            <namespace key="14" case="first-letter">Category</namespace>
            <namespace key="15" case="first-letter">Category talk</namespace>
            <namespace key="100" case="first-letter">Portal</namespace>
            <namespace key="101" case="first-letter">Portal talk</namespace>
            <namespace key="108" case="first-letter">Book</namespace>
            <namespace key="109" case="first-letter">Book talk</namespace>
        </namespaces>
    </siteinfo>
    <page>
        <title>Jack Guynn</title>
        <ns>0</ns>
        <id>10261726</id>
        <revision>
            <id>443236487</id>
            <parentid>399884552</parentid>
            <timestamp>2011-08-05T20:06:58Z</timestamp>
            <contributor>
                <username>GTBacchus</username>
                <id>6781</id>
            </contributor>
            <minor/>
            <comment>stub sorting</comment>
            <sha1>d995xbaaup38p3psewju96lfxdzssf3</sha1>
            <text xml:space="preserve" bytes="1982">'''Jack Guynn''' was the President and CEO of the [[Federal Reserve Bank of Atlanta]] from 1996 to 2006.&lt;ref&gt;{{cite news| url=http://www.alumni.gatech.edu/news/ttopics/spr96/guynn.html| title=Guynn Heads Atlanta Fed| work=Tech Topics| publisher=Georgia Tech Alumni Association| date=Spring 1996| accessdate=2007-03-25}}&lt;/ref&gt; He has retired from that position&lt;ref&gt;{{cite press release| url=http://www.frbatlanta.org/invoke.cfm?objectid=FBDFB035-5056-9F1A-E2A4E68240C4CEC9&amp;method=display_pressrelease| title=Atlanta Fed president Jack Guynn to retire October 1, 2006| publisher=[[Federal Reserve Bank of Atlanta]]| date=2006-06-22| accessdate=2007-03-25}}&lt;/ref&gt; and been appointed to [[Oxford Industries, Inc.]]'s Board of Directors.&lt;ref&gt;{{cite news|url=http://www.fibre2fashion.com/news/company-news/oxford-industries/newsdetails.aspx?news_id=28853| title=USA : Jack Guynn joins Atlanta-based apparel marketer firm| publisher=www.fibre2fashion.com| date=2007-01-09| accessdate=2007-03-25}}&lt;/ref&gt;

Guynn received a Bachelor's degree in Industrial Engineering from [[Virginia Tech]] and also is a 1969 graduate of [[Georgia Institute of Technology|Georgia Tech]]'s [[Georgia Institute of Technology College of Management|College of Management]] from which he received an MBA.&lt;ref&gt;{{cite web|url=http://mgt.gatech.edu/news_room/news/2006/jackguynn/index.html|title=Alumni Profile: Jack Guynn Leads Federal Reserve Bank of Atlanta|work=Georgia Tech College of Management|accessdate=2007-03-25}} {{Dead link|date=October 2010|bot=H3llBot}}&lt;/ref&gt;

==References==
{{reflist}}

{{Persondata &lt;!-- Metadata: see [[Wikipedia:Persondata]]. --&gt;
| NAME              = Guynn, Jack
| ALTERNATIVE NAMES =
| SHORT DESCRIPTION =
| DATE OF BIRTH     =
| PLACE OF BIRTH    =
| DATE OF DEATH     =
| PLACE OF DEATH    =
}}
{{DEFAULTSORT:Guynn, Jack}}
[[Category:Living people]]
[[Category:Georgia Institute of Technology alumni]]
[[Category:Year of birth missing (living people)]]


{{US-economist-stub}}</text>
        </revision>
    </page>
</mediawiki>"""
        
        expected = """<doc id="10261726" url="http://en.wikipedia.org/wiki/Jack_guynn" title="Jack Guynn">Jack Guynn

Jack Guynn was the President and CEO of the Federal Reserve Bank of Atlanta from 1996 to 2006. He has retired from that position and been appointed to Oxford Industries, Inc.'s Board of Directors.
Guynn received a Bachelor's degree in Industrial Engineering from Virginia Tech and also is a 1969 graduate of Georgia Tech's College of Management from which he received an MBA.

</doc>
"""        
        actual = extractor.run(input_str)
        self.assertEqual(expected, actual, "expected={}, actual={}".format(expected, actual))





if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_wiki_extractor']
    unittest.main()