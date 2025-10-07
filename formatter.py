from typing import Final

VERSION: Final[str] = "1.0"

def format_title(title: str) -> str:
    words: list[str] = []
    for word in title.split():
        words.append(word.capitalize())
    
    return ' '.join(words)


if __name__ == "__main__":
    sample_title: str = "the quick brown fox jumps over the lazy dog"
    print(format_title(sample_title))
# if we run this file directly, it will execute the code in the if block
# if we import this file as a module, it will not execute the code in the if block
