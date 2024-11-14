from repositories.bibtex_repository import bibtex_repository
from config import app

import unittest

class TestBibtexRepository(unittest.TestCase):
    def setUp(self):
        self.repo = bibtex_repository
        self.test_data = {
            "title": "Creating bibs",
            "year": 2024
        }
        self.content = {
            "label": "test_bib",
            "data": self.test_data
        }

    def test_create_bibtex_adds_a_bibtex(self):
        with app.app_context():
            self.repo.create_bibtex(self.content)
            result = self.repo.get_bibtexs()

        bibtex = str(result[0])

        self.assertEqual(bibtex, "1: test_bib")


    def test_bibtex_data_from_db_is_dict(self):
        with app.app_context():
            self.repo.create_bibtex(self.content)
            result = self.repo.get_bibtexs()

        bibtex = result[0].data

        reference_dict = {
            "title": "Creating bibs",
            "year": 2024
        }

        self.assertEqual(bibtex, reference_dict)
