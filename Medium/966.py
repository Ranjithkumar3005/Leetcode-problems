from typing import List


class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        def devowel(word):
            vowels = "aeiou"
            return "".join("*" if char in vowels else char for char in word.lower())

        # Exact match set
        words_exact = set(wordlist)

        # Case-insensitive map (lowercase word -> first word with that casing)
        words_case = {}

        # Vowel error map (vowel-replaced word -> first word with that pattern)
        words_vowel = {}

        for word in wordlist:
            lower_word = word.lower()
            devoweled_word = devowel(lower_word)

            if lower_word not in words_case:
                words_case[lower_word] = word

            if devoweled_word not in words_vowel:
                words_vowel[devoweled_word] = word

        result = []

        for query in queries:
            if query in words_exact:
                result.append(query)
            elif query.lower() in words_case:
                result.append(words_case[query.lower()])
            elif devowel(query) in words_vowel:
                result.append(words_vowel[devowel(query)])
            else:
                result.append("")

        return result
