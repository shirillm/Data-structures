def find_longest_word_length(text):
    return max(len(word) for word in text.split())