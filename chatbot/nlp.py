import string

def preprocess(text):
    text_lower = text.lower().strip()
    clean_text = "".join(char for char in text_lower if char not in string.punctuation)
    list_of_words = clean_text.split()
    final_list = []
    for word in list_of_words:
        if len(word) >= 2:
            final_list.append(word)

    return final_list