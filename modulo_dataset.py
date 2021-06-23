# Clase que trae los corpus del dataset    https://living-sun.com/es/python/696855-creating-a-new-corpus-with-nltk-python-nlp-nltk-corpus.html


# import nltk
from nltk.corpus import PlaintextCorpusReader


class ModuloDataSet:

    def __init__(self):
        corpus_root = "./Dataset/"
        self.corpusDataset = PlaintextCorpusReader(corpus_root, r'.*.txt')
        #for sentence in self.corpusDataset.sents():
         #   print(sentence)




dataset = ModuloDataSet()
