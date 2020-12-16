import unittest 
from anagrams import compute_anagrams

class TestAnagram(unittest.TestCase):
    
    def test_anagrams(self):
        words = ["listen", "silent", "enlist", "inlets"]
        self.assertEqual(compute_anagrams(words), {"eilnst" : ['listen', 'silent', 'enlist', 'inlets' ]})
    
    def test_anagrams2(self):
        words = ["sinks", "skins"]
        self.assertEqual(compute_anagrams(words), {"iknss" : ['sinks', 'skins']})

if __name__ == '__main__':
    unittest.main()
