import random


def firstUniqChar(s):
    char_count = {}

    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    for i, char in enumerate(s):
        if char_count[char] == 1:
            return i

    return -1


def generate_random_string(length):
    letters = [chr(random.randint(97, 122)) for _ in range(length)]
    return ''.join(letters)


def print_result(index):
    print("Index of the first non-repeating character:", index)


string_length = random.randint(5, 10)
s = generate_random_string(string_length)

print("Input string:", s)

result = firstUniqChar(s)

print_result(result)
