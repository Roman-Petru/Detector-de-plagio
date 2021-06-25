import glob
import io
import os

from nltk.corpus import PlaintextCorpusReader
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams

class TextoAAnalizar():

    def obtener_texto(self):
        corpus_root = "./ChequearPlagio/"
        print("Nombre del archivo o archivos de texto que se procesará: ", os.listdir("./ChequearPlagio/"))
        contarch = 0
        for filename in glob.glob(os.path.join(corpus_root, '*.pdf')):
            with open(os.path.join(os.getcwd(), filename), 'rb') as f:  # open in readonly mode
                resMgr = PDFResourceManager()
                retData = io.StringIO()
                TxtConverter = TextConverter(resMgr, retData, laparams=LAParams())
                interpeter = PDFPageInterpreter(resMgr, TxtConverter)

                for page in PDFPage.get_pages(f):
                    interpeter.process_page(page)

                txt = retData.getvalue()
                nuevo_filename = ("./ChequearPlagio/" + str(contarch) + ".txt")
                contarch = contarch + 1
                with open(nuevo_filename, "w", encoding="utf-8") as fileTxt:
                    fileTxt.write(txt)


        texto_a_evaluar = PlaintextCorpusReader(corpus_root, r'.*.txt')
        return texto_a_evaluar



texto_a_analizar = TextoAAnalizar()
