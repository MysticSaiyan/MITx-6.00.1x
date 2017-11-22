def lyrics_to_frequencies(lyrics):
    myDict = {}
    for word in lyrics:
        if word in myDict:
            myDict[word] += 1
        else:
            myDict[word] = 1
    return myDict

rains = ['And', 'who', 'are', 'you', 'the', 'proud', 'lord', 'said',
'that', 'I', 'must', 'bow', 'so', 'low',
'Only', 'a', 'cat', 'of', 'a', 'different', 'coat',
"that's", 'all', 'the', 'truth', 'I', 'know',
'In', 'a' ,'coat', 'of' ,'gold' ,'or', 'a', 'coat', 'of', 'red',
'a' ,'lion', 'still', 'has', 'claws',
'And', 'mine', 'are' ,'long', 'and' ,'sharp', 'my', 'lord',
'as' ,'long' ,'and' ,'sharp', 'as', 'yours',
'And', 'so' ,'he' 'spoke', 'and', 'so' ,'he', 'spoke',
'that', 'lord' 'of' ,'Castamere',
'And' ,'now', 'the', 'rains', 'weep', "o'er" ,'his', 'hall',
'with', 'no', 'one', 'there', 'to', 'hear',
'Yes', 'now', 'the', 'rains', 'weep', "o'er", 'his', 'hall',
'and', 'not' ,'a', 'soul', 'to', 'hear',]

castamere = lyrics_to_frequencies(rains)


def most_common_words(freqs):
    values = freqs.values()
    best = max(values)
    words = []
    for k in freqs:
        if freqs[k] == best:
            words.append(k)
    return (words, best)