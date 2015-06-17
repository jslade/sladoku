import unittest

class InitializationTests(unittest.TestCase):
    def test_import(self):
        """ Ensure the test suite can import our module"""
        try:
            import sladoku
        except ImportError:
            self.fail("Was not able to import")

