
class CompararTextual:

    def plagio_directo(self, texto_a_evaluar, corpus):
        if texto_a_evaluar == corpus:
            print("Se encontro plagio directo en la frase:", texto_a_evaluar)
            return True

comparador_directo = CompararTextual()