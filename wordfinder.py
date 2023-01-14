"""Word Finder: finds random words from a dictionary."""
import os
import random


class WordFinder:
    ...

    def __init__(self, path):
        self.file_path = os.path.join(os.path.dirname(__file__), path)
        """capture the files pathway in a new variable"""
        with open(self.file_path, "r") as x:
            """open the file as read only, and store its contents in x"""
            self.lines_count = len(x.readlines())

    def random(self):
        with open(self.file_path, "r") as y:
            """open the file as read only, and store its contents in y"""
            self.words = y.readlines
            """capture all lines in the file into a new variable"""
            return self.words()[random.randrange(0, self.lines_count - 1)]
            """returns a random selection by generating a number between one and the highest number in the doc, and uses that number as an index number"""

class SpecialWordFinder(WordFinder):
    """this is a subclass that inherits from the WordFinder class"""
    def __init__(self, path):
        super().__init__(path)
        """initilaize same settings from superclass"""
    def random(self):
        with open(self.file_path, "r") as y:
            """open the file as read only, and store its contents in y"""
            self.words = [line for line in y if not line.startswith("#") and line.strip()]
            """check for and skip lines that start with a # or are blank"""
            return self.words[random.randrange(0, len(self.words) - 1)]
            """returns a random selection by generating a number between one and the highest number in the doc, and uses that number as an index number"""

webster = WordFinder("/Users/philfryer/Desktop/School Spring/Unit21.4pythonoop/python-oo-practice/words.txt")
print(webster.random())
