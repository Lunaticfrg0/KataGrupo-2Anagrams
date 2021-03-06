import unittest 
from anagrams import compute_anagrams

class TestAnagram(unittest.TestCase):
    
    def test_anagrams(self):
        words = ["listen", "silent", "enlist", "inlets"]
        self.assertEqual(compute_anagrams(words), {"eilnst" : ['listen', 'silent', 'enlist', 'inlets' ]})
    
    def test_anagrams2(self):
        words = ["sinks", "skins"]
        self.assertEqual(compute_anagrams(words), {"iknss" : ['sinks', 'skins']})

    def test_anagrams3(self):
        words = ["sort", "rots"]
        self.assertEqual(compute_anagrams(words), {"orst" : ['sort', 'rots']})

    def test_anagrams4(self):
        words = ["pAste", "tapeS", "Sepat"]
        self.assertEqual(compute_anagrams(words), {"aepst" : ['paste', 'tapes', 'sepat']})
        
    def test_anagrams5(self):
        words = ["abc", 'hi', "jereMy", "RONIEL"]
        self.assertEqual(compute_anagrams(words), {"abc" : ['abc'],'hi':['hi'], 'eejmry':['jeremy'], 'eilnor':['roniel']})


if __name__ == '__main__':
    unittest.main()
