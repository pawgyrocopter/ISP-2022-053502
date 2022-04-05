import re
from methods import get_unique_text, \
    get_number_of_repeats, generate_top_k_grams, \
    get_average_value, \
    get_median_value



def solve():
    n = 4
    k = 10
    text = input("Text please:\n")
    text = text.lower()

    filtered_text = re.findall(r'\S+', re.sub(r'[^A-zА-я0-9\s\-]', " ", text))
    # print(filtered_text)

    number_of_words = get_number_of_repeats(get_unique_text(filtered_text), text)
    print(number_of_words)

    print("Average words in sentence: " + get_average_value(text))
    print("Median value: " + get_median_value(text))

    input_n = input("Input n gram: ")
    if input_n == ' ':
        input_n = n

    input_k = input("Input k: ")
    if input_k == ' ':
        input_k = k

    result = generate_top_k_grams(filtered_text, int(input_n), int(input_k))

    print(result)
