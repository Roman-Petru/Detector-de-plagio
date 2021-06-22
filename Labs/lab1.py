msg = "Hola"
print(msg)

>>> from nltk.book import *


*** Introductory Examples for the NLTK Book ***
Loading text1, ..., text9 and sent1, ..., sent9
Type the name of the text or sentence to view it.
Type: 'texts()' or 'sents()' to list the materials.
text1: Moby Dick by Herman Melville 1851
text2: Sense and Sensibility by Jane Austen 1811
text3: The Book of Genesis
text4: Inaugural Address Corpus
text5: Chat Corpus
text6: Monty Python and the Holy Grail
text7: Wall Street Journal
text8: Personals Corpus
text9: The Man Who Was Thursday by G . K . Chesterton 1908


>>> moby_dick_tokens = text1.tokens

>>> from nltk import re
>>> moby_dick_tokens_nopunct = [word.lower() for word in moby_dick_tokens if re.search("\w", word)]

1. Cuál es el número de tokens en Moby Dick?

>>> len (moby_dick_tokens_nopunct)
218621

2. Cuál es el número de types en Moby Dick?

>>>len(set(moby_dick_tokens_nopunct))
17140

3. Moby Dick type-token ratio =  17140/218621 = 0,078

4. WSJ type-token ratio is =

>>> len(WSJ_tokens_nopunct)
87608
>>> len(set(WSJ_tokens_nopunct))
11367

11367/ 87608 = 0,1297

5. Cuál de los dos tiene más diversidad léxica?

WSJ (Wall Street Journal).

6. Puede pensar una razón por por la cual ese corpus es más diverso que el otro?

En una novela como Moby Dick se pueden repetir muy seguido palabras como los nombres de los personajes y sus características, como por ejemplo ballena.

7. Cual es el “Maximum Likelikhood Estimate (MLE)” de la palabra “whale” (ballena) en Moby Dick?

>>> moby_dick_tokens_nopunct_whale = [word for word in moby_dick_tokens_nopunct if re.search("whale", word)]
>>> len(moby_dick_tokens_nopunct_whale)
1685

Pmoby dick(“whale”) = 1685 / 218621 = 0,0077

8. Cuál es el MLE de “whale” en el corpus de WSJ?

>>> WSJ_tokens_whale = [word for word in WSJ_tokens_nopunct if re.search("whale", word)]
>>> len( WSJ_tokens_whale)
0

PWSJ(“whale”) =  0 / 87608 = 0