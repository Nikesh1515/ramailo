lexicon = {
    'test_directions' : ('north', 'south', 'east'),
    'test_verbs' : ('go', 'kill', 'eat'),
    'test_stops' : ('the', 'in', 'of'),
    'test_noun' : ('bear', 'princess'),
    'test_number' : (3, 91234),
    'test_errors' : ('bear', 'IAS', 'princess')
            }
def scan(sentence):
    words = sentence.split()
    result = []
    
    for word in words:
        pair = (lexicon[word], word)
        result.append(pair)
    return result
    
