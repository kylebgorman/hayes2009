"""Unit tests."""

import unittest

import hayes2009


class HayesTest(unittest.TestCase):
    def test_normal_g(self):
        with self.assertRaises(KeyError):
            hayes2009.universal["g"]
        with self.assertRaises(KeyError):
            hayes2009.english["g"]

    def test_single_storey_g(self):
        features = frozenset(hayes2009.universal["ɡ"])
        self.assertIn("-nasal", features)
        self.assertIn("-round", features)
        self.assertIn("+high", features)
        self.assertNotIn("+tense", features)
        self.assertNotIn("-tense", features)

    def test_i_universal(self):
        features = frozenset(hayes2009.universal["i"])
        self.assertIn("-nasal", features)
        self.assertIn("-round", features)
        self.assertIn("+high", features)
        self.assertIn("+tense", features)

    def test_i_english(self):
        features = frozenset(hayes2009.english["i"])
        self.assertIn("-nasal", features)
        self.assertIn("-round", features)
        self.assertIn("+high", features)
        self.assertIn("+tense", features)


if __name__ == "__main__":
    unittest.main()
