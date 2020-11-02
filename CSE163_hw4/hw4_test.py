"""
Name: Michael Shieh
Section: CSE 163 AB

This file is for testing the two classes for this homework.
"""
from cse163_utils import assert_equals
from document import Document
from search_engine import SearchEngine


def test_document():
    """
    This function is for testing the "Document" class function by function.
    I use two different directory "test-files" and "baseball_teams"

    If passed, this function should show nothing.
    """
    assert_equals(0.2,
                  Document('/home/test-files/doc1.txt').term_frequency('dogs'))
    assert_equals(0.2, Document(
                          '/home/test-files/doc1.txt').term_frequency('dogs!'))
    assert_equals(0.25,
                  Document('/home/test-files/doc2.txt').term_frequency('CATS'))
    assert_equals(0,
                  Document('/home/test-files/doc3.txt').term_frequency(
                      'greatest'))
    assert_equals(0.0625,
                  Document('/home/baseball_teams/LAD.txt').term_frequency(
                      'baseball'))
    assert_equals(0.0625,
                  Document('/home/baseball_teams/LAD.txt').term_frequency(
                      'BaseBall?'))
    assert_equals(0.05555555555555555,
                  Document('/home/baseball_teams/NYY.txt').term_frequency(
                      'american'))
    assert_equals(['i', 'love', 'dogs'],
                  Document('/home/test-files/doc3.txt').get_words())
    lst_NYM = ['the', 'new', 'york', 'mets', 'are', 'a', 'major', 'league',
               'baseball', 'team', 'based', 'in', 'city', 'borough', 'of',
               'queens', 'they', 'compete', 'as', 'member', 'club', 'national',
               'east', 'division']
    assert_equals(lst_NYM,
                  Document('/home/baseball_teams/NYM.txt').get_words())
    lst_NYY = ['the', 'new', 'york', 'yankees', 'are', 'an', 'american',
               'professional', 'baseball', 'team', 'based', 'in', 'city',
               'borough', 'of', 'bronx', 'they', 'compete', 'major',
               'league', 'as', 'a', 'member', 'club', 'east', 'division']
    assert_equals(lst_NYY,
                  Document('/home/baseball_teams/NYY.txt').get_words())


def test_search_engine():
    """
    This function is for testing the "SearchEngine" class function by function.
    I use two different directory "test-files" and "baseball_teams"

    If passed, this function should show nothing.
    """
    assert_equals(0.4054651081081644,
                  SearchEngine('test-files')._calculate_idf('dogs'))
    assert_equals(0.6931471805599453,
                  SearchEngine('baseball_teams')._calculate_idf('california'))
    assert_equals(0.0,
                  SearchEngine('baseball_teams')._calculate_idf('baseball'))
    lst_dogs = ['test-files/doc3.txt', 'test-files/doc1.txt']
    assert_equals(lst_dogs, SearchEngine('test-files').search('dogs'))
    lst_greatest_dogs = ['test-files/doc1.txt', 'test-files/doc3.txt']
    assert_equals(lst_greatest_dogs,
                  SearchEngine('test-files').search('greatest dogs'))
    assert_equals(lst_greatest_dogs,
                  SearchEngine('test-files').search('GREatest dogs'))
    lst_la = ['baseball_teams/LAD.txt', 'baseball_teams/LAA.txt']
    assert_equals(lst_la,
                  SearchEngine('baseball_teams').search('los angeles'))
    assert_equals(lst_la,
                  SearchEngine('baseball_teams').search('los! ang.ELES'))
    lst_nyb = ['baseball_teams/NYY.txt', 'baseball_teams/NYM.txt']
    assert_equals(lst_nyb,
                  SearchEngine('baseball_teams').search('New York Yankees'))


def main():
    test_document()
    test_search_engine()


if __name__ == '__main__':
    main()
