import pyterrier as pt
import os

def create_index(documents):
    stopwords = './stopwordlists/stopwords_english_long.txt'
    if not os.path.exists(stopwords):
        raise ValueError('Could not find stopwords file at %s' % stopwords)

    print('I will use a custom stopwords list at %s' % stopwords)

    indexer = pt.IterDictIndexer(
        "/tmp/index", 
        overwrite=True, 
        stopwords=stopwords, 
        meta={'docno': 100, 'text': 20480},
        stemmer='porter'
    )
    index_ref = indexer.index(({'docno': i.doc_id, 'text': i.text} for i in documents))
    return pt.IndexFactory.of(index_ref)
