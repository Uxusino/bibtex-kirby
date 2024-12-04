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
        expected_str = "@article{test_label,\n    title = {Test Title},\n    year = {2024}\n}"
        self.assertEqual(str(self.bibtex), expected_str)

    def test_bibtex_str_empty_data(self):
        content = (2, "empty_label", "book", "2024-01-01 00:00:00", "2024-01-01 00:00:00", {})
        bibtex = Bibtex(content)
        expected_str = "@book{empty_label\n}"
        self.assertEqual(str(bibtex), expected_str)

    def test_set_tags(self):
        tags = ["tag1", "tag2"]
        self.bibtex.set_tags(tags)
        self.assertEqual(self.bibtex.tags, tags)


if __name__ == '__main__':
    unittest.main()
