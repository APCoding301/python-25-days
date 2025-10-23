from collections import Counter
import re


# 1. Function to analyse text files
def analyse(filename: str) -> None:
    with open(filename, 'r') as f:
        text: str = f.read()

    words: list[str] = re.findall(r'\b\w+\b', text.lower())
    word_count: int = len(words)
    comma_count: int = text.count(',')
    full_stop_count: int = text.count('.')
    exclamation_count: int = text.count('!')
    question_mark_count: int = text.count('?')
    colon_count: int = text.count(':')
    semicolon_count: int = text.count(';')
    char_count_incl_ws: int = len(text)
    whitespace_count: int = sum(c.isspace() for c in text)
    top_words: list[tuple[str, int]] = Counter(words).most_common(3)

    print('-' * 30)
    print(f'Word count: {word_count}')
    print(f'Commas used: {comma_count}')
    print(f'Full stops used: {full_stop_count}')
    print(f'Exclamation marks used: {exclamation_count}')
    print(f'Question marks used: {question_mark_count}')
    print(f'Colons used: {colon_count}')
    print(f'Semicolons used: {semicolon_count}')
    print(f'Character count (incl. whitespaces): {char_count_incl_ws}')
    print(f'Whitespace characters: {whitespace_count}')
    print('')
    print('Top 3 most used words:')

    for word, count in top_words:
        print(f' > {word}: {count}')
    
    print('')
    print(f'Average word length (1st method): {sum(len(word) for word in words) / word_count:.2f}')
    print(f'Average word length (2nd method): {(char_count_incl_ws - whitespace_count) / word_count:.2f}')
    # 2nd method SHOULD subtract punctuation marks count for more accuracy..does NOT do this currently!
    print('-' * 30)


def main() -> None:
    analyse('sample.txt')
    #analyse('sample2.txt')



if __name__ == '__main__':
    main()


# Homework:
# 1. Count punctuation marks (`.`, `!`, `?`, `:`, `;`).
# 2. Calculate the average word length.