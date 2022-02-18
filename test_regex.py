import unittest

from regex import entry_point


class TestRegex(unittest.TestCase):

    def test_equal_regex_string(self):
        self.assertTrue(entry_point('a|a'))

    def test_empty_regex(self):
        self.assertTrue(entry_point('|a'))

    def test_start_char(self):
        self.assertTrue(entry_point('^app|apple'))

    def test_ending_char(self):
        self.assertTrue(entry_point('le$|apple'))

    def test_start_char_with_letter(self):
        self.assertTrue(entry_point('^a|apple'))

    def test_ending_with_any(self):
        self.assertTrue(entry_point('.$|apple'))

    def test_ending_with_two_words(self):
        self.assertTrue(entry_point('apple$|tasty apple'))

    def test_start_with_two_words(self):
        self.assertTrue(entry_point('^apple|apple pie'))

    def test_start_and_end(self):
        self.assertTrue(entry_point('^apple$|apple'))

    def test_start_and_end_with_two_words(self):
        self.assertFalse(entry_point('^apple$|tasty apple'))

    def test_start_and_end_with_word_at_start(self):
        self.assertFalse(entry_point('^apple$|apple pie'))

    def test_end_with_start_of_word(self):
        self.assertFalse(entry_point('app$|apple'))

    def test_start_with_end_of_word(self):
        self.assertFalse(entry_point('^le|apple'))
