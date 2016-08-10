#!/usr/bin/env python3
"""Retrieve and print words from a URL.

Usage:

    python3 text_processor.py <URL>
"""

import sys
from urllib.request import urlopen


def fetch_words(url):
    """Fetch a list of words from a URL.

    Args:
        url: The URL of a UTF-8 text document.

    Returns:
        A UTF-8-decoded list of strings containing the words from the document.

    """
    with urlopen(url) as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)
        return story_words


def print_items(items):
    """Print items six per line with a space in between each item

    Args:
        items: an iterable series that can be parsed as a string
    """
    word_list = ''
    word_cursor = 0
    print("Word Count", len(items))
    while word_cursor < len(items):
        paragraphCursor = 0
        while paragraphCursor < 6:
            if (word_cursor + paragraphCursor) == len(items):
                break
            word_list += str(items[word_cursor + paragraphCursor])
            word_list += ' '
            paragraphCursor += 1
        word_cursor += paragraphCursor
        word_list += '\n'
    print(word_list)


def main(url):
    """Print each word from a text document from a URL.

    Args:
        url: The URL to a UTF-8 text document
    """
    print_items(fetch_words(url))

if __name__ == '__main__':
    main(sys.argv[1]) # The 0th arg is the module filename
