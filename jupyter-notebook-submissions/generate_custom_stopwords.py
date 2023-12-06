import os
import pyterrier as pt

def generate_custom_stopwords(documents):
    # create a standart index
    indexer = pt.IterDictIndexer(
        "/tmp/index_for_stopwords", 
        overwrite=True, 
        meta={'docno': 100, 'text': 20480},
    )
    index_ref = indexer.index(({'docno': i.doc_id, 'text': i.text} for i in documents))
    index = pt.IndexFactory.of(index_ref)


    # use other methods e.g. normalised term frequency, idf, normalised idf
    stopword_list_length = 550

    # Get the lexicon (term dictionary)
    lexicon = index.getLexicon()

    # Retrieve term frequencies and terms
    term_frequencies = [(term, le.getFrequency()) for term, le in lexicon]

    # Sort the terms by frequency in descending order
    sorted_terms = sorted(term_frequencies, key=lambda x: x[1], reverse=True)

    file_path = './stopwordlists/custom_stopwords.txt'

    with open(file_path, 'w') as file:
        file.write("")

    # Open the file in 'a' (append) mode
    with open(file_path, 'a') as file:
        # Your loop
        for term, le in sorted_terms[:stopword_list_length]:
            string_to_append = f"{term}\n"
            file.write(string_to_append)   