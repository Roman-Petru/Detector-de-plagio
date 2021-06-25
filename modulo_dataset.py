# Clase que trae los corpus del dataset    https://living-sun.com/es/python/696855-creating-a-new-corpus-with-nltk-python-nlp-nltk-corpus.html


# import nltk
import glob
import os

from nltk.corpus import PlaintextCorpusReader
import PyPDF2
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
import io
import pypandoc

class ModuloDataSet:

    def __init__(self):
        corpus_root = "./Dataset/"
        self.corpusDataset = PlaintextCorpusReader(corpus_root, r'.*.txt')
        #for sentence in self.corpusDataset.sents():
         #   print(sentence)
        #for infile in sorted(self.corpusDataset.fileids()):
            #print (infile)
            #with self.corpusDataset.open(infile) as fin:  # Opens the file.
        #  print (fin.read().strip())  # Prints the content of the file
        #  print
        """
        path = './Dataset/'
        contarch = 200
        for filename in glob.glob(os.path.join(path, '*.docx')):
            nuevo_filename = ("./Dataset/Temp//" + str(contarch) + ".txt")
            contarch = contarch + 1
            output = pypandoc.convert_file(filename, 'plain', outputfile=nuevo_filename)
            assert output == ""

    #path = './Dataset/Temp/'
   
    contarch = 0;
    path = './Dataset/'
    for filename in glob.glob(os.path.join(path, '*.pdf')):
        with open(os.path.join(os.getcwd(), filename), 'rb') as f:  # open in readonly mode
            resMgr = PDFResourceManager()
            retData = io.StringIO()
            TxtConverter = TextConverter(resMgr, retData, laparams=LAParams())
            interpeter = PDFPageInterpreter(resMgr, TxtConverter)

            for page in PDFPage.get_pages(f):
                interpeter.process_page(page)

            txt = retData.getvalue()
            nuevo_filename = ("./Dataset/Temp//" + str (contarch) + ".txt")
            contarch = contarch + 1
            with open(nuevo_filename, "w", encoding="utf-8") as fileTxt:
                fileTxt.write(txt)
            
            pdfReader = PyPDF2.PdfFileReader(f)

            nuevo_filename = ("./Dataset/Temp//" + str (contarch) + ".txt")
            contarch = contarch + 1
            with open(nuevo_filename, "w") as fileTxt:
                for page in range(pdfReader.getNumPages()):
                    #data = pdfReader.getPage(page).extractText()
                    #print(data)
                    #fileTxt.write(data)
                    fileTxt.close()"""
            #f.close()





dataset = ModuloDataSet()
