"""
import nltk

#from nltk.book import *
#nltk.help.upenn_tagset(".*")

from nltk.corpus import PlaintextCorpusReader


corpus_root = "./Dataset/"
newcorpus = PlaintextCorpusReader(corpus_root, r'.*.txt')
#newcorpus.words()


for sentence in newcorpus.sents():
    print (sentence)
"""
import os
from modulo_comparador import comparador


print ("Nombre del archivo de texto que se procesará: ", os.listdir("./ChequearPlagio/"))


comparador.comparar()

