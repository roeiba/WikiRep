'''
Created on Oct 23, 2012

@author: roeib
'''
import logging

def DEBUG(msg):
    logging.debug(msg)
def INFO(msg):
    logging.info(msg)
def WARNING(msg):
    logging.warning(msg)
def ERROR(msg):
    logging.error(msg)

def log_text(text):
    return text[:80] + "... total chars {}".format(len(text))