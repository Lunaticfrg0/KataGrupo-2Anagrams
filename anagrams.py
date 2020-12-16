import sys

def compute_anagrams(words):
    anagrams = {}
    
    for word in range(len(words)):
        lowercase_word = words[word].lower()
        ordered = ''.join(sorted(lowercase_word))
        if ordered in anagrams:
            anagrams[ordered].append(lowercase_word)
        else:
            anagrams[ordered] = [lowercase_word]

    return anagrams

def read_file():
     filename = sys.argv[1]
     file = open(filename, "r")
     content = file.readlines()
     words = []
     
     for word in content:
         words.append(word.replace("\n", ""))
    
     anagrams = compute_anagrams(words)
    
     for ang in anagrams:
         if len(anagrams[ang]) > 1:
             print(anagrams[ang])

if __name__ in '__main__':
    read_file()