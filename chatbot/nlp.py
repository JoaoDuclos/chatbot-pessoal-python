import string

def preprocess(text):
    text_lower = text.lower().strip()
    clean_text = "".join(char for char in text_lower if char not in string.punctuation)
    list_of_words = clean_text.split()
    ignore = set(["de", "para", "que", "até", "após", "com", "contra", "desde", "em", "entre", "perante", "por", "sem", "sob", "sobre", "trás"])
    final_list = []
    for word in list_of_words:
        if len(word) >= 2 and word not in ignore:
            final_list.append(word)

    return final_list