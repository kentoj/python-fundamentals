"""Class to show file manipulations"""
import sys


original_file = open('wasteland.txt', mode='rt', encoding='utf-8')
file_to_write = open('wasteland-copy.txt', mode='wt', encoding='utf-8')

file_to_write.write("What are the roots that clutch, ")
file_to_write.write('what branches grow\n')
file_to_write.close()

file_reading = open('wasteland.txt', mode='rt', encoding='utf-8')
for line in file_reading.readlines():
    print(line)


file_to_append = open('wasteland-copy.txt', mode='at', encoding='utf-8')
file_to_append.writelines(
    ['Son of man,\n',
     'You cannot say, or guess, ',
     'for you know only,\n',
     'A heap of broken images, ',
     'where the sun beats\n'])
file_to_append.close()