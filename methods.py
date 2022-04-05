import re
import itertools


def get_unique_text(text):
    unique = []

    for i in text:
        if i not in unique:
            unique.append(i)
    return unique


def get_number_of_repeats(result, text):
    temp = {}

    for i in range(len(result)):
        size = str(len(re.findall(r'\b{}\b'.format(result[i]), text)))
        temp.update({result[i]: size})

    return temp


def get_average_value(text):
    temp = re.split(r'[((\.)(\!)(\?)]\s', text)
    split_text = [re.sub(r'[^A-zА-я0-9\s\-]', " ", element) for element in temp]
    counter = []
    average = 0
    for element in split_text:
        length = len(re.findall(r'\S+', element))
        average += length
        counter.append(length)
    counter.sort()
    return str(round(average/len(counter)))


def get_median_value(text):
    temp = re.split(r'[((\.)(\!)(\?)]\s', text)
    split_text = [re.sub(r'[^A-zА-я0-9\s\-]', " ", element) for element in temp]
    counter = []
    for element in split_text:
        length = len(re.findall(r'\S+', element))
        counter.append(length)
    counter.sort()
    return str(round(counter[len(counter)//2]))


def generate_n_size_words(n, text):
    ngram = []

    for i in text:
        for j in range(len(i)):
            if j + n <= len(i):
                ngram.append(i[j:j + n])
            else:
                break
    return ngram


def generate_top_k_grams(text, n, k):
    n_text = generate_n_size_words(n, text)
    unique_text = get_unique_text(n_text)
    temp = {}
    temp = temp.fromkeys(unique_text, 0)

    for i in n_text:
        temp[i] = temp[i] + 1

    top_k = dict(sorted(temp.items(), key=lambda item: item[1], reverse=True))
    return dict(itertools.islice(top_k.items(), k))
