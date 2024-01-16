def words_to_frequency(words):
    # this function will be used in the main function we need to write
    d={}
    for i in words:
        if i not in d:
            d[i]=0
        if i in d:
            d[i]=d[i]+1
    return d


def freq_to_words(words):
    freq_dict = words_to_frequency(words)

    result = dict()
    a=[]
    for word in freq_dict:
        freq = freq_dict[word]
        if freq not in freq_dict.values():
            a.append(word)
            result[freq] = a
            a=[]
        else:
            for w in freq_dict:
                if freq==freq_dict[w]:
                    a.append(w)
            result[freq]=a
            a=[]
    return result
print(freq_to_words(['a', 'random', 'collection', 'a', 'another', 'a', 'random']))
print(words_to_frequency(['a', 'random', 'collection', 'a', 'another', 'a', 'random']))