from document import Document
import os
import math
import re


class SearchEngine:
    def __init__(self, directory_name):
        """
        This initializer takes a directory name
        and create a "Document" object
        for each of the file in the directory
        """
        self._directory_name = directory_name
        self._files = {}
        self._inverse_index = {}
        for file_name in os.listdir(self._directory_name):
            if not file_name.startswith('.'):
                doc = Document(directory_name + '/' + file_name)
                self._files[file_name] = doc

                for word in doc.get_words():
                    if word not in self._inverse_index:
                        self._inverse_index[word] = [file_name]
                    else:
                        self._inverse_index[word].append(file_name)

    def _calculate_idf(self, word):
        """
        This function takes a word
        and calcualte the idf of it within the files
        """
        total = len(self._files.keys())
        count = len(self._inverse_index[word])

        if count == 0:
            return 0
        else:
            return math.log(total / count)

    def search(self, term):
        """
        This function takes a term,
        which could be one or multiple words,
        and return a sorted list of file names
        that include the term based on total tf_idf values.
        """
        term = term.lower().split()
        term = [re.sub(r'\W+', '', word) for word in term]
        lst = []
        selected_files = set()

        for word in term:
            if word in self._inverse_index:
                files = self._inverse_index[word]
                for file in files:
                    selected_files.add(file)

        for file in selected_files:
            tf_idf = 0
            for word in term:
                tf = self._files[file].term_frequency(word)
                idf = self._calculate_idf(word)
                tf_idf += tf * idf

            if tf_idf > 0:
                path = self._files[file].get_path()
                lst.append((path, tf_idf))

        lst = sorted(lst, key=lambda x: x[1], reverse=True)
        lst = [x[0] for x in lst]

        return lst
