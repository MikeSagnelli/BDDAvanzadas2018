import math
from collections import Counter
import sys
import os
import string

ROOT = lambda base : os.path.join(os.path.dirname(__file__), base).replace('\\','/')
FILE_NAME = "file.txt"
DICTIONARY_FILE = "dictionary.txt"
ERROR = 0.20

class WordCounter:

    # Define a default constructor. It asumes you have a file named as the FILE_NAME variable.
    def __init__(self):
        self.dictionary = {}
        self.analyzer_dictionary = {}
        try:
            self.file = open(ROOT(FILE_NAME), "r")
        except IOError:
            print ("Cannot open " + FILE_NAME)
        else:
            text = self.file.read()
            self.file.close()
            words = text.split()
            table = str.maketrans('','', string.punctuation)
            raw_words = [w.translate(table).encode('ascii',errors='ignore').decode().lower() for w in words]
            for w in raw_words:
                if(w in self.dictionary):
                    self.dictionary[w] = self.dictionary[w] + 1
                else:
                    self.dictionary[w] = 1
        
    # Function for printing frequency of words in a text.
    def print_output(self, dictionary):
        for i, key in enumerate(dictionary.keys()):
            print (i, ".- " + key + ": ", dictionary[key])

    def cosine_distance(self, v1, v2):
        common = v1[1].intersection(v2[1])
        x = sum(v1[0][ch] * v2[0][ch] for ch in common) / v1[2] / v2[2]
        return x
    
    def word_to_vector(self, word):
        cw = Counter(word)
        sw = set(cw)
        lw = math.sqrt(sum(c * c for c in cw.values()))
        return cw, sw, lw

    def open_dictionary_file(self, file_name):
        try:
            file = open(file_name, "r")
        except IOError:
            print ("Cannot open " + file_name)
        else:
            return file

    def define_analyzer_dictionary(self, file):
        text = file.read()
        file.close()
        words = text.split()
        table = str.maketrans('','', string.punctuation)
        raw_words = [w.translate(table).encode('ascii',errors='ignore').decode().lower() for w in words]
        for i, w in enumerate(raw_words):
            self.analyzer_dictionary[w] = i

    def print_separator(self):
        print ()
        print ("+---------------------------------------+")
        print ()

    def print_analyzed_output(self):
        self.define_analyzer_dictionary(self.open_dictionary_file(DICTIONARY_FILE))
        final = {}
        added = False
        for key1 in self.dictionary.keys():
            for key2 in self.analyzer_dictionary.keys():
                distance = self.cosine_distance(self.word_to_vector(key1), self.word_to_vector(key2))
                if(distance >= (1 - ERROR)):
                    if(key2 in final):
                        final[key2] = final[key2] + 1
                    else:
                        final[key2] = 1
                    added = True
                    break
            if(added):
                added = False
            else:
                if(key1 in final):
                    final[key1] = final[key1] + 1
                else:
                    final[key1] = 1
        
        self.print_output(final)