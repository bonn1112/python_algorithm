def g():
    for i in range(10):
        yield i

l = ['mon', 'tue', 'wed']

def change_word(words, func):
    for w in words:
        print(func(w))

change_word(l, lambda word: word.capitalize())

if __name__ == '__main__':

    g = g()
    g = (i for i in range(10) if i % 2 == 0)

    for i in g:
        print(i)
