def reduce_words(word: str, words: list):
    if(words):
        for index in range(len(words)):
            if(len(words[index]) > 5):
                words[index] = words[index][:5] + "@"
        return words
    else:
        if(len(word) > 5):
            word = word[:5] + "@"
        return word

word_list = ['Amazing Job', 'Waterwall', 'Sunshine', "Cat"]
if(len(word_list) == 0):
    word = input("Insert your word: ")
    cutted_words = reduce_words(word, False)
    print(cutted_words)
else: 
    cutted_words = reduce_words(False, word_list)
    for word in cutted_words:
        print(word)
