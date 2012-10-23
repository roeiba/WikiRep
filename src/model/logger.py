'''
Created on Oct 23, 2012

@author: roeib
'''

def DEBUG(msg):
    print "[DEBUG] ", msg
def INFO(msg):
    print "[INFO] ", msg
def WARNING(msg):
    print "[WARNING] ", msg
def ERROR(msg):
    print "[ERROR] ", msg

def log_text(text):
    return text[:80] + "... total chars {}".format(len(text))