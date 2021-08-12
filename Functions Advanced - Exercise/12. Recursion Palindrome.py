def palindrome(word, index):
    rev_word = word[::-1]

    if rev_word == word:
        return f"{word} is a palindrome"
    else:
        return f"{word} is not a palindrome"


print(palindrome("abcba", 0))
print(palindrome("peter", 0))
