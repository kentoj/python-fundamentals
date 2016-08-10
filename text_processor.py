from urllib.request import urlopen


def fetch_words():
    with urlopen('http://sixty-north.com/c/t.txt') as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)
        return story_words


def print_items(story_words):
    word_list = ''
    word_cursor = 0
    print("Word Count", len(story_words))
    while word_cursor < len(story_words):
        paragraphCursor = 0
        while paragraphCursor < 6:
            if (word_cursor + paragraphCursor) == len(story_words):
                break
            word_list += str(story_words[word_cursor + paragraphCursor])
            word_list += ' '
            paragraphCursor += 1
        word_cursor += paragraphCursor
        word_list += '\n'
    print(word_list)


def main():
    print_items(fetch_words())

if __name__ == '__main__':
    main()
