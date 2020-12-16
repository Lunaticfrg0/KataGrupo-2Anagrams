import unittest 
from anagrams import compute_anagrams

class TestAnagram(unittest.TestCase):
    
    def test_anagrams(self):
        words = ["listen", "silent", "enlist", "inlets"]
        self.assertEqual(compute_anagrams(words), {"listen" : ['listen', 'silent', 'enlist', 'inlets' ]})


if __name__ == '__main__':
    unittest.main()
