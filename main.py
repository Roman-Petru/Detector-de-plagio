import time
from texto_a_analizar import texto_a_analizar
from modulo_comparador import comparador
from definidor_topico import definidor_topico

start_time = time.time()

texto_a_evaluar = texto_a_analizar.obtener_texto()

definidor_topico.definidor_topico(texto_a_evaluar)

porcentaje_plagio = comparador.comparar(texto_a_evaluar)

print("Porcentaje de plagio encontrado en el texto: ", porcentaje_plagio)

print ("time elapsed: {:.2f}s".format(time.time() - start_time))