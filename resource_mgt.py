"""Class to show file manipulations"""
import sys


original_file = open('wasteland.txt', mode='rt', encoding='utf-8')
file_to_write = open('wasteland-copy.txt', mode='wt', encoding='utf-8')

file_to_write.write("What are the roots that clutch, ")
file_to_write.write('what branches grow\n')
