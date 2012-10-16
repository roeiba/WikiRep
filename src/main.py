from model.semantic_interpreter import SemanticInterpreter
from model import math_utils
filepath = ""
text_1 = ""
text_2 = ""

'''

config.yml

workspace/
    production/
    
    active_space/
        wikidumb.bz2
        wikiparsed.xml
        wikibuild.wdb
    spaces/
        tests/
        ivan_try
    users/

wikiknows --makedump article1 [article2] [...] [-dump wikidump.bz2]
    downloads specified articles from wikipedia site, 
    merges them into one file, compreses it as wikipedia dump file
    article1 - article canonic name on wikipedia webpage
    -dump - output filename if not specified [[defaults]] are used
    
wikiknows --download [-form url] [-to wikidump.bz2]
    downloads wikipedia dump file  from wikipedia site,
    -form:  url of dump file, if not specified [[defaults]] are used
    -to:    dump filepath on disk, if not specified [[defaults]] are used
    
wikiknows --parse  [-dump wikidump.bz2] [-to wikiparsed.xml]
wikiknows --bulid [-from wikiparsed.xml] [-to wikibuild.wdb]
wikiknows --compare [-text text1.txt] [-with text2.txt] [-using wikibuild.wdb]
wikiknows --wikivalue [-text text1.txt] [-using wikibuild.wdb]
wikiknows --analize  [-text text1.txt] [-using wikibuild.wdb]
'''
def main():
    pass
    #load database 
    #database = utilites.load_db_from_file(filepath)
    #database = utils.load_db_stub(filepath)
    
    #init interpreter
    #semantic_interpreter = SemanticInterpreter(database)
 
    #generate weighted vectors
    #w_vector_1 = semantic_interpreter.build_weighted_vector(text_1) 
    #w_vector_2 = semantic_interpreter.build_weighted_vector(text_2)
    
    #compare vectors
    #correlation = math_utils.cosine_metrics(w_vector_1, w_vector_2)
    #print "correlation is: {}".format(correlation)
    
if __name__ == '__main__':
    main() 
    
    
