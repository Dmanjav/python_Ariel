from typing import Optional

def word_break(s: str, words: set[str]) -> Optional[str]:
    result: Optional[list[str]] = find(s, words)
    if result:
        return ' '.join(result)
    return None
    
def find(s: str, words: set[str], answer: list[str] = []) -> Optional[list[str]]:  
    if s == '':
        return answer
    index: int = 0
    word: str = ''
    while index < len(s):
        word += s[index]
        if word in words:
            new_answer = find(s[index + 1:], words, answer + [word])
            if new_answer:
                return new_answer
        index += 1
    return None

if __name__ == '__main__':
    words: set[str] = {'he', 'she', 'it', 'dog', 'ran',
                        'ate', 'the', 'homework', 'them'}
    print(word_break('thedogatethehomework', words))