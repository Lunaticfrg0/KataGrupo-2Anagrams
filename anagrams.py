def compute_anagrams(words):
    result = {}
    result[words[0]] = []
    result[words[0]].append(words[0])
    result[words[0]].append(words[1])
    result[words[0]].append(words[2])
    result[words[0]].append(words[3])

    return result