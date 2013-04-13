'''
Created on Oct 23, 2012

@author: roeib
'''
import logging

#logging.basicConfig()

_log = logging.getLogger("MAIN")
mainlog = _log  #alias

def getLogger(name):
    return logging.getLogger(name)

def DEBUG(msg):
    _log.debug(msg)
def INFO(msg):
    _log.info(msg)
def WARNING(msg):
    _log.warning(msg)
def ERROR(msg):
    _log.error(msg)

