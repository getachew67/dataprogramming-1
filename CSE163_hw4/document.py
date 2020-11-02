"""
Name: Michael Shieh
Section: CSE 163 AB

This file contains the "Document" class.
"""
import re


class Document:
    def __init__(self, file_name):
        """
        This initializer read a file
        and create a dictionary with every word as the key.
        Also records how many words are in the file.
        """
        self._word_list = {}
        self._word_count = 0
        self._file = file_name

        with open(self._file) as f:
            lines = f.readlines()
            for line in lines:
                words = line.split()
                for word in words:
                    word = re.sub(r'\W+', '', word.lower())
                    if word not in self._word_list:
                        self._word_list[word] = 1
                    else:
                        self._word_list[word] += 1

                    self._word_count += 1

    def get_path(self):
        """
        This function returns the path of this file
        """
        return self._file

    def term_frequency(self, word):
        """
        This function takes a word
        and return the frequency
        of its appearance in the file.
        """
        word = re.sub(r'\W+', '', word.lower())
        if word in self._word_list.keys():
            freq = self._word_list[word]
            freq /= self._word_count
            return freq
        else:
            return 0

    def get_words(self):
        """
        This function returns a list of words
        that are in the file.
        """
        return list(self._word_list.keys())
