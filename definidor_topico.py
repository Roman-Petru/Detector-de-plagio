import spacy
spacy.load("es_core_news_sm")
from spacy.lang.es import Spanish
parser = Spanish()
import nltk
nltk.download('wordnet')
from nltk.corpus import wordnet as wn
from nltk.stem.wordnet import WordNetLemmatizer
nltk.download('stopwords')
import random

class DefinidorTopico():

    def definidor_topico(self, texto):
        text_data = []
        for line in texto:
            tokens = self.preparador_texto(line)
            if random.random() > .99:
                print(tokens)
                text_data.append(tokens)

    def preparador_texto(self, texto):
        es_stop = set(nltk.corpus.stopwords.words('spanish'))
        tokens = self.tokenize(texto)
        tokens = [token for token in tokens if len(token) > 4]
        tokens = [token for token in tokens if token not in es_stop]
        tokens = [self.get_lemma(token) for token in tokens]
        return tokens


    def tokenize(text):
        lda_tokens = []
        tokens = parser(text)
        for token in tokens:
            if token.orth_.isspace():
                continue
            elif token.like_url:
                lda_tokens.append('URL')
            elif token.orth_.startswith('@'):
                lda_tokens.append('SCREEN_NAME')
            else:
                lda_tokens.append(token.lower_)
        return lda_tokens

    def get_lemma(word):
        lemma = wn.morphy(word)
        if lemma is None:
            return word
        else:
            return lemma

    def get_lemma2(word):
        return WordNetLemmatizer().lemmatize(word)



definidor_topico = DefinidorTopico()