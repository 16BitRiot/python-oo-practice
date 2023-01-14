"""Word Finder: finds random words from a dictionary."""
import os
import random

class WordFinder:
    ...
    def __init__(self, path): 
        self.file_path = os.path.join(os.path.dirname(__file__), path)
        """capture the files pathway in a variable"""
        self.words =[]
        with open(self.file_path, "r") as x:
            """open the file as read only, and store its contents in x"""
            self.lines_count = len(x.readlines())
            self.words = x.readlines()
            print(self.lines_count)

    def random(self):
        rando =  self.words[random.randrange(0, self.lines_count -1)].strip()
        return rando

webster = WordFinder("/Users/philfryer/Desktop/School Spring/Unit21.4pythonoop/python-oo-practice/words.txt")