#https://stackoverflow.com/questions/46732843/compare-two-sentences-on-basis-of-grammar-using-nlp
import string
import pandas as pd
import nltk
from nltk.corpus import wordnet as wn
import itertools


class CompararParafraseo:

    def evaluar_parafraseo(self, texto_a_evaluar, corpus, stm):

        if len(texto_a_evaluar) < 5:
            return False


        texto_a_evaluar = "".join([" " + i if not i.startswith("'") and i not in string.punctuation else i for i in texto_a_evaluar]).strip()
        corpus = "".join([" " + i if not i.startswith("'") and i not in string.punctuation else i for i in corpus]).strip()
        texto_posible_plagio = texto_a_evaluar
        texto_posible_ser_plagiado = corpus
        #Convert the tag given by nltk.pos_tag to the tag used by wordnet.synsets
        tag_dict = {'N': 'n', 'J': 'a', 'R': 'r', 'V': 'v'}

        s1 = nltk.pos_tag(nltk.word_tokenize(texto_a_evaluar))

        s1 = dict(filter(lambda x: len(x[1])>0,
                         map(lambda row: (row[0],wn.synsets(
                               stm.stem(row[0]),
                               tag_dict[row[1][0]], lang='spa')) if row[1][0] in tag_dict.keys()
                             else (row[0],[]),s1)))

        s2 = nltk.pos_tag(nltk.word_tokenize(corpus))

        s2 = dict(filter(lambda x: len(x[1])>0,
                         map(lambda row: (row[0],wn.synsets(
                                  stm.stem(row[0]),
                                  tag_dict[row[1][0]], lang='spa')) if row[1][0] in tag_dict.keys()
                             else (row[0],[]),s2)))

        res = {}
        for w2,gr2 in s2.items():
            for w1,gr1 in s1.items():
                tmp = pd.Series(list(map(lambda row: row[1].path_similarity(row[0]),
                                         itertools.product(gr1,gr2)))).dropna()
                if len(tmp)>0:
                    res[(w1,w2)] = tmp.max()

        similarity = pd.Series(res).groupby(level=0).max().mean()

        if 0.7 < similarity < 1:
            print("Se ha encontrado un posible parafraseo en la oración: ", texto_posible_plagio)
            print("Con respecto a la oración: ", texto_posible_ser_plagiado)
            print("El porcentaje de similitud de estas dos últimas oraciones es de: ", similarity * 100)
            return True


comparador_con_parafraseo = CompararParafraseo()