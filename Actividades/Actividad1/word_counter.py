import sys
import os

ROOT = lambda base : os.path.join(os.path.dirname(__file__), base).replace('\\','/')
FILE_NAME = "file.txt"

class WordCounter:

    def __init__(self):
        self.dictionary = {}
        try:
            self.file = open(ROOT(FILE_NAME), "r")
        except IOError:
            print "Cannot open " + FILE_NAME
        else:
            for line in self.file:
                words_in_line = line.split(" ")
                for word in words_in_line:
                    if(word in self.dictionary):
                        self.dictionary[word] = self.dictionary[word] + 1
                    else:
                        self.dictionary[word] = 1
            
            self.file.close()

    def from_file(cls, file_name):
        dictionary = {}
        try:
            file = open(file_name, "r")
        except IOError:
            print "Cannot open " + file_name
        else:
            for line in file:
                words_in_line = line.split(" ")
                for word in words_in_line:
                    if(word in dictionary):
                        dictionary[word] = dictionary[word] + 1
                    else:
                        dictionary[word] = 1
            
            file.close()
        
        return cls(dictionary)
        
    def print_output(self):
        for key in self.dictionary.keys():
            print "Key: " + key + " is in file ", self.dictionary[key], " times."
