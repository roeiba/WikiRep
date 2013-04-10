import parse_tools as pt
import os


def print_xmldump_statistics(file_like):
    template = "{:<12}{:<30}{:>12}"
    print template.format('id', ' title', 'length')
    print '----------------------------------------------------------------------'
    
    for tid, title, text, _ in pt.extract_pages(file_like):
        print template.format(tid, title, len(text))
