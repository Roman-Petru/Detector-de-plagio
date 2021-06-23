from modulo_dataset import dataset

from comparar_textual import comparador_directo
from comparar_con_parafraseo import comparador_con_parafraseo
from nltk import re
from nltk.stem import SnowballStemmer
import string

class ModuloComparador:

    def comparar(self, texto_a_evaluar):
        stm = SnowballStemmer('spanish')
        contador = 0
        alumno_encontrado = False

        for oracion_a_evaluar in texto_a_evaluar.sents():

            oracion_a_evaluar_no_punct = [word.lower() for word in oracion_a_evaluar if re.search("\w", word)]

            for oracion_dataset in dataset.corpusDataset.sents():

                oracion_dataset_no_punct = [word.lower() for word in oracion_dataset if re.search("\w", word)]

                if not alumno_encontrado and ((oracion_a_evaluar_no_punct[0] == 'alumno') or (oracion_a_evaluar_no_punct[0] == 'nombre')):
                    string_para_print = oracion_a_evaluar_no_punct;
                    del string_para_print[0]
                    string_para_print = "".join([" " + i if not i.startswith("'") and i not in string.punctuation else i for i in string_para_print]).strip()
                    print("Se detectó alumno autor del trabajo: ", string_para_print)
                    alumno_encontrado = True

                if comparador_directo.plagio_directo(oracion_a_evaluar_no_punct, oracion_dataset_no_punct):
                    contador += 1
                    break

                if comparador_con_parafraseo.evaluar_parafraseo(oracion_a_evaluar_no_punct, oracion_dataset_no_punct, stm):
                    contador += 1
                    break

        return contador / (len(texto_a_evaluar.sents())) * 100

comparador = ModuloComparador()