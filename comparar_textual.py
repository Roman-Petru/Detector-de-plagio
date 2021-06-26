from nltk.tokenize.treebank import TreebankWordDetokenizer
import string

class CompararTextual:

    def plagio_directo(self, texto_a_evaluar, corpus):
        if (texto_a_evaluar == corpus) and (len(texto_a_evaluar) > 5):
            texto_plagiado = "".join([" "+i if not i.startswith("'") and i not in string.punctuation else i for i in texto_a_evaluar]).strip()
            print("Se encontro plagio directo en la frase:", texto_plagiado)
            return True

comparador_directo = CompararTextual()