import gensim
import spacy
spacy.load("es_core_news_sm")
from spacy.lang.es import Spanish
import nltk
from nltk.corpus import wordnet as wn
from nltk.stem.wordnet import WordNetLemmatizer
import string
from gensim import corpora
import pickle
parser = Spanish()

#nltk.download('wordnet')
#nltk.download('stopwords')

class DefinidorTopico():

    def definidor_topico(self, texto):
        datos_texto = []


        for sentence in texto.sents():
            sentence_string = "".join([" " + i if not i.startswith("'") and i not in string.punctuation else i for i in sentence]).strip()
            tokens = self.preparador_texto(sentence_string)
            datos_texto.append(tokens)

        dictionary = corpora.Dictionary(datos_texto)
        corpus = [dictionary.doc2bow(text) for text in datos_texto]
        pickle.dump(corpus, open('corpus.pkl', 'wb'))
        dictionary.save('dictionary.gensim')
        NUM_TOPICS = 1
        ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=NUM_TOPICS, id2word=dictionary, passes=15)
        ldamodel.save('model5.gensim')
        topics = ldamodel.print_topics(num_words=4)

        for topic in topics:
            print("Posibles tópicos del texto que se analizará: ", topic)

    def preparador_texto(self, texto):
        es_stop = set(nltk.corpus.stopwords.words('spanish'))
        tokens = self.tokenize(texto)
        tokens = [token for token in tokens if len(token) > 4]
        tokens = [token for token in tokens if token not in es_stop]
        tokens = [self.get_lemma(token) for token in tokens]
        return tokens


    def tokenize(self, text):
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

    def get_lemma(self, word):
        lemma = wn.morphy(word)
        if lemma is None:
            return word
        else:
            return lemma

    def get_lemma2(self, word):
        return WordNetLemmatizer().lemmatize(word)



definidor_topico = DefinidorTopico()