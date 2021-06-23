#https://stackoverflow.com/questions/46732843/compare-two-sentences-on-basis-of-grammar-using-nlp

from modulo_dataset import dataset
from nltk.tokenize import sent_tokenize, word_tokenize
import nltk
from nltk.corpus import PlaintextCorpusReader
from comparar_textual import comparador_directo


class ModuloComparador:

    def comparar(self):
        contador = 0
        corpus_root = "./ChequearPlagio/"
        texto_a_evaluar = PlaintextCorpusReader(corpus_root, r'.*.txt')
        for oracionAEvaluar in texto_a_evaluar.sents():
            for oracionDataset in dataset.corpusDataset.sents():
                if comparador_directo.plagio_directo(oracionAEvaluar, oracionDataset):
                    contador += 1
                    break

        porcentaje_plagio = contador / (len(texto_a_evaluar.sents())) * 100
        print("Porcentaje de plagio encontrado en el texto: ", porcentaje_plagio)

comparador = ModuloComparador()