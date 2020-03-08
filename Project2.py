from bs4 import BeautifulSoup
import requests
import re
import os
import csv
import unittest


def get_headlines_from_search_results(filename):
    """
    Write a function that creates a BeautifulSoup object on the passed filename. Parse
    through the object and return a list of headlines for each search result in the
    following format:

    ['Headline 1', 'Headline 2'...]
    """

    pass


def get_most_recent():
    """
    Write a function that creates a BeautifulSoup object after retrieving content from
    "https://www.freep.com". Parse through the object and return a list of URLs for each
    of the articles in the "MOST RECENT" section using the following format:

    ['https://www.freep.com/story/news/local/michigan/2020/02/26/michigan-foia-slow-costly-whitmer-transparency/4786653002/', ...]
    """

    pass


def get_article_summary(article_url):
    """
    Write a function that creates a BeautifulSoup object that extracts information 
    from an article, given the relative URL of the article. parse through
    the BeautifulSoup object, and capture the article title, author, and date. Make
    sure to strip() any whitespace from the date. If the timestamp contains
    "Published" and "Updated" information, you should only capture the "Published"
    part.

    This function should return a list of tuples in the following format:

    [('Some headline', 'Some Author', 'Published 12:00 a.m. ET Jan 01, 2020')...]

    HINT: Using BeautifulSoup's find() method may help you here.
    You can easily capture CSS selectors with your browser's inspector window.
    """

    pass


def summarize_corrections(filepath):
    """
    Write a function to get the section tags and dates of the Corrections &
    Clarifications article in "corrections.htm". You need to use regex to accomplish
    this. This function should create a BeautifulSoup object from a filepath and
    return a list of (tag, date) tuples.

    For example, if the article contains: "Sports: Jan 1, a basketball story was
    Published", you should append ("Sports", "Jan 1") to your list of tuples.
    """

    pass


def write_csv(data, filename):
    """
    Write a function that takes in a list of tuples called data
    (i.e. the one that is returned by summarize_corrections()),
    writes the data to a csv file, and saves it to the passed filename.

    The first row of the csv should contain "Tag" and
    "Date" respectively. For each tuple in data, write a new row to
    the csv, placing each element of the tuple in the correct column.

    When you are done your CSV file should look like this:

    Tag,Date
    Some Tag, Jan. 1
    Another Tag, Feb. 2
    Yet another Tag, Mar. 3


    This function should not return anything.
    """

    pass


# def summarize_corrections_expanded(filepath):
#     """
#     EXTRA CREDIT – Uncomment if you wish to attempt.
#
#     Please see the instructions document for more information on how to complete this function.
#     You do not have to write test cases for this function.
#     """
#
#     pass


class TestCases(unittest.TestCase):


    # Create a class variable and store the most recent article url list in it.
    # This can be accessed using TestCases.article_url_list in the test functions
    article_url_list = get_most_recent()

    def test_get_headlines_from_search_results(self):
        # call get_headlines_from_search_results("search.htm") and save the result 
        # check that the number of headlines extracted is correct (10 headlines)
        # check that the variable you saved after calling the function is a list
        # check that each headline in the list is a string
        # check that the first headline is correct (open search.htm and find it)
        # check that the last headline is correct (open search.htm and find it)
        pass

    def test_get_most_recent(self):
        # check that TestCases.article_url_list is a list
        # check that the length of TestCases.article_url_list is correct (6 URLs)
        # check that each URL in the TestCases.article_url_list is a string
        # check that each URL contains the correct url for the Detroit Free Press followed by /story/
        pass

    def test_get_article_summary(self):
    	# create a local variable – summaries – a list that contains the results from 
    	# get_article_summary() for each URL in TestCases.article_url_list

        # check that the number of article summaries is correct (6)
            # check that each item in the list is a tuple
            # check that each tuple has 3 elements
            # check that each element is a string
            # check that each date contains the word "Published"
        pass

    def test_summarize_corrections(self):
        # call summarize corrections and save the results to a variable
        # check that we have the right number of corrections (37)
            # assert each item in the list of corrections is a tuple
            # check that each tuple has a length of 2
        # check that the first tuple is made up of the following 2 strings: "Life" and "July 1"
        # check that the last tuple is made up of the following 2 strings: "Opinion" and "Jan. 26"
        pass

    def test_write_csv(self):
        # call summarize_corrections on "corrections.htm" and save the result to a variable
        # call write csv on the variable you saved
        # read in the csv that you wrote

        # check that there are 38 lines in the csv
        # check that the header row is correct
        # check that the next row is "Life,July 1"
        # check that the last row is "Opinion,Jan. 26"
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)

