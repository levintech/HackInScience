def longest_word(text):
    word_list = text.split()
    word_list = sorted(word_list, key = lambda x: len(x), reverse=True)
    
    if len(word_list) == 0:
        return None
    else:
        return word_list[0]