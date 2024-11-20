import unittest
from entities.bibtex import Bibtex


class TestBibtex(unittest.TestCase):
    def setUp(self):
        self.content = (1, "test_label", "article", "2024-01-01 00:00:00", "2024-01-01 00:00:00", {"title": "Test Title", "year": 2024})
        self.bibtex = Bibtex(self.content)

    def test_bibtex_initialization(self):
        self.assertEqual(self.bibtex.id, 1)
        self.assertEqual(self.bibtex.label, "test_label")
        self.assertEqual(self.bibtex.type, "article")
        self.assertEqual(self.bibtex.creation_time, "2024-01-01 00:00:00")
        self.assertEqual(self.bibtex.modified_time, "2024-01-01 00:00:00")
        self.assertEqual(self.bibtex.data, {"title": "Test Title", "year": 2024})

    def test_bibtex_str(self):
        self.assertEqual(str(self.bibtex), "1 article: test_label")

if __name__ == '__main__':
    unittest.main()