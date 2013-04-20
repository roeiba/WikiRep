import parse_tools as pt

def print_xmldump_statistics(file_like):
    template = "{:<12}{:<30}{:>12}"
    print template.format('id', ' title', 'length')
    print '----------------------------------------------------------------------'
    
    for doc in pt.iterate_wiki_pages(file_like):
        print template.format(doc.id, doc.title, len(doc.wiki_text))
