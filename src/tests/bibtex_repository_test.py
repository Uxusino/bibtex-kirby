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
            "type": "article",
            "data": self.test_data
        }

    def test_create_bibtex_adds_a_bibtex(self):
        with app.app_context():
            self.repo.reset_db()
            self.repo.create_bibtex(self.content)
            result = self.repo.get_bibtex_by_label("test_bib")

        self.assertEqual(result.label, "test_bib")

    def test_delete_bibtex_deletes_the_bibtex(self):
        with app.app_context():
            self.repo.reset_db()
            self.repo.create_bibtex(self.content)
            result = self.repo.get_bibtex_by_label("test_bib")
            self.repo.delete_bibtex(result.id)
            result2 = self.repo.get_bibtexs()

        self.assertEqual(result2, [])

    def test_bibtex_data_from_db_is_dict(self):
        with app.app_context():
            self.repo.reset_db()
            self.repo.create_bibtex(self.content)
            result = self.repo.get_bibtex_by_label("test_bib")

        bibtex = result.data

        reference_dict = {
            "title": "Creating bibs",
            "year": 2024
        }

        self.assertEqual(bibtex, reference_dict)

    def test_reset_db(self):
        with app.app_context():
            self.repo.reset_db()
            self.repo.create_bibtex(self.content)
            self.repo.reset_db()
            result = self.repo.get_bibtexs()
        
        self.assertEqual(result, [])
