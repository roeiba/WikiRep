
class WikiKnowledge(object):
    
    def make_dump(self, wiki_dump, *articles):
        """
        Download specified articles from Wikipedia site, 
        merges them into one file, compresses it as Wikipedia dump file
        @param articles: article's canonic name on Wikipedia web page
        @param wiki_dump: output filename (if not specified default is used)
        """
        pass
    
    def download(self, src_url, wiki_dump=None):
        """
        Download wikipedia dump file.
        @param src_url: url of dump file (if not specified default is used)
        @param wiki_dump: dump filename, etc. wikidump.bz2 (if not specified default is used)
        """
        pass
    
    def parse(self, wiki_dump, output):
        """
        Parses wiki_dump.
        @param wiki_dump: input wikipedia dump filename  
        @param output: output xml filename
        """
        pass
    def build(self, src, output):
        """
        builds WikiRep database.
        @param src: Wikipedia source xml (etc. wikiparsed.xml)
        @param output: WikiRep database output file
        """
        pass
    def compare(self, text1, text2, db):
        """
        Compares two texts in wikipedia space.
        @param db: WikiRep database filename
        """
        pass
    def get_text_value(self, text, db):
        """
        returns the text vector in wikipedia space.
        @param db: WikiRep database filename
        """
        pass
    def analize(self, text1, db):
        """
        @param db: WikiRep database filename
        """
        pass