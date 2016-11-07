#parses a list of strings and checks for anagrams against a given word

import unittest

def find_anagrams(list_of_strings, word):
    word_table = [0] * 128
    string_table = [0] * 128
    anagrams = []
    for c in word.lower():
        word_table[ord(c)] += 1

    for w in list_of_strings:
        for c in w.lower():
            string_table[ord(c)] += 1
        if string_table == word_table:
            anagrams.append(w.lower())
        string_table = [0] * 128

    return anagrams
    
class AnagramsTestCase(unittest.TestCase):

    def test_parse(self):
        l1 = ["spare", "hello", "pears", "world", "reaps"]
        word = "parse"
        output = ["spare", "pears", "reaps"]
        self.assertEqual(find_anagrams(l1, word), output)

    def test_uppercaseWord(self):
        l1 = ["spare", "hello", "pears", "world", "reaps"]
        word = "PARSE"
        output = ["spare", "pears", "reaps"]
        self.assertEqual(find_anagrams(l1, word), output)

    def test_lowercaseWord(self):
        l1 = ["SPARE", "HELLO", "PEARS", "WORLD", "REAPS"]
        word = "parse"
        output = ["spare", "pears", "reaps"]
        self.assertEqual(find_anagrams(l1, word), output)

    def test_no_anagrams(self):
        l1 = ["SPARE", "HELLO", "PEARS", "WORLD", "REAPS"]
        word = "pars"
        output = []
        self.assertEqual(find_anagrams(l1, word), output)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(AnagramsTestCase)
    unittest.TextTestRunner(verbosity=2).run(suite)