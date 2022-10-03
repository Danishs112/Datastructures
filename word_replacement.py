def replace_word():

    sentence = "Hi, My name is Danish Soma"

    word_to_replace = input("Enter the word to replace:")
    word_replacement = input("Enter the word:")
    print(sentence.lower().replace(word_to_replace, word_replacement))

replace_word()