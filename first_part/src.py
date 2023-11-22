def exercise_one():
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print("ThreeFive")
        elif num % 3 == 0:
            print("Three")
        elif num % 5 == 0:
            print("Five")
        else:
            print(num)
pass
# exercice 2


def is_colorful_number(number):
    digits = list(str(number))
    products_set = set()

    for i in range(len(digits)):
        for j in range(i + 1, len(digits) + 1):
            subset = digits[i:j]
            product = 1
            for digit in subset:
                product *= int(digit)
            if product in products_set:
                return False
            products_set.add(product)

    return True

#exercice 3
def calculate(lst):
    if not isinstance(lst, list):
        return False

    total = 0

    for item in lst:
        if isinstance(item, str) and (item.lstrip('-')).isdigit():
            total += int(item)

    return total if total != 0 else False

#exercice 4
def find_anagrams(word, word_list):
    # Sort the characters of the input word
    sorted_word = sorted(word)

    # Use a list comprehension to filter anagrams from the word list
    anagrams = [w for w in word_list if sorted(w) == sorted_word]

    return anagrams