from collections import defaultdict


# Defaultdict counter
def counter(sentence='a quick brown fox jumps over the lazy dog'):
    count = defaultdict(int)

    for letter in sentence.lower().replace(' ', ''):
        count[letter] += 1

    for i in count.items():
        print i


# Wrapper counter
def printer(text):
    print text


def count(f):
    def wrapper(*args, **kwargs):
        sentence = args[0]
        sentence = sentence.lower().replace(' ', '')
        counter = defaultdict(int)

        for letter in sentence:
            counter[letter] += 1

        for l, c in counter.items():
            print '{}: {}'.format(l, c)
        return f(*args, **kwargs)
    return wrapper


###  As a Decorator
@count
def printer(text):
    print text
