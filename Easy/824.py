class Solution(object):
    def toGoatLatin(self, sentence):
        vowels = set("aeiouAEIOU")
        words = sentence.split()
        transformed_words = []
        for index, word in enumerate(words, 1):
            if word[0] in vowels:
                word = word + "ma"
            else:
                word = word[1:] + word[0] + "ma"

            word = word + "a" * index

            transformed_words.append(word)

        return " ".join(transformed_words)
