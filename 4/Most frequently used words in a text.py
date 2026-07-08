"""
Write a function that, given a string of text (possibly with punctuation and line-breaks), returns an array of the top-3 most occurring words, in descending order of the number of occurrences.

Assumptions:
A word is a string of letters (A to Z) optionally containing one or more apostrophes (') in ASCII.
Apostrophes can appear at the start, middle or end of a word ('abc, abc', 'abc', ab'c are all valid)
Any other characters (e.g. #, \, / , . ...) are not part of a word and should be treated as whitespace.
Matches should be case-insensitive, and the words in the result should be lowercased.
Ties may be broken arbitrarily.
If a text contains fewer than three unique words, then either the top-2 or top-1 words should be returned,
 or an empty array if a text contains no words.

Напишите функцию, которая, получив строку текста (возможно, с пунктуацией и переносами строк),
 возвращает массив из трех наиболее часто встречающихся слов в порядке убывания количества вхождений.

Допущения:
Слово - это строка букв (от А до Я), необязательно содержащая один или несколько апострофов (') в ASCII.
Апострофы могут появляться в начале, середине или конце слова (допустимы все символы "abc", "авс", "авс-с").
Любые другие символы (например, #, \, / , . ...) не являются частью слова и должны рассматриваться как пробелы.
Совпадения должны быть без учета регистра, а слова в результате должны быть написаны строчными буквами.
Связи могут быть нарушены произвольно.
Если текст содержит менее трех уникальных слов, то должны быть возвращены либо 2 первых, либо 1 первое слово,
 либо пустой массив, если текст не содержит слов.
"""


def top_3_words(text):
    words = ''.join(c if c.isalpha() or c == "'" else " " for c in text).lower().split()
    popularity = dict()

    def word_is_valid(word: str) -> bool:
        for symbol in word:
            if ord('a') <= ord(symbol) <= ord('z'):
                return True
        return False

    for word in words:
        if word_is_valid(word):
            if word not in popularity:
                popularity[word] = 1
            else:
                popularity[word] += 1

    new_popularity = sorted(popularity.items(), key=lambda x: x[1], reverse=True)
    popularity_list = [word for word, count in new_popularity]

    if len(popularity_list) > 3:
        return popularity_list[:3]

    return popularity_list
