from urllib.request import urlopen


def fetch_words():
    with urlopen('http://sixty-north.com/c/t.txt') as story:
        story_words = []
        word_list = ''
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)
        wordCursor = 0
        print("Word Count", len(story_words))
        while wordCursor < len(story_words):
            paragraphCursor = 0
            while paragraphCursor < 6:
                if (wordCursor + paragraphCursor) == len(story_words):
                    break
                word_list += story_words[wordCursor + paragraphCursor] + ' '
                paragraphCursor += 1
            wordCursor += paragraphCursor
            word_list += '\n'
        return word_list


def print_words(word_list):
    print(word_list)


def main():
    print(fetch_words())

if __name__ == '__main__':
    main()
