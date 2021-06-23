import time
from nltk.corpus import PlaintextCorpusReader
import os
from modulo_comparador import comparador
from definidor_topico import definidor_topico

start_time = time.time()

print ("Nombre del archivo de texto que se procesará: ", os.listdir("./ChequearPlagio/"))
corpus_root = "./ChequearPlagio/"
texto_a_evaluar = PlaintextCorpusReader(corpus_root, r'.*.txt')

definidor_topico.definidor_topico(texto_a_evaluar)

porcentaje_plagio = comparador.comparar(texto_a_evaluar)

print("Porcentaje de plagio encontrado en el texto: ", porcentaje_plagio)

print ("time elapsed: {:.2f}s".format(time.time() - start_time))