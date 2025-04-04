def get_num_words(text):
    lst_word = text.split()
    count = 0
    for i in lst_word:
        count += 1
    return count

def get_dict(text):
    text_tmp = text.lower()
    set_sy = set(text_tmp)
    dict_sym = {}
    for i in set_sy:
        num = text_tmp.count(i)
        dict_sym[i] = num
    return dict_sym

def sort_count(dict_sym):
    sorted_dict = dict(sorted(dict_sym.items(), key = lambda item: item[1], reverse=True))
    return sorted_dict

