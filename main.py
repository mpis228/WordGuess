from Parsing import pars
from random import *
from Health import TargetWord
from protection import *


def hat():
    print('             (да / нет)')
    while True:
            answer = input('                 >')
            options = Check('да', 'нет')
            try:
                options.chek(answer)
                break
            except TypeError:
                continue

    return options.chek(answer)


def play():
    while True:
        print(*user.word_completion)
        print(*user.health)
        char = input('ведите букву >')
        """нужно будет еще проверить что вели"""
        user.define_answer(char)
        if user.win_or_over():
            break


if __name__ == '__main__':
    print('      Давайте играть в угадайку слов!     ')
    while True:
        if hat():
            word = choice(pars())
            user = TargetWord(word)
            play()
        else:
            break
    print('Удачи!')
