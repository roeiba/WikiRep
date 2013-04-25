'''
Created on Nov 28, 2012

@author: inesmeya
'''
from os.path import dirname, join 


data_input_dir =  join(dirname(__file__), 'data_input')
data_output_dir =  join(dirname(__file__), 'data_output')

def getInputFile(filename):
    return join(data_input_dir,filename)

def getOutputFile(filename):
    return join(data_output_dir,filename)

class FilesList(object):
    test__parse_tools ='test__parse_tools.xml'
    
