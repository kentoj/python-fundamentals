"""Analyzes a text file and computes metrics"""

import os
import unittest


def analyze_text(filename):
    lines = 0
    chars = 0
    with open(filename, mode='rt', encoding='utf-8') as file:
        for line in file:
            lines += 1
            chars += len(line)
        return lines, chars


class TextAnalysisTests(unittest.TestCase):
    """Tests for the ''analyze_text()'' function."""

    def setUp(self):
        """Fixture that creates a file for the text methods to use."""
        self.filename = 'text_analysis_test_file.txt'
        with open(self.filename, 'w') as f:
            f.write('Now we are engaged in a great civil war.\n'
                    'testing whether that nation,\n'
                    'or any nation so conceived and so dedicated,\n'
                    'can long endure.')

    def tearDown(self):
        """Fixture that deletes the files used by the test methods."""
        try:
            os.remove(self.filename)
        except:
            pass

    def test_function_runs(self):
        """Basic smoke test: does the function run"""
        analyze_text(self.filename)

    def test_line_count(self):
        """Check that the line count is correct."""
        self.assertEqual(analyze_text(self.filename)[0], 4)

    def test_character_count(self):
        """Check that the character count is correct"""
        self.assertEqual(analyze_text(self.filename)[1], 131)

    def test_no_such_file(self):
        """Check the proper exception is thrown for a missing file."""
        with self.assertRaises(IOError):
            analyze_text("nonexistent")

    def test_no_deletion(self):
        """Check that the function doesn't delete the input file"""
        analyze_text(self.filename)
        self.assertTrue(os.path.exists(self.filename))


if __name__ == '__main__':
    unittest.main()
