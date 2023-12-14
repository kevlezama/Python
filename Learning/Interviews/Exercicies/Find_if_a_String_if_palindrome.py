s = 'aNa'

def is_palindrome(word):
    lowered_word= word.lower()
    word_to_list = list(lowered_word)
    word_to_list.reverse()
    reversed_word = ''.join(word_to_list)

    if lowered_word == reversed_word:
        return True
    else:
        return False

print(is_palindrome(s))


s2='AnA'


def is_palindrome2(word):
    if word[::-1].lower() == word.lower():
        return True
    else:
        return False 

print(is_palindrome2(s2))


