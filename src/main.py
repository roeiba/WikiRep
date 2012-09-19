from semantic_interpreter import SemanticInterpreter
import utilites


filepath = ""
text_1 = ""
text_2 = ""


def main():
    #load database 
    database = utilites.load_db_from_file(filepath)
    
    #init interpreter
    semantic_interpreter = SemanticInterpreter(database)
 
    #generate weighted vectors
    w_vector_1 = semantic_interpreter.build_weighted_vector(text_1) 
    w_vector_2 = semantic_interpreter.build_weighted_vector(text_2)
    
    #compare vectors
    correlation = utilites.compare_vectors(w_vector_1, w_vector_2)
    print "correlation is: {}".format(correlation)
    
if __name__ == '__main__':
    main() 