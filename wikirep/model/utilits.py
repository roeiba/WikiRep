'''
Created on Apr 25, 2013

@author: inesmeya
'''

def get_top(d,n):
    s = sorted(d.items(), key=lambda x: x[1], reverse=True)[:n]
    return s