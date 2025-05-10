dictionary_words_amount = int(input("Insert the amount of words in the dictionary: "))

words_dictionary = {}
for i in range(dictionary_words_amount):
    word = input("Insert your word: ")
    translate = input("Insert the word in english: ")
    words_dictionary[word] = translate

print("Dictionary: \n")
for spanish_word in words_dictionary.keys():
    print(spanish_word)

english_word = input("Insert the word are you looking to translate to english: ")

if(words_dictionary.get(english_word)):
    print(f"The translate is: {words_dictionary.get(english_word)}")
else:
    print("The word is not in the dictionary")
