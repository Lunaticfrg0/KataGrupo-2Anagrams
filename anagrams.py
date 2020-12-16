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

